import tkinter
import tkinter.font

def click_btn():
    button["text"] = "클릭했습니다!"


if __name__ == "__main__":
    # Tk 객체 생성
    root = tkinter.Tk()
    root.title("첫번째 윈도우")  # 창 이름
    root.geometry("1280x720")  # 사이즈

    button = tkinter.Button(root, text="버튼 문자열", font=("D2coding", 24), command=click_btn)
    button.place(x=200, y=100)


    root.mainloop()
    
