# 데이터 분석에 많이 사용되는 외부모듈 : numpy, pandas, matplotlib

#1) numpy ( numberic python ) : 리스트같은 데이터에 대해 행렬 수학계산을 해주는 모듈

#1. 일반적인 파이썬의 리스트 연산 특징
aaa= [10,20,30]
bbb= [4,5,6]

print(aaa)
print(bbb)

#파이썬의 리스트 데이터를 덧셈하면 수학의 덧셈이 아니라.. concat()이 되어 결합됨.
ccc= aaa + bbb
print(ccc)
print()

print(len(aaa))
print(len(bbb))
print(len(ccc))
print()

# 위와 같은 리스트의 덧셈 특징을 수학적으로 계산해주는 모듈 사용하면.. 나중에 ML이나 데이터분석에 활용가능
# numpy 모듈 설치 [ pip install numpy ]
import numpy as np

#넘파이 전용 리스트(배열 array)로 생성
aa= np.array([10,20,30])
bb= np.array([4,5,6])

print(aa)
print(bb)

# 리스트와 차이점. 산수 덧셈을 하면 배열의 요소끼리 덧셈을 수행함
cc= aa + bb
print(cc)

# 넘파이 배열을 본인의 요소개수(행렬 모양 - 2차원)를 볼수 있는 값을 이미 보유하고 있음. len()사용 안함
print( aa.shape )
print( bb.shape )
print( cc.shape )
print()

# 2차원 배열(행렬 - 표 구조)
aaaa= np.array([ [100,200,300,400],[500,600,700,800]  ])
print(aaaa.shape) #(행,열) (2,4)

bbbb= np.array([ 
    [3,4,5,6],
    [7,8,9,0] 
    ])
print(bbbb.shape) #(2,4)

#행렬의 수학연산.. (각 자리에 해당하는 요소끼리 산술연산)
cccc= aaaa + bbbb
print(cccc)
print(cccc.shape)

# 사칙연산 모두 가능
print(aaaa-bbbb)
print(aaaa*bbbb)
print(aaaa/bbbb)

# 연산할때 주의.. 행렬 요소끼리 연산이기에.. 개수가 다르면...에러..
# dddd= np.array([ [10,20,30,40],[40,50,60] ])
# #print(aaaa + dddd) 
# print(dddd.shape)

print('-'*30)
print()
#-------------------------------------------------------------

#2) pandas - 데이터분석할 때 n차원 행렬(2차원구조 표형태가 가장 흔함)의 구조를 용이하게 만들어주는 모듈(엑셀, csv, tsv 데이터 처리에 용이)
# pandas 외부모듈 설치 pip install pandas
import pandas as pd

# 1차원 배열 구조 : Series [엑셀의 한 column(열) 데이터들 - 세로줄]
aa= pd.Series(['sam', 'robin', 'hong'])
print(aa)
print()

#자동으로 부여되는 인덱스 번호를 원하는 식별자로 변경가능
bb= pd.Series(['seoul', 'tokyo', 'paris'], index=['korea', 'japan', 'france'])
print(bb)
print()

# 2차원 배열 구조(표구조) : DataFrame
cc= pd.DataFrame([ ['aa','bb','cc','dd'],['11','22','33','44']  ])
print(cc)
print()

# key:value 형태의 딕셔너리 타입으로 데이터프레임을 생성하면 key 식별값이 column 의 이름의 됨
dd= pd.DataFrame( {"aa":[10,20,30], "bb":[100,200,300], "cc":[1000,2000,3000]} )
print(dd)
print()

# csv 파일을 읽어와서 DataFrame 만들기
ee= pd.read_csv('./files/scores.csv') # 읽어온 결과가 DataFrame 객체임
print(ee)
print()

print(ee.head()) #상위 5줄
print()

print(ee.tail()) #하위 5줄
print()

print(ee.head(3)) #상위 3줄

#행열모양 확인 변수
print(ee.shape)

#컬룸명을 확인할 수 있음
print(ee.columns)
print()

#컬룸명을 변경하여 지정할 수도 있음.
# ee.columns= ['aa','bb','cc','dd']
# print(ee)

#데이터프레임의 구조정보를 한번에 알려주는 기능함수
print( ee.info() )
print()

# 특정한 컬룸데이터만 보기 -- 한 column의 Series 
print( ee['국어'] )
print()

# 국어성적 평균, 영어성적 중에 1등값(max)
print('korea average :', ee['국어'].mean() )
print('english maximum :', ee['영어'].max() )
print()

# 데이터분석(숫자데이터)에 많이 사용되는 평균, 최대, 최소값, 개수 등의 계산 정보를 한번에 볼 수 있는 기능
print( ee.describe() )
print()

# 여러개의 컬룸을 동시에 보기 - 결과를 DataFrame 으로 줌
print( ee[['영어','수학']] )
print()

# 데이터 프레임에서 특정 줄(row) 데이터 가져오기 -- 첫번째 줄(행row)
row= ee.loc[0] #0번 인덱스의 한줄
print(row)
print(type(row))
print()

# 특정 범위의 행 데이터 가져오기 2~5
rows= ee.loc[2:5]
print(rows)
print(type(rows))
print()

# 특정 범위 이후..모든 줄.. 즉. 끝까지
rows= ee.loc[2:]
print(rows)
print()

rows= ee.loc[:4]
print(rows)
print()

rows= ee.loc[:]
print(rows)
print()

# 행,열 모두를 지정
rows= ee.loc[2:, '이름']
print(rows)
print()

rows= ee.loc[4:, ['이름','수학']]
print(rows)
print()

# 데이터 전처리 할때 용이한 연산 문법.. 
# 예) 모든 국어점수에 2배를 해야 함.
ee['국어']= ee['국어'] * 2 # 모든 각가의 요소들에 *2 연산 해줌. 이를 broadcast 브로드캐시팅 ...
print(ee)
print()

print('-'*30)
print()
# 엑셀파일 읽기!!

#예전버전에서는 xlrd 라는 모듈을 이용하여 엑셀을 읽어들였음.
#현재버전에서는 openpyxl 라는 모듈을 기본으로 사용함
# openpyxl 는 별도 설치가 필요함. [ pip install openpyxl 
# import 안해도 판다스가 openpyxl 모듈을 import 하여 읽어들임.

gg= pd.read_excel('./files/scores.xlsx')
print(gg)
print()

# 특정 sheet의 표를 데이터프레임으로 읽어오기
hh= pd.read_excel('./files/scores.xlsx', sheet_name='Scores')
print(hh)
print()

ww= pd.read_excel('./files/seoul_weather_2025.xlsx')
print(ww)
print(ww.columns)
print(ww['최저기온(°C)'])
print(ww['최저기온(°C)'].max())
print(ww['최저기온(°C)'].min())
print(ww['최저기온(°C)'].mean())
print()

#이후 수업은... ML/데이터분석 수업에 만나요~~ web 수업 후
print('='*50)
print()

# 데이터 분석을 용이하게 하려면.. 시각화를 해야함.. 이를 위한 모듈
#3) matplotlib 모듈 설치 
# 숫자 데이터들에 대한 그래프를 쉽게 그려줌 [ 선 그래프, 막대 그래프, 원 그래프, 산점도 그래프 등..제공 ]
import matplotlib.pyplot as plt

#한글깨지면..한글글꼴로 지정
plt.rcParams['font.family']= 'Malgun Gothic'

#예제1: 하루 동안의 온도 변화 그래프 [ 선 그래프 : plot() ]
# 시간(시)별 온도
hours = [6, 9, 12, 15, 18, 21, 24]           # 그래프의 x 축 데이터
temperature = [10, 14, 18, 20, 17, 13, 11]   # 그래프의 y 축 데이터

#plt.plot(hours,temperature)
#plt.plot(hours,temperature, marker='o')
#plt.plot(hours,temperature, marker='x')
#plt.plot(hours,temperature, marker='v')
#plt.plot(hours,temperature, marker='o', linestyle='-')
#plt.plot(hours,temperature, marker='o', linestyle='--')
#plt.plot(hours,temperature, marker='o', linestyle=':')
plt.plot(hours,temperature, marker='o', linestyle='-', color='orange')

plt.title('하루 동안의 온도 변화')
plt.xlabel('시간 (시)')
plt.ylabel('온도 (°C)')
plt.show()
#--------------------------------------

#예제2: 학생 수학 점수 비교  [ 막대 그래프 bar() ]
# 데이터 준비
students = ["홍길동", "손흥민", "류현진", "박세리"]
scores = [85, 45, 52, 92]


# plt.bar(students, scores, color='skyblue')
colors= ['green' if s>60 else 'red' for s in scores ]
plt.bar(students, scores, color=colors)

plt.title('학생별 수학 점수')
plt.xlabel('학생 이름')
plt.ylabel('점수')
plt.ylim(0,100)
plt.grid(axis='y')

plt.show()

# 예제3: 롯데리아 월별 매출 데이터 시각화  [ 산점도 그래프 ]
# 롯데리아 월별 매출 데이터 준비 (가상)
data = {
    '월': ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'],
    '매출액(만원)': [4200, 3900, 4500, 4700, 5200, 5800, 6100, 6400, 5900, 5500, 5300, 5000]
}

#판다스로 딕셔너리를 처리
df= pd.DataFrame(data)
print('롯데리아 월별 매출 데이터')
print(df)

plt.figure(figsize=(8,5)) #너리 8인치, 높이 5인치 -- 그래프 여러개가 그려지는 도화지
plt.scatter(df['월'], df['매출액(만원)'], marker='o', color='tomato')

plt.title('롯데리아 2025년 월별 매출 변화')
plt.xlabel('월')
plt.ylabel('매출액 (만원)')
plt.grid(True)

#각 점 위에 매출 숫자 표시
for i,value in enumerate(df['매출액(만원)']):
     plt.text(i, value+50, f'{value}', ha='center', fontsize=14)

plt.show()





