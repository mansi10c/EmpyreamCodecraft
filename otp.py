import random
def generate_otp():
    # Generate a random 6-digit OTP
    otp = str(random.randint(100000, 999999))
    return otp
def send_otp(otp, phone_number):
    # Send the OTP to the user's phone number
    print(f"Sending OTP {otp} to phone number {phone_number}")
def verify_otp(otp, user_input):
    # Verify the OTP entered by the user
    if otp == user_input:
        print("OTP verification successful")
    else:
        print("OTP verification failed")
if __name__ == "__main__":
    phone_number = input("Enter your phone number: ")
    otp = generate_otp()
    send_otp(otp, phone_number)
    user_input = input("Enter the OTP: ")
    verify_otp(otp, user_input)
