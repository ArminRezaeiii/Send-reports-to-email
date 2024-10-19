import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


sender_email = "your_email@gmail.com"  
receiver_email = "recipient_email@example.com"  
password = "your_password" 


report_content = """
این یک گزارش نمونه است.
این گزارش می‌تواند شامل اطلاعات مختلف باشد.
"""


report_file_path = "report.txt"
with open(report_file_path, "w") as file:
    file.write(report_content)


subject = "گزارش روزانه"
body = "لطفاً گزارش پیوست شده را مشاهده کنید."

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject


msg.attach(MIMEText(body, 'plain'))


with open(report_file_path, "rb") as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={report_file_path}')
    msg.attach(part)

try:

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  
    server.login(sender_email, password) 
    server.send_message(msg) 
    print("Email sent successfully with the report attached!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()  
