import pyautogui as gui
from src.common import click_on_image,random_click
import time

class Chest():
    def __init__(self, driver):
        self.driver = driver

    def main(self):
        if not self.start():
            return
        self.claim_reward()

    def start(self):
        return click_on_image('screenshot\chest_start.PNG', pass_msg='chest has event', fail_msg='chest has no event', confidence=0.98)

    def claim_reward(self):
        click_on_image('screenshot\chest_open.PNG')
        click_on_image('screenshot\popup_close.PNG')