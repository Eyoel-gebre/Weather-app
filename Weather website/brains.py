from bs4 import BeautifulSoup
import requests 

html = requests.get('https://weather.com/weather/tenday/l/Kent+WA?canonicalCityId=87f99532a3620b4c85a20ad8ee3ebdeb604f349d79d2d072faff0873d1912d13')
soup = BeautifulSoup(html.content, 'html.parser')
weekweather = soup.find_all('div', class_ = 'QpFD- _1MLf5') #gets all days

# data is kept in indexed list
days = []     #list of days
weathers = []  #list of weather
for daydata in weekweather:
	day = daydata.find('h2', class_='_1Mebr').string
	weather = daydata.find('span', class_='_3x6cL').string
	days.append(day)            #grabse day and puts into list
	weathers.append(weather)	#grabs weahter and puts in list

#gets todays weather
weather = soup.find('span', class_='_8DL5').string 
days.insert(0,'Today')
weathers.insert(0, weather)

#gets rid of weird symbol
for i in range(len(weathers)):
	weathers[i] = weathers[i][0:2]+" F"

#opens index file and places new data
with open('index.html') as f:
	soup = BeautifulSoup(f, 'html.parser')

htmldivs = soup.find_all('div')

for i in range(len(htmldivs)):
	htmldivs[i].h2.string = days[i]
	htmldivs[i].p.string = weathers[i]

with open('index.html', 'w') as f:
	f.write(str(soup))
	print('FINISHED')