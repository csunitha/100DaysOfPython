''' connecting to oracle db using SQLAlchemy and getting data in panda
ref article https://gist.github.com/DGrady/7fb5c2214f247dcff2cb5dd99e231483
and using the second way of connectivity providing the service name
'''

import pandas as pd
from sqlalchemy import create_engine
import cx_Oracle

username='dummy'
password='mummy'
hostname='ghost'
port='1531'
service_name='db-name'

oracle_connection_string = f'oracle+cx_oracle://{username}:{password}@' + cx_Oracle.makedsn(f'{hostname}', f'{port}', service_name=f'{service_name}')
print(oracle_connection_string)

#connectivity data to be filled in
engine = create_engine (oracle_connection_string)
data = pd.read_sql("select * from hotel'" , engine)

print(data)
