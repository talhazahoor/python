# -*- coding: utf-8 -*-
"""
Created on Sun May 21 06:13:27 2023

@author: talha
"""


import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

import undetected_chromedriver as uc

import csv


#googles the url in the driver automatically 
driver = uc.Chrome()
elements = [
    "Binaural",
    "Ambient",
    "Serene",
    "Zenith",
    "Tranquil",
    "Harmonious",
    "Ethereal",
    "Therapeutic",
    "Calming",
    "Melodic",
    "Peaceful",
    "Resonant",
    "Soothing",
    "Gentle",
    "Enchanting",
    "Radiant",
    "Uplifting",
    "Blissful",
    "Nurturing",
    "Immersive",
    "Rejuvenating",
    "Celestial",
    "Transcendent",
    "Vibrant",
    "Sublime",
    "Mellow",
    "Tranquility",
    "Enveloping",
    "Solfeggio",
    "Harmonic",
    "Healing",
    "Restorative",
    "Sacred",
    "Grounding",
    "Seraphic",
    "Enchanting",
    "Melting",
    "Dreamlike",
    "Ascending",
    "Revitalizing",
    "Ambient",
    "Wholesome",
    "Pulsating",
    "Lush",
    "Captivating",
    "Therapeutic",
    "Blissful",
    "Subtle",
    "Evocative",
    "Immersive",
    "Ethereal",
    "Serenity",
    "Transcendental",
    "Meditative",
    "Illuminating",
    "Synchronizing",
    "Melting",
    "Mindful",
    "Balancing",
    "Deepening",
    "Vibration",
    "Chanting",
    "Celestial",
    "Harmonious",
    "Euphoric",
    "Ambient",
    "Harmonizing",
    "Reverberating",
    "Rhythmic",
    "Infusing",
    "Enveloping",
    "Zen",
    "Harmonizing",
    "Radiating",
    "Blissful",
    "Transcendent",
    "Nurturing",
    "Illuminating",
    "Enchanting",
    "Grounding",
    "Resonating",
    "Soothing",
    "Evolving",
    "Euphoric",
    "Ethereal",
    "Seraphic",
    "Therapeutic",
    "Radiant",
    "Melodic",
    "Flowing",
    "Solfeggio",
    "Tranquil",
    "Sacred",
    "Restorative",
    "Ambient",
    "Harmonic",
    "Healing",
    "Wholesome",
    "Rejuvenating",
    "Zen-like"
]


e=0

while elements[e]:
    
    artistUrl=[]
    verified=[]
    artistName=[]
    followers=[]
    monthlyListeners=[]
    facebook=[]
    instagram=[]
    url='https://spotify.com/'
    driver.get(url)
    try:
        time.sleep(5)
        driver.find_element(By.XPATH,'//*[@id="onetrust-accept-btn-handler"]').click()
    except:
        print("NOTHING")
    driver.find_element(By.CSS_SELECTOR,'#main > div > div.ZQftYELq0aOsg6tPbVbV > div.BdcvqBAid96FaHAmPYw_ > nav > div > ul > li:nth-child(2) > a').click()
    
    time.sleep(1)
    inputSearch=driver.find_element(By.CSS_SELECTOR,'#main > div > div.ZQftYELq0aOsg6tPbVbV > div.PHgyArRLVFknlaOm31ID > header > div.rovbQsmAS_mwvpKHaVhQ > div > div > form > input')
    index=e
    inputSearch.send_keys(elements[index])
    
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="main"]/div/div[2]/div[4]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/div/div/div/div/div/a[2]/button/span')))
    element.click()
    time.sleep(1)
    j=0
    while True:
        try:
            
            artistUrl.append(driver.find_elements(By.CLASS_NAME,'Nqa6Cw3RkDMV8QnYreTr')[j].get_attribute('href'))
            
            j=j+1
            try:
                wait = WebDriverWait(driver, 25)
                element = wait.until(EC.presence_of_element_located((By.XPATH,f'//*[@id="searchPage"]/div/div/div/div[1]/div[{j}]')))
                time.sleep(1)
                driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)
            except:
                break
             
            print(j)
        
        except:
            break
        if j==100:
            break
    
    i=0
    time.sleep(1)
    while True:
        time.sleep(1)
        try:
            driver.get(artistUrl[i])
            
            print(artistUrl[i])
            i=i+1
            try:
                
                wait = WebDriverWait(driver, 10)

                # Wait for an element to be visible and store it in a variable
                try:
                    element = wait.until(EC.visibility_of_element_located((By.TAG_NAME,'h1')))
                    # Do something with the element once it's visible
                    element.click()
                except:
                    print("Element not found or not visible within the given time.")
               
                artistName.append(element.text)
                wait = WebDriverWait(driver, 10)
                element = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'xaeunxBdlShScWay5mQR')))
                element.click()
            except:
                artistName.append('NA')
                followers.append('NA')
                verified.append('NA')
                monthlyListeners.append('NA')
                facebook.append('NA')
                instagram.append('NA')
            time.sleep(3)
            try:
                fo=driver.find_elements(By.CLASS_NAME,'upZIQtiBy1Tr0ZbvhnSL')[0]
                fo=fo.find_element(By.TAG_NAME,'div').text
                followers.append(fo)
            except:
                followers.append("NA")
            try:
                mo=driver.find_elements(By.CLASS_NAME,'upZIQtiBy1Tr0ZbvhnSL')[1]
                mo=mo.find_element(By.TAG_NAME,'div').text
                monthlyListeners.append(mo)
            except:
                monthlyListeners.append("NA")
            try:
                wow=driver.find_element(By.CLASS_NAME,'CmR9tHJ5ta6oWJlKBm3k')
                verified.append('yes')
            except:
                verified.append('no')
        
            try:
                f=driver.find_elements(By.CLASS_NAME,'oe0FHRJU7PvjoTnXJmfr')[0]
                facebook.append(f.get_attribute('href'))
            except:
                facebook.append('NA')   
            try:
                insta=driver.find_elements(By.CLASS_NAME,'oe0FHRJU7PvjoTnXJmfr')[1].get_attribute('href')
                instagram.append(insta)
            except:
                instagram.append('NA')
        except:
            break
    filename = 'D:/'+elements[index]+'.csv'  # Specify the complete file path on the D drive
            
    # Combine the lists into a list of rows
    rows = zip(artistUrl, verified, artistName, followers, monthlyListeners, facebook, instagram)

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
    
        # Write the column headers
        writer.writerow(['artistUrl', 'verified', 'artistName', 'followers', 'monthlyListeners', 'facebook', 'instagram'])
    
        # Write the rows of data
        writer.writerows(rows)

    print('CSV file saved successfully.')
    index=index+1
    
    e=index

    
    
    
    
    
    
    
    
