import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from django.conf import settings
import os
from decouple import config



ADMIN_EMAIL = settings.ADMIN_EMAIL
FROM_EMAIL = settings.FROM_EMAIL
EMAIL_PASSWORD = settings.EMAIL_PASSWORD
EMAIL_SMTP_SERVER = settings.EMAIL_SMTP_SERVER
EMAIL_SMTP_PORT=465
MAIN_ADMIN = ADMIN_EMAIL


def send_beautiful_html_email_create_user(bank_id, account_details, to_email):
    # Email subject
    subject = "Welcome to HSBC Bank"
    
    # Create the HTML content
    html_content = f"""
    <html>
    <body style="font-family: Arial, sans-serif; color: #333; background-color: #f4f4f4; padding: 20px;">
        <div style="max-width: 600px; margin: auto; background-color: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
            <h2 style=" text-align: center;">Welcome to HSBC Bank!</h2>
            <p style="font-size: 16px; line-height: 1.6;">
                Dear Customer,
            </p>
            <p style="font-size: 16px; line-height: 1.6;">
                Your bank ID is: <strong>{bank_id}</strong>
            </p>
            <p style="font-size: 16px; line-height: 1.6;">
                We're thrilled to have you with us. If you have any questions, feel free to reach out to our customer service team.
            </p>
            <p style="text-align: center; font-size: 14px; color: #777; margin-top: 30px;">
                © 2025 HSBC Bank. All rights reserved.
            </p>
        </div>
    </body>
    </html>
    """
    # 
    # Set up the email message
    msg = MIMEMultipart()
    msg['From'] = f"HSBC Bank <{FROM_EMAIL}>"
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the HTML content to the email
    msg.attach(MIMEText(html_content, 'html'))

    try:
        # Set up the SMTP server connection using SSL
        with smtplib.SMTP_SSL(EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT) as server:
            server.login(FROM_EMAIL, EMAIL_PASSWORD)  # Log in with Hostinger credentials
            
            # Send the email
            server.sendmail(FROM_EMAIL, to_email, msg.as_string())
        
        print(f"HTML email successfully sent to {to_email}!")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")




def send_admin_mail(message, subject="Admin Message"):
    # Email content
    subject = subject
    html_content = f"""
    <html>
    <body>
        <div style="max-width: 600px; margin: auto; background-color: #ffffff; padding: 20px;">
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="https://res.cloudinary.com/daf9tr3lf/image/upload/v1742379468/1_ptuuq7.png" alt="Logo" style="width: 150px;"/>
            </div>
            <p>{message}</p>
            
            <p>This message is directly to the admin strictly for notification purposes,</p>
            <p>Thank you.</p>
            <p style="text-align: center; font-size: 14px; color: #777; margin-top: 30px;">
                © 2025 HSBC Bank. All rights reserved.
            </p>
        </div>
    </body>
    </html>
    """
    
    msg = MIMEMultipart()
    msg['From'] = f"HSBC Bank <{FROM_EMAIL}>"
    msg['To'] = MAIN_ADMIN
    msg['Subject'] = subject
    msg.attach(MIMEText(html_content, 'html'))
    


    try:
        # Set up the SMTP server connection using SSL
        with smtplib.SMTP_SSL(EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT) as server:
            server.login(ADMIN_EMAIL, EMAIL_PASSWORD)  # Log in with Hostinger credentials
            
            # Send the email
            server.sendmail(FROM_EMAIL, ADMIN_EMAIL, msg.as_string())
        
        print(f"HTML email successfully sent to {ADMIN_EMAIL}!")
    except Exception as e:
        print(f"Failed to send email to {ADMIN_EMAIL}: {e}")


def send_ordinary_user_mail(to_email, message, subject="User message"):
    # Email content
    subject = subject
    html_content = f"""
    <html>
    <body>
        <div style="max-width: 600px; margin: auto; background-color: #ffffff; padding: 20px;">
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="https://res.cloudinary.com/daf9tr3lf/image/upload/v1742379468/1_ptuuq7.png" alt="Logo" style="width: 150px;"/>
            </div>
            <p>{message}</p>
            
            <p>Thank you for banking with us.</p>
            <p>If you didn't request this, please ignore this email.</p>
            <p>Thank you.</p>
            <p style="text-align: center; font-size: 14px; color: #777; margin-top: 30px;">
                © 2025 HSBC Bank. All rights reserved.
            </p>
        </div>
    </body>
    </html>
    """
    
    msg = MIMEMultipart()
    msg['From'] = f"HSBC Bank <{FROM_EMAIL}>"
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(html_content, 'html'))
    

    try:
        # Set up the SMTP server connection using SSL
        with smtplib.SMTP_SSL(EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT) as server:
            server.login(ADMIN_EMAIL, EMAIL_PASSWORD)  # Log in with Hostinger credentials
            
            # Send the email
            server.sendmail(ADMIN_EMAIL, to_email, msg.as_string())
        
        print(f"HTML email successfully sent to {ADMIN_EMAIL}!")
    except Exception as e:
        print(f"Failed to send email to {ADMIN_EMAIL}: {e}")




def send_beautiful_html_email_create_account(
    account_name, 
    account_details, 
    to_email, 
    bank_id
):
    # Email subject
    subject = "Welcome to Our Bank"
    
    # Create the HTML content
    html_content = f"""
    <html>
    <body style="font-family: Arial, sans-serif; color: #333; background-color: #f4f4f4; padding: 20px;">
        <div style="max-width: 600px; margin: auto; background-color: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="https://res.cloudinary.com/daf9tr3lf/image/upload/v1742379468/1_ptuuq7.png" alt="Bank Logo" style="width: 150px; height: auto;"/>
            </div>
            <h2 style=" text-align: center;">Welcome to Our Bank!</h2>
            <p style="font-size: 16px; line-height: 1.6;">
                Dear customer,
            </p>
            <p style="font-size: 16px; line-height: 1.6;">
                Your bank ID is: <strong>{bank_id}</strong>
            </p>
            <p style="font-size: 16px; line-height: 1.6;">
                You can now log into your account with your bank ID.
            </p>

    
            <p style="font-size: 16px; line-height: 1.6;">
                We're thrilled to have you with us. If you have any questions, feel free to reach out to our customer service team.
            </p>
            <p style="text-align: center; font-size: 14px; color: #777; margin-top: 30px;">
                © 2025 HSBC Bank. All rights reserved.
            </p>
        </div>
    </body>
    </html>
    """
    
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = f"HSBC Bank <{FROM_EMAIL}>"
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # Attach the HTML content
    msg.attach(MIMEText(html_content, 'html'))
    


    try:
        # Set up the SMTP server connection using SSL
        with smtplib.SMTP_SSL(EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT) as server:
            server.login(ADMIN_EMAIL, EMAIL_PASSWORD)  # Log in with Hostinger credentials
            
            # Send the email
            server.sendmail(ADMIN_EMAIL, to_email, msg.as_string())
        
        print(f"HTML email successfully sent to {to_email}!")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")




def send_beautiful_html_email_create_account(
    initial_deposit,
    info_details,
    account_name, 
    account_details,  # This should be a dictionary with details like {"Account Number": "123456789", "Account Type": "Savings", "Branch": "Main"}
    to_email
):
    # Email subject
    subject = f"Thank you for banking with us - {info_details}"
    
    # Generate table rows from account details
    account_details_html = "".join([
        f"<tr><td style='padding: 8px; border: 1px solid #ddd;'>{key}</td><td style='padding: 8px; border: 1px solid #ddd;'>{value}</td></tr>"
        for key, value in account_details.items()
    ])
    
    # Create the HTML content
    html_content = f"""
    <html>
    <body style="font-family: Arial, sans-serif; color: #333; background-color: #f4f4f4; padding: 20px;">
        <div style="max-width: 600px; margin: auto; background-color: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="https://res.cloudinary.com/daf9tr3lf/image/upload/v1742379468/1_ptuuq7.png" alt="Bank Logo" style="width: 150px; height: auto;"/>
            </div>
            
            <p style="font-size: 16px; line-height: 1.6;">
                Dear {account_name},
            </p>
            <p style="font-size: 16px; line-height: 1.6;">
                {info_details}
                
            </p>
            <h3 style="color: #333;">Your Account Details:</h3>
            <table style="width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 16px;">
                {account_details_html}
            </table>
            <p style="font-size: 16px; line-height: 1.6;">
                We're thrilled to have you with us. If you have any questions, feel free to reach out to our customer service team.
            </p>
            <h2 style=" text-align: center;">Thank you for banking with us, {account_name}!</h2>
            <p style="text-align: center; font-size: 14px; color: #777; margin-top: 30px;">
                © 2025 HSBC Bank. All rights reserved.
            </p>
        </div>
    </body>
    </html>
    """
    
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = f"HSBC Bank <{FROM_EMAIL}>"
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # Attach the HTML content
    msg.attach(MIMEText(html_content, 'html'))
    

    try:
        # Set up the SMTP server connection
        server = smtplib.SMTP(EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT)
        server.starttls()  # Secure the connection
        server.login(ADMIN_EMAIL, EMAIL_PASSWORD)
        
        # Send the email
        server.sendmail(ADMIN_EMAIL, to_email, msg.as_string())
        
        # Close the SMTP server connection
        server.quit()
        
        print("HTML email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")






def send_password_reset_email(to_email, reset_link):
    # Email content
    subject = "Password Reset Request"
    html_content = f"""
    <html>
    <body>
        <div style="max-width: 600px; margin: auto; background-color: #ffffff; padding: 20px;">
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="https://res.cloudinary.com/daf9tr3lf/image/upload/v1742379468/1_ptuuq7.png" alt="Logo" style="width: 150px;"/>
            </div>
            <h2>Password Reset</h2>
            <p>You requested a password reset. Click the link below to set a new password:</p>
            <a href="{reset_link}" style="display:inline-block; padding:10px; background- color:white; text-decoration:none;">
                Reset Password
            </a>
            <p>If you didn't request this, please ignore this email.</p>
            <p>Thank you.</p>
            <p style="text-align: center; font-size: 14px; color: #777; margin-top: 30px;">
                © 2025 HSBC Bank. All rights reserved.
            </p>
        </div>
    </body>
    </html>
    """
    
    msg = MIMEMultipart()
    msg['From'] = f"HSBC Bank <{FROM_EMAIL}>"
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(html_content, 'html'))
    
    
    try:
        with smtplib.SMTP(EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT) as server:
            server.starttls()
            server.login(ADMIN_EMAIL,EMAIL_PASSWORD)
            server.sendmail(ADMIN_EMAIL, to_email, msg.as_string())
        print(f"Email sent successfully to {to_email}.")
    except Exception as e:
        print(f"Failed to send email: {e}")





def send_otp_code_verification(to_email, otp_code, transaction_type):
    # Email content
    subject = "OTP Verification"
    html_content = f"""
    <html>
    <body>
        <div style="max-width: 600px; margin: auto; background-color: #ffffff; padding: 20px;">
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="https://res.cloudinary.com/daf9tr3lf/image/upload/v1742379468/1_ptuuq7.png" alt="Logo" style="width: 150px;"/>
            </div>
            <h2>OTP Verification</h2>
            <p>Your transaction is almost complete. We noticed you are trying to initiate a {transaction_type}.</p>
            <p>The OTP Code is required to complete the transaction is: {otp_code}.</p>
            
            <p>Please keep this OTP code a secret. Do not reveal your it to anyone.</p> 
            <p>Thank you.</p>
            <p style="text-align: center; font-size: 14px; color: #777; margin-top: 30px;">
                © 2025 HSBC Bank. All rights reserved.
            </p>
        </div>
    </body> 
    </html>
    """
    
    msg = MIMEMultipart()
    msg['From'] = f"HSBC Bank <{FROM_EMAIL}>"
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(html_content, 'html'))
    

    try:
        # Set up the SMTP server connection using SSL
        with smtplib.SMTP_SSL(EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT) as server:
            server.login(ADMIN_EMAIL, EMAIL_PASSWORD)  # Log in with Hostinger credentials
            
            # Send the email
            server.sendmail(ADMIN_EMAIL, to_email, msg.as_string())
        
        print(f"HTML email successfully sent to {ADMIN_EMAIL}!")
    except Exception as e:
        print(f"Failed to send email to {ADMIN_EMAIL}: {e}")





def send_transaction_mail(to_email, message, subject="OTP Verification"):
    # Email content
    subject = "Transfer Pending"
    html_content = f"""
    <html>
    <body>
        <div style="max-width: 600px; margin: auto; background-color: #ffffff; padding: 20px;">
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="https://res.cloudinary.com/daf9tr3lf/image/upload/v1742379468/1_ptuuq7.png" alt="Logo" style="width: 150px;"/>
            </div>
            <p>Your transaction is almost complete.</p>
            <p>{message}</p>
            
            <p>If you didn't request perform a transaction, please ignore this email.</p>
            <p>Thanks for banking with us.</p>
            <p style="text-align: center; font-size: 14px; color: #777; margin-top: 30px;">
                © 2025 HSBC Bank. All rights reserved.
            </p>
        </div>
    </body>
    </html>
    """
    
    msg = MIMEMultipart()
    msg['From'] = f"HSBC Bank <{FROM_EMAIL}>"
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(html_content, 'html'))
    

    try:
        # Set up the SMTP server connection using SSL
        with smtplib.SMTP_SSL(EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT) as server:
            server.login(ADMIN_EMAIL, EMAIL_PASSWORD)  # Log in with Hostinger credentials
            
            # Send the email
            server.sendmail(ADMIN_EMAIL, to_email, msg.as_string())
        
        print(f"HTML email successfully sent to {ADMIN_EMAIL}!")
    except Exception as e:
        print(f"Failed to send email to {ADMIN_EMAIL}: {e}")







def send_contact_mail( message, subject="Mail from Customer", to_email=ADMIN_EMAIL,):
    # Email content
    subject = subject
    html_content = f"""
    <html>
    <body>
        <div style="max-width: 600px; margin: auto; background-color: #ffffff; padding: 20px;">
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="https://res.cloudinary.com/daf9tr3lf/image/upload/v1742379468/1_ptuuq7.png" alt="Logo" style="width: 150px;"/>
            </div>
            <p>{message}</p>
            
            
            <p>Thank you.</p>
            <p style="text-align: center; font-size: 14px; color: #777; margin-top: 30px;">
                © 2025 HSBC Bank. All rights reserved.
            </p>
        </div>
    </body>
    </html>
    """
    
    msg = MIMEMultipart()
    msg['From'] = f"HSBC Bank <{FROM_EMAIL}>"
    msg['To'] = ADMIN_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(html_content, 'html'))
    
    try:
        with smtplib.SMTP(EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT) as server:
            server.starttls()
            server.login(ADMIN_EMAIL, EMAIL_PASSWORD)
            server.sendmail(ADMIN_EMAIL, ADMIN_EMAIL, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")




def send_mail_from_admin_to_user(to_email, message, subject):
    # Email content
    subject = subject
    html_content = f"""
    <html>
    <body>
        <div style="max-width: 600px; margin: auto; background-color: #ffffff; padding: 20px;">
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="https://res.cloudinary.com/daf9tr3lf/image/upload/v1742379468/1_ptuuq7.png" alt="Logo" style="width: 150px;"/>
            </div>
            <p>{message}</p>
            
            <p>Thank you for banking with us.</p>
            <p style="text-align: center; font-size: 14px; color: #777; margin-top: 30px;">
                © 2025 HSBC Bank. All rights reserved.
            </p>
        </div>
    </body>
    </html>
    """
    
    msg = MIMEMultipart()
    msg['From'] = f"HSBC Bank <{FROM_EMAIL}>"
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(html_content, 'html'))
    
    
    try:
        with smtplib.SMTP(EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT) as server:
            server.starttls()
            server.login(ADMIN_EMAIL, EMAIL_PASSWORD)
            server.sendmail(ADMIN_EMAIL, ADMIN_EMAIL, msg.as_string())
        print("email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")


def send_mail_for_payment_options(to_email, message, subject):
    # Email HTML content
    html_content = f"""
    <html>
    <body>
        <div style="max-width: 600px; margin: auto; background-color: #ffffff; padding: 20px;">
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="https://res.cloudinary.com/daf9tr3lf/image/upload/v1742379468/1_ptuuq7.png" alt="Logo" style="width: 150px;"/>
            </div>
            <p>{message}</p>
            
            <p>Thank you for banking with us.</p>
            <p style="text-align: center; font-size: 14px; color: #777; margin-top: 30px;">
                © 2025 HSBC Bank. All rights reserved.
            </p>
        </div>
    </body>
    </html>
    """
    
    # Create the email message
    msg = MIMEMultipart('related')  # Use 'related' to attach inline images
    msg['From'] = f"HSBC Bank <{FROM_EMAIL}>"
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # Attach the HTML content
    msg_alternative = MIMEMultipart('alternative')
    msg.attach(msg_alternative)
    msg_alternative.attach(MIMEText(html_content, 'html'))
    

    # Send the email
    try:
        with smtplib.SMTP(EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT) as server:
            server.starttls()
            server.login(ADMIN_EMAIL, EMAIL_PASSWORD)
            server.sendmail(ADMIN_EMAIL, to_email, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")






