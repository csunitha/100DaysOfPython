''' connecting to oracle db using SQLAlchemy and getting data in panda

Ref: https://gist.github.com/DGrady/7fb5c2214f247dcff2cb5dd99e231483
tried first type of connectivity provided in that article

this is using sid connectivity and got the following error.
cx_Oracle.DatabaseError: ORA-12505:
TNS:listener does not currently know of SID given in connect descriptor
'''

import pandas as pd
from sqlalchemy import create_engine

oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{hostname}:{port}/{database}'

engine = create_engine (
    oracle_connection_string.format(
        username = 'username',
        password = 'blah',
        hostname = 'somehost',
        port = '1521',
        database = 'somedb'))

data = pd.read_sql("select * from blah_user" , engine)

print(data)

