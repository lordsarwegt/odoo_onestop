import lib.email_sender as email_sender
import ordenes as ord
import os



def main():
    from dotenv import load_dotenv
    load_dotenv()

    # Buscar las ordenes en Odoo
    odc = ord.odoo_conection()
    models = odc.start_odoo_connection()
    
    rows = odc.get_ordenes(models)

    sender = email_sender.EmailSender(
            smtp_server = os.getenv('MAIL_SERVER'), 
            smtp_port = os.getenv('MAIL_PORT'), 
            username = os.getenv('MAIL_USERNAME'), 
            password = os.getenv('MAIL_PASSWORD'), use_tls=True)
    
    template = sender.mail_template(title="Recordatorio de Órdenes Pendientes", rows=rows)

    sender.send_html_email(
        to_email="sistemas@agiotech.com",
        subject="Recordatorio de Órdenes Pendientes",
        html_content=template,
        from_email=os.getenv('MAIL_FROM')
    )

    odc.close_odoo_connection()

if __name__ == "__main__":
    main()