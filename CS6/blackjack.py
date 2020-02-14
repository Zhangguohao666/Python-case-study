import random

def get_shuffled_deck():
    """初始化包括52张扑克牌的列表，并混排后返回，表示一副洗好的扑克牌"""
    # 花色suits和序号
    suits = {'♣', '♠', '♦', '♥'}
    ranks = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}
    deck = []
    # 创建一副52张的扑克牌
    for suit in suits:
        for rank in ranks:
            deck.append(suit + ' ' + rank)
    random.shuffle(deck)
    return deck

def deal_card(deck, participant):
    """发一张牌给参与者participant"""
    card = deck.pop()
    participant.append(card)
    return card

def compute_total(hand):
    """计算并返回一手牌的点数和"""
    values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, \
              '9':9, '10':10, 'J':10, 'Q':10, 'K':10, ' A':11}
    result = 0 #初始化点数和为0
    numAces = 0 #A的个数

    # 计算点数和A的个数
    for card in hand:
        result += values[card[2:]]
        if card[2] == 'A':
            numAces += 1
    
    #如果点数和>21，则尝试把A当做1来计算
    # (即减去10)，多个A循环减去10，直到点数<=21
    while result > 21 and numAces > 0:
        result -= 10
        numAces -= 1
    return result

def print_hand(hand):
    for card in hand:
        print(card, end = '  ')
    print()

def blackjack():
    """21点扑克牌游戏，计算机人工智能AI为庄家，用户为玩家"""
    # 初始化一副洗好的扑克牌，初始化庄家和玩家手中的牌为空
    deck = get_shuffled_deck()
    house = [] # 庄家的牌
    player = [] # 玩家的牌
    
    # 依次给玩家和庄家各发两张牌
    for i in range(2):
        deal_card(deck, player)
        deal_card(deck, house)
        
    # 打印一手牌
    print('庄家的牌：', end = ''); print_hand(house)
    print('玩家的牌：', end = ''); print_hand(player)

    # 询问玩家是否继续拿牌，如果是，继续给玩家发牌
    answer = input('是否继续拿牌（y/n，缺省为y）：')
    while answer in ('', 'y', 'Y'):
        card = deal_card(deck, player)
        print('玩家拿到的牌为：', end = ''); print_hand(player)
        # 计算牌点
        if compute_total(player) > 21:
            print('爆掉  玩家输牌!')
            return
        answer = input('是否继续拿牌（y/n，缺省为y）：')

    # 庄家(计算机人工智能)按“庄家规则”确定是否拿牌
    while compute_total(house) < 17:
        card = deal_card(deck, house)
        print('庄家拿到的牌为：', end =''); print_hand(house)
        # 计算牌点
        if compute_total(house) > 21:
            print('爆掉  玩家赢牌!')
            return

    # 分别计算庄家和玩家的点数，比较点数大小，输出输赢结果信息
    houseTotal, playerTotal = compute_total(house), compute_total(player)
    if houseTotal > playerTotal:
        print('庄家赢牌!')
    elif houseTotal < playerTotal:
        print('玩家赢牌!')
    elif houseTotal == 21 and 2 == len(house) < len(player) : # 拥有blackjack的庄家赢牌
        print('庄家赢牌!')
    elif playerTotal == 21 and 2 == len(player) < len(house) : # 拥有blackjack的玩家赢牌
        print('玩家赢牌!')
    else:
        print('平局！')

if __name__ == '__main__':
    blackjack()
