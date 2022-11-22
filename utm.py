from datetime import datetime
import pandas as pd
import requests
from bs4 import BeautifulSoup

def find_utm(date_utm: datetime = datetime.now()):
    date_year = date_utm.year
    date_month = date_utm.month
    url_sii = f"https://www.sii.cl/valores_y_fechas/utm/utm{fecha_year}.htm"
    
    r = requests.get(url_sii)
    soup = BeautifulSoup(r.text, 'html.parser')
    table_ = soup.select_one('table#table_export')
    rows_ = table_.select('tr')    
    date_row = rows_[date_month +1]
    utm_value = date_row.select('td')[0].text.replace(".","")
    return float(utm_value)


    