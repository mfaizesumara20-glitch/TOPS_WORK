# """A simple OTP sender and verifier.

# Install Twilio first for real SMS sending:
#     pip install twilio
# """

# import os
# import random


# def create_otp():
#     """Return a six-digit one-time password as text."""
#     return str(random.randint(100000, 999999))


# def send_otp(phone_number, otp):
#     """Send an OTP by SMS using Twilio.

#     Put your Twilio values in environment variables before running:
#     TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, and TWILIO_PHONE_NUMBER.
#     """
#     account_sid = os.getenv("TWILIO_ACCOUNT_SID")
#     auth_token = os.getenv("TWILIO_AUTH_TOKEN")
#     twilio_number = os.getenv("TWILIO_PHONE_NUMBER")

#     if not all([account_sid, auth_token, twilio_number]):
#         print("\nTwilio credentials are not set, so SMS was not sent.")
#         print("Demo OTP (only for learning):", otp)
#         return False

#     try:
#         from twilio.rest import Client

#         client = Client(account_sid, auth_token)
#         message = client.messages.create(
#             body=f"Your OTP is {otp}. Do not share it with anyone.",
#             from_=twilio_number,
#             to=phone_number,
#         )
#         print("OTP sent successfully. Message ID:", message.sid)
#         return True
#     except ImportError:
#         print("Install Twilio first: pip install twilio")
#     except Exception as error:
#         print("Could not send the OTP:", error)
#     return False


# def main():
#     print("--- OTP Sender ---")
#     phone_number = input("Enter phone number with country code (example: +919876543210): ").strip()

#     if not phone_number.startswith("+") or len(phone_number) < 8:
#         print("Please enter a valid phone number with its country code.")
#         return

#     otp = create_otp()
#     send_otp(phone_number, otp)

#     entered_otp = input("Enter the OTP to verify it: ").strip()
#     if entered_otp == otp:
#         print("OTP verified successfully!")
#     else:
#         print("Incorrect OTP.")


# if __name__ == "__main__":
#     main()
