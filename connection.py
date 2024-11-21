import os
import json
import psycopg2
from sqlalchemy import create_engine


def config(connection_db):
    path = os.getcwd()
    with open(os.path.join(path,'config.json'),'r') as file:
        conf = json.load(file)[connection_db]
        return conf

def get_conn(conf,name_conn):
    try:
        conn = psycopg2.connect(
            host=conf['host'],
            database=conf['db'],
            user=conf['user'],
            password=conf['password'],
            port=conf['port']
        )
        print(f'Success connect post {name_conn}')
        engine = create_engine(
            "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
                conf['user'],
                conf['password'],
                conf['host'],
                conf['port'],
                conf['db']
        ))
        return conn,engine
    except Exception as e:
        print(f"Can't success connect to postgres")
        print(e)