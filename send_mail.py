import smtplib,ssl,Important
from email.message import EmailMessage



def send_mail(image_path):


    email_message = EmailMessage()

    email_message["Subject"] = "Some disturbance in the frame!"
    email_message.set_content("Here is the picture of the fame")

    with open(image_path, "rb") as file:
        content = file.read()

    email_message.add_attachment(content,maintype="image")



    host = "smtp.gmail.com"
    port = 465
    user_name = Important.get_mail()
    password = Important.get_pass()
    receiver = Important.get_mail()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, email_message.as_string())

    if __name__ == "__main__":
        send_mail("images/test.png")