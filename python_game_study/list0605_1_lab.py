import tkinter


if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("가챠!!")
    # 왜인지 모르겠는 없어도 되더라
    # root.geometry("1280x720")  # 사이즈
    root.resizable(False, False)  # 창 크기 고정

    #####

    # Safari 보기에서 시작
    # canvas = tkinter.Canvas(root, width=1280, height=960, bg="#50C878")

    # 초록 창은 root 창을 꽉 채움
    # 현주는 Safari 보기에서 시작
    # 캔버스는 1280 * 720
    # 캔버스 객체상에서 현주 이미지의 중심이 위치할 좌표: 400, 300
    # 캔버스상에서 띄워지는 현주 이미지는 전체 창사이즈와는 무관하네
    canvas = tkinter.Canvas(root, width=1280, height=720, bg="#50C878")

    # 초록 창은 Safari 방문기록에서 시작
    # 현주는 Safari 윈도우에서 시작
    # 캔버스, 이미지 둘 다 창의 정중앙에서 좌우로 퍼져나가는듯??
    # 캔버스 객체상에서 현주 이미지의 중심이 위치할 좌표 : 400, 300
    # canvas = tkinter.Canvas(root, width=800, height=600, bg="#50C878")



    #####

    canvas.pack()
    
    # 얘는 잘 되는데....
    # 이거 두개 합쳐서 한줄에 적으려니까 이미지가 안뜬다...
    hyunju = tkinter.PhotoImage(file="hyunju.png")
    canvas.create_image(400, 300, image=hyunju)
    
    # 아래 두개 같이 쓰면 이미지만 짤림
    # canvas = tkinter.Canvas(root, width=1280, height=720, bg="#50C878")
    # canvas.create_image(100, 300, image=hyunju)
    
    

    # 이거 왜 이미지 안나오냐??
    # PhotoImage객체가 바로 리턴되는줄 알았는데 그게 아닌듯?
    # 그런데 왜 변수 선언할 때는 되는거지?
    
    # canvas.create_image(400, 300, image=tkinter.PhotoImage(file="hyunju.png"))
    
    # 이미지를 참조하는 대상자체가 없어서 생성되지마자 가비지컬렉터가 뺏어가버림
    # 이미지도 객체로 남겨놓는게 맞네...

    root.mainloop()
