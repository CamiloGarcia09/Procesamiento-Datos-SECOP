from sqlalchemy import create_engine

def getEngine():
    user = "postgres"
    password = "653200"
    host = "localhost"
    port = "5432"
    db = "secop"

    url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"
    return create_engine(url)


def cargarDatosCrudos(df, engine, name_table):
    df.to_sql(
        name=name_table,
        schema="datoscrudos",
        con=engine,
        if_exists="replace",
        index=False
    )


def cargarDatosProcesados(df, engine, name_table):
    df.to_sql(
        name=name_table,
        schema="procesados",
        con=engine,
        if_exists="replace",
        index=False
    )