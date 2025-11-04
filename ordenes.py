from dotenv import load_dotenv
import os
import xmlrpc.client
from datetime import datetime

class odoo_conection:

    def __init__(self):
        load_dotenv()

    def start_odoo_connection(self):
        # -- Odoo connection - Begin
        self.common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(os.getenv('URL_ACCS')))

        self.uid = self.common.authenticate(os.getenv('DB_LOC'), os.getenv('DB_USR'), os.getenv('DB_PASS'), {})
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(os.getenv('URL_ACCS')))
        # -- Odoo connection - Begin

        # Save DataBase 
        return models

    def close_odoo_connection(self):
        self.common._ServerProxy__transport.close()
        return self.uid


    def get_ordenes(self, models):
        domain =  [[
            ['x_studio_agendado_el','=',False],
            ['name','ilike','ONESTOP'],
            ['x_studio_tipo_de_servicio_lb','=','ONE STOP']
        ]]
        
        fields = ['name', 'x_studio_cliente_origen', 'product_id','lot_id','x_studio_fecha_gspn',
                  'create_date','x_studio_status_general_rep']

        datos = models.execute_kw(os.getenv('DB_LOC'), self.uid, os.getenv('DB_PASS'),     
            'repair.order', 'search_read', 
            domain,
            {'fields': fields})
        
        

        rows = ""
        for item in datos:
            url = f"https://agiotech.odoo.com//web#id={item.get('id')}&model=repair.order&view_type=form"

            str_date = item.get('create_date').split(' ')[0]
            #format_code = "%Y-%m-%d"
            #createdate = datetime.strptime(str_date, format_code).split(' ')[0]

            rows += f"<tr>"
            rows += f"    <td>{item.get('name')}</td>"
            rows += f"    <td>{item.get('x_studio_cliente_origen')}</td>"
            rows += f"    <td>{item.get('product_id', ['',''])[1] }</td>"
            rows += f"    <td>{item.get('lot_id', ['',''])[1] if item.get('lot_id') else '' }</td>"
            #rows += f"    <td>{item.get('x_studio_fecha_gspn')}</td>"
            rows += f"    <td>{str_date}</td>"
            rows += f"    <td>{item.get('x_studio_status_general_rep', ['',''])[1]}</td>" #background:#007BFF; color:#ffffff;
            rows += f"    <td><a href='{url}' style='display:inline-block;   font-weight:600; font-size:16px; line-height:1; border-radius:10px; padding:12px 20px; text-align:center;'>"
            rows += f"        Ver Ticket"
            rows += f"    </a></td>"
            rows += f"    </tr>"

        return rows
            

''' METODOS DE CONEXION A ODOO No probados -- Begin
    def conexion(self):

        #VALIDAMOS SI LA CONEXION ES CORRECTA 
        self.common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(os.getenv('URL_ACCS')))
        print(self.common.version())

    def iniciar_sesion(self):

        #INICIAMOS SESION
        self.uid = self.common.authenticate(os.getenv('DB_LOC'), os.getenv('DB_USR'), os.getenv('DB_PASS'), {})
        print('UID: ',self.uid) '''