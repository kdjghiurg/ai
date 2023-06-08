import requests
from bs4 import BeautifulSoup

def read( word ):
    url = f'https://crptransfer.moe.gov.tw/index.jsp?SN={word}#result'

    html = requests.get( url )
    bs = BeautifulSoup(html.text,'lxml')
    data = bs.find('td', axis="資料類型")
    try:
        row = data.find_all('tr')[2]
        chinese = row.find('cr').text
        phones = row.find_all('code')
        phone = [e.text for e in phones]
        s = " ".join( phone )
        # s = row.find('sub')
        return( chinese + s)
    except:
        return( '查無此字' )
