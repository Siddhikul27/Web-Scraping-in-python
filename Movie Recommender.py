from bs4 import BeautifulSoup as SOUP
import re
import requests as HTTP

def main(emotion):
	if(emotion == 'sad'):
		urlhere =  'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter'

	elif(emotion == 'surprise'):
		urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter'


	response = HTTP.get(urlhere)
	data = response.text

	soup = SOUP(data, "lxml")

	title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})
	return title

if __name__ == '__main__':

	emotion = input("Enter the emotion: ")
	a=main(emotion)
	count = 0

	if(emotion == "anger" or emotion == 'surprise'):
		for i in a:
			tmp = str(i).split('>;')

			if(len(tmp)== 3):
				print(tmp[1][:-3])
			if(count>13):
				break
			count += 1
	else:
		for i in a: 
            tmp = str(i).split('>') 
  
            if(len(tmp) == 3): 
                print(tmp[1][:-3]) 
  
            if(count > 11): 
                break
            count+=1