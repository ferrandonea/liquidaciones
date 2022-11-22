"""_utm.py_
Obtiene la UTM desde el sitio del SII
"""
from datetime import datetime
import requests
from bs4 import BeautifulSoup


def find_utm(date_utm: datetime = datetime.now()) -> float:
    """find_utm: Baja UTM desde SII

    Args:
        date_utm (datetime, optional): Fecha para el cálculo de la UTM. Defaults to datetime.now().

    Returns:
        float: UTM del mes date_utm
    """
    date_year = date_utm.year
    date_month = date_utm.month
    url_sii = f"https://www.sii.cl/valores_y_fechas/utm/utm{date_year}.htm"

    req_ = requests.get(url_sii, timeout=100000)
    soup = BeautifulSoup(req_.text, "html.parser")
    table_ = soup.select_one("table#table_export")
    rows_ = table_.select("tr")
    date_row = rows_[date_month + 1]
    utm_value = date_row.select("td")[0].text.replace(".", "")
    return float(utm_value)
