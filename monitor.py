import boto3
import json
import smtplib
from email.message import EmailMessage

# AWS CloudTrail client
client = boto3.client('cloudtrail', region_name='us-east-1')

# Suspicious actions to watch for
suspicious_actions = [
    "CreateUser", "DeleteUser", "AttachUserPolicy", "DetachUserPolicy",
    "CreateAccessKey", "DeleteAccessKey", "UpdateAssumeRolePolicy",
    "PutRolePolicy", "CreatePolicy", "DeletePolicy", "ListPolicies"
]

# Fetch recent CloudTrail events
response = client.lookup_events(MaxResults=50)

# Track detected events
suspicious_events = []

# Process logs and filter only suspicious actions
for event in response['Events']:
    event_data = json.loads(event['CloudTrailEvent'])
    event_name = event_data.get('eventName', 'Unknown')

    if event_name in suspicious_actions:
        log_entry = f"\n🚨 **ALERT: Suspicious Activity Detected!** 🚨\n"
        log_entry += f"User: {event_data.get('userIdentity', {}).get('arn', 'Unknown')}\n"
        log_entry += f"Action: {event_name}\n"
        log_entry += f"Date: {event_data.get('eventTime')}\n"
        log_entry += "-" * 40

        print(log_entry)
        suspicious_events.append(log_entry)

# Save logs to a file
with open("security_log.txt", "a") as log_file:
    if suspicious_events:
        log_file.write("\n".join(suspicious_events) + "\n")
    else:
        log_file.write("\n✅ No suspicious activity detected.\n")


# Send Email Alert if suspicious events found
def send_email_alert(alert_message):
    sender_email = "victorhugogrando@gmail.com"  # Replace with your email
    sender_password = "knqj ilgb vjwj wybh"  # Replace with your Gmail App Password
    receiver_email = "vhgrandobusiness@gmail.com"  # Replace with the recipient's email

    subject = "🚨 AWS Security Alert - Suspicious Activity Detected!"

    msg = EmailMessage()
    msg.set_content(alert_message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print("\n📩 Email Alert Sent Successfully!\n")
    except smtplib.SMTPAuthenticationError:
        print("\n❌ Authentication Error: Check your email and App Password.")
    except smtplib.SMTPException as smtp_error:
        print(f"\n⚠️ SMTP Error: {smtp_error}")
    except Exception as e:
        print(f"\n⚠️ Failed to send email: {e}")


# Send email if suspicious events exist
if suspicious_events:
    send_email_alert("\n".join(suspicious_events))
else:
    print("\n✅ No security issues detected. Your AWS environment is safe!\n")
