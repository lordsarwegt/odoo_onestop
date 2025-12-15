import lib.email_sender as email_sender
from lib.agioLog import AgioLog as log
import ordenes as ord
import os
import time



def main():
    from dotenv import load_dotenv
    load_dotenv()

    # Buscar las ordenes en Odoo
    odc = ord.odoo_conection()
    models = odc.start_odoo_connection()
    
    print( log.add_log("Obteniendo las ordenes", "Mensaje", "System") )
    rows, status_count = odc.get_ordenes(models)
    

    print( log.add_log("Preparando correo", "Mensaje", "System") )
    sender = email_sender.EmailSender(
            smtp_server = os.getenv('MAIL_SERVER'), 
            smtp_port = os.getenv('MAIL_PORT'), 
            username = os.getenv('MAIL_USERNAME'), 
            password = os.getenv('MAIL_PASSWORD'), use_tls=True)
    
    template = sender.mail_template(title="Recordatorio de Órdenes Pendientes", status_count = status_count,  rows=rows)

    print( log.add_log("enviando correo", "Mensaje", "System") )
    
    sender.send_html_email(
        to_email="informacion.ce@agiotech.com",
        subject="Recordatorio de Órdenes Pendientes",
        html_content=template,
        from_email=os.getenv('MAIL_FROM')
    )

    odc.close_odoo_connection()

if __name__ == "__main__":
    logPath = os.getcwd() + "\\logs"
    log = log(path=logPath)

    print( log.add_log("Iniciando aplicación ", "Mensaje", "System") )
    main()

    time.sleep(10)
    print( log.add_log("Terinando aplicación", "Mensaje", "System") )