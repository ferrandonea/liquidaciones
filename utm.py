from datetime import datetime
import pandas as pd
import requests

def encuentra_utm(fecha_utm: datetime = datetime.now()):
    fecha_year = fecha_utm.year
    url_sii = f"https://www.sii.cl/valores_y_fechas/utm/utm{fecha_year}.htm"
    print (url_sii)
    
    r = requests.get(url_sii)
    df = pd.read_html(r.text)
    return fecha_utm


print (type(encuentra_utm()))
    