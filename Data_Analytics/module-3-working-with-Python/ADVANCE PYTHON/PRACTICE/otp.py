# #  997692 password

# import requests
# import random

# # Your 2Factor API key
# API_KEY = "3a67bad7-adcf-11f1-90d7-0200cd936042"

# # Receiver's mobile number
# phone = "+918320993969"

# # Generate 6-digit OTP
# otp = str(random.randint(100000, 999999))

# # 2Factor API URL
# url = f"https://2factor.in/API/V1/{API_KEY}/SMS/{phone}/{otp}"

# try:
#     response = requests.get(url)

#     print("Status Code:", response.status_code)
#     print("Response:", response.text)

#     if response.status_code == 200:
#         print("OTP sent successfully!")

#         # Ask user to enter OTP
#         entered_otp = input("Enter the OTP you received: ")

#         # Check OTP
#         if entered_otp == otp:
#             print("OTP verified successfully! ✅")
#         else:
#             print("Invalid OTP! ❌")

# except requests.exceptions.RequestException as e:
#     print("Error:", e)





   