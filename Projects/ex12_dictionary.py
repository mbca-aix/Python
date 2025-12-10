#3. Dictionary {} - 리스트처럼 요소의 추가/삭제/변경 모두 가능 [단. 인덱스번호 대신에 원하는 '식별자'로 요소를 구별함]

# {key:value, key:value, .....}
ccc= {'name':"sam", 'age':20, 'address':"seoul"}
print(ccc)
print(type(ccc))

# 요소 개별값 사용 -- '식별자' key 사용
print( ccc['name'] )
print( ccc['age'] )
print( ccc['address'] )

# 요소값 변경
ccc['age']= 25
print(ccc)

# 요소 추가.
ccc['email']= 'aaa@aaa.com'
print(ccc)

# 요소 제거
del ccc['email']
print(ccc)

# 요소모두 삭제
ccc.clear()
print(ccc)

# in 연산자를 활용 - 값을 찾는게 아니라.. 식별자를 찾아서 그 안의 값에 접근해야 함.
ccc= {'name':'robin', 'age':25, 'address':'busan'}
if 'name' in ccc: #'name'이라는 식별자가 존재하는가?
    print('name:', ccc['name'])

value= ccc.get('tel') #없는 key를 사용하면 None 값을 줌
print(value)
print()

#반복문으로 딕셔너리의 요소값을 접근해보기..
#range()는 불가능..
for a in ccc: #요소값이 아니라 식별자 key 가 뽑아짐
    print(a)
print()

#딕셔너리는 다른 리스트,튜플과 다르게 요소값이 for로 뽑아지지 않고.. key가 뽑아짐.
#요소값을 알고 싶다면.......뽑아진 key를 이용하여 값을 취득
for key in ccc:
    print(key, ":", ccc[key])
print()

# 딕셔너리의 (key,value) 튜플쌍을 가지고 있는 Item이라는 녀석으로 for를 사용하기
items= ccc.items()
print(items)

for item in ccc.items():
    print(item)
    key, value= item
    print(key, value)
print()

for key,value in ccc.items():
    print(key, value)
print()


print('------------------------------------')
print()



