import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def youtube_like():

    driver = webdriver.Chrome("D:\\chromedriver.exe")

    driver.get("https://youtube.com")
    # go to youtube
    time.sleep(5)

    driver.maximize_window()
    #searchBox = driver.find_element_by_class_name("style-scope ytd-searchbox")
    searchBox = driver.find_element(by=By.CLASS_NAME, value="style-scope ytd-searchbox")
    #searchButton = driver.find_element_by_id("search-icon-legacy")
    searchButton = driver.find_element(by=By.ID, value="search-icon-legacy")
    searchBox.send_keys("tell me why brooklyn 99")
    searchButton.click()
    #enter search + click on search
    time.sleep(5)

    #video = driver.find_element_by_class_name("style-scope ytd-video-renderer")
    video = driver.find_element(by=By.CLASS_NAME, value="style-scope ytd-video-renderer")
    video.click()
    #click on first video
    time.sleep(10)
    try:
        #like = driver.find_element_by_class_name("style-scope ytd-toggle-button-renderer")      #try to click on first video
        like = driver.find_element(by=By.CLASS_NAME, value="style-scope ytd-toggle-button-renderer")
        like.click()
    except:
        driver.refresh()
        time.sleep(10)                                                                          #if error - refreshand try again
        #like = driver.find_element_by_class_name("style-scope ytd-toggle-button-renderer")
        like = driver.find_element(by=By.CLASS_NAME, value="style-scope ytd-toggle-button-renderer")
        like.click()
    time.sleep(5)
    try:
        #login = driver.find_element_by_xpath("/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-modal-with-title-and-button-renderer/div/ytd-button-renderer/a/tp-yt-paper-button")
        login = driver.find_element(by=By.XPATH, value="/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-modal-with-title-and-button-renderer/div/ytd-button-renderer/a/tp-yt-paper-button")
        login.click()
        #click on the login button
        time.sleep(4)
        driver.close()
        return "LIKE OK"        #return LIKE OK for pytest
    except:
        driver.close()
        return "LIKE NOT OK"    #return LIKE NOT OK for pytest if failure
