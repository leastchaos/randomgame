import pyautogui as gui
from src.common import click_on_image,random_click
import time

class AirShip():
    def __init__(self, driver):
        self.driver = driver

    def main(self):
        if not self.start():
            return
        self.collect_key()
        self.collect_chest()
        self.expedition()
        

    def start(self):
        return click_on_image('screenshot\\airship_start.PNG', pass_msg='airship has event', fail_msg='airship has no event', confidence=0.98)

    def collect_key(self):
        click_on_image('screenshot\\airship_start.PNG')
        click_on_image('screenshot\\airship_key.PNG')
        click_on_image('screenshot\\airship_collect.PNG')
        click_on_image('screenshot\popup_close.PNG')

    def collect_chest(self):
        for i in range(0, 10):
            if not click_on_image('screenshot\\airship_chest.PNG', confidence=0.8, num_retry=5):
                break
            click_on_image('screenshot\\airship_chest_key.PNG')
            click_on_image('screenshot\popup_close.PNG')
            click_on_image('screenshot\popup_close.PNG')

    def expedition(self):
        for i in gui.locateAllOnScreen('screenshot\\airship_battle.PNG', confidence=0.8):
            gui.moveTo(i)
            gui.click()
            if click_on_image('screenshot\\airship_battle_start.PNG', num_retry=4):
                click_on_image('screenshot\\airship_battle_auto.PNG')
                if click_on_image('screenshot\\airship_battle_OK.PNG', num_retry=4):
                    click_on_image('screenshot\\popup_close.PNG')
                else:
                    click_on_image('screenshot\\airship_battle_start2.PNG')
            click_on_image('screenshot\\popup_close.PNG')
            time.sleep(1)
        click_on_image('screenshot\\popup_close.PNG')
        click_on_image('screenshot\\popup_close.PNG')