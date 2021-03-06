
# Aqui vamos a escribir funciones donde recoger los datos que queremos. las llamadas que hace streamlit a la api en forma de 
# funciones para recoger datos y luego jugar con ellos en los graficos 

import requests
import os
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("url")

# dashboard covid
def get_all_data_base_map(var):
    base_url = url+f"/alldbmap/{var}"
    res = requests.get(base_url).json()
    return res

# dashboard EDA
def get_all_data_base_TR(country):
    base_url = url+f"/alldb/{country}"
    res = requests.get(base_url).json()
    return res

# dashboard covid
def get_list_continent():
    base_url = url+"/continent"
    res = requests.get(base_url).json()
    return res

# dashboard covid
# dashboard EDA
def get_list_countrys_of_continent(continent):
    base_url = url+f"/continent/{continent}"
    res = requests.get(base_url).json()
    return res

# dashboard covid
def get_oneline():
    base_url = url+"/alldboneline"
    res = requests.get(base_url).json()
    return res

# dashboard covid
def get_data_one_country(country,var):
    base_url = url+f"/continent/{country}/{var}"
    res = requests.get(base_url).json()
    return res

