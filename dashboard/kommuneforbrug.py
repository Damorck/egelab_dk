from selenium import webdriver

#Solceller i Egedal Kommune


driver = webdriver.PhantomJS() 
driver.get('http://evishine.dk/sites/egedal/index.html?idx=7')

#kWh produceret idag
prodKwhToday = driver.find_element_by_id('daily_counter').text
prodKwhToday_numbered = prodKwhToday.split(' ')[0]
print("I dag er der produceret: " + prodKwhToday)


#Co2 produktion totalt
totalCo2Prod =  driver.find_element_by_id('totalCo2').text
totalCo2Prod_numbered = str(totalCo2Prod.split(' ')[0])
print("Total reduktion af Co2 er " + totalCo2Prod)

#Co2 produktion totalt
co2ReducToday =  driver.find_element_by_id('co2').text
co2ReducToday_numbered = str(co2ReducToday.split(' ')[0])
print("Reduktion af Co2 er i dag " + co2ReducToday)

TotalKwh = driver.find_element_by_id('totalProd').text
TotalKwh_numbered = str(TotalKwh.split(' ')[0])
print("Totalproduktionen er lig med " + TotalKwh)

#pærere tændt lige nu
bulbsOn = driver.find_element_by_id('co2_2').text
bulbsOn_numbered = str(bulbsOn.split(' ')[0])

print("Så mange pærere kan være tændt nu: " + bulbsOn)
