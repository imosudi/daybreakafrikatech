from. import mail
from flask_mail import Mail, Message
from datetime import datetime
import os


# ============================================
# EMAIL FUNCTIONS
# ============================================


def send_admin_notification(ip_address, name, email, company, service, message):
    """Send email notification to admin"""
    try:
        msg = Message(
            subject=f'New Contact Form Submission from {name}',
            recipients=['info@daybreakafrika.com.ng'],  # Admin email
            body=f"""
New contact form submission:

Name: {name}
Email: {email}
Company: {company}
Service Interest: {service}

Message:
{message}

---
Submitted at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            """,
            html=f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
        .header {{ background: linear-gradient(135deg, #0066CC 0%, #00B4D8 100%); color: white; padding: 20px; border-radius: 8px 8px 0 0; }}
        .content {{ background: #f9f9f9; padding: 20px; border-radius: 0 0 8px 8px; }}
        .field {{ margin-bottom: 15px; }}
        .label {{ font-weight: bold; color: #0066CC; }}
        .message-box {{ background: white; padding: 15px; border-left: 4px solid #00B4D8; margin-top: 10px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h2>New Contact Form Submission</h2>
        </div>
        <div class="content">
            <div class="field">
                <span class="label">Name:</span> {name}
            </div>
            <div class="field">
                <span class="label">Email:</span> <a href="mailto:{email}">{email}</a>
            </div>
            <div class="field">
                <span class="label">Company:</span> {company}
            </div>
            <div class="field">
                <span class="label">Service Interest:</span> {service}
            </div>
            <div class="field">
                <span class="label">Message:</span>
                <div class="message-box">{message}</div>
            </div>
            <hr>
            <p style="color: #666; font-size: 12px;">
                Submitted at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            </p>
        </div>
    </div>
</body>
</html>
            """
        )
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Error sending admin notification: {str(e)}")
        return False
    

def send_user_confirmation(name, email):
    """Send confirmation email to user"""
    try:
        msg = Message(
            subject='Thank you for contacting Daybreak Afrika Technologies',
            recipients=[email],
            body=f"""
Dear {name},

Thank you for reaching out to Daybreak Afrika Technologies!

We have received your message and will get back to you within 24 hours.

In the meantime, feel free to explore our services at www.daybreakafrika.com.ng or contact us directly:

📧 Email: info@daybreakafrika.com.ng
📞 Phone: +234 809 867 3498
💬 WhatsApp: +234 809 867 3498

Best regards,
Daybreak Afrika Technologies Team
            """,
            html=f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
        .header {{ background: linear-gradient(135deg, #0066CC 0%, #00B4D8 100%); color: white; padding: 30px; text-align: center; border-radius: 8px 8px 0 0; }}
        .content {{ background: #f9f9f9; padding: 30px; border-radius: 0 0 8px 8px; }}
        .button {{ display: inline-block; padding: 12px 30px; background: #00B4D8; color: white; text-decoration: none; border-radius: 6px; margin: 20px 0; }}
        .footer {{ text-align: center; margin-top: 20px; color: #666; font-size: 12px; }}
        .contact-info {{ background: white; padding: 20px; border-radius: 8px; margin: 20px 0; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Thank You!</h1>
        </div>
        <div class="content">
            <p>Dear {name},</p>
            <p>Thank you for reaching out to <strong>Daybreak Afrika Technologies</strong>!</p>
            <p>We have received your message and will get back to you within <strong>24 hours</strong>.</p>
            
            <div class="contact-info">
                <h3 style="color: #0066CC; margin-top: 0;">Contact Information</h3>
                <p>📧 <strong>Email:</strong> info@daybreakafrika.com.ng</p>
                <p>📞 <strong>Phone:</strong> +234 809 867 3498</p>
                <p>💬 <strong>WhatsApp:</strong> +234 809 867 3498</p>
            </div>
            
            <center>
                <a href="https://www.daybreakafrika.com.ng" class="button">Visit Our Website</a>
            </center>
            
            <p>Best regards,<br><strong>Daybreak Afrika Technologies Team</strong></p>
        </div>
        <div class="footer">
            <p>© 2025 Daybreak Afrika Technologies. All rights reserved.</p>
        </div>
    </div>
</body>
</html>
            """
        )
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Error sending user confirmation: {str(e)}")
        return False

