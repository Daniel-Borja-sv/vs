import smtplib


servidor = "smtp.gmail.com"
puerto = 587
correo = "daniel.borjxl24@gmail.com"
contra = "twfh fkhm atvh xzsi"

conex = smtplib.SMTP(servidor, puerto)
conex.starttls()
(conex.login(correo, contra))
conex.sendmail(correo, correo, "Subject: Este es el asunto \n\n" + 
               "Este es el contenido del correo")
conex.quit()