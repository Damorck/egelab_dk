import pygsheets
import hydrometri_7_dage_snydebro
dag1 = hydrometri_7_dage_snydebro.day1
dag2 = hydrometri_7_dage_snydebro.day2
dag3 = hydrometri_7_dage_snydebro.day3
dag4 = hydrometri_7_dage_snydebro.day4
dag5 = hydrometri_7_dage_snydebro.day5
dag6 = hydrometri_7_dage_snydebro.day6
dag7 = hydrometri_7_dage_snydebro.day7
#------------------------------------
vs1 = hydrometri_7_dage_snydebro.vandstand1
vs2 = hydrometri_7_dage_snydebro.vandstand2
vs3 = hydrometri_7_dage_snydebro.vandstand3
vs4 = hydrometri_7_dage_snydebro.vandstand4
vs5 = hydrometri_7_dage_snydebro.vandstand5
vs6 = hydrometri_7_dage_snydebro.vandstand6
vs7 = hydrometri_7_dage_snydebro.vandstand7


gc = pygsheets.authorize(outh_file='client_secret_681285020382-onkp5ka50n034lnkji5fmo6dvdsr0u0s.apps.googleusercontent.com.json', no_cache=True)

# snydebro_vandstand_7_dage
sh = gc.open_by_key('1qO559nHwKhSefk8_YM_GJ86DVCz9dg0GjKIazGONPqU')
wks = sh.sheet1

# snydebro_dag1 + vandstand
wks.update_cell('B2', dag1)
wks.update_cell('C2', vs1)

# snydebro_dag2 + vandstand
wks.update_cell('B3', dag2)
wks.update_cell('C3', vs2)

# snydebro_dag3 + vandstand
wks.update_cell('B4', dag3)
wks.update_cell('C4', vs3)

# snydebro_dag4 + vandstand
wks.update_cell('B5', dag4)
wks.update_cell('C5', vs4)

# snydebro_dag5 + vandstand
wks.update_cell('B6', dag5)
wks.update_cell('C6', vs5)

# snydebro_dag6 + vandstand
wks.update_cell('B7', dag6)
wks.update_cell('C7', vs6)

# snydebro_dag7
wks.update_cell('B8', dag7)
wks.update_cell('C8', vs7)