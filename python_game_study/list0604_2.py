import tkinter


if __name__ == "__main__":
    # Tk 객체 생성
    root = tkinter.Tk()
    root.title("첫번째 캔버스")  # 창 이름
    root.geometry("1280x720")  # 사이즈

    # 캔버스 크기 지정
    canvas = tkinter.Canvas(root, width=400, height=600)
    canvas.pack()  # 윈도우에 캔버스를 배치

    # 200, 300은 캔버스의 (200,300) 좌표에 이미지의 "중심"을 집어넣으므로 주의!!
    hyunju = tkinter.PhotoImage(file="hyunju.png")
    # canvas.create_image(0, 0, image=hyunju)
    canvas.create_image(200, 300, image=hyunju)

    root.mainloop()
