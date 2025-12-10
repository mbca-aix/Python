100
#이렇게 값만 쓰면 화면에 데이터가 출력되지 않아요..

# 화면출력... 데이터 유형에 따라.. 출력해보기.
print(10)
print(3.14)
print("Hello")
print('Nice')
print("hello world")
print(    100)
print(      "good")
print("      good")
print(True)
print(3>5)

print()
print('nice to meet you.')
print()

#print 기능은 한번에 여러개의 데이터를 출력할 수 있음.
print(10)
print(20)
print(1020)
#print(10 20)
print(10,20)
print(10, 20)
print(10,   3.14,   '        Hello',       False)
print('나는','이제','그만 쉬고 싶어요.')
print()

# 파이썬은 산술연산 가능.
print(3+5)
print('3+5')

print('asaa 한글 1234 ~!@#$%^&**"')

# 문자열안에 큰따옴표를 출력하고 싶다면.. 문자열을 작은 따옴표로 감싸기.
print('나는 "홍길동" 입니다.')
# 문자열안에 작은따옴표를 출력하고 싶다면.. 큰따옴표로 감싸기
print("나는 '홍길동' 입니다.")

# 만약 문자열안에 작은따옴표와 큰 따옴표를 모두 사용하고 싶다면... 특수문자를 사용해야 함.
# 원래 규칙을 벗어나는 문자.. 라고 해서. 이스케이프 문자 라고 부름. [ 역슬래시 \ ]
print('나는 \'의적\'으로 활동하는 \"홍길동\" 입니다.')

# 역슬래시를 출력하고 싶으면..
print("\\\\")
print('It\'s good')
print("It's good")
print()

# 출력데이터가 여러줄로 이루어져 있다면..
print("안녕하세요. " \
"반가워요.")

# 이스케이프 문자의 또 다른 사용모습.
# \n : new line
print("안녕하세요.     \n   반가\n워요.")
print("Hello\nNi ce\nGo  od\naaaq")
print('\n'*4)
print('Hell'*4)
print('Hell'+' Nice')
print('Hello','Nice')

#\t [tab 간격을 가지는 문자]
print('Hello\tNic\te')
print('-'*30)
print()

#여러개의 데이터를 출력상황 [ EX. 학생들의 국영수 성적 표시 ]
print('이름','국어','영어','수학')
print('홍길동', 85, 90, 75)
print('sam', 100, 4, 45)
print()

print('이름','\t','국어','\t','영어','\t','수학')
print('홍길동','\t', 85, '\t', 90, '\t', 75)
print('김철수','\t', 100, '\t', 4, '\t', 72)
print()

# \t 는 고정적인 사이즈는 아님. 다음 탭간격으로 커서를 이동해서..[통상적인 1탭의 간격은 8칸]
print("a\tb") # a가 표시되는 1탭의 간격이 8칸.. 그 후 b표시 [그러니 이상황에서의 \t는 7칸 간격]
print("aa\tb") # aa가 표시되는 1탭의 간격이 8칸.. 그 후 b표시 [그러니 이상황에서의 \t는 6칸 간격]
print("aaa\tb") # aa가 표시되는 1탭의 간격이 8칸.. 그 후 b표시 [그러니 이상황에서의 \t는 5칸 간격]
print("aaaa\tb") # aa가 표시되는 1탭의 간격이 8칸.. 그 후 b표시 [그러니 이상황에서의 \t는 4칸 간격]
print("aaaaaaa\tb") # aa가 표시되는 1탭의 간격이 8칸.. 그 후 b표시 [그러니 이상황에서의 \t는 1칸 간격]
print("aaaaaaaa\tb") # aa가 표시되는 1탭의 간격이 8칸.. 그 후 b표시 [그러니 이상황에서의 \t는 8칸 간격]
print()

# 여러개의 데이터 출력기법을 사용함.. 이를 이용하면 특정 서식 모양을 출력형태를 만들 수는 있음.
print(3+5)
print(3,5,3+5)
print("3 + 5 = 8")
print("3 + 5 = 7")
print(3, '+', 5, '=', 3+5)
print(32, 'x', 56, '=', 32*56)
print()

# 이런식으면.. 3단 구구단을 출력해주는 프로그램을 만들어 달라고 요청받았다..
print(3, 'x', 1, '=', 3*1)
print(3, 'x', 2, '=', 3*2)
print(3, 'x', 3, '=', 3*3)
print(3, 'x', 4, '=', 3*4)
print(3, 'x', 5, '=', 3*5)
print(3, 'x', 6, '=', 3*6)
print(3, 'x', 7, '=', 3*7)
print(3, 'x', 8, '=', 3*8)
print(3, 'x', 9, '=', 3*9)

# 가능은 한데.. , 쓰고.. 문자열 따옴표 쓰고.. 아... 이거 짜증..

# 이 특정 서식(형식format)으로 만들기 편한 기능이 있으면... 그래서 등장한 문자열의 특별한 서식만들기 기능 .format()

print("나는 {} 입니다.".format('홍길동'))
print("당신의 성적은 {}점입니다.".format(80+3))
print("당신의 성적은",80,"점입니다.")
print("나의 이름은 {}이고 나이는 {}살입니다.".format('sam', 20))
print("{} x {} = {}".format(4, 1, 4*1))
print("{} x {} = {}".format(4, 2, 4*2))

#주의.. {}의 개수와 format()에 전달하는 값들의 개수는 같아야 함.!!!
#print("{} - {}".format(179)) #error
print("{} - {}".format(179, 72, 20)) # {}보다 값의 개수가 많으면 에러 아님.. 마지막값만 소실..

# PYTHON 3버전 이상부터.. 등장한 f-string 포멧기술을 사용함.
print(f"{100+3}점 입니다.")
print("100+3점 입니다.")
print(f"{8}x{1}={8*1}")
print(f"나의 이름은 {"홍길동"}입니다.")
print(f"나의 이름은 {'손흥민'}입니다.")
print("나의 이름은 {'손흥민'}입니다.")
print("나의 이름은 {\"손흥민\"}입니다.")
print()

print(10, end=' ')
print(20, end='@')
print(30, end='')
print(40, end=' - ')
print(50, end='alskdjflaksjdf')
print(60, end='\n') # 기본값. default
print(70)
print()

# 문자열 데이터를 만들때 진짜 코드로 보이는 모습 그대로 출력해줬으면...할때. 사용하는 [따옴표3개 문자열]
print('''이렇게.. 따옴표 3개
를 사용하면
보이는 그대로..
표시되는 문자열''')
print()

print('''
이렇게.. 따옴표 3개
를 사용하면
보이는 그대로..
표시되는 문자열
''')

print("--------------------")
print(''' \
이렇게.. 따옴표 3개 \
를 사용하면
보이는 그대로.. 
표시되는 문자열 \
''')

print()
print('-'*40)
print()


# 변수의 필요성 소개
# 8단 구구단을 출력해주는 프로그램을 만들어 줘. 라고 요청받았음.

a= input("단수를 입력하세요.")
dan= int(a)

print( dan, "x", 1, "=", dan*1)
print( dan, "x", 2, "=", dan*2)
print( dan, "x", 3, "=", dan*3)
print( dan, "x", 4, "=", dan*4)
print( dan, "x", 5, "=", dan*5)
print( dan, "x", 6, "=", dan*6)
print( dan, "x", 7, "=", dan*7)
print( dan, "x", 8, "=", dan*8)
print( "dan", "x", 9, "=", dan*9)

# 위 처럼 값을 특정한 문자에 대입해 놓고 사용하면 그 문자를 변수 라고 부름.
# 문자열 데이터와는 다름. 문자열은 따옴표가 있음.

print()
print()
print()
print()
print()
