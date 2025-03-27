# インポート

# グローバル変数の宣言
monster_names = [
        'スライム',
        'ゴブリン',
        'オオコウモリ',
        'ウェアウルフ',
        'ドラゴン',
        ]

# 関数宣言

def main():
    while True:
        player_name=input('プレイヤー名を入力してください>>')
        if len(player_name) > 0:
            break
        print('エラー:プレイヤー名を入力してください')

    print('*** Puzzle & Monsters ***')
    kills = go_dungeon(player_name)
    if kills == len(monster_names):
        print('*** GAME CLEARED!! ***')
    else:
        print('*** GAME OVER!! ***')

    print(f'倒したモンスター数={kills}')


def go_dungeon(player_name):
    kills = 0
    print(f'{player_name}はダンジョンに到着した')
    for monster_name in monster_names:
        kills += do_battle(monster_name)
    print(f'{player_name}はダンジョンに制覇した')
    return kills

def do_battle(monster_name):
    print(f'{monster_name}が現れた!')
    print(f'{monster_name}倒した!')
    return 1

# main関数の呼び出し
main()
