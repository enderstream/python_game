import random, os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def initialize() -> dict:
    player_name = input("플레이어 닉네임을 입력해주세요 : ")
    clear_screen()
    init_data = {
        "map_size": 60,
        "player_name": player_name,
        "player_init_pos": 1,
        "computer_init_pos": 1,
    }
    return init_data


def board(map_size, player_pos, computer_pos):
    print("=" * (map_size + 1))
    print(f'{" "*(player_pos-1)}P{" "*(map_size-player_pos)}|')
    print(f"-" * map_size + "|")
    print(f'{" "*(computer_pos-1)}C{" "*(map_size-computer_pos)}|')
    print("=" * (map_size + 1))


def game_main_loop(init_data: dict):
    map_size = init_data["map_size"]
    player_name = init_data["player_name"]
    player_pos = init_data["player_init_pos"]
    computer_pos = init_data["computer_init_pos"]
    player_turn = 1
    while True:
        board(map_size, player_pos, computer_pos)
        if player_pos == map_size:
            return True
        elif computer_pos == map_size:
            return False

        if player_turn:
            input(f"{player_name}의 턴, ENTER키를 눌러 전진하세요!")
            player_pos += random.randint(1, 6)
            if player_pos >= map_size:
                player_pos = map_size
        else:
            input(f"컴퓨터의 턴, ENTER키를 눌러 전진하세요!")
            computer_pos += random.randint(1, 6)
            if computer_pos >= map_size:
                computer_pos = map_size
        player_turn = 1 - player_turn

        clear_screen()


if __name__ == "__main__":
    player_win = game_main_loop(init_data=initialize())
    if player_win:
        print(f"이걸 이겨? 좀 치네?")
    else:
        print(f"이걸 지네? ㅋㅋ허접")
