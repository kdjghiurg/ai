import requests
from bs4 import BeautifulSoup

def read( word ):
    url = f'https://crptransfer.moe.gov.tw/index.jsp?SN={word}#searchL'

    html = requests.get( url )
    bs = BeautifulSoup(html.text,'lxml')
    data = bs.find_all('td')
    try:
        row = data.[2]
        chinese = row.text
        two = data[4]
        phones = two
        phone = [e.text for e in phones]
        s = " ".join( phone )
        # s = row.find('sub')
        return( chinese + s)
    except:
        return( '查無此字' )
