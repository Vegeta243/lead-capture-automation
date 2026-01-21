#!/usr/bin/env python3
"""Process lead data and add to Google Sheets with Slack notification."""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta
import gspread
from google.oauth2.service_account import Credentials
import requests


def get_google_sheets_client():
    """Initialize Google Sheets client with service account."""
    creds_json = os.environ.get('GOOGLE_SERVICE_ACCOUNT_JSON')
    if not creds_json:
        raise ValueError('GOOGLE_SERVICE_ACCOUNT_JSON environment variable not set')
    
    creds_dict = json.loads(creds_json)
    creds = Credentials.from_service_account_info(
        creds_dict,
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )
    return gspread.authorize(creds)


def send_slack_notification(lead_data):
    """Send Slack notification for new lead."""
    webhook_url = os.environ.get('SLACK_WEBHOOK_URL')
    if not webhook_url:
        print('Warning: SLACK_WEBHOOK_URL not set, skipping Slack notification')
        return
    
    message = {
        "text": f"🎯 NOUVEAU LEAD ARRIVÉ!\n\n"
                f"👤 Nom: {lead_data['full_name']}\n"
                f"✉️ Email: {lead_data['email']}\n"
                f"📞 Téléphone: {lead_data['phone']}\n"
                f"🏢 Entreprise: {lead_data.get('company', 'Non renseigné')}\n"
                f"📈 Secteur: {lead_data.get('business_sector', 'Non renseigné')}\n"
                f"💬 Besoins: {lead_data.get('needs', 'Non renseigné')}"
    }
    
    try:
        response = requests.post(webhook_url, json=message, timeout=10)
        response.raise_for_status()
        print('Slack notification sent successfully')
    except Exception as e:
        print(f'Error sending Slack notification: {e}')


def add_lead_to_sheet(lead_data):
    """Add lead data to Google Sheet."""
    sheet_id = os.environ.get('GOOGLE_SHEET_ID')
    if not sheet_id:
        raise ValueError('GOOGLE_SHEET_ID environment variable not set')
    
    client = get_google_sheets_client()
    sheet = client.open_by_key(sheet_id).sheet1
    
    # Calculate dates
    date_reception = datetime.now().strftime('%d/%m/%Y %H:%M')
    date_envoi_email = (datetime.now() + timedelta(days=2)).strftime('%d/%m/%Y %H:%M')
    
    # Prepare row data matching column order
    row = [
        date_reception,
        lead_data['full_name'],
        lead_data['email'],
        lead_data['phone'],
        lead_data.get('company', ''),
        lead_data.get('business_sector', ''),
        lead_data.get('needs', ''),
        'En attente',  # Statut
        date_envoi_email,  # Date envoi email programmé
        ''  # Email envoyé (vide par défaut)
    ]
    
    sheet.append_row(row)
    print(f'Lead added to sheet: {lead_data["full_name"]}')


def main():
    """Main function to process lead data."""
    parser = argparse.ArgumentParser(description='Process lead data')
    parser.add_argument('--full-name', required=True, help='Full name of the lead')
    parser.add_argument('--email', required=True, help='Email address')
    parser.add_argument('--phone', required=True, help='Phone number')
    parser.add_argument('--company', default='', help='Company name')
    parser.add_argument('--business-sector', default='', help='Business sector')
    parser.add_argument('--needs', default='', help='Expressed needs')
    
    args = parser.parse_args()
    
    lead_data = {
        'full_name': args.full_name,
        'email': args.email,
        'phone': args.phone,
        'company': args.company,
        'business_sector': args.business_sector,
        'needs': args.needs
    }
    
    print('Processing new lead...')
    print(f'Name: {lead_data["full_name"]}')
    print(f'Email: {lead_data["email"]}')
    
    try:
        # Add to Google Sheet
        add_lead_to_sheet(lead_data)
        
        # Send Slack notification
        send_slack_notification(lead_data)
        
        print('Lead processed successfully!')
        return 0
    except Exception as e:
        print(f'Error processing lead: {e}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
