# 🔊 AWS Polly Text-to-Speech Converter

A serverless Text-to-Speech application using **AWS Polly** and **AWS Lambda**.  
This project converts input text into natural-sounding speech (MP3 format) using AWS Polly voices.

---

## 🧠 Architecture

User Input → AWS Lambda → AWS Polly → MP3 Audio Output

---

## 🚀 Technologies Used

- AWS Polly
- AWS Lambda
- Python 3.12
- IAM Roles
- AWS Free Tier

---

## ⚙️ Setup Instructions

### 1️⃣ Create IAM Role
Attach:
- AWSLambdaBasicExecutionRole
- AmazonPollyFullAccess

### 2️⃣ Create Lambda Function
- Runtime: Python 3.12
- Upload `lambda_function.py`
- Assign IAM role

###🎙️ Supported Voices
Joanna (English – Female)
Matthew (English – Male)
Aditi (Indian English)
Kajal (Hindi)

#### CHange in Python to apply voices
#### >> Here : VoiceId='Aditi'

### 3️⃣ Test Event
```json
{
  "text": "Hello from AWS Polly"
}


