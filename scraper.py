from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sqlite3
import time
def scraper():
    while True:
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)
        driver.get(
            "https://www.google.com/search?q=tempature&oq=tempa&aqs=chrome.0.69i59j69i57.3083j0j1&sourceid=chrome&ie=UTF-8")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wob_tm"]')) )
        print("Grabbing Temp")
        tempature = driver.find_element_by_xpath("""//*[@id="wob_tm"]""")
        print("Grabbing Rain")
        per = driver.find_element_by_xpath("""//*[@id="wob_pp"]""")
        print("Grabbing Humidity")
        hum = driver.find_element_by_xpath("""//*[@id="wob_hm"]""")
        print("Grabbing Wind")
        wind = driver.find_element_by_xpath("""//*[@id="wob_ws"]""")
        all = [tempature.text, per.text, hum.text, wind.text]
        driver.close()
        return all
while True:
    car = scraper()
    conn = sqlite3.connect("fun.db")
    c = conn.cursor()
    '''c.execute("""CREATE TABLE weather(
        Tempature integer,
        Percipitation integer,
        Humidity integer,
        Wind integer
    )""")'''
    c.execute("INSERT INTO weather VALUES(:Tempature, :Percipitation, :Humidity, :Wind)", {"Tempature": car[0], "Percipitation": car[1], "Humidity": car[2], "Wind": car[3]})
    conn.commit()
    conn.close()
    time.sleep(1800)