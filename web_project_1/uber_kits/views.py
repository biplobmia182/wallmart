from django.shortcuts import render
from django.shortcuts import HttpResponse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def show(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.ubereats.com/search?diningMode=DELIVERY&kn=FastFood&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMk5ldyUyMFlvcmslMjIlMkMlMjJyZWZlcmVuY2UlMjIlM0ElMjJDaElKT3dnXzA2VlB3b2tSWXY1MzRRYVBDOGclMjIlMkMlMjJyZWZlcmVuY2VUeXBlJTIyJTNBJTIyZ29vZ2xlX3BsYWNlcyUyMiUyQyUyMmxhdGl0dWRlJTIyJTNBNDAuNzEzNTIlMkMlMjJsb25naXR1ZGUlMjIlM0EtNzQuMDA2ODg1JTdE&q=Fast%20Food&sc=HOME_FEED_ITEM")

    x_path = '//*[@id="main-content"]/div/div/div[2]/div/div[2]/div[1]/div/a/h3'

    title = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, x_path))).text

    scrape = {"title":title,"price":30}
    
    return render(request,'uber_kits/form.html',context=scrape)


# Create your views here.
