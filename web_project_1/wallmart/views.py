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
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.get("https://www.daraz.com.bd/catalog/?spm=a2a0e.home.search.2.183012f7kVAuZh&q=shirt%20for%20man&_keyori=ss&clickTrackInfo=textId--7180086757713097669__abId--300705__pvid--4e318e09-7e65-478c-9a00-bfb153ffb764__matchType--1__srcQuery--shart%20for%20man__spellQuery--shirt%20for%20man&from=suggest_normal&sugg=shirt%20for%20man_1_1")

#     x_path = '//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a'

#     title = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, x_path))).text

#     scrape = {"title":title,"price":30}
    
#     return HttpResponse(title)
    return render(request,'daraz/form.html')


# Create your views here.

# Create your views here.
