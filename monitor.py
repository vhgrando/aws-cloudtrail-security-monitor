import boto3
import json
import requests
import smtplib
from email.message import EmailMessage

# AWS CloudTrail client
client = boto3.client('cloudtrail', region_name='us-east-1')

# Define event categories
CRITICAL_EVENTS = [
    "ConsoleLogin", "CreateUser", "DeleteUser", "AttachUserPolicy",
    "PutRolePolicy", "CreateAccessKey", "CreateRole"
]

MEDIUM_EVENTS = [
    "ChangePassword", "PutGroupPolicy", "DeletePolicy"
]

LOW_EVENTS = [
    "ListUsers", "ListPolicies"
]

# Webhook URLs (Replace with your actual Webhooks)
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1341137468656717874/QcansKijcqgVs7ThKry9wItKw7Z1L_DBpdrd2UOkkLOps_MtmjsmhjZe7OouYOgJNOe-"
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"

# Email configuration (Replace with your details)
SENDER_EMAIL = "victorhugogrando@gmail.com"
SENDER_PASSWORD = "knqj ilgb vjwj wybh"  # Use an App Password, not your real password
RECEIVER_EMAIL = "vhgrandobusiness@gmail.com"

# Function to send a message to Discord
def send_discord_alert(message):
    data = {"content": message}
    response = requests.post(DISCORD_WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print("\n✅ Discord alert sent successfully!")
    else:
        print(f"\n⚠️ Failed to send Discord alert: {response.text}")

# Function to send a message to Slack
def send_slack_alert(message):
    data = {"text": message}
    response = requests.post(SLACK_WEBHOOK_URL, json=data)
    if response.status_code == 200:
        print("\n✅ Slack alert sent successfully!")
    else:
        print(f"\n⚠️ Failed to send Slack alert: {response.text}")

# Function to send an email alert
def send_email_alert(alert_message):
    subject = "🚨 AWS Security Alert - Suspicious Activity Detected!"

    msg = EmailMessage()
    msg.set_content(alert_message)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
            print("\n📩 Security alert sent via email!")
    except Exception as e:
        print(f"\n⚠️ Failed to send email: {e}")

# Fetch recent CloudTrail events
response = client.lookup_events(MaxResults=50)

suspicious_events = []

# Process logs and classify events
for event in response['Events']:
    event_data = json.loads(event['CloudTrailEvent'])
    event_name = event_data.get('eventName', 'Unknown')
    user_identity = event_data.get('userIdentity', {}).get('arn', 'Unknown')
    event_time = event_data.get('eventTime')

    # Define risk level
    if event_name in CRITICAL_EVENTS:
        risk_level = "🚨 CRITICAL"
    elif event_name in MEDIUM_EVENTS:
        risk_level = "⚠️ MEDIUM"
    elif event_name in LOW_EVENTS:
        risk_level = "🔎 LOW"
    else:
        risk_level = None  # Ignore irrelevant events

    # If the event is relevant, log it and send alerts
    if risk_level:
        log_entry = f"{risk_level} | User: {user_identity} | Action: {event_name} | Date: {event_time}"
        print(log_entry)
        suspicious_events.append(log_entry)

        # Send alerts to Slack, Discord, and Email
        send_slack_alert(log_entry)
        send_discord_alert(log_entry)
        send_email_alert(log_entry)

# Save logs to a file
with open("security_log.txt", "a") as log_file:
    if suspicious_events:
        log_file.write("\n".join(suspicious_events) + "\n")
    else:
        log_file.write("\n✅ No suspicious activity detected.\n")

print("\n✅ Script execution completed!")
