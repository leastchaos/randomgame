import time
import random
import pyautogui as gui


def random_click(box):
    '''A function to return random click coordinates from box object by pyautogui'''
    x_click = int(random.uniform(box.left, box.left+box.width))
    y_click = int(random.uniform(box.top, box.top+box.height))
    gui.moveTo(x_click, y_click)

    return


def click_on_image(screenshot_path, pass_msg=None, fail_msg=None, num_retry=20, confidence=0.9):
    for i in range(0, num_retry):
        box = gui.locateOnScreen(screenshot_path, confidence=confidence)
        time.sleep(0.5)
        if box:
            if pass_msg:
                print(pass_msg)
            break
    if not box:
        if fail_msg:
            print(fail_msg)
        return False
    random_click(box)
    return True