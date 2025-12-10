# 나만의 모듈 만들어 적용해보기.

# 모듈 : 특정 기능을 수행하는 함수들과 값을 가진 변수,상수를 모아놓은 집합체(별도파일,폴더)

#1] 별도의 .py에 변수1개와 함수1개를 만들어 사용해보기
#print(title)

import module_a
print(module_a.title)
module_a.show()

#2] 모듈용 파일만 모아 놓은 폴더를 만들어 사용해보기
import mymodule.module_b
print(mymodule.module_b.title)
mymodule.module_b.show()

# 하위모듈의 사용을 편하기 하기 위해..
from mymodule import module_b
print(module_b.title)
module_b.show()
print()
#--------------------------------------------------------


#3] 모듈파일을 만들때 주의 점.. 모듈을 파일을 import만 해도.. 그 파일안의 모든 코드가 실행되는 것임.
import mymodule.module_c # 이 순간 모듈c의 파이썬 코드는 실행됨.

mymodule.module_c.display()

