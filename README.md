🚀 AWS CloudTrail Security Monitor – Detect & Alert Suspicious AWS Activity

🔐 This Python-based security monitoring tool automates AWS CloudTrail log analysis to detect security-sensitive actions, such as user creation, access key generation, and policy changes. It logs all detected activities and sends real-time email alerts for security events.

🔍 Key Features

✅ Monitors AWS CloudTrail logs for security-related actions

✅ Detects and alerts on:

* IAM user creation (CreateUser)
* Access key generation (CreateAccessKey)
* Privilege changes (AttachUserPolicy, DetachUserPolicy)
* Policy modifications (PutRolePolicy, DeletePolicy)
  
✅ Stores logs securely in security_log.txt for auditing

✅ Sends real-time email alerts for immediate response

✅ Lightweight & efficient – Can run on any Python environment

🛠 Technologies Used

* Python
* AWS CloudTrail & Boto3
* SMTP for Email Alerts
* Logging for Security Analysis
  
🚀 How to Run the AWS Security Monitor

1️⃣ Install Dependencies
* pip install boto3
  
2️⃣ Configure AWS Credentials

* Ensure your AWS CLI is set up:
  
* aws configure

  
🔹 You'll be asked for:
  
* AWS Access Key ID
* AWS Secret Access Key
* Default region name → Use us-east-1 or your preferred AWS region
  
3️⃣ Run the Monitoring Script
* python3 monitor.py
  
🔹 If Suspicious Activity is Found:
* 🚨 An alert will appear on the screen
* 📩 An email will be sent (if SMTP is configured)
* 📜 The event will be logged in security_log.txt
  
🔹 If No Issues Are Found:
* ✅ The script will print:
* No security issues detected. Your AWS environment is safe!

  
📌 Example Output

🚨 **ALERT: Suspicious Activity Detected!** 🚨  

User: arn:aws:iam::123456789012:user/admin  
Action: **CreateAccessKey**  
Date: 2025-02-15T21:08:34Z  
----------------------------------------
✅ No security issues detected. Your AWS environment is safe.


📌 Future Improvements

🔹 🔗 Integrate Slack Alerts – Notify security teams instantly in a Slack channel

🔹 📊 Web Dashboard – Build a frontend to display AWS security events visually

🔹 🛡️ AWS GuardDuty Integration – Combine with GuardDuty for deeper security insights

🔹 📜 Log Filtering – Reduce false positives by refining CloudTrail queries

🔹 🎯 Multi-Region Support – Expand monitoring to multiple AWS regions
