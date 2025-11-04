import lib.email_sender as email_sender


MAIL_SERVER = "smtp.office365.com"
MAIL_PORT = 587
MAIL_USERNAME = "firewall@agiotech.com"
MAIL_PASSWORD = "Agiotech01"
MAIL_FROM = "firewall@agiotech.com"


def main():

    sender = email_sender.EmailSender(smtp_server = MAIL_SERVER, smtp_port = MAIL_PORT, username = MAIL_USERNAME, password = MAIL_PASSWORD, use_tls=True)
    template = sender.mail_template(title="Weekly Performance Report")

    sender.send_html_email(
        to_email="carlos.barreto@agiotech.com",
        subject="Weekly Performance Report",
        html_content=template,
        from_email=MAIL_FROM
    )

if __name__ == "__main__":
    main()