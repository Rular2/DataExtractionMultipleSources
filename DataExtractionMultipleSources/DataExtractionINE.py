import json
import requests

url = "https://www.ine.pt/json_indicador_pindica.jsp=op?op-2&varcd=0008074&Dim1=S7A2015&Dim2=200&Dim3=3&lang=PT"
response = requests.get(url)
df = pd.json_normalize(response.json())
print(df)