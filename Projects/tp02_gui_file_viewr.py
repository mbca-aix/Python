# tkinter file choice & viewer ... [엑셀파일을 읽어서. 내용을 보여주는 GUI. 컬룸명으로 버튼들 보여주고. 클릭하면. 그 데이터 보여주고. 평균.]


#0. 필요한 라이브러리 추가
# gui library ..
from tkinter import *

#7. 파일선택 작업...할때 추가
# from tkinter import * 로 임포트하면 tkinter의 기본 위젯과 클래스만 현재 네임스페이스로 가져오고,
# filedialog, messagebox 같은 서브모듈(submodule) 은 자동으로 임포트되지 않음
from tkinter import filedialog, messagebox, ttk   # ttk [Themed Tkinter]

#7.2
# 파일 경로를 제어하기 위한 os 내장 라이브러리 
import os
# exel file 을 쉽게 읽어오기 위해
import pandas as pd

# 판다스로 읽은 데이터프레임을 저장할 전역변수 df
df=None

#10. 그래프 라이브러리 추가.
import matplotlib.pyplot as plt
# windows
plt.rcParams['font.family'] ='Malgun Gothic'
# mac os
#plt.rcParams['font.family'] = 'AppleGothic'
# 마이너스 기호 깨짐 방지
plt.rcParams['axes.unicode_minus'] =False

#11. 그래프 그리기. [Tkinter 위젯으로 그래프 그리기.]
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

figure_canvas=None
#---------------------------------------------------------------

#1. 최상위 컨테이너 위젯 생성
window= Tk()
window.title('엑셀 파일 뷰어')
window.geometry('800x600')

#2. 파일 선택 영역 Frame(창안에 있는 작은 영역 위젯)
#frame_top= Frame(window, bg='yellow') # 배경은 패딩을 제외한 영역만 그려짐.
frame_top= Frame(window) # 배경은 패딩을 제외한 영역만 그려짐.
frame_top.pack(padx=10, pady=5, fill='x') # x축 패딩, 가로 채우기... [패딩이 마진과 비슷함]
# 안에 자식뷰들이 없기에 높이가... 아주 얇게 보임.

#3. 파일의 경로를 직접 입력하거나. 선택된 파일의 경로가 보이기 위한 한줄 텍스트입력 위젯을 Frame에 붙이기.
entry= Entry(frame_top, width=60) # 대문자 60글자 정도 들어갈 사이즈
entry.pack(side='left', padx=5)

#6. 아래 버튼 클릭할때 실행될 함수들. [우선 UI 작업할때 까지는 pass 로... [파일 선택 및 파일읽기 코드 먼저 작업.]]
def clicked_file_chooser():
    #pass
    #7. 파일선택기 보이도록 tkinter 의 서브모듈인 filedialog 를 import [ from tkinter import filedialog ]
    file_path = filedialog.askopenfilename(title="엑셀 파일 선택", filetypes=[("Excel files", "*.xlsx *.xls") ] ) #엑셀파일만 선택가능하도록.
    if file_path: # file_path 가 비어있지 않다면...[파이썬은 None, 0, '', []를 제외하고 모두 참.]
        #기존에 선택된 파일경로가 있을 수 있으니 일단 지우기
        entry.delete(0, END) # 0번위치부터 글씨 끝위치까지.
        #사용자가 선택한 파일경로를 표시
        entry.insert(0, file_path)    

#6.1
def clicked_file_read():
    global df # 전역변수 df를 사용하겠다교 표시

    #7.2 선택한 파일의 내용을 판다스로 읽기.
    file_path= entry.get() # entry 위젯에 써있는 경로 읽어오기
    #해당경로의 폴더나 파일이 실제로 존재하지 없다면 읽을 수 없기에 os 모듈을 통해 존재를 학인 (file_path가 비어있는 것도 체크 가능)
    if not os.path.exists(file_path):
        messagebox.showerror('파일읽기 오류', '파일을 찾을 수가 없습니다.')
        #파일이 없으면 더 이상 읽을 필요가 없기에 여기서 작업그만.
        return
    
    #위레서 return 되지 않았으니.. pandas 모듈을 이용하여 선택된 엑셀파일을 DataFrame 으로 읽기
    df= pd.read_excel(file_path)
    #일단 데이터프레임이 잘 읽어졌는지 확인...용으로 console에 출력
    print(df)

    #8. 읽은 데이터를 사용자가 볼 수 있도록. Treeview 위젯 [ ttk.Treeview : 표 형태의 데이터를 표시할 수 있는 table-like 위젯 ]
    # 여기에 바로 쓰면.. 코드가 지저분해서 별도의 함수로 분리하는 것을 권장하지만 현재 클래스를 만든 구조가 아니어서 함수를 더 위해 작성해야함. 이것도 별로..
    # 일단, 여기에 만들고 나중에 class 로 앱 전체를 구성한 후 메소드로 분리작성 [ display_dataframe() 권장 ]
    # Treeview 생성은 UI 작업이므로 아래.. 5번 버튼 위쳇 만든 이후 추가..하고 ... 여기서는 만들어지 Treeview 의 데이터를 갱신하는 작업...
    show_data() # 아래 만든 함수 [엑셀데이터 보기]버튼 클릭할때 실행됨


#4. 파일선택 버튼 [ Entry 옆에 배치 ]
btn_file_chooser= Button(frame_top, text='파일선택', command=clicked_file_chooser)
btn_file_chooser.pack(side='left', padx=5) # Entry 가 왼쪽에 있기에.. 이어서 옆에 배치됨.

#5. 선택된 파일 읽기 버튼 [ 파일선택 버튼 옆에 배치 ]
btn_file_read= Button(frame_top, text='파일읽기', command=clicked_file_read)
btn_file_read.pack(side='left', padx=5)

# ---------------------------------------------------------------------------------
#9. [엑셀데이터 보기], [그래프 보기] 버튼] 클릭에 반응하는 함수
def show_data(): 
    # df 전역변수를 사용하겠다고 선언.
    global df
    #pass
    # 기존 내용 초기화
    if df is None:
        return
    
    global figure_canvas
    if figure_canvas is not None:
        figure_canvas.get_tk_widget().destroy()
        figure_canvas=None
    
    
    print(treeview.get_children())
    treeview.delete(*treeview.get_children()) #* (언패킹 연산자) 리스트나 튜플 안의 요소를 개별 인자로 풀어줌.  delete()는 지울 항목들을 , , , 여러개 전달하는 것임. [ 그렇기에 리스트나 튜플, dict 같은 형태의 데이터를 * 언패킹연산자로 풀어야 함.]
    
    treeview['columns']= list(df.columns)
    treeview['show']= 'headings' # 이걸 지정하지 않으면 컬룸명이 표시되지 않음.

    #표의 제목줄[컬룸]들 설정
    for col in df.columns:        
        treeview.heading(col, text=col) # 첫번째 파라미터 col 에게 보여질 글씨 지정. "최저온도","최고온도",...
        treeview.column(col, width=120) # 첫번째 파라미터 col 의 너비를 120픽셀 지정
    
    #데이터 삽입
    for idx, row in df.iterrows(): # 데이터프레임의 각 줄을 이터레이터로 반복 접근.. [인덱스, 한줄(row) 데이터[ Series 타입]]
        #print(row)
        treeview.insert("","end", values=list(row)) # Series → 리스트로 변환
        #"" : 최상위 레벨(parent)
        #"end" : 마지막 위치에 삽입
        #values=list(row) : 컬럼별 데이터 값 지정

def show_graph():
    #pass
    #10. 일단 그래프를 matplotlib 로 그리기. 별도의 창으로 보여짐.
    global df
    if df is None:
        return
    
    treeview.delete(*treeview.get_children()) #* (언패킹 연산자) 리스트나 튜플 안의 요소를 개별 인자로 풀어줌.  delete()는 지울 항목들을 , , , 여러개 전달하는 것임. [ 그렇기에 리스트나 튜플, dict 같은 형태의 데이터를 * 언패킹연산자로 풀어야 함.]

    
    # 그래프의 x축을 첫번째 컬룸으로 지정.
    # 1. x축 = 첫 번째 컬럼
    xs = df.iloc[:, 0] 
    xs_label = df.columns[0]

    # 그래프는 숫자데이터만 그릴 수 있기에... 숫자 컬럼만 추출
    numeric_df = df.select_dtypes(include=['int64', 'float64'])

    # 혹시 숫자 컬룸이 없다면.. 메세지 보여주고 종료.
    if numeric_df.empty:
        messagebox.showwarning("경고", "그래프를 그릴 수 있는 숫자 컬럼이 없습니다.")
        return
    
    #10.
    figure=plt.figure(figsize=(10, 6))

    for col in numeric_df.columns:
        # 첫 번째 컬럼이 숫자여서 y에 포함될 수 있으므로 제외
        if col == xs_label:
            continue

        # x, y 값들로 그래프 값 설정. [ plot..직선 그래프 ]
        plt.plot(xs, numeric_df[col], label=col, marker='o')

    plt.xlabel(xs_label)
    plt.ylabel("Values")
    plt.title("엑셀 데이터 그래프")
    plt.legend() #범례표시 
    plt.grid(True) # 격자 라인 보여주기.    
    #plt.show()

    global figure_canvas
    if figure_canvas is None:
        figure_canvas= FigureCanvasTkAgg(figure=figure, master=treeview)
        figure_canvas.get_tk_widget().pack()

    #여기까지해서 마무리.. -----------


#8. [엑셀데이터 보기], [그래프 보기] 버튼으로 데이터를 보여줄 것임.

# 위 파일선택영역과의 식별을 위해 구분서 위젯 사용. ttk.Separator 위젯. ttk 서브모듈을 명시적으로 import 해야 함.
separator= ttk.Separator(window, orient='horizontal') # horizontal : 수평선
separator.pack(pady=10, fill='x')

# 버튼 2개를 배치하기 위한 Frame 부터 배치
frame_buttons= Frame(window)
frame_buttons.pack(padx=10, anchor='center')

# 버튼 2개 붙이기.
btn_show_data= Button(frame_buttons, text='엑셀데이터 보기', command=show_data)
btn_show_data.pack(side='left', padx=10)

btn_show_graph= Button(frame_buttons, text='그래프 보기', command=show_graph)
btn_show_graph.pack(side='left', padx=10)


#8.1 ttk.TreeView 위젯을 사용하려면. ttk 서브모듈을 명시적으로 import 해야 함.
# 표와 그래프를 교차로 보여줄 것이기에. 프레임을 배치하고 버튼으로 바꿔가며 보여줄 것임. 
treeview= ttk.Treeview(window)
treeview.pack(expand=True, fill='both', padx=10, pady=10) # expand=True: 여유 공간이 있을 경우, 해당 위젯이 그 공간 안에서 확대될 수 있게 함, fill="both": 가로 + 세로 모두 늘어남
# expand=True 와 fill='both'를 조합하면 화면을 꽉 채우는 효과



#1.~ 이벤트 처리 및 
window.mainloop()

# 과제
#1. 그래프를 별도의 창이 아니라.. Treeview 위치에 토클링 하며 보여주기.
#2. 클래스로 만들어. 클릭함수들을 메소드로 만들어.. 코드의 가독성을 향상. [ ex20_zzz.py 참고.]

# gui event 처리를 위한 함수들의 작성 순서에 영향을 받지 않으려면 클래스와 메소드
# class ExcelViewerApp:
#     def __init__(self):
#         pass