import random

level = input("choose your difficulty 'easy' or 'hard' : ").lower()
rand = random.randint(1,100)
lives = 0
if level == 'hard':
    lives+=5
else:
    lives+=10
end_of_game = False
while not end_of_game:
    guess = int(input("guess the number : "))

    if rand < guess:
        print('Too high ...try again')
        lives-=1
        print(f'remaning changes : {lives}')
    elif rand > guess:
        print(f'Too low ...try again')
        lives-=1
        print(f'remaning changes : {lives}')
    elif rand == guess:
        print(f'you guessed the number .... : {rand} \n you win')
        end_of_game = True
    if lives == 0:
        end_of_game = True    


