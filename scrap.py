from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from aiogram import Bot, Dispatcher,executor, types
import requests


import time
import os


bot = Bot(token = '1603505226:AAHS4zRrf0Y6LBmKiX9OVZrRop8Ao-L1cSY')

dp = Dispatcher(bot)
tvar = True
# executable_path=os.environ.get("CHROMEDRIVER_PATH"),


@dp.channel_post_handler(chat_id=-1001159850794)
async def sadqwe(post):
    global tvar
    if tvar == True:
        tvar = False
        await  tim()






async def tim():
    while True:
        print('Начинаем')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("window-size=1920x1080")
        chrome_options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),options=chrome_options)

        driver.get('https://scrolller.com/r/feet?filter=videos')

        driver.find_element_by_class_name('nsfw-warning__accept-button').click()

        WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.TAG_NAME, 'video')))

        a = driver.find_element_by_tag_name('video')

        link = a.find_element_by_tag_name('source').get_attribute('src')
        driver.close()
        r = requests.get(link)
        with open('tata.mp4', 'wb')as f:
            f.write(r.content)
        with open('tata.mp4', 'rb')as tata:
            await bot.send_video(-1001159850794, tata)
        print('ждем')
        time.sleep(3600)
        print('идем')





executor.start_polling(dp, skip_updates=True)