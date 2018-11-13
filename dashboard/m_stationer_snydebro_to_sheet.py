import pygsheets
import maaler


vandstand_snydebro = maaler.curVandStand_snydebro
vandføring_snydebro = maaler.curVandFor_snydebro


gc = pygsheets.authorize(outh_file='client_secret_681285020382-onkp5ka50n034lnkji5fmo6dvdsr0u0s.apps.googleusercontent.com.json', no_cache=True)

# m_stationer
sh = gc.open_by_key('1yT3EXh3887oQVN4Xi6tm5Y7ybCEujg9zx76LkoIANhc')
wks = sh.sheet1

# vandstand_snydebro
wks.update_cell('B2', vandstand_snydebro)

# vandføring_snydebro
wks.update_cell('C2', vandføring_snydebro)

