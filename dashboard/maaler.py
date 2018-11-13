from bs4 import BeautifulSoup as bs
import requests

#Hydrometri.dk

url = 'http://www.hydrometri.dk/hymer/hymercom_online.xml'

page = requests.get(url)
soup = bs(page.content, 'html.parser')


findTags = soup.find(id='20784')
curVandStand_snydebro_float = float(findTags['tslastvalue'])
curVandStand_snydebro = round(curVandStand_snydebro_float,2)
#print("Vandstand for Snydebro er lig med " + str(curVandStand_snydebro))
findTags = soup.find(id='20806')
curVandFor_snydebro = str(findTags['tslastvalue'])
#print("Vandføring for Snydebro er lig med " + curVandFor_snydebro + " liter pr sek.")



#urf
findTags = soup.find(id='2140')
curVandStand_urf = str(findTags['tslastvalue'])
#print("Vandstand for urf er lig med " + curVandStand_urf)

