#!/usr/bin/env python3
"""Generate daily lead report and send to Slack."""

import json
import os
import sys
from datetime import datetime, timedelta
import gspread
from google.oauth2.service_account import Credentials
import requests


def get_google_sheets_client():
    """Initialize Google Sheets client."""
    creds_json = os.environ.get('GOOGLE_SERVICE_ACCOUNT_JSON')
    if not creds_json:
        raise ValueError('GOOGLE_SERVICE_ACCOUNT_JSON not set')
    
    creds_dict = json.loads(creds_json)
    creds = Credentials.from_service_account_info(
        creds_dict,
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )
    return gspread.authorize(creds)


def generate_report():
    """Generate daily report from Google Sheets."""
    sheet_id = os.environ.get('GOOGLE_SHEET_ID')
    if not sheet_id:
        raise ValueError('GOOGLE_SHEET_ID not set')
    
    client = get_google_sheets_client()
    sheet = client.open_by_key(sheet_id).sheet1
    
    # Get all data
    all_rows = sheet.get_all_values()
    
    if len(all_rows) <= 1:
        return {
            'total': 0,
            'today': 0,
            'pending': 0,
            'sent': 0
        }
    
    headers = all_rows[0]
    rows = all_rows[1:]
    
    # Find column indices
    col_date = headers.index('Date réception')
    col_statut = headers.index('Statut')
    
    # Calculate stats
    total = len(rows)
    today = datetime.now().date()
    today_count = 0
    pending = 0
    sent = 0
    
    for row in rows:
        if len(row) > max(col_date, col_statut):
            # Count today's leads
            date_str = row[col_date].split()[0] if row[col_date] else ''
            try:
                lead_date = datetime.strptime(date_str, '%d/%m/%Y').date()
                if lead_date == today:
                    today_count += 1
            except (ValueError, IndexError):
                pass
            
            # Count by status
            statut = row[col_statut].lower() if col_statut < len(row) else ''
            if 'attente' in statut:
                pending += 1
            elif 'envoy' in statut:
                sent += 1
    
    return {
        'total': total,
        'today': today_count,
        'pending': pending,
        'sent': sent
    }


def send_report_to_slack(stats):
    """Send daily report to Slack."""
    webhook_url = os.environ.get('SLACK_WEBHOOK_URL')
    if not webhook_url:
        print('Warning: SLACK_WEBHOOK_URL not set')
        return
    
    message = {
        "text": f"📈 RAPPORT QUOTIDIEN DES LEADS\n\n"
                f"📊 Total des leads: {stats['total']}\n"
                f"🆕 Nouveaux aujourd'hui: {stats['today']}\n"
                f"⏳ En attente: {stats['pending']}\n"
                f"✅ Emails envoyés: {stats['sent']}\n\n"
                f"Date: {datetime.now().strftime('%d/%m/%Y')}"
    }
    
    try:
        response = requests.post(webhook_url, json=message, timeout=10)
        response.raise_for_status()
        print('Report sent to Slack')
    except Exception as e:
        print(f'Error sending report: {e}')


def main():
    """Main function."""
    print('Generating daily report...')
    
    try:
        stats = generate_report()
        print(f'Stats: {stats}')
        
        send_report_to_slack(stats)
        
        print('Report generation completed')
        return 0
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
