# インポート
import random

# グローバル変数の宣言
ELEMENT_SYMBOLS={
        '火':'$',
        '水':'~',
        '風':'@',
        '土':'#',
        '命':'&',
        '無':' ',
}
ELEMENT_COLORS={
        '火':1,
        '水':6,
        '風':2,
        '土':3,
        '命':5,
        '無':7,
}
gems=[]

IDXS ='ABCDEFGHIJKLMN'

# 関数宣言

def main():
    friends=[
            {
                'name':'朱雀',
                'hp':150,
                'max_hp':150,
                'element':'火',
                'ap':25,
                'dp':10
            },
            {
                'name':'青龍',
                'hp':150,
                'max_hp':150,
                'element':'風',
                'ap':15,
                'dp':10
            },
            {
                'name':'白虎',
                'hp':150,
                'max_hp':150,
                'element':'土',
                'ap':20,
                'dp':5
            },
            {
                'name':'玄武',
                'hp':150,
                'max_hp':150,
                'element':'水',
                'ap':20,
                'dp':15
            },

    ]
    monster_list=[
            {
                'name':'スライム',
                'hp':100,
                'max_hp':100,
                'element':'水',
                'ap':10,
                'dp':1
            },
            {
                'name':'ゴブリン',
                'hp':200,
                'max_hp':200,
                'element':'土',
                'ap':20,
                'dp':5
            },
            {
                'name':'オオコウモリ',
                'hp':300,
                'max_hp':300,
                'element':'風',
                'ap':30,
                'dp':10
            },
            {
                'name':'ウェアウルフ',
                'hp':400,
                'max_hp':400,
                'element':'風',
                'ap':40,
                'dp':15
            },
            {
                'name':'ドラゴン',
                'hp':600,
                'max_hp':600,
                'element':'火',
                'ap':50,
                'dp':20
            },
    ]
    while True:
        player_name=input('プレイヤー名を入力してください>>')
        if len(player_name) > 0:
            break
        print('エラー:プレイヤー名を入力してください')

    print('*** Puzzle & Monsters ***')
    party=organize_party(player_name,friends)
    kills = go_dungeon(party,monster_list)
    if kills == len(monster_list):
        print('*** GAME CLEARED!! ***')
    else:
        print('*** GAME OVER!! ***')

    print(f'倒したモンスター数={kills}')


def go_dungeon(party,monster_list):
    kills = 0
    print(f'{party['name']}のパーティ(HP={party['hp']})はダンジョンに到着した')
    show_party(party)
    for monster in monster_list:
        kills += do_battle(party,monster)
        if party['hp'] <= 0:
            print(f'{party['name']}はダンジョンから逃げ出した')
            break
        print(f'{party['name']}はさらに奥に進んだ')
        print('==================================')
    else:
        print(f'{party['name']}はダンジョンに制覇した')

    return kills

def do_battle(party,monster):
    print_monster_name(monster)
    print('が現れた!')

    fill_gems()
    
    while True:
        on_player_turn(party,monster)
        if monster['hp'] <= 0:
            break
        on_enemy_turn(party,monster)
        if party['hp'] <= 0:
            print('パーティのHPは0になった')
            return 0
        
    print_monster_name(monster)
    print('を倒した!')
    return 1

def print_monster_name(monster):
    monster_name=monster['name']
    symbol = ELEMENT_SYMBOLS[monster['element']]
    color=ELEMENT_COLORS[monster['element']]

    #モンスター名を表示
    print(f'\033[30;4{color}m{symbol}{monster_name}{symbol}\033[0m',end='')

def organize_party(player_name,friends):
    total_hp = 0
    total_dp = 0
    for friend in friends:
        total_hp += friend['hp']
        total_dp += friend['dp']

    party = {
            'name':player_name,
            'friends':friends,
            'hp':total_hp,
            'max_hp':total_hp,
            'dp':total_dp / len(friends)
    }
    return party

def show_party(party):
    print('<パーティ編成>----------------------')
    for friend in party['friends']:
        print_monster_name(friend)
        print(f' HP= {friend['hp']} 攻撃={friend['ap']} 防御= {friend['dp']}')
    print('------------------------------------')
    print()


def on_player_turn(party,monster):
    print(f'\n【{party['name']}のターン】(HP={party['hp']})')
    show_battle_field(party,monster)
    while True:
        command = input('コマンド? >').upper()
        if check_valid_command(command):
            break
        print('エラー:正しいコマンドを入力してください')

    move_gem(command)
    evaluate_gems(monster,command)

    do_attack(monster,command)

def on_enemy_turn(party,monster):
    print(f'\n【',end='')
    print_monster_name(monster)
    print(f'のターン】(HP={monster['hp']})')
    do_enemy_attack(party)
def do_attack(monster,command):
    damage = int(hash(command)) % 50
    rand = random.uniform(-0.1,0.1)+1
    damage = int(damage * rand)
    print(f'{damage}のダメージを与えた')
    monster['hp'] -= damage
def do_enemy_attack(party):
    damage = 200
    print(f'{damage}のダメージを受けた')
    party['hp'] -= damage

def show_battle_field(party,monster):
    print('バトルフィールド')
    print_monster_name(monster)
    print(f'HP = {monster['hp']} / {monster['max_hp']}')

    for friend in party['friends']:
        print_monster_name(friend)
        print(' ',end='')
    print(f'\nHP = {party['hp']} / {party['max_hp']}\n')
    print('------------------------------')
    for c in IDXS:
        print(c,end=' ')
    print()
    print_gems()
    print('------------------------------')

    
def fill_gems():
    global gems
    gems=[random.randint(0,4) for _ in range(len(IDXS))]

def print_gems():
    eles=['火','水','風','土','命','無']
    for i in gems:
        color=ELEMENT_COLORS[eles[i]]
        symbol =ELEMENT_SYMBOLS[eles[i]]
        print(f'\033[30;4{color}m{symbol}\033[0m',end=' ')
    print()
def check_valid_command(command):
    if len(command) != 2:
        return False
    if command[0] == command[1]:
        return False
    for c in command:
        if not 'A' <= c <= 'N':
            return False
    return True

def move_gem(command):
    b_index = IDXS.index(command[0])
    e_index = IDXS.index(command[1])
    dir = 1 if b_index < e_index else -1
    print_gems()
    print()
    for i in range(b_index,e_index,dir):
        gems[i],gems[i+dir] = gems[i+dir],gems[i]
        print_gems()
        print()

def evaluate_gems(monster,command):
    do_attack(monster,command)
# main関数の呼び出し
main()
