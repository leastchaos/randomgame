import pyautogui as gui
from src.common import click_on_image,random_click
import time

class Outland():
    def __init__(self, driver):
        self.driver = driver

    def main(self):
        if not self.start():
            return
        self.claim_all_reward()

    def start(self):
        return click_on_image('screenshot\outland_start.PNG', pass_msg='outland has event', fail_msg='outland has no event', confidence=0.98)

    def claim_all_reward(self):
        self.claim_reward()
        for boss in ['screenshot\outland_weaver.PNG', 'screenshot\outland_brog.PNG']:
            click_on_image(boss)
            self.claim_reward()
        click_on_image('screenshot\popup_close.PNG')

    def claim_reward(self):
        if click_on_image('screenshot\outland_claim.PNG', pass_msg='clicked on claim', fail_msg='no claim available'):
            for i in range(0, 20):
                click_on_image('screenshot\outland_claim.PNG', num_retry=5)
                click_on_image(
                    'screenshot\outland_open_chest.PNG', num_retry=5)
                if click_on_image('screenshot\outland_open_chest2.PNG'):
                    break
            click_on_image('screenshot\popup_close.PNG')