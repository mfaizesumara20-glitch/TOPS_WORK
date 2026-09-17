<!-- # Beginner OTP Sender

This Python program creates a six-digit OTP, sends it to the receiver number in `otp_sender.py` using Twilio, and then checks the OTP entered by the user.

## Setup

1. Install Python and then install Twilio:

   ```powershell
   pip install twilio
   ```

2. Create a Twilio account, obtain an Account SID, Auth Token, and a Twilio phone number.

3. Set the credentials for the current PowerShell window:

   ```powershell
   $env:TWILIO_ACCOUNT_SID="SKaa7b5a1d19cb84c67cab8adfed1c245f"
   $env:TWILIO_AUTH_TOKEN="008d891fb4ff4bada6c17fea6b6f700b"
   $env:TWILIO_PHONE_NUMBER="+17372508034"
   ```

4. Run it:

   ```powershell
   python otp_sender.py
   ```

The receiver number is set near the bottom of `otp_sender.py`:

```python
RECEIVER_NUMBER = "+919998003879"
```

Change that value whenever you want to send to another number. Phone numbers must be in international format, for example `+919876543210`.

Without Twilio credentials, the program runs in learning/demo mode and prints the OTP instead of sending an SMS.

> This is a learning example. A production system should expire OTPs quickly, limit retry attempts, and store only a secure hash of each OTP. -->
