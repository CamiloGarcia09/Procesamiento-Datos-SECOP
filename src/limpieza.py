import pandas as pd
import re

def limpiezaStrings(texto, default='N/D'):
    if texto is None or pd.isna(texto):
        return default

    texto = str(texto).strip()
    texto = re.sub(r'^[¿¡´.*#&:|_\'"`!?)/}\¨\[\]+<-]+', '',  texto)

    texto = re.sub(r'^\(|\)$', '', texto)
    texto = re.sub(r'\.{2,}', '.', texto)
    texto = texto.strip()

    if re.fullmatch(r'0+', texto) or re.fullmatch(r'\d', texto):
        return default

    if texto == '' or re.fullmatch(r'[¿´\.\-\*\#\&\:\|\_]+', texto):
        return default

    return texto


def limpiarDocumento(documento, default=None):
    if documento is None or pd.isna(documento):
        return default

    doc = str(documento).strip()
    doc = doc.replace('.', '')
    doc = re.sub(r'[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]', '', doc)
    doc = re.sub(r'[^0-9]', '', doc)

    if doc == '':
        return default

    if re.fullmatch(r'0+', doc):
        return '0'

    return doc

