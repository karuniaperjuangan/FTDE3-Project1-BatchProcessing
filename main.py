import os
import pandas as pd
import sqlparse
import connection

if __name__ == "__main__":
    # connection of data source
    name_source = 'marketplace_prod'
    conf = connection.config(name_source)
    conn, engine = connection.get_conn(conf,name_source)
    cursor = conn.cursor()

    #connection of data warehouse
    name_source_dwh = 'dwh'
    conf_dwh = connection.config(name_source_dwh)
    conn_dwh, engine_dwh = connection.get_conn(conf_dwh,name_source_dwh)
    cursor_dwh = conn_dwh.cursor()

    #get query string
    path_query = os.path.join(os.getcwd(),'query')
    query = sqlparse.format(
        open(os.path.join(path_query,'query.sql'),'r').read(),strip_comments=True
    ).strip()
    dwh_design = sqlparse.format(
        open(os.path.join(path_query,'dwh_design.sql'),'r').read(),strip_comments=True
    ).strip()

    try:
        print('service etl is running')
        df = pd.read_sql(query,engine)
        print(df)

        cursor_dwh.execute(dwh_design)
        conn_dwh.commit()
        df.to_sql(
            'dim_orders',
            engine_dwh,
            schema='public',
            if_exists='replace',
            index=False
        )
        print('service etl is successful')
    except Exception as e:
        print('service etl is failed')
        print(e)


