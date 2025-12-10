#변수에 대해 알아보기.
#변수란. 데이터를 저장하는 메모리공간.

# 숫자 100을 저장하는 변수를 만들려면.. 그 값이 무엇인지 의미하는 이름으로 변수명(영문자)을 쓰고.. = 대입연산자로 값을 대입하면 됨.
number= 100 # 이렇게 값을 가지고 있는 영문자을 만들면.. 이 영문자를 변수라고 부름.

print(number) # 변수의 이름을 쓰면.. 그 안에 있는 값이 출력됨.
print("number") # number라는 이름의 변수를 출력하는 것이 아니라.. number라는 글씨(문자열) 데이터를 출력한 것임.

print(number) #변수명을 한번더 사용해도 그 값이 여전히 잘 출력됨.

print(3+5)
print(number+200)
print(number+number)
print(number*number) #제곱 연산

# 변수는 한번에 1개의 값만 가질 수 있음.
# 그렇기에 다른 값을 대입하면 이전에 가지고 있던 값을 없어짐.
number= 200
print(number)


# 변수에 값을 대입할때. 값이 아니라. 식을 쓰면 그 결과가 대입됨.
number= 30+50
print(number)

# = 는 등호연산이 아님.!!! 파이썬에서 = 는 오른쪽값을 왼쪽변수에 대입하는 대입연산자임.
#200= number #error
print()
#-----------

# 변수의 이름을 정하는 규칙.
#1. 영문자 사용(대소문자 구분) - 가급적 소문자로만...(글자수 제한 없음.)
#2. 숫자 사용가능. 단, 첫글자는 안됨.  number1(O), 3number(X); 
#3. 특수문자는 오직 _(언더바)만 허용. (띄어쓰기도 안됨.)

#+. 가급적 변수의 이름은 그 값이 어떤값인지 알수있는 의미를 가진 영문자를 사용할 것을 권장함.
# [이름, 나이, 성별, 집 주소, 회사 주소, 성인여부 ]
name= '홍길동'
age= 20
gender= 'male'
home_address='seoul'   # 두 단어 이상을 사용하여 변수명을 지정해야 할는 경우도 아주 많음. 두 단어가 있다면 구분자로 언더바를 사용
company_address2='incheon' 
is_adult=True

#언더바로 구분하는 표기법을 [스네이크 표기법 snake case]이라고 부름.
#다른 유명한 표기법이 2개 더 존재함.
#낙타 표기법(camel case) :    homeAddress [파이썬을 제외한 다른 모든 프로그램 언어들의 변수명 짓는 표기법]
#쌍봉낙타 표기법(pascal case) : HomeAddress [클래스라는 문법이 이름을 정할때 사용됨.(파이썬에서도...)]

#파이썬에서 [변수, 함수]는 '(소문자)스네이크 표기법', [클래스]는 '파스칼 표기법' 사용을 권장함.

#가끔은 그 의미를 나타내는 영단어를 모를수도 있음. ( 구구단의 '단' 값을 저장 two times table)
#모를때는 소리나는 데로.. 그냥 알파벳 사용
dan= 5

#영문자를 권장하지만.. 한국에 대한 국뽕이 너무 심하면..
나이= 30
print(나이)
#원래 파이썬은 한글이름을 식별자로 사용하면 에러.임.
#파이썬3버전 이상의 인터프리터(통역가)가 알아서 알파벳으로 변경해서 동작함
#--------------------------------------------------

# 데이터를 저장하는 공간을 '변수'라고 부르는 이유..
# 가지고 있는 값을 변경할 수 있다는 것을 강조하고 싶어서..
100 # <-- 이건 언제나 100 [ 그래서 이런 값을 '리터럴 literal 상수'라고 부름 ]

# 변수는 값이 변경될 수 있는 것을 의미함.
number= 300
print(number)

#변수는 한번에 1개만 가질 수있기에 다른 값을 저장하고 싶다면..
#새로운 변수롤 만들어서 대입해야 함.
#[10, 20] 2개의 숫자를 저장하려면.. 변수 1개가 아니라 2개를 사용해야 함.
number1= 10
number2= 20

#변수끼리 연산도 가능함.
print(number1 + number2)
#연산에 사용한 데이터도 보여주고 싶다면..[여러개의 데이터 출력 방식]
print(number1, number2, number1+number2)
#연산기호(특수문자 + =)도 화면에 같이 보여주고 싶다면.
print(number1, '+', number2, '=', number1+number2 )

#어제의 복습. 여러개 출력을 조금 편하게..  "".format() 기능 사용해보기
print("{} + {} = {}".format(number1, number2, number1+number2))
#더 새로운 문법. f-string
print(f"{number1} + {number2} = {number1+number2}")
print("number1 + number2 = number1+number2")

# 당연히 값이 없는 변수는 에러..
# number3 #이건 변수를 만든것이 아님.
# print(number3)
#----------------------------
print()

# 변수는 데이터를 저정하는 것임.
# 근데 데이터는 숫자만 있는것은 아님. 이름, 로그인여부 등.. 많은 종류의 데이터들이 존재함.
# 이 종류들을 파이썬을 구분하여 사용함. 이 종류들을 파이썬에서는 Data Type(자료형) 이라고 부름.

# 파이썬은 여러종류의 데이터 유형을 구분하여 명칭을 정해놓았음.
# 이 명칭을 이해하는 것은 앞으로 매우 중요함. 
#1. 기본 자료형 : 숫자(int, float), 문자(열) str, 논리값 bool
#2. 배열 자료형 : list, tuple, dictionary, [set]
#3. 값이 없는 자료형 : None
#4. 개발자가 만드는 자료형 : [class 라는 문법을 통해 설계]

# 파이썬은 각 데이터의 자료형을 알려주는 기능(function 함수)이 내장되어 있음.
print( type(100) ) #정수
print( type(3.14) ) #실수
print( type('hello') ) #문자열
print( type("hello") ) #문자열
print( type(True) ) #논리값 (bool 값)
print( type(3+5) ) #식의 결과 자료형
print( type(5>10) )
print()

#파이썬의 변수는 어떤 자료형이든 저장이 가능함.

a=10
print(a)

b=5.26
print(b)

c= False
print(c)

d= 5>3
print(d)

e= "sam"
print(e)

# 변수들이 가진 자료형을 출력해보기
print( type(a) )
print( type(b) )
print( type(c) )
print( type(d) )
print( type(e) )
print("----------------")
print()

# C, Java, Kolin 와 같은 컴파일 언어들은 변수를 만들때 저장할 수 있는 값의 자료형이 고정되어 있음.[정적 타입 언어]
# Python, JavaScript 와 같은 인터프리터 언어들은 변수에 저장하는 값의 자료형이 달라도 모두 저장됨.[동적 타입 언어]

# data 라는 이름의 변수 선언(만들다)
data= 10
print(data)
print(type(data))

data= 3.14
print(data)
print(type(data))

data= False
print(data)
print(type(data))

data= "robin"
print(data)
print(type(data))

#data= robin #error
robin= 1000
data= robin
print(data)
print(type(data))

data= "100"
print(data)
print(type(data))

#그렇기에..
#print( data + 20 ) #error -- 문자+숫자 는 에러!!

# 그럼에도 산술적인 덧셈을 하고 싶다면.. "100" --> 100 로 변환을 요청..
# 파이썬은 문자열을 숫자로 변환해주는 기능함수가 존재함. 
print( int(data) + 20  )

data="nice"
#print( int(data) + 30 ) #error - 숫자모양의 문자열이 아니면 int로 바꿀 수 없어요..

data= "537 45"
#print( int(data) + 10 ) # error- 공백문자도 ... 문자열내용이기에..int로 바꿀 수 없어요.

data= "3.14"
#print( int(data) + 20  ) # 소수점이 있는 숫자는 int()는 불가능. 에러..

#당연히 실수형으로 바꿔주는 기능함수도 있게죠.. float()
print( float(data) + 5.2 )

#float()은 정수숫자모양도 변환가능
data= "1000"
print( float(data) )

# 나머지 기본자료형.. str(), bool()

# [잠깐..] + 연산은 숫자일때는 덧셈연산임.
print(10 + 20 + 30)
# 문자열에 + 연산을 하면 두 문자열이 결합된 하나의 문자열로 바뀜 "aaa"+"bbb"==> "aaabbb"
print("aaa" + "bbb" + "ccc") # 이때 + 는 결합연산자 라고 부름.

num= 10
print("aaa" + str(num)) #"aaa10"

no=1
print('학생' + str(no))
no=2
print('학생' + str(no))
no=3
print('학생' + str(no))
no=4
print('학생' + str(no))
no=5
print('학생' + str(no))
no=6
print('학생' + str(no))

num= 3.25
print("bbb" + str(num))

# 값이 없음을 논리값으로 변환하고 싶을 때 사용. 
# '값이 없음' 이라는 개념은 파이썬에서는 0
print( bool(0) )
print( bool(1) )
print( bool(2) )
print( bool("aaa") )
print( bool("") )

aaa=None
print(aaa)
print(type(aaa))
print()
#--------------------------------------------------------

# 변수의 효용성
# 결국, 프로그램이 실행될때 마다 그 값이 바뀔 수 있는 것은 변수를 만들어 사용.

#예) 사용자의 나이를 보여주는 프로그램 만들기...
print('당신의 나이는:', 20)
#이렇게 20이라는 숫자를 바로 쓰면.. 이건 언제나 20.. 상수..

age= 20
print('당신의 나이는:', age)

age= 30
print('당신의 나이는:', age)
print("-"*30)
print()
# 이렇게 숫자를 직접 개발자가 대입하면 그냥 그값이 나옴..
# 이건 사용자의 데이터가 아님.

# 그래서 사용자가 본인의 데이터를 키보드를 통해 입력하도록...
# 파이썬에서 키보드 입력을 받아서 주는 기능함수가 존재함 input()

# 사용자의 나이를 저장
#age= 값
# age= input('당신의 나이를 입력하세요 : ')
# print('입력받은 나이:', age)

# name= input('당신의 이름을 입력하세요 : ')
# print('이름 : ', name)

# 숫자, 문자열 모두 잘 받아짐.. 그래서 특별히 더 이상 볼게 없어보이지만..
# 아주 중요한....특징...  input()기능은 키보드의 모든 입력은 데이터의 모양과 상관없이 '문자열'이라고 생각함.
#print(10+"20") #error

# age= input('나이 : ') # age 변수에 입력된 값은 숫자키보드를 눌러도.. 문자열로 입력됨. "3"
# print('당신의 나이보다 5살 많은 나이는 : ', int(age)+5) #"3"-->3 변환

# 소수점 숫자 입력받아 연산해보기..
# average= input('평균을 입력하세요 : ') #"85.7" --> 85.7
# print('평균값 : ', float(average) + 1.5) 

#예1) 사용자로부터 정수 2개를 입력받아서 덧셈해주는 프로그램을 만들기.
# num1= input('숫자1 입력: ')
# num2= input('숫자2 입력: ')

# #print(num1, num2) "50" + "30" ==> "5030"
# num3= int(num1) + int(num2)
# print("덧셈 결과 :", num3)
# print()

#예2) 사용자로부터 원하는 구구단의 단수를 입력받아 그 단의 구구단을 출력하는 프로그램 만들기.
# print("원하는 구구단을 출력해주는 프로그램 입니다.")
# print()

# dan= input('단수 입력: ') #"8"
# dan= int(dan) #"8"-->8

# print()
# print("{} x {} = {}".format(dan, 1, dan*1))
# print("{} x {} = {}".format(dan, 2, dan*2))
# print("{} x {} = {}".format(dan, 3, dan*3))
# print("{} x {} = {}".format(dan, 4, dan*4))
# print("{} x {} = {}".format(dan, 5, dan*5))
# print("{} x {} = {}".format(dan, 6, dan*6))
# print("{} x {} = {}".format(dan, 7, dan*7))
# print("{} x {} = {}".format(dan, 8, dan*8))
# print("{} x {} = {}".format(dan, 9, dan*9))
#-----------------------------------------------------

# 파이썬 언어만의 엄청 특이한 ... 여러개의 값을 여러개의 변수에 한줄에 차례대로 대입하기.
a,b = 10, 20
print( a )
print( b )

name, age= 'sam', 20
print(name)
print(age)

#당연히 변수와 값의 개수는 같아야 함.
#n1, n2= 100 #error

#단, 변수는 1개인데 값이 여러개,...대입하면 에러아님
aa= 10,20,30
print(aa) #tuple 이라는 타입의 값.
print(type(aa))
print(aa[0])
print(aa[1])
print(aa[2])






