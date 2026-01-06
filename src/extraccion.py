import pandas as pd
from sodapy import Socrata
import time

DATASET_ID = "rpmr-utcd"
DOMAIN = "www.datos.gov.co"
LIMIT = 10000  

def descargarDatosSecop(fecha_inicio="2025-01-01T00:00:00", fecha_fin="2025-12-31T23:59:59"):
    client = Socrata(DOMAIN, None, timeout=60)
    offset = 0
    resultados = []

    while True:
        print(f"Descargando registros desde offset {offset}...")

        try:
            registros = client.get(
                DATASET_ID,
                limit=LIMIT,
                offset=offset,
                where=(
                    f"fecha_de_firma_del_contrato between "
                    f"'{fecha_inicio}' and '{fecha_fin}'"
                )
            )

        except Exception as e:
            print(f"⚠️ Error temporal en offset {offset}: {e}")
            print("⏳ Reintentando en 5 segundos...")
            time.sleep(5)
            continue

        if not registros:
            break

        resultados.extend(registros)
        offset += LIMIT

    return pd.DataFrame.from_records(resultados)