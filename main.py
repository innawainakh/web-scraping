import requests
from bs4 import BeautifulSoup
import csv
user_input = input("enter country:  ")
def weather1():
    #the url of the main weather page
    weather_url = "https://www.timeanddate.com/weather/"
    #adding the main url will the user input will go to the page of country weather the user choosed
    weather = weather_url + user_input
    weather_page = requests.get(weather)
    content = weather_page.content
    soup = BeautifulSoup(content, "lxml")
    web1 = soup.findAll("div", {"class": "bk-focus__info"})
    weather_data_web1=[]
    for i in web1:
        # tbody because all the data i need is in a table
        country=i.contents[0].find("tbody")
        #  for loop in all the rows i want to print data from
        rows = country.find_all("tr")
        for row in rows:
            data = ' '.join(r.get_text(strip=True) for r in row.find_all(["th", "td"]))
            #abd then append all the data in a list
            weather_data_web1.append(data)
            # to convert the list to string txt
            weather_data_text1 = '\n'.join(weather_data_web1)
    return weather_data_text1

def weather2():
    weather_url = "https://www.timeanddate.com/weather/"
    weather = weather_url + user_input
    weather_page = requests.get(weather)
    content = weather_page.content
    soup = BeautifulSoup(content, "lxml")
    web2=soup.findAll("div", {"class": "bk-focus__qlook"})
    weather_data_web2=[]
    for x in web2:
        country_capital=x.find("a")
        weather= x.find("div", class_="h2")
        paragraphs = x.find_all("p")
        print("Country Capital:", country_capital.text.strip())
        print("Weather:", weather.text.strip())
        for p in paragraphs:
           data=p.get_text("\n", strip=True)
           weather_data_web2.append(data)
           weather_data_text2 = '\n'.join(weather_data_web2)
    return weather_data_text2

def time_zone():
    # here is the same code as def weather 1 because the both are in a table
    weather_url = "https://www.timeanddate.com/time/zone/"
    weather = weather_url + user_input
    weather_page = requests.get(weather)
    content = weather_page.content
    soup = BeautifulSoup(content, "lxml")
    web1 = soup.findAll("div", {"class": "bk-focus__info"})
    time_zone_data=[]
    for i in web1:
        country = i.contents[0].find("tbody")
        rows = country.find_all("tr")
        for row in rows:
            data = ' '.join(r.get_text(strip=True) for r in row.find_all(["th", "td"]))
            time_zone_data.append(data)
            time_data_text = '\n'.join(time_zone_data)
    print("-----------------")
    return time_data_text
weather_data_text1 = weather1()
print(weather_data_text1)
print("-------------")
weather_data_text2=weather2()
print(weather_data_text2)
time_data_text = time_zone()
print(time_data_text)

with open(f"countries/{user_input.lower()}.csv", "a",encoding="utf-8")as file:
 csv_writer=csv.writer(file)
 csv_writer.writerow(["data ", "value" ])
 csv_writer.writerow([weather_data_text1])
 csv_writer.writerow([weather_data_text2])
 csv_writer.writerow([time_data_text])