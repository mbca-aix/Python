#반복문 for -- 소괄호 ()는 쓰면 에러

#반복하는 데이터를 나열하면 그 개수만큼 반복... 여러개의 데이터를 가진 []리스트의 데이터만큼 반복..(리스트 수업은 내일..)
for n in [1,2,3,4,6,8]:
    print(n)
print()

# 반복하면서 숫자를 일일이 직접 쓰기 어려워서.. 반복숫자를 만들어주는 파이썬의 내장된 기능함수가 존재함. range()
for n in range(10): #0~9 [0부터 10전까지..]
    print(n)
print()

#시작숫자을 5부터 하고 싶다면.. [5~9]
for n in range(5, 10):
    print(n)
print()

# 혹시 간격이 2씩 증가하고 싶다면..
for n in range(0, 10, 2):
    print(n)
print()

# 역순으로.. 작아지고 싶다면..
for n in range(10, 0, -1):
    print(n)
print()
#3씩 감소
for n in range(10, -10, -3):
    print(n)
print()

# 임시변수 n 을 이용하면 구구단 출력도 가능
dan=5
for a in range(1,10):
    print("{} x {} = {}".format(dan, a, dan*a))
print()
# 역순 구구단
dan=5
for a in range(9,0,-1):
    print("{} x {} = {}".format(dan, a, dan*a))
print()

# 'Hello' 글씨를 5번 출력해.
for a in range(5): #0~4
    print('Hello')
print()

# range()에 전달하는 값을 변수가 가진 값으로 지정하는 것도 가능
num= 6
for a in range(num):
    print('nice')
print()

#[응용] 글자수만큼 반복하며 'GOOD' 출력해보기
word='MBCA'
word='MBCACADEMY'
for n in range(len(word)):
    print('GOOD')
print()

#[별외.] 사실 '문자열'은 '한글자' 여러개가 붙어서 나열되어 있는 데이터임. 마치 리스트처럼..
for w in word:
    print(w)
print()

# ---------------------------------------------------

# 중첩 반복문..
# -- 특정작업을 5번씩 3회 반복해라..
for a in range(3):
    print('세트 :', a+1)

    for b in range(5):
        print('푸시업:', b+1)
    print()
print()

# 중첩 반복문 - 2~9단까지의 구구단 모두 출력하기
for dan in range(2,10):
    for n in range(1,10):
        print( f"{dan} x {n} = {dan*n}" )
    print()

