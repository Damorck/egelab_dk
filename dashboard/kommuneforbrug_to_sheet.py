import pygsheets
import evishine_kommunen as ek





gc = pygsheets.authorize(outh_file='client_secret_681285020382-onkp5ka50n034lnkji5fmo6dvdsr0u0s.apps.googleusercontent.com.json', no_cache=True)


sh = gc.open_by_key('1uJOfUME7-THAs7jsnn0FE663bOhUlCZadlinWWjV0Oc')
wks = sh.sheet1


wks.update_cell('A2', ek.bulbsOn_numbered)
wks.update_cell('B2', ek.totalCo2Prod_numbered)
wks.update_cell('C2', ek.co2ReducToday_numbered)
wks.update_cell('D2', ek.prodKwhToday_numbered)
wks.update_cell('E2', ek.TotalKwh_numbered)


print("Uploaded til 'evishine_kommunen")