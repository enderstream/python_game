import random, os

player_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def initialize() -> dict:
    print("당신의 운빨을 시험해보세요!")
    while True:
        player_cnt = int(input("플레이어 인원수를 입력해주세요 : ").strip())
        if 2 <= player_cnt <= 26:
            break
        else:
            clear_screen()
            print("최소 2명, 최대26명까지만 플레이할 수 있습니다")
    players = [
        [input(f"플레이어{i}의 닉네임을 입력해주세요 : ").strip(), 1]
        for i in range(1, player_cnt + 1)
    ]
    clear_screen()
    init_data = {
        "map_size": 60,  # 맵 사이즈를 바꾸려면 이거 하나만 바꾸세요
        "player_cnt": player_cnt,
        "players": players,
    }
    return init_data


def board(map_size: int, player_cnt: int, players: list):
    print("=" * (map_size + 1))
    for i in range(player_cnt - 1):
        print(f'{" "*(players[i][1]-1)}{player_char[i]}{" "*(map_size-players[i][1])}|')
        print(f"-" * map_size + "|")
    else:
        print(
            f'{" "*(players[player_cnt-1]-1)}{player_char[player_cnt-1]}{" "*(map_size-players[player_cnt-1])}|'
        )
    print("=" * (map_size + 1))


def game_main_loop(init_data: dict):
    map_size = init_data["map_size"]
    player_cnt = init_data["player_cnt"]
    players = init_data["players"]
    while True:
        board(map_size, player_cnt, players)
        
        # 승자 결정
        for 

        # 턴 진행
        for i in range(player_cnt):
            input(f"{players[i][0]}님의 턴, ENTER키를 눌러 전진하세요!")
            players[i][1] += random.randint(1, 6)
            players[i][1] = min(players[i][1], map_size)

        clear_screen()


if __name__ == "__main__":
    player_win = game_main_loop(init_data=initialize())
    if player_win:
        print(f"이걸 이겨? 좀 치네?")
    else:
        print(f"이걸 지네? ㅋㅋ허접")
