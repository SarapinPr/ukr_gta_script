import pyautogui
import time
import keyboard

def main_script():
    x, y = 1656, 900
    pyautogui.moveTo(x, y, duration=0.1)  # duration - время в секундах, в течение которого будет перемещение

        # Симулируем клик левой кнопкой мыши
    pyautogui.mouseDown(button='left')
        
    pyautogui.moveTo(1500, 1030, duration=0.1)
    pyautogui.mouseUp(button='left')

    i = 1
    # Указываем координаты, куда переместить курсор мыши
    while i <= 30:
       
        pyautogui.moveTo(1500, 1030, duration=0.1)
        pyautogui.click()
        pyautogui.moveTo(940, 570, duration=0.1)
        time.sleep(0.05)
        pyautogui.click()
        time.sleep(0.3)
        pyautogui.click()
        i += 1


keyboard.add_hotkey('F4', main_script)
keyboard.wait()