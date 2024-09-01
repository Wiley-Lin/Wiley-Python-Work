import requests
from bs4 import BeautifulSoup


def main():
	url = "https://www.imdb.com/chart/top/"
	header = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}
	response = requests.get(url, headers=header)
	html = response.text
	soup = BeautifulSoup(html)
	tags = soup.find.all('span', {'class': 'ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating'})
	for tag in tags:
		print(tag)
		print('-')


if __name__ == '__main__':
	main()
