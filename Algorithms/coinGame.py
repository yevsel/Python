from random import choice
my_money=100
coin=['Heads','Tails']
running=True
print('RULES','\n')
print('Type money to display your current account')

def check_win():
    global running
    if my_money>=120:
        print('COngratulation')
        running=False
    
    elif my_money<=80:
        print('Sorry you lost')
        running=False


while running:
    computer=choice(coin)
    confirm=input('Heads or Tails: ')

    if confirm=='money':
        print('You have',my_money)

    elif computer.lower()==confirm.lower():
        my_money+=9
        print('Correct')

    elif computer.lower()!=confirm.lower():
        my_money-=10
        print('Wrong')
    check_win()

    
    