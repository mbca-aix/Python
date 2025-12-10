from tkinter import *
# 위 * 로 추가하면 클래스나 함수는 추가되지만 하위 모듈을 추가되지 않기에 다시 추가해줘야 함.
from tkinter import messagebox


#[6]버튼 클릭이벤트 처리 ----------------------------------------------------------------
def clicked_complete():
    name= entry_name.get()
    kor= entry_kor.get()
    eng= entry_eng.get()
    math= entry_math.get()
    total = int(kor) + int(eng) + int(math)
    aver= total/3
    listbox_result.insert(END, f'{name},{kor},{eng},{math},{total},{aver}') 

    # entry_name.delete(0,END)
    # entry_kor.delete(0,END)
    # entry_eng.delete(0,END)
    # entry_math.delete(0,END)
    clicked_reset()

def clicked_reset():
    entry_name.delete(0,END)
    entry_kor.delete(0,END)
    entry_eng.delete(0,END)
    entry_math.delete(0,END)

def clicked_delete():
    indices= listbox_result.curselection()
    #print(indices)
    # for idx in indices:
    #     listbox_result.delete(idx)
    
    listbox_result.delete(indices[0])

    
import csv
def clicked_save():
    all_items= listbox_result.get(0,END)
    print(all_items)

    with open('files/grades.csv','w',encoding='UTF-8', newline='') as file:
        writer= csv.writer(file)
        
        for row in all_items:
            writer.writerow(row.split(','))
#---------------------------------------------------------------------------------------


#[1] 화면 구현
window= Tk()
window.title('성적처리 프로그램')
window.resizable(False, True)
window.geometry('450x500+100+50')
# window.mainloop()

#[2] 이름, 국어, 영어, 수학 성적 입력 위젯
frame1= Frame(window, padx=10, pady=10)
frame1.pack(fill='x')
label_name= Label(frame1, text='이름', font=('', 14))
label_name.grid(row=0, column=0, padx=10, pady=10)
entry_name= Entry(frame1, font=('',14), width=15)
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_kor= Label(frame1, text='국어', font=('', 14))
label_kor.grid(row=1, column=0, padx=10, pady=10)
entry_kor= Entry(frame1, font=('',14), width=15)
entry_kor.grid(row=1, column=1, padx=10, pady=10)

label_eng= Label(frame1, text='영어', font=('', 14))
label_eng.grid(row=2, column=0, padx=10, pady=10)
entry_eng= Entry(frame1, font=('',14), width=15)
entry_eng.grid(row=2, column=1, padx=10, pady=10)

label_math= Label(frame1, text='수학', font=('', 14))
label_math.grid(row=3, column=0, padx=10, pady=10)
entry_math= Entry(frame1, font=('',14), width=15)
entry_math.grid(row=3, column=1, padx=10, pady=10)


#[3] 입력 완료 버튼 / 입력 취소 버튼 추가
frame2= Frame(window, padx=10, pady=10)
frame2.pack(fill='x')
btn_complete= Button(frame2, text='입력완료', font=('', 14), command=clicked_complete)
btn_complete.pack(side='left', padx=10, pady=10)
btn_reset= Button(frame2, text='입력취소', font=('', 14), command=clicked_reset)
btn_reset.pack(side='left', padx=10, pady=10)

#[4] 입력완료 성적 리스트 위젯 추가
frame3= Frame(window, padx=10, pady=10)
frame3.pack(fill='x')
listbox_result= Listbox(frame3, font=('',14), height=5, selectmode='multiple')
listbox_result.pack(fill='x')

#[5] 리스트 내용 csv 파일로 저장하는 버튼
btn_delete= Button(frame3, text='항목 삭제', font=('', 14), command=clicked_delete)
btn_delete.pack(side='left', padx=10, pady=10)
btn_svae= Button(frame3, text='csv 파일 저장', font=('', 14), command=clicked_save)
btn_svae.pack(side='right', padx=10, pady=10)



window.mainloop()