import pyautogui as gui
from src.common import click_on_image,random_click
import time

class Tower():
    def __init__(self, driver):
        self.driver = driver
        self.PAUSE=gui.PAUSE
        gui.PAUSE = 0.5

    def main(self):
        if not self.start():
            return
        for i in range(0,100):
            click_on_image('screenshot\\tower\\proceed.PNG',pass_msg='proceed',num_retry=1)
            click_on_image('screenshot\\tower\\proceed2.PNG',pass_msg='proceed',num_retry=1)
            if click_on_image('screenshot\\tower\\battle.PNG',pass_msg='enter battle',num_retry=1):
                self.battle()
                
            if click_on_image('screenshot\\tower\\buff.PNG',pass_msg='enter buff',num_retry=1):
                self.buff()

            if click_on_image('screenshot\\tower\\chest.PNG',pass_msg='enter chest',num_retry=1):
                self.open_chest()

            if click_on_image('screenshot\\tower\\big_chest.PNG',pass_msg='enter chest',num_retry=1):
                self.open_chest()
            
            if click_on_image('screenshot\\tower\\final_chest.PNG',pass_msg='enter chest',num_retry=1):
                self.final_chest()
                break

        gui.PAUSE = self.PAUSE
        

    def start(self):
        return click_on_image('screenshot\\tower\\start.PNG', pass_msg='airship has event', fail_msg='airship has no event', confidence=0.98)

    def buff(self):
        click_on_image('screenshot\\popup_close.PNG')
        click_on_image('screenshot\\tower\\proceed.PNG')
        time.sleep(2)
    
    def open_chest(self):
        click_on_image('screenshot\\tower\\open_chest.PNG',fail_msg='cannot open chest',confidence=0.8)
        click_on_image('screenshot\\tower\\chest_proceed.PNG')
    
    def final_chest(self):
        click_on_image('screenshot\\tower\\open_chest.PNG',fail_msg='cannot open chest',confidence=0.8)
        click_on_image('screenshot\\popup_close.PNG')
        click_on_image('screenshot\\tower\\tower_points.PNG')
        click_on_image('screenshot\\popup_close.PNG')
        click_on_image('screenshot\\tower\\skull.PNG')
        click_on_image('screenshot\\tower\\exchange_skull.PNG')
        click_on_image('screenshot\\popup_close.PNG')

    def battle(self):
        if click_on_image('screenshot\\tower\\skip.PNG',num_retry=2):
            return
        if click_on_image('screenshot\\tower\\attack.PNG',num_retry=2):
            click_on_image('screenshot\\tower\\to_battle.PNG')
            click_on_image('screenshot\\tower\\auto.PNG')
            while not click_on_image('screenshot\\tower\\battle_OK.PNG',pass_msg='battle over'):
                return