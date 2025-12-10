# 1. Error     (오류) : 문법적으로 문제가 있어서 처음부터 실행조차 불가능한 문제
# 2. Exception (예외) : 실행 중(Run Time) 문제 발생

print('예외처리에 대해 알아봅니다.')
print()

#1) 에러인 경우..
#10= a
# 해결방법은.. 문법에 맞게 코드를 수정..

#2) 예외인 상황
#print( 10/0  )   #산수연산에서 0 나눗셈을 불가능한 연산.

# 예외가 발생하면. 프로그램이 다운됨.. 예외발생 줄 아래있는 정상적인 코드들 조차도 실행되지 못함..
# 이게 싫어...
# [예외처리] 라는 것은...예외가 발생하더라도.. 앱이 다운되지 않게(아래 코드들이 정상적으로 실행되도록) 하는 문법

# 흔하게 볼 수 있는 예외 상황들 4가지 정도 알아보고 '예외처리'를 해보기
#1. 0 나눗셈
n= 2
n= 0
#예외가 발생할 가능성이 있는 코드에 대해 예외처리 문법을 사용 try - except 문법
try:
    print( 10/n )
except: # 예외가 발생하면 실행되는 영역
    print("0나눗셈은 불가능 해요.")


#2. 리스트의 인덱스번호를 잘못 사용하는 경우
aaa= [10,20,30]
#print( aaa[3] ) #방번호 문제 발생.
try:
    print( aaa[3] )
except:
    print('잘못된 인덱스 번호를 사용했어요.')

#3. 다른 자료형의 연산 [ 숫자 + 문자 ]
try:
    print( 10 + '5' )  
except:
    print('문자와 숫자는 연산이 불가능합니다.')

#4. 바꿀 수 없는 자료형으로 형변환 시도.
try:
    print( 10 + int('3.14') )
except:
    print('정수모양의 문자열만 int로 변환할 수 있어요~~')


# 결국. 예외처리라는 것은.. 예외가 발생되지 않도록 하는 것이 아니라.. 예외가 발생해도..다운되지 않도록 하는 기술!
# ------------------------------------

#3) 코드의 가독성을 위해 등장한 else 영역 추가...
# 예외가 발생하지 않았을때 수행할 작업을 try 영역안에 모아서 쓰는 것이 가독성이 떨어진다고...봐서..등장한 문법

#예) 정수를 입력받아 제곱하여 출력 작업

# try 구문으로만 처리
# try:
#     #예외발생 가능성 있는 코드
#     number= int(input('정수 입력: ')) 
#     #성공했을때 수행할 코드..
#     print( number**2 )
# except:
#     print('정수만 입력하세요')

# # try 영역안에 모든 성공코드를 작성하지않고..
# # 예외발생 가능성 코드만 try 영역에.. 예외가 아닐때(성공했을때) 수행할 코드를 다른 영역에 작성하여 가독성 향샹 - else
# try:
#     #예외발생 가능성 있는 코드
#     number= int(input('정수 입력: ')) 
# except:
#     print('정수만 입력하세요')
# else:
#     #성공했을때 수행할 코드..
#     print( number**2 )
#-------------------------------------------------
print()

#4) 예외발생 여부와 상관없이 무조건 수행할 작업이 있다면...사용하는 finally
#예) 파일 읽기 작업 중.. 예외발생... 이로 인해.. close()의 미스...문제..
try:
    file= open('aaa.txt', 'r', encoding='UTF-8')
    print( file.read() )
    #print(file.reah()) #함수명을 잘못 작성.
    #file.close()
except:
    print('파일 읽기 작업중에 오류가 발생했어요.')
finally:
    print('이 영역은 예외가 발생하든. 안하든.. 무조건 실행되는 영역임')
    file.close()

#파일 스트림이 닫혀 있는지 확인 가능.
print('파일스트림이 닫혀있나요? : ', file.closed)
#---------------------------------------------------------------------
print()

#5) 예외가 발생했을때 그 이유를 알고싶다면..
try:
    print(10/0)
except Exception as e: #Exception 예외객체 사용 및 e 라는 이름의 변수로 참조하여 제어
    print('에러')
    print('에러종류:', type(e))
    print('에러이유:', e)


try:
    aaa= [10,20,30]
    print(aaa[3])
except Exception as e: #Exception 예외객체 사용 및 e 라는 이름의 변수로 참조하여 제어
    print('에러')
    print('에러종류:', type(e))
    print('에러이유:', e)

print()
#이런식으로 에러의 종류를 알수 있다면.. 에러별로 대응하는 코드가 가능함.

#6) try영역안에 2개 이상의 예외가 발생할 가능성이 있는 경우도 존재함.
try:
    print(10/0)
    num1= int( input('입력: ') )
    num2= int( input('입력: ') )

    div= num1/num2
    print('나눗셈 결과 :', div)
except ValueError as e:
    print('숫자만 입력하세요 : ', e)
except ZeroDivisionError as e:
    print('0나눗셈은 불가능 합니다 : ', e)
except Exception as e:
    print('알수 없는 예외가 발생했어요.', e)

print()
#---------------------------------------------------

#[추가] 예외상황이 아닌데.. 개발자가 강제로 예외야!!! 라고 문제를 발생시는 문법 raise

#예) 원래 파이썬은 계산의 결과가 음수라고 해서 예외는 아님..
# num= int( input('enter number: ') )
# if num<0:
#     raise Exception 
# else:
#     print(num)
# print()

# 예외처리로 위 [음수값에 대한 예외]를 처리해보기
try:
    num= int( input('enter number: ') )
    if num<0:
        raise Exception 
    else:
        print(num)
    
except:
    print('양수만 입력해!!!')

print()




# exception(예외)가 발생하면 그 줄 다음부터의 코드는 실행되지 않음.. 이를 확인해보기
print()
print('-'*30)
print('프로그램 종료')
print()

