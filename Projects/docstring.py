#''' ''' 이 문자열을 doc string [도움말을 만들어주는 문자열]

# 이름을 전달받아서 환영인사를 출력하는 기능을 만들어보기 -함수
def show_name(name):
    #이건 설명서글이 될 수 없음.
    '''이름을 소괄호 안에 넣으면 환영인사를 출력해줘요,'''
    print("{}님 환영합니다".format(name))

show_name('sam')
show_name('robin')
show_name()





