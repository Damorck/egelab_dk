import pygsheets
import hydrometri_7_dage_urf

dag1 = hydrometri_7_dage_urf.day1
dag2 = hydrometri_7_dage_urf.day2
dag3 = hydrometri_7_dage_urf.day3
dag4 = hydrometri_7_dage_urf.day4
dag5 = hydrometri_7_dage_urf.day5
dag6 = hydrometri_7_dage_urf.day6
dag7 = hydrometri_7_dage_urf.day7
#-----------------------------------
vs1 = hydrometri_7_dage_urf.vandstand1
vs2 = hydrometri_7_dage_urf.vandstand2
vs3 = hydrometri_7_dage_urf.vandstand3
vs4 = hydrometri_7_dage_urf.vandstand4
vs5 = hydrometri_7_dage_urf.vandstand5
vs6 = hydrometri_7_dage_urf.vandstand6
vs7 = hydrometri_7_dage_urf.vandstand7


gc = pygsheets.authorize(outh_file='client_secret_681285020382-onkp5ka50n034lnkji5fmo6dvdsr0u0s.apps.googleusercontent.com.json', no_cache=True)

# urf_vandstand_7_dage
sh = gc.open_by_key('185CgDhXgImow31_7X57zypqbsZ4F_iAaJ8x7Z3Cr1Ps')
wks = sh.sheet1

# urf_dag1 + vandstand
wks.update_cell('B2', dag1)
wks.update_cell('C2', vs1)

# urf_dag2 + vandstand
wks.update_cell('B3', dag2)
wks.update_cell('C3', vs2)

# urf_dag3 + vandstand
wks.update_cell('B4', dag3)
wks.update_cell('C4', vs3)


# urf_dag4 + vandstand
wks.update_cell('B5', dag4)
wks.update_cell('C5', vs4)

# urf_dag5 + vandstand
wks.update_cell('B6', dag5)
wks.update_cell('C6', vs5)

# urf_dag6 + vandstand
wks.update_cell('B7', dag6)
wks.update_cell('C7', vs6)

# urf_dag7 + vandstand
wks.update_cell('B8', dag7)
wks.update_cell('C8', vs7)
