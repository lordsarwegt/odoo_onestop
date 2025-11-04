from dotenv import load_dotenv
import os
import xmlrpc.client
import requests
import time



class odoo_conection:

    def __init__(self):
        load_dotenv()

    def conexion(self):

        #VALIDAMOS SI LA CONEXION ES CORRECTA 
        self.common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(os.getenv('URL_ACCS')))
        print(self.common.version())

    def iniciar_sesion(self):

        #INICIAMOS SESION
        self.uid = self.common.authenticate(os.getenv('DB_LOC'), os.getenv('DB_USR'), os.getenv('DB_PASS'), {})
        print('UID: ',self.uid)

    def get_ordenes(self):
        self.conexion()
        self.iniciar_sesion()
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(os.getenv('URL_ACCS')))
        self.datos = models.execute_kw(os.getenv('DB_LOC'), self.uid, os.getenv('DB_PASS'), 'repair.order', 'search_read', 
            [[
            ['x_studio_agendado_el','!=',False],
            ['name','ilike','ONESTOP'],
            ['x_studio_tipo_de_servicio_lb','=','ONE STOP']
            ]],
              {'fields': ['name', 'x_studio_cliente_origen', 'product_id','lot_id','x_studio_fecha_gspn','create_date','x_studio_status_general_rep']})
        print(self.datos)
ODC = odoo_conection()
ODC.get_ordenes()