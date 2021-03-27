from src.utils import load_driver,save_cookie
driver=load_driver()
driver.get('http://www.hero-wars.com')
#login normally
save_cookie(driver,'cookie\herowar.pkl')