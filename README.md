# 🚀 AWS Cloud Security Monitoring System 🔐

![AWS Security](https://user-images.githubusercontent.com/your-image.png)  

### **A Real-Time Security Monitoring System for AWS CloudTrail**
This project automates **AWS security monitoring**, detects **suspicious activity**, and **sends alerts via Slack, Discord, and Email**. It also **visualizes security logs in a real-time dashboard** using **Streamlit**.

---

## 📜 **Features**
✅ **Monitors AWS CloudTrail logs in real-time**  
✅ **Detects security threats** 🚨 (e.g., unauthorized access, privilege escalations)  
✅ **Sends alerts via Slack, Discord, and Email** 📩  
✅ **Stores security logs in AWS DynamoDB** 📊  
✅ **Provides a web dashboard using Streamlit** 🌐  
✅ **Exposes an API using AWS Lambda & API Gateway**  

---

## 📌 **Tech Stack**
🔹 **Cloud:** AWS (CloudTrail, Lambda, DynamoDB, API Gateway, EC2)  
🔹 **Programming Language:** Python  
🔹 **Automation:** Boto3 (AWS SDK for Python)  
🔹 **Data Storage:** DynamoDB  
🔹 **Alerting:** Email (SMTP), Slack Webhooks, Discord Webhooks  
🔹 **Visualization:** Streamlit  

---

## 🚀 **How It Works**
### **1️⃣ AWS CloudTrail Security Monitoring**
- The system **fetches logs from AWS CloudTrail**  
- It detects **suspicious security events** (e.g., unauthorized access)  
- Stores logs in **AWS DynamoDB**  

### **2️⃣ Real-Time Alerts**
- Sends **alerts to Slack, Discord, and Email** 📩  
- Notifies of **critical security threats**  

### **3️⃣ Web Dashboard**
- Displays security logs in a **real-time Streamlit dashboard**  
- Filters logs by **risk level (Critical, Medium, Low)**  
- Visualizes security trends with **graphs and charts** 📊  

### **4️⃣ Exposed API for Security Logs**
- Uses **AWS Lambda + API Gateway** to expose logs  
- Allows external applications to **query security data**  

---

✅ The dashboard will be available at: http://localhost:8501

🔔 Security Alerts & Notifications

* 🟢 Discord Alerts: Configured via Webhooks
 
* 🔵 Slack Alerts: Uses Slack Incoming Webhooks
  
* 📩 Email Alerts: Sent via SMTP (Gmail, Outlook, etc.)
  
🌍 Deployment on AWS

1️⃣ Deploying the Web Dashboard to AWS EC2

* The dashboard is hosted on AWS EC2 using a t2.micro instance
  
* To keep Streamlit running, we use screen for background execution

  
2️⃣ Exposing API Gateway

* The security logs API is exposed via AWS API Gateway
  
* Logs are fetched from DynamoDB using AWS Lambda


🚀 Maintained by [Victor Hugo Grando](https://www.linkedin.com/in/vhgrando/)

Follow me for more AWS & Cybersecurity projects! 🚀
