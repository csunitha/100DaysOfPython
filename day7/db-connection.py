''' connecting to oracle db using SQLAlchemy and getting data in panda
ref article https://gist.github.com/DGrady/7fb5c2214f247dcff2cb5dd99e231483
and using the second way of connectivity providing the service name
'''

import pandas as pd
from sqlalchemy import create_engine
import cx_Oracle

oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@'+ cx_Oracle.makedsn('{hostname}', '{port}', service_name='{service_name}')


#connectivity data to be filled in
engine = create_engine (
    oracle_connection_string.format(
        username = '',
        password = '',
        hostname = '',
        port = '1521',
        service_name = ''))

data = pd.read_sql("select * from hotel'" , engine)

print(data)
