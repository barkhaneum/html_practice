import requests
from bs4 import BeautifulSoup

base_url = f'https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=194344&target=after'
# start_num = 1
# end_url = '&refresh_start=0'

# URL = base_url + str(start_num) + end_url
URL = base_url

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

# movie_title = soup.select('select[id=current_movie] > option')
# news_section = soup.select('select[id=current_movie] > option[value]')[0].string  #태그 안의 내용가져오기
# news_section = soup.select('select[id=current_movie] > option[value]')[0]['value']   #태그안의 속성값 가져오기
news_section = soup.select('select[id=current_movie] > option[value]')

movie_title = []
movie_code = []

# 영화 코드와 영화 제목 크롤링
for i in news_section:
    movie_title.append(i.string)
    movie_code.append(i['value'])


# 상영중인 영화의 평점과 감상평 가져오기

end_URL = '&target=after'
movie_code_ = ''
Review_URL = 'https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=' + movie_code + end_URL


# for i in movie_code:
#     movie_code_ = str(i)
#     response = requests.get(Review_URL)
#     soup = BeautifulSoup(response.text, 'html.parser')

#평점이랑 리뷰 가져오는중...
# Review_URL = https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=189622&target=after
# response = requests.get(Review_URL)
# soup = BeautifulSoup(response.text, 'html.parser')
# soup.select('td[class=title]')

# print(news_section)

# for news in news_section:
#     a_tag = news.select_one('dl > dt > a')
#     news_title = a_tag['title']
#     news_link = a_tag['href']
#     print(news_title)
#     print(news_link, '\n')
