import time
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
class Scraper():
    def __init__(self):
        self.initialize_driver()

    def shut_down(self):
        self.driver.quit()

    def initialize_driver(self):
        # Setup headless Chrome
        options = Options()
        options.add_argument("--headless=new")
        #options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(options=options)

    def scrape(self, player : str, save_to_file: bool = False) -> str:
        """
        Scrape the player (or coach) image from FotMob and save it to a file.
        :param player: The name of the player (or coach) to scrape.
        :param save_to_file: Whether to save the image to a file, or just return the scraped image's URL.
        :return: The path to the saved image/the URL of the image.
        """
        img_url = self.get_player_image_url(player)
        if img_url:
            if save_to_file:
                return self.download_image(img_url, f"pitchiq/scripts/out/{player.replace(' ', '_')}.png")
            else:
                return img_url
        else:
            print(f"Failed to find image for {player}!!!")

    def get_player_image_url(self, player_name):
        try:
            self.driver.get("https://www.fotmob.com/")
            time.sleep(2)  # Wait for page to load

            # Click on the search bar
            search_box = self.driver.find_element(By.CSS_SELECTOR, "[aria-label='Search input']")
            search_box.send_keys(player_name)
            time.sleep(2)
            img_element = self.driver.find_element(By.CSS_SELECTOR, "img.Image.PlayerImage.ImageWithFallback")
            img_url = img_element.get_attribute("src")
            time.sleep(3)

            # Click first result
            #first_result = driver.find_element(By.CSS_SELECTOR, "a.Search_link__R9ikH")
            #first_result.click()
            #time.sleep(3)

            # Extract image
            #img_element = driver.find_element(By.CSS_SELECTOR, "img.PlayerHeader_playerImg__6JeYy")
            #img_url = img_element.get_attribute("src")

            return img_url
        except selenium.common.exceptions.NoSuchElementException:
            print(f"❌❌❌{player_name} COULD NOT HAVE THEIR IMAGE FETCHED.")
            return None
        finally:
            pass

    def download_image(self, img_url, save_path):
        response = requests.get(img_url)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print(f"Saved: {save_path}")
            return save_path
        else:
            print(f"Failed to download image from {img_url}")

