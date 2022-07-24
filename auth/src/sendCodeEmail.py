import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
class EmailToSend():
    def __init__(self, reciver_email, message):
        self.title = f"""
            Your App Account Password Reset: noreply
        """
        self.reciver_email = reciver_email
        self.message = f"""
            We have received a request to reset your password. Please copy the following code: {message} - and forward it to enable the password reset process and choose a new password. Otherwise, you can ignore this email.
        """
    def send(self):
        sender_email = os.getenv("EMAIL_RECOVERY_USERNAME_AUTH")
        sender_password = os.getenv("EMAIL_RECOVERY_PASSWORD_AUTH")
        smtp_host = os.getenv("EMAIL_RECOVERY_HOST_AUTH")
        smtp_port = os.getenv("EMAIL_RECOVERY_PORT_AUTH")
        from_addr = sender_email
        to = self.reciver_email  

        msg = MIMEMultipart()
        msg["from_addr"] = from_addr
        msg["to"] = to 
        msg["Subject"] = self.title

        body = self.message
        msg.attach(MIMEText(body, "Plain"))

        server = smtplib.SMTP(smtp_host, smtp_port)
        server.ehlo()
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(from_addr, to, text)
        
        return {"email_sended": True}