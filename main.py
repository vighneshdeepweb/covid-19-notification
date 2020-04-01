from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\Vighnesh\\Desktop\\Python Projects\\covidNotify\\icon.ico",
        timeout = 6,
    )

def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    while True:
    #notifyMe("Vighnesh", "Lets Sop the spread of this Virus together")
         myhtmlData = getData('https://www.mohfw.gov.in/')

         soup = BeautifulSoup(myhtmlData, 'html.parser')

    #print(soup.prettify())
         myDataStr = ""
         for tr in soup.find_all('tbody')[0].find_all('tr'):
             myDataStr += (tr.get_text())
         myDataStr = myDataStr[0:]
      
       
      

         itemList = myDataStr.split("\n\n")
         states = ['Maharashtra', 'Bihar', 'Uttar Pradesh', 'Telengana']

         for item in itemList[0:27]:
           dataList = item.split('\n')
           if dataList[1] in states:
            
              nTitle = 'Cases of Covid-19'
              nText = f"State: {dataList[1]}\n  Confirmed Case:  {dataList[2]} \n Cured: {dataList[3]}\n Deaths: {dataList[4]}"
              notifyMe(nTitle, nText)
              time.sleep(2)
         time.sleep(3600)


    
    