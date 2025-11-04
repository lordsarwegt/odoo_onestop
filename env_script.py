import os

# Registrar variables de entorno
os.environ['MI_VARIABLE'] = 'Hola Mundo'
os.environ['OTRA_VARIABLE'] = '123'

# Acceder a las variables
print("MI_VARIABLE:", os.environ['MI_VARIABLE'])
print("OTRA_VARIABLE:", os.environ['OTRA_VARIABLE'])