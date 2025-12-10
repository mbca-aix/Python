#Tuple () -- 리스트와 비슷한데.. 요소의 값변경/요수추가/요소삭제 불가능

bbb= (10,20,30)
print(bbb)
print(type(bbb))

#요소값 사용하는 방법은 같음- 인덱스 번호
print(bbb[0])
print(bbb[1])
print(bbb[2])

# 값변경.. 요소추가..삭제 모두 불가능.
#bbb[0]= 100 #error
#bbb.append(50) #error
#bbb.remove()

for value in bbb:
    print(value+1)
print()

# 특이하게 튜플 생성 방법. 권장은 아닌데.. 은근..보여...
bbb= 10,20,30 # 파이썬이 알아서 튜플로 만들어 버림
print(bbb)
print(type(bbb))

# 반대로 튜플의 요소값들을 여러개의 변수로 분리해서 대입하는 것이 가능(ML 작업할때 애용)
bbb=(10,20,30)
print(bbb[0])
print(bbb[1])
print(bbb[1])

a,b,c= bbb # 요소들이 분해되서.. 각 변수에 대입됨
print(a)
print(b)
print(c)
print()

z,x,c,d= (10,20,30) #error.. 개수가 다르면 에러..
print(z)
print(x)

# 튜플은 원본데이터를 실수로라도 건드리지 못하도록 할때 유용하게 사용됨.





