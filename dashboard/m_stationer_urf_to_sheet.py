import pygsheets
import maaler



vandstand_urf = maaler.curVandStand_urf

gc = pygsheets.authorize(outh_file='client_secret_681285020382-onkp5ka50n034lnkji5fmo6dvdsr0u0s.apps.googleusercontent.com.json', no_cache=True)


sh = gc.open_by_key('1BEvtvgdu81vk4hM7D3mFV_j805wrNgm55lB8lUVo6gk')
wks = sh.sheet1


# vandstand_udløb_roskilde_fjord
wks.update_cell('B2', vandstand_urf)

print("Uploaded til 'DB_urf_maaler")