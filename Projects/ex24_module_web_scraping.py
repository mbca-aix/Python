# 웹 스크래핑 : 웹 페이지에서 특정 정보를 추출하는 작업

# 외부 모듈 : requests, beautifulsoup4 [별도 설치 필요]

# 웹 페이지를 분석 - 웹 페이지를 만드는 문법 HTML, CSS, JavaScript

# 아주 간단한 웹페이지를 만들어보기. [ HTML, CSS, JavaScript 언어를 다뤄보기. (web-test)]

import requests
response= requests.get('https://2017mrhi.github.io/web-test/')
print(response.text)
print()

# html 웹문서를 분석.. 요소들을 찾아서 안에 있는 값을 뽑아내기 [외부 모듈 BeautifulSoup]
from bs4 import BeautifulSoup

# HTML분석가 객체를 생성
soup= BeautifulSoup(response.text, "html.parser")

# p요소들 모두를 찾아보기
p_list= soup.select('p')
print( len(p_list) )

print(p_list[0].string)
print(p_list[1].string)

# 아이디로 찾기 - 이미지경로 찾기
img= soup.select_one('#kk')
print('이미지 경로 :', img.get('src')) #src 속성의 값을 얻어오기

# 클래스로 찾기 
es= soup.select('.aa')
print(es[1].string)
print()
#--------------------------------------------------------------

#[실습] 네이버 금융 페이지의 '코스피 지수' 스크래핑 해보기 (주의. 막 실행하면 안됨.)
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response= requests.get('https://finance.naver.com/sise/', headers=headers)
#print(response.text)
soup= BeautifulSoup(response.text, 'html.parser')

# 웹 문서에서 특정 요소를 찾기
span_element= soup.select_one('#KOSPI_now')
print('코스피 지수 :', span_element.string)



#[과제] 웹 페이지 분석하기... [쇼핑몰 사이트의 가격 추출. robots.txt 확인]




