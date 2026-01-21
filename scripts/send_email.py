#!/usr/bin/env python3
"""Send scheduled follow-up emails to leads."""

import json
import os
import sys
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import gspread
from google.oauth2.service_account import Credentials


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


def send_email(to_email, full_name):
    """Send follow-up email via SMTP."""
    smtp_server = os.environ.get('SMTP_SERVER')
    smtp_port = int(os.environ.get('SMTP_PORT', 587))
    smtp_email = os.environ.get('SMTP_EMAIL')
    smtp_password = os.environ.get('SMTP_PASSWORD')
    
    if not all([smtp_server, smtp_email, smtp_password]):
        raise ValueError('SMTP configuration incomplete')
    
    # Create email content
    msg = MIMEMultipart('alternative')
    msg['From'] = smtp_email
    msg['To'] = to_email
    msg['Subject'] = 'Audit Automatisation - Résultats et recommandations'
    
    # Email body
    body = f"""Bonjour {full_name},

Merci pour votre intérêt pour notre audit automatisation.

Nous avons analysé votre demande et souhaitons vous partager nos recommandations personnalisées.

Voici les prochaines étapes :

1. Consulter votre rapport d'audit personnalisé
2. Planifier un appel de 30 minutes pour discuter de la mise en place
3. Recevoir votre plan d'action détaillé

Cliquez ici pour accéder à votre espace personnel : [LIEN]

Cordialement,
L'équipe Automatisation
"""
    
    msg.attach(MIMEText(body, 'plain'))
    
    # Send email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_email, smtp_password)
            server.send_message(msg)
        print(f'Email sent to {to_email}')
        return True
    except Exception as e:
        print(f'Error sending email to {to_email}: {e}')
        return False


def process_scheduled_emails():
    """Check sheet for emails to send and send them."""
    sheet_id = os.environ.get('GOOGLE_SHEET_ID')
    if not sheet_id:
        raise ValueError('GOOGLE_SHEET_ID environment variable not set')
    
    client = get_google_sheets_client()
    sheet = client.open_by_key(sheet_id).sheet1
    
    # Get all rows
    all_rows = sheet.get_all_values()
    
    if len(all_rows) <= 1:
        print('No leads found')
        return 0
    
    headers = all_rows[0]
    rows = all_rows[1:]
    
    # Find column indices
    col_date_envoi = headers.index('Date envoi email programmé')
    col_email_envoye = headers.index('Email envoyé')
    col_email = headers.index('Email')
    col_nom = headers.index('Nom complet')
    col_statut = headers.index('Statut')
    
    now = datetime.now()
    emails_sent = 0
    
    for idx, row in enumerate(rows, start=2):  # Start at 2 (1 for header, +1 for 1-indexing)
        if len(row) <= max(col_date_envoi, col_email_envoye, col_email, col_nom):
            continue
        
        date_envoi_str = row[col_date_envoi]
        email_envoye = row[col_email_envoye] if col_email_envoye < len(row) else ''
        
        # Skip if already sent
        if email_envoye.lower() == 'oui':
            continue
        
        # Check if it's time to send
        if date_envoi_str:
            try:
                date_envoi = datetime.strptime(date_envoi_str, '%d/%m/%Y %H:%M')
                if now >= date_envoi:
                    # Send email
                    to_email = row[col_email]
                    full_name = row[col_nom]
                    
                    if send_email(to_email, full_name):
                        # Update sheet
                        sheet.update_cell(idx, col_email_envoye + 1, 'Oui')
                        sheet.update_cell(idx, col_statut + 1, 'Email envoyé')
                        emails_sent += 1
            except ValueError:
                print(f'Invalid date format in row {idx}: {date_envoi_str}')
    
    print(f'Sent {emails_sent} emails')
    return emails_sent


def main():
    """Main function."""
    print('Checking for scheduled emails...')
    
    try:
        emails_sent = process_scheduled_emails()
        print(f'Process completed: {emails_sent} emails sent')
        return 0
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
