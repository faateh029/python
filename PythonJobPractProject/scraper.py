import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"

mainPage= requests.get(url)
soup=BeautifulSoup(mainPage.text , "lxml")

Job_Title =[]

Company_Name=[] 
Location =[]

Date_Posted=[] 

Full_Description=[] 

cards = soup.find_all("div" , class_="card-content")
for card in cards:
    title_element = card.find("h2" , class_="title is-5")
    #Extracting Job_Title
    title_element_text=title_element.text
    if "Python" in title_element_text:
        #appending Job_Title
        Job_Title.append(title_element_text)


        
        #Extracting Location
        locationElement = card.find("p" , class_="location")
        if(locationElement):
            locationElementText=locationElement.text
            Location.append(locationElementText.strip())
        else:
            Location.append("N/A")
        
       


        #Extracting Date_Posted
        datePostedElement = card.find("time")
        if(datePostedElement):
            datePostedElementText = datePostedElement.text
            Date_Posted.append(datePostedElementText)
        else:
            Date_Posted.append("N/A")



        #Extracting company name
        companyNameElement = card.find("h3" , class_="subtitle is-6 company")
        if(companyNameElement):
            companyNameText = companyNameElement.text
            Company_Name.append(companyNameText)
        else:
            Company_Name.append("N/A")
        
        DescPageUrl=card.find("a" , string=lambda t: "Apply" in t if t else False).get("href")
        descriptionPage = requests.get(DescPageUrl)
        descPage = BeautifulSoup(descriptionPage.text , "lxml")
        fullDescriptionBox = descPage.find_all("p")
        if(len(fullDescriptionBox)>1):
            fullDescriptionBoxText= fullDescriptionBox[1].text
            Full_Description.append(fullDescriptionBoxText.strip())
        else:
            Full_Description.append("N/A")




dataFrame = pd.DataFrame({
    "Job Title": Job_Title,
    "Company": Company_Name,
    "Location": Location,
    "Date Posted": Date_Posted,
    "Full Description": Full_Description
})


print(dataFrame)          
dataFrame.to_csv("C:/Users/fa/Desktop/python/PythonJobPractProject/PythonJobs.csv", index=False)

