import docx
import smtplib
import random
import string

# Generate OTP
def generate_otp(length=6):
    otp = ''.join(random.choices(string.digits, k=length))
    return otp

# Send OTP via email
def send_otp(email, otp):
    sender_email = "your_gmail"
    sender_password = "your_pass"
    
    subject = "Your OTP Code"
    body = f"Your OTP code is: {otp}"

    # Set up the SMTP server
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender_email, sender_password)
        message = f"Subject: {subject}\n\n{body}"
        
        # Send email
        server.sendmail(sender_email, email, message)
        server.quit()
        print(f"OTP sent to {email}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
email = "recipient_email@example.com"
otp = generate_otp(6)
send_otp(email, otp)
