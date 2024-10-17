import tkinter
import tkinter.font

# Tk 객체 생성
root = tkinter.Tk()

# 단순히 tkinter에 쓸 수 있는 폰트들
for f in tkinter.font.families():
    print(f)

root.title("첫번째 윈도우")  # 창 이름
root.geometry("1280x720")  # 사이즈

# 창 안에 넣을 문자열 : 라벨 문자열이 출력됨
label = tkinter.Label(root, text="라벨 문자열", font=("System", 24))
label.place(x=200, y=100)  # 문자열의 위치

root.mainloop()
