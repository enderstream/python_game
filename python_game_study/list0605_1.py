import tkinter


if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("가챠!!")
    # root.geometry("1280x720")  # 사이즈 : 안해도 됨
    root.resizable(False, False)  # 창 크기 고정

    canvas = tkinter.Canvas(root, width=1280, height=720, bg="white")
    canvas.pack()
    hyunju = tkinter.PhotoImage(file="hyunju.png")
    canvas.create_image(150, 420, image=hyunju)

    root.mainloop()
