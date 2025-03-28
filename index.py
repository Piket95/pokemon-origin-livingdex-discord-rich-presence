# libraries
from pypresence import Presence
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from dotenv import load_dotenv

# build in
import sys
import time
import threading
import os

# project classes/files
from src.pokemon_game_selector import *

load_dotenv()

url = os.getenv('SUPEREFFECTIVE_PROFILE_URL')
app = PokemonGameSelector()
start_time = int(time.time())

def check_catched_status():
    global url

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, timeout=30)

    try:
        driver.get(url)

        try:
            span = wait.until(lambda d: driver.find_element(By.XPATH, "/html/body/div/div/main/div/div[2]/div[1]/div[2]/div[2]/span[2]"))
            state = span.get_attribute("innerHTML").split('>')[-1].strip()
            
            # Den String in zwei Zahlen aufteilen
            caught, total = map(int, state.split('/'))
            return caught, total  # Gibt ein Tupel mit beiden Zahlen zurück

        except (TimeoutException, NoSuchElementException):
            sys.exit(1)
    finally:
        driver.close()

def startRichPresence():
    global start_time

    time.sleep(5) # wait 5 seconds to let the app gui start
    
    client_id = os.getenv('DISCORD_APPLICATION_ID')
    RPC = Presence(client_id)
    RPC.connect()

    while True:  # The presence will stay on as long as the program is running
        catched_status = check_catched_status()

        if app.selected_game.get():
            details = "Currently in: " + app.selected_game.get()
            game_name = app.selected_game.get()
            game_image_key = app.getImageKey()
        else:
            details = "Idle"
            game_name = None
            game_image_key = None

        # Set the presence
        print(
            RPC.update(
                details=details,
                state="Catched: " + str(catched_status[0]) + " of " + str(catched_status[1]),
                large_text="Pokémon Origin Livingdex",
                small_image=game_image_key,
                small_text=game_name,
                start=start_time
            )
        )

        # time.sleep(60 * 5) # Can only update rich presence every 5 minutes
        time.sleep(15) # dev only

# Starte die GUI in einem separaten Thread
gui_thread = threading.Thread(target=startRichPresence, daemon=True)
gui_thread.start()

app.run()
