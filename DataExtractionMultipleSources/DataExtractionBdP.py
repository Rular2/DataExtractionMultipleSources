import pandas as pd
import requests
from pyjstat import pyjstat

def BdP_extract(series_id=12518356): #final do link
  BPSTAT_API_URL="https://bpstat.bportugal.pt/data/v1"
  url = f"{BPSTAT_API_URL}/series/?lang=EN&series_ids={series_id}"
  series_info = requests.get(url).json()[0] # uma série pode estar em vários domínios, no entanto é raro. Pode-se usar o 1º valor em grande parte dos casos
  domain_id = series_info["domain_ids"][0]
  dataset_id = series_info["dataset_id"] 
  dataset_url = f"{BPSTAT_API_URL}/domains/{domain_id}/datasets/{dataset_id}/?lang=EN&series_ids={series_id}"
  dataset = pyjstat.Dataset.read(dataset_url)
  df = dataset.write('dataframe')
  print(df)
