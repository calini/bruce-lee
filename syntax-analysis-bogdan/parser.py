import sys
import requests
from bs4 import BeautifulSoup

url = 'http://nactem7.mib.man.ac.uk/geniatagger/a.cgi'

if __name__ == '__main__':
    fp = open(sys.argv[1])
    paragraph = fp.read()

    response = requests.post(url, data={'paragraph': paragraph}) 
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find('table')

    for row in table.findAll('tr'):
        if len(row.findAll('td')) != 0:
            column1 = row.findAll('td')[0].contents
            column3 = row.findAll('td')[2].contents
            print(column1[0] + "/" + column3[0])