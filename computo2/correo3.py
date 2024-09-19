import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

servidor = "smtp.gmail.com"
puerto = 587
correo = "daniel.borjxl24@gmail.com"
contra = "twfh fkhm atvh xzsi"

try:
    conex = smtplib.SMTP(servidor, puerto)
    conex.starttls()
    conex.login(correo, contra)
    mensaje = MIMEMultipart()
    mensaje["From"] = correo
    mensaje["To"] = correo
    mensaje ["Subject"] = "Asunto del mensaje"
    html = """
    <html>
        <body>
            <h1 style="color:blue">Este es el titulo del mensaje</h1>
            <p style="color:green">Contenido de mi mensaje aqui</p>
        <body>
    </html>
"""
    mensaje.attach(MIMEText(html, 'html'))
    conex.sendmail(correo, correo, mensaje.as_string())
    print("Correo enviado correctamente")
except smtplib.SMTPResponseException as e:
    print(f"hay un error: {e}")
finally:
    conex.quit()