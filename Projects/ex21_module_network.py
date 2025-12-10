# 데이터 분석을 통한 서비스를 개발하려면.. 데이터 수집이 필요
#1. 회사나 개인이 가진 매출데이터, 설문데이터, 회원데이터 등 엑셀파일같은 형태의 데이터 [ 파일 입출력(표준함수 open) ]
#2. 날씨정보, 채용정보, 행사정보 등 웹을 통해 서비스 되는 데이터 [ urlib requst 모듈, 외부모듈(requests, BeautifuSoup)]

# 파이썬에서 웹의 데이터를 불러와서 분석하는 맛보기 수업.

#1) 네트워크 작업을 위한 모듈 추가
from urllib import request

# request라는 하위모듈이 가진 네트워크상의 파일을 열어주는 기능함수를 호출
address= 'https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/aaa.txt'
url= request.urlopen(address)
data= url.read()
print(data)
print()
#한글이 깨진다면.. UTF-8로 디코딩(해독)해야함. 
print( data.decode('UTF-8') )
print('-'*20)
print()

#2) 엑셀파일 같은 표형태의 대량의 값들을 가진 데이터를 간단한 텍스트만 제공할때. 어떤 문제가 있는지..
address= 'https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/bbb.txt'
url= request.urlopen(address)
data= url.read()
print(data.decode('UTF-8'))
print('-'*20)
print()
# 데이터 구별이 안가...분석이 불가능

#3) 데이터 구별을 위해 cel별로. 띄어쓰기를 도입해봄.. 1차 시도. (한줄 단위로.. 엑셀의 행을 처리하고.. 띄어쓰기로 칸들을 처리)
address= 'https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/ccc.txt'
url= request.urlopen(address)
data= url.read()
print(data.decode('UTF-8'))

# 띄어쓰기 방식의 문제점 확인 .. 값별로 분리해내기.. 왜? 분석하려면.. 분리해야 하니까.
str_data= data.decode('UTF-8')

# 한 행(줄row) 별로 문자열을 분리.. [ 줄바꿈문자 \n 을 기준으로 문자열을 분리. ]
lines= str_data.split('\n')
print(lines)
print(lines[0])
print(lines[1])
print(lines[2])

# 한줄안에서 칸별로 분리.. [ 줄별로 띄어쓰기 ' ' 를 기준으로 문자열을 분리]
values= lines[0].split(' ')
print(values)
#나이 출력?
print('나이:', values[1])
#전공 출력?
print('전공:', values[2])

values= lines[1].split(' ')
#나이 출력?
print('나이:', values[1])
#전공 출력?
print('전공:', values[2])
print("-"*20)
print()

#4) 그래서 등장한 칸별로 데이터 구분을 확실히 하기위해 ,(꼼마) 를 구분자로 하는 표기형식(파일형식)을 도입됨 [csv] - 초기 웹 open api 표준형식
address= 'https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/ddd.csv'
url= request.urlopen(address)
data= url.read()
print(data.decode('UTF-8'))

#분석
#줄 단위 분리
lines= data.decode('UTF-8').split('\n') 
print(lines)
print()

#먼저, 제목줄의 글씨들 뽑아오기
values= lines[0].split(',')
for v in values:
    print(v, end='\t')
print()
print('-'*40)

# 제목 줄 제외한 값들을 반복문으로 처리
for idx in range(1,len(lines)):
    values= lines[idx].split(',')
    for v in values:
        print(v, end='\t')
    print()
print('-'*40)
print()

# csv와 유사한 파일형식 tsv(tab separated values) 도 존재함. ML 데이터셋에 꽤 존재함.
# 분석기법은 csv와 같기에 no 수업

#5) csv의 단점인.. 값들의 식별자를 알기 어렵다는 문제를 개선한 XML 표기형식(파일형식)
address= 'https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/ggg.xml'
url= request.urlopen(address)
data= url.read()
print(data.decode('UTF-8'))

#csv 처럼 .. 읽어온 파일형식을 분석(parse) 해보기. [ split()으로 처리하기에는 너무 번거로움. ]

#xml문자열을 분석해주는 별도의 모듈이 등장함. 표준모듈임. 별로설치는 필요없고. 단지 import만.
import xml.etree.ElementTree as ET

# 최상위 요소(element) 부터 찾아오기
root= ET.fromstring(data.decode('UTF-8'))
print(root)

# studenst 요소(root) 안에 있는 item 이라는 이름을 가진 요소들을 모두 찾기
items= root.findall('item')
print(items)
print(len(items))
print()

#각 item 요소안에 있는 [이름,나이,전공,주소] 요소들 분리하기 (태그이름으로 요소들을 찾아오기)
for item in items:
    name= item.find('name') # 태그명으로 요소 찾기
    age= item.find('age')
    major= item.find('major')
    address= item.find('address')

    #각 요소안에 있는 글씨데이터 출력
    print(name.text, age.text, major.text, address.text)
print()
print('-'*30)
print()

#6) XML의 불변한점.. 시작.종료태그문이 글자수를 너무 많이 차지함. 그래서 등장한 json 형식
address= 'https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/hhh.json'
url= request.urlopen(address)
data= url.read()
print(data.decode('UTF-8'))
print(type(data.decode('UTF-8')))
print()

# json 표기형식의 문자열을 분석하기 위한 표준 모듈 추가
import json

# json모듈의 기능 중.. json형식의 문자열을 파이썬의 dictionary 타입으로 변환해주는 기능 loads()
aa= json.loads(data.decode('UTF-8'))
print(type(aa))

# 데이터 전체 제목 얻어오기
title= aa['data_title']
print(title)

t_count= aa['total_count']
print(t_count + 2)

items= aa['data']
for item in items:
    print( item['name'], item['age'], item['major'], item['address'])
print()
print('-'*20)
print()

# [별외]  표준모듈인 request의 단점. [한글깨짐 문제, 예외처리를 직접 해야 함.]
try:
    address= 'https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/aaa.txt'
    address= 'https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/aa.txt' # 파일명 오류. url 오류
    url= request.urlopen(address)
    data= url.read()
    print(data)
except:
    print('에러!!')

print('여기가 코드 마지막...')

# 그래서 보통 네트워크 통신작업에.. request 표준모듈을 조금 미흡함.
# 해서.... 외부에서 개발된 네트워크 전용 모듈을 사용함 requests 외부모듈..소개












