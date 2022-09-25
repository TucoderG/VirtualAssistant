import webbrowser as wb
import pyautogui as at
import time

def send_message(contact, message):
    wb.open(f"https://web.whatsapp.com/send?phone={contact}&text={message}")
    time.sleep(8)
    at.press('enter')

