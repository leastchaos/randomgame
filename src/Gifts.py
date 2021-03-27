import pyautogui as gui
from src.common import click_on_image,random_click
import time

class Gifts():
    def __init__(self, driver):
        self.driver = driver

    def main(self):
        if not self.start():
            return
        self.send_gift()

    def start(self):
        return click_on_image('screenshot\gift_start.PNG', pass_msg='gift has event', fail_msg='gift has no event', confidence=0.98)

    def send_gift(self):
        click_on_image('screenshot\gift_send.PNG')
        click_on_image('screenshot\gift_send_present.PNG')
        click_on_image('screenshot\popup_close.PNG')
        click_on_image('screenshot\popup_close.PNG')