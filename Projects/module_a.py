title='Hello python module'

def show():
    print('show module a')


#8장 수업 - 클래스를 모듈에 미리 설계해 놓고.. 필요할 때 import 해서 사용하도록 제공
class Person:
    school_name= 'aaa'
    #객체가 생성될때 자동으로 호출되는 아주 특별한 이름의 함수... 생성자 함수
    def __init__(self, name, age):
        self.name= name
        self.age= age
    
    def display(self):
        print('name :', self.name)
        print('age :', self.age)
        print()

    #생성자 함수와 반대로 메모리에서 이 객체가 더이상 필요 없을때 자동으로 실행되는 특별한 함수 -- 소멸자 함수
    def __del__(self):
        print('객체가 소멸되었되었습니다. : ', self.name)