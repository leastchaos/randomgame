import pyautogui as gui
from src.common import click_on_image,random_click
import time
from src.utils import load_driver, load_cookie
from src.AirShip import AirShip
from src.Chest import Chest
from src.Gifts import Gifts
from src.Outland import Outland
from src.Tower import Tower

gui.PAUSE = 0.5
class HeroWarBot():
    def __init__(self):
        self.driver = load_driver()
        self.login()
        self.Outland = Outland(driver)
        self.Chest = Chest(driver)
        self.Gifts = Gifts(driver)
        self.AirShip=AirShip(driver)
        self.Tower=Tower(driver)

        self.run()

    def login(self):
        self.driver.get('http://www.hero-wars.com')
        load_cookie(self.driver, 'cookie\herowar.pkl')
        self.driver.get('http://www.hero-wars.com')
        time.sleep(4)
        click_on_image('screenshot\popup_close.PNG')

    def run(self):
        self.check_main_page()
        self.Outland.main()
        self.check_main_page()
        self.Chest.main()
        self.check_main_page()
        self.Gifts.main()
        self.check_main_page()
        self.AirShip.main()
        self.check_main_page()
        self.Tower.main()
        self.check_main_page()

    def check_main_page(self):
        for i in range(0, 5):
            click_on_image('screenshot\popup_close.PNG', num_retry=2)
            click_on_image('screenshot\\to_city.PNG', num_retry=2)

if __name__=='__main__':
    bot=HeroWarBot()