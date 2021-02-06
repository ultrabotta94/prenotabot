from selenium import webdriver
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
import time

def chrome():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    return browser
    

def apri_pagina(aula):
    browser = chrome()
    if aula == 'FB':
        browser.get('https://agende.unipi.it/xop-afl-swa')
        print("Fai il login con le credenziali d'ateneo")
        return browser
    elif aula == 'PC':
        browser.get('https://agende.unipi.it/lfm-snn-wpj')
        print("Fai il login con le credenziali d'ateneo")
        return browser
    else:
        print("Aula studio non trovata")
        
    
    
    
#funzione che preme lo slot n volte (si usa per prenotare la mattina)

def premi_slot(button, i, n):
    for h in range(n):
        button[i].click()
        time.sleep(0.4)
        button[i + 1].click()
        
        
def prenota_mattina(pagina, giorno):
    button = pagina.find_elements_by_class_name('fc-time-grid-event')

    condizione = True

    while condizione:
        x = datetime.now()
        time.sleep(5)
        if x.hour ==  8 and x.minute == 30:
            condizione = False
        
        if condizione == False:
            for i in range(10):
                time.sleep(1)
                premi_slot(button, giorno, 50)
                
def trova_posto(pagina, giorno, slot):
    continua = True
    i = giorno +slot
    while continua:
        pagina.refresh()
        while True:
            time.sleep(0.5)
            button = pagina.find_elements_by_class_name('fc-time-grid-event')
            if button != []:
                break
    #time.sleep(2)
        if "ag-slot-mine" in button[i].get_attribute("class"):
            #DA FARGLI FARE UN SUONINO
            continua = False
        else:
            time.sleep(2)
            button[i].click()
            time.sleep(1)
