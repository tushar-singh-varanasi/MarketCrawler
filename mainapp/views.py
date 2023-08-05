from django.shortcuts import render,HttpResponse
import requests
from bs4 import BeautifulSoup
import pandas as pd



headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'} 
webpage = requests.get('https://finance.yahoo.com/quote/%5ENSEI/components?p=%5ENSEI', headers=headers).text
soup = BeautifulSoup(webpage, 'html.parser')
# table=soup.find_all('table')
nse_live_data=soup.find('fin-streamer',class_="Fw(b) Fz(36px) Mb(-4px) D(ib)").text
nse_live_data_change=soup.find('fin-streamer',class_="Fw(500) Pstart(8px) Fz(24px)").text
table = soup.find('table') 
data = []
for row in table.find_all('tr'):
    row_data = []
    for col in row.find_all('td'):
        row_data.append(col.text)
    data.append(row_data)
df = pd.DataFrame(data)
column_names = []
header_row = table.find('tr')
for header in header_row.find_all('th'):
    column_names.append(header.text)
df.columns = column_names

def show_data(request):
   
    return render(request, 'data.html',{'df':df,'nse_live_data':nse_live_data,'nse_live_data_change':nse_live_data_change} )    


