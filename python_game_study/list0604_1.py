import tkinter


if __name__ == "__main__":
    # Tk 객체 생성   
    root = tkinter.Tk()
    root.title("첫번째 캔버스")  # 창 이름
    root.geometry("1280x720")  # 사이즈

    # width는 무조건 중앙에서 시작, 좌우로 절반의 길이만큼 차지
    # height는 무조건 최상단에서 시작, 지정된 길이만큼 하강
    # bg는 #키워드로 헥스코드 사용 가능:ex)"#50C878" / 혹은 지정된 키워드로 색깔 지정 가능 :ex)"skyblue"
    canvas = tkinter.Canvas(root, width=100, height=200, bg="grey")
    canvas.pack()

    root.mainloop()
