import pandas as pd
import requests
from pyjstat import pyjstat

#matplotlib inline  # allows plots to be rendered inline

BPSTAT_API_URL="https://bpstat.bportugal.pt/data/v1"
series_id = 12518356 #é o número que aparece no final do link (usar bpstat.bportugal.pt)
url = f"{BPSTAT_API_URL}/series/?lang=EN&series_ids={series_id}"
series_info = requests.get(url).json()[0]
domain_id = series_info["domain_ids"][0]
dataset_id = series_info["dataset_id"] 

# uma série pode estar em vários domínios, no entanto é raro. Pode-se usar o 1º valor em grande parte dos casos

dataset_url = f"{BPSTAT_API_URL}/domains/{domain_id}/datasets/{dataset_id}/?lang=EN&series_ids={series_id}"
dataset = pyjstat.Dataset.read(dataset_url)
df = dataset.write('dataframe')
print(df)
