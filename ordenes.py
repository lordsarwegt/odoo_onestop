from dotenv import load_dotenv
import os
import xmlrpc.client
from datetime import datetime, date, timedelta

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
            ['x_studio_tipo_de_servicio_lb','=','ONE STOP'],
            ['x_studio_status_general_rep','not in',[103]],
        ]]
       
        fields_list = ['name', 'x_studio_cliente_origen', 'product_id','lot_id','x_studio_fecha_gspn',
                  'create_date', 'x_studio_status_general', 'x_studio_status_general_rio','x_studio_status_general_rep',
                  'x_studio_referencia_de_ingreso', 'x_studio_orden_nr']
        
        fields = fields_list
        datos = models.execute_kw(os.getenv('DB_LOC'), self.uid, os.getenv('DB_PASS'),     
            'repair.order', 'search_read', 
            domain,
            {'fields': fields})
        
        status_count = {}        

        rows = ""
        for item in datos:
            url = f"https://agiotech.odoo.com//web#id={item.get('id')}&model=repair.order&view_type=form"

            from lib.status import status_list
               


            str_date = item.get('create_date').split(' ')[0]
            st_id = item.get('x_studio_status_general_rep', ['',''])[0]
            status_name = status_list.get(st_id, 'Desconocido') 

            referencia = item.get('x_studio_referencia_de_ingreso', '') 
            orden_nr = item.get('x_studio_orden_nr', '')

            if isinstance(status_name, list):
                status_name = status_name[0]

            #Aumentar el contador o iniciarlo en 1
            status_count[status_name] = status_count.get(status_name, 0) + 1

            
           
            rows += f"<tr>"
            rows += f"    <td>{item.get('name')}</td>"
            rows += f"    <td>{item.get('x_studio_cliente_origen')}</td>"
            rows += f"    <td>{item.get('product_id', ['',''])[1] }</td>"
            rows += f"    <td>{item.get('lot_id', ['',''])[1] if item.get('lot_id') else '' }</td>"
            #rows += f"    <td>{item.get('x_studio_fecha_gspn')}</td>"
            rows += f"    <td>{referencia}</td>"
            rows += f"    <td>{orden_nr}</td>"

            rows += f"    <td>{str_date}</td>"
            rows += f"    <td>{status_name}</td>" #, ['',''])[1]
            rows += f"    <td><a href='{url}' style='display:inline-block;   font-weight:600; font-size:16px; line-height:1; border-radius:10px; padding:12px 20px; text-align:center;'>"
            rows += f"        Ver Ticket"
            rows += f"    </a></td>"
            rows += f"    </tr>"

           # print (item)


        return rows, status_count
    
    def get_ordenes_inventory_trigger(self, models):
    
        # Obtener todas las ordenes desde stock.quants
        domain =  [[
            ['location_id',"ilike", "GDL/STOCK/31 LINEA BLANCA RACK/ONE STOP LB"],
            ['quantity','>',0],      
            ['reserved_quantity','=',0],
        ]]       

        fields_list = ['x_studio_orden_reparacion_asociada']
        prev_data = models.execute_kw(os.getenv('DB_LOC'), self.uid, os.getenv('DB_PASS'),     
            'stock.quant', 'search_read', 
            domain,
            {'fields': fields_list})
        
        new_list = [ item.get('x_studio_orden_reparacion_asociada')[0] if isinstance(item.get('x_studio_orden_reparacion_asociada'), (list, tuple)) else 0 for item in prev_data ]

        #print (prev_data)
        second_domain = [[
            ['id', 'in', new_list ],
        ]]

        #domain =  [[
        #    ['x_studio_agendado_el','=',False],           
        #    ['x_studio_tipo_de_servicio_lb','=','ONE STOP'],
        #    ['x_studio_status_general_rep','not in',[103]],
        #]]
       
        fields_list = ['name', 'x_studio_cliente_origen', 'product_id','lot_id','x_studio_fecha_gspn',
                  'create_date', 'x_studio_status_general', 'x_studio_status_general_rio','x_studio_status_general_rep',
                  'x_studio_referencia_de_ingreso', 'x_studio_orden_nr']
        
        fields = fields_list
        datos = models.execute_kw(os.getenv('DB_LOC'), self.uid, os.getenv('DB_PASS'),     
            'repair.order', 'search_read', 
            second_domain,
            {'fields': fields})
        
        status_count = {}        

        rows = ""
        for item in datos:
            url = f"https://agiotech.odoo.com//web#id={item.get('id')}&model=repair.order&view_type=form"

            from lib.status import status_list
               


            str_date = item.get('create_date').split(' ')[0]
            st_id = item.get('x_studio_status_general_rep', ['',''])[0]
            status_name = status_list.get(st_id, 'Desconocido') 

            referencia = item.get('x_studio_referencia_de_ingreso', '') 
            orden_nr = item.get('x_studio_orden_nr', '')

            if isinstance(status_name, list):
                status_name = status_name[0]

            #Aumentar el contador o iniciarlo en 1
            status_count[status_name] = status_count.get(status_name, 0) + 1

            
           
            rows += f"<tr>"
            rows += f"    <td>{item.get('name')}</td>"
            rows += f"    <td>{item.get('x_studio_cliente_origen')}</td>"
            rows += f"    <td>{item.get('product_id', ['',''])[1] }</td>"
            rows += f"    <td>{item.get('lot_id', ['',''])[1] if item.get('lot_id') else '' }</td>"
            #rows += f"    <td>{item.get('x_studio_fecha_gspn')}</td>"
            rows += f"    <td>{referencia}</td>"
            rows += f"    <td>{orden_nr}</td>"
            
            rows += f"    <td>{str_date}</td>"
            rows += f"    <td>{status_name}</td>" #, ['',''])[1]
            rows += f"    <td><a href='{url}' style='display:inline-block;   font-weight:600; font-size:16px; line-height:1; border-radius:10px; padding:12px 20px; text-align:center;'>"
            rows += f"        Ver Ticket"
            rows += f"    </a></td>"
            rows += f"    </tr>"

           # print (item)


        return rows, status_count
    
    def get_pending_sim(self, models): 

        # Obtener todas las ordenes desde stock.quants
        domain =  [[]]  
        '''     
            ['location_id',"ilike", "GDL/STOCK/31 LINEA BLANCA RACK/ONE STOP LB"],
            ['quantity','>',0],      
            ['reserved_quantity','=',0],
        '''

        fields_list = ['x_name', 'x_studio_usuario', 'x_studio_marca', 'x_studio_utima_recarga', 'x_studio_frecuencia' ]
        datos = models.execute_kw(os.getenv('DB_LOC'), self.uid, os.getenv('DB_PASS'),     
            'x_control_de_sim', 'search_read', 
            domain,
            {'fields': fields_list})
        
        
        status_count = {}        

        rows = ""
        for item in datos:
            #url = f"https://agiotech.odoo.com//web#id={item.get('id')}&model=repair.order&view_type=form"


            str_phone = item.get('x_name', '')
            str_user = item.get('x_studio_usuario', ['',''])[1]
            str_carrier = item.get('x_studio_marca', ['',''])[1] 
            str_date = item.get('x_studio_utima_recarga').split(' ')[0]
            str_date = str_date.replace('-', '/')   

            frecuencia = item.get('x_studio_frecuencia', '')
            frecuency = 0
            if frecuencia == '15 DÍAS':
                frecuency = 15
            elif frecuencia == '30 DÍAS':
                frecuency = 30
            elif frecuencia == '45 DÍAS':
                frecuency = 45
            else:
                frecuency = 60

            objeto_fecha_completa = datetime.strptime(str_date, '%Y/%m/%d')
            fecha_actual = date.today()
            diferencia_dias = (fecha_actual - objeto_fecha_completa.date()).days
            if diferencia_dias < frecuency:
                continue

                       
            rows += f"<tr>"
            rows += f"    <td>{str_phone}</td>"
            rows += f"    <td>{str_user}</td>"
            rows += f"    <td>{str_carrier}</td>"
            rows += f"    <td>{str_date }</td>"
            rows += f"    <td>{diferencia_dias }</td>"
            rows += f"</tr>"

           # print (item)


        return rows
