#2. 반복문 : while, for

#1) while
a=0
while(a<3):
    print('aaa')
    print('bbb')
    print('ccc')
    #조건에 사용한 변수(제어변수)의 값을 변경해보기
    #a=a+1
    a+=1
print()

# 특정 조건에 도달할때까지 반복수행해야 할때.. 많이 사용함.
# ex) 게임할때.. level이 있는데 10을 넘어야 사냥을 갈 수 있다고 할때...
# 레벨을 높이기위해 훈련을 해야함.. 한번 훈련할때 마다 1씩 레벨이 업되는 ....

level=0
while(level<10):
    print('훈련!! 레벨업!!', level)
    level= level+1

print('전투 참여')
print('END')
print()

# while문을 이용한 반복의 횟수는 하나의 코드만으로 결정되지 않음.
# 1)제어변수 초기값,  2)제어조건,  3)제어변수연산...을 모두 고려하여 결정하게 됨.

# "Hello"라는 글씨를 화면에 5번 출력하는 프로그램을 만들어 보세요.. 
a=0
while(a<5):
    print('Hello')
    a+=1
print()

a=0
while(a<10):
    print('Hello')
    a+=2
print()

a=5
while(a<10):
    print('Hello')
    a+=1
print()

a=5
while(a>0):
    print('Hello')
    a-=1
print()

# 만약. 판단이 안서면.. 초기값 0.  조건은 <횟수.   연산은 +=1

# 반복문의 실행문 영역에 print()만 사용할 수 있는 것은 아님. 어떤 코드든 가능함.

#예) 사용자로부터 정수를 5번 입력받으면서 짝수/홀수 인지 를 출력해주는 프로그램
# a=0
# while(a<5):
#     num= input('숫자 입력 : ') #키보드의 입력은 무조건 문자열 데이터로 인식함. 50을 입력하면 '50'
#     num= int(num) #'50'-->50

#     if num%2==0:
#         print('짝수')
#     else:
#         print('홀수')
    
#     a+=1
# print()

#예2) 사용자로부터 정수를 5번 입력받으면서 그 값들을 모두 더한 누적값을 출력하기.
# total=0
# a=0
# while(a<5):
#     num= int(input('숫자 입력 : '))
#     total= total+num #누적 연산
#     a+=1

# print('입력된 정수의 총합은:', total)
# print()

#누적합의 구하는 방법을 문자열에 적용하면.. 문자열을 결합하여 새로운 긴 문자열을 만드는 방법으로 활용할 수 있음.
ss=""
ss= ss+"aaa"  #"aaa"
ss= ss+",bbb"  #"aaa,bbb"
ss= ss+",ccc"  #"aaa,bbb,ccc" 
print(ss)
print()
# Q5 조건문에.. 이를 이용해야 하는 문제들을 존재함.

# 반복에 사용했던 제어변수를 출력할 수도 있음.
n=0
while(n<5):
    print(n)
    n+=1
print()

#이 제어변수를 단지 출력하는 것이 아니라. 다른 변수와의 연산에 사용도 가능함.
dan=4
n=1
while(n<10):
    print(dan, 'x', n, '=', dan*n)
    n+=1
print()

#조건식에 사용하는 값을 변수가 가진 값으로 지정하는 것도 가능.
num=6
# num= input()
a=0
while(a<num):
    print('nice')
    a+=1
print()

# ()는 생략가능
a=0
while a<10:
    print('good')
    a+=3

print(a)




