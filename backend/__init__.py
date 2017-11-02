import random

cards = {
        'A' : '1',
        '1' : '1',
        '2' : '2',
        '3' : '3',
        '4' : '4',
        '5' : '5',
        '6' : '6',
        '7' : '7',
        '8' : '8',
        '9' : '9',
        '10' : '10',
        'J' : '10',
        'Q' : '10',
        'K' : '10'
}

def process_user_query(query_string):
    return [f"Hi {name}!\n" for name in query_string.split(' ') if name[0].isupper()==True]


def get_card():
    chosen_card = random.choice(list(cards.keys()))
    value = []
    value.append(chosen_card)
    value.append(cards[chosen_card])
    return value

def hit(sum,value):
    return (sum+value)



print(get_card())
