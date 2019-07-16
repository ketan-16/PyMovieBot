from requests import get
from bs4 import BeautifulSoup

s1='https://www.imdb.com/search/title/?title='
temp= input("Enter Movie Name:")
s2=temp.replace(' ', '+')
s3='&sort=num_votes,desc&page=1'

response = get(s1+s2+s3)

html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)
movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')

movie = movie_containers[0] 
name = movie.h3.a.text
year = movie.h3.find('span', class_ = 'lister-item-year text-muted unbold').text
print("Movie Name:"+name)
year=year.replace('(','')
print("Year:"+year.replace(')',''))
print("IMDB Rating:" + movie.strong.text)
temp = movie.p.find('span', class_ = "genre").text
genre = temp[1:].replace(" ","")
print("Genre:"+genre)
print(" ")
	
	
a1='https://www.imdb.com/search/title/?genres='
a3='&sort=boxoffice_gross_us,desc'

b1='https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&genres='

ch=input("Select Algorithm: \n Algorithm 1 \n Algorithm 2 \n >>")
if(ch==1):
	take=(a1+genre+a3)
else:
	take=(b1+genre)
	
response = get(take)

html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)
movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')

print("Here are the best recommendations:")
try:
	for j in range (0,5):
		movie = movie_containers[j] 
		moviename=movie.h3.a.text
		if(moviename==name):
			continue
		print("Movie Name:"+moviename)
		print("IMDB Rating:" + movie.strong.text)
except:
	print("")

