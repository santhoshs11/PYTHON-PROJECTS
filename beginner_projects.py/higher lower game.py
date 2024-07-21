import random
from art_higher import logo,vs
from higher_lower_data import data 
def ranacc():
    return random.choice(data)

def format(acc):
    name = acc['name']
    desc = acc['description']
    country =acc['country']
    return f'{name} , a {desc} from {country}'


score =0
def check_follower(guess,a_follower,b_follower):
    if a_follower > b_follower:
        return guess == 'a'
    else:
        return guess=='b'



def game():
    person_a = ranacc()
    person_b = ranacc()
    should_con = False

    while not should_con:
        print(logo)
        person_a = person_b
        person_b = ranacc()
        while person_a == person_b:
            person_b = ranacc()

        print(f'compare A {format(person_a)}')
        print(vs)
        print(f'against B {format(person_b)}')

        follower_a = person_a['follower_count']
        follower_b = person_b['follower_count']
        guess = input('guess who got more followers : ').lower()

        check = check_follower(guess,follower_a,follower_b)

        if check:
            global score 
            score += 1
            print(f'you are right your score : {score}')

        else:
            print('wrong answer !!')
            if input('do you want to play again ? (yes / no) : ').lower() =='no':
                print('good bye !!')
                should_con = True  
            else:
                should_con = False    


game()


