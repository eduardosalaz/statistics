# este archivo no va a funcionar porque no estoy proporcionando los CSV que necesita, estan en el otro repositorio
# tampoco se usar un ciclo for perdón
from sqlalchemy import create_engine
import pymysql
import pandas as pd

tableName1 = "municipios"
tableName2 = "confirmados"
tableName3 = "examinados"
tableName4 = "hosp_def_rec"
tableName5 = "neg_sos"

dataFrame1 = pd.read_csv('municipios.csv')
dataFrame2 = pd.read_csv('conf.csv')
dataFrame3 = pd.read_csv('totales.csv')
dataFrame4 = pd.read_csv('hospDefRec.csv')
dataFrame5 = pd.read_csv('negYsos.csv')

sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/covid', pool_recycle=3600)
dbConnection = sqlEngine.connect()
try:
    frame1 = dataFrame1.to_sql(tableName1, dbConnection, if_exists='fail');
    frame2 = dataFrame2.to_sql(tableName2, dbConnection, if_exists='fail');
    frame3 = dataFrame3.to_sql(tableName3, dbConnection, if_exists='fail');
    frame4 = dataFrame4.to_sql(tableName4, dbConnection, if_exists='fail');
    frame5 = dataFrame5.to_sql(tableName5, dbConnection, if_exists='fail');

except ValueError as vx:
    print(vx)
except Exception as ex:
    print(ex)
else:
    print("Table %s created successfully." % tableName1);
    print("Table %s created successfully." % tableName2);
    print("Table %s created successfully." % tableName3);
    print("Table %s created successfully." % tableName4);
    print("Table %s created successfully." % tableName5);
finally:
    dbConnection.close()
