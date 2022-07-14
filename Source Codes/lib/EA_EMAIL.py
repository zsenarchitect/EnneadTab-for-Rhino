def send_email():
    print "sending"
    pass
    import smtplib
    from smtplib import SMTP

    #server = "smtp-mail.outlook.com"
    #port = 587
    server = "smtp.gmail.com"
    port = 465

    with smtplib.SMTP_SSL(server, port) as server:

        #server.login("szhang@outlook.com", password = "Iliveinapt1006!")
        server.login("ennead.tab@gmail.com", password = "ennead2022")


def send_email2():
    import smtplib

    import ssl

    port = 465

    smtp_server = "smtp.gmail.com"

    sender = "ennead.tab@gmail.com"

    recipient = "szhang@ennead.com"

    sender_password = "ennead2022"

    message = "Subject: This is a test message Send using Python."

    SSL_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, SSL_context) as server:

        server.login(sender, sender_password)

        server.sendmail(sender, recipient, message)

def send_email3():
    import sys

    import chilkat

    mailman = chilkat.CkMailMan()

    receiver_address = "szhang@ennead.com"

    smtpHost = mailman.mxLookup(receiver_address)

    if (mailman.get_LastMethodSuccess() != True):

        print(mailman.lastErrorText())

        sys.exit()

    mailman.put_SmtpHost(smtpHost)

    mail = chilkat.CkEmail()

    mail.put_Subject("A test subject")

    mail.put_Body("Hello!")

    mail.put_From("")

    mail.AddTo("", receiver_address)

    success = mailman.SendEmail(mail)

    if (success != True):

        print(mailman.lastErrorText())

    else:

        print("Sent!")


def send_email4():
    from email.mime.text import MIMEText

    from email.mime.multipart import MIMEMultipart

    import smtplib

    import ssl

    server = "smtp.gmail.com"
    port = 465

    sender = "ennead.tab@gmail.com"

    recipient = "szhang@ennead.com"

    password = "ennead2022"

    msg = MIMEMultipart()

    message = """Hi,
    This is a MIME text
    """

    msg['From']= sender

    msg['To']= recipient

    msg['Subject']="This is a text email for MIME"

    msg.attach(MIMEText(message, "plain"))

    text = msg.as_string()

    SSLcontext = ssl.create_default_context()

    with smtplib.SMTP(server, port) as server:

        server.starttls(context=SSLcontext)

        server.login(sender, password)

        server.sendmail(sender, recipient, text)
#################
if __name__ == "__main__":
    send_email2()
    print "#########finish"
