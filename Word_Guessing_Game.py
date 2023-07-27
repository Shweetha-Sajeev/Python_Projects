import random
animals = ['elephant','bear','cheetah','giraffe','wolf','tiger','penguin','rabbit','lion','monkey','rhinoceros','sheep','kangaroo','zebra']
fruits = ['apple', 'banana','grapes','mango','lime','watermelon','jackfruit','guava','orange','papaya','pear','peach','pomegranate','strawberry']
stationery = ['pencil','eraser','sharpener','envelope','paper','stapler','folder','marker','inkpot','calculator','glue','notebook','scissors','ruler']
while 1:
    words = animals + fruits + stationery
    random_word = random.choice(words)
    print('WORD GUESSING GAME')
    if random_word in animals:
        print('HINT: It is an animal')
    elif random_word in fruits:
        print('HINT: It is a fruit')
    else:
        print('HINT: It is a stationery item')

    user_guesses = ''
    chances = 5
    while chances>0:
        wrong_guess = 0
        for ch in random_word:
            if ch in user_guesses:
                print(ch, end=' ')
            else:
                wrong_guess+=1
                print('_', end = ' ')
        if wrong_guess ==0:
            print('\nCongrats.you won. The word is', random_word)
            again = input('Do you like to play again? Y or N')
            if again == 'Y':
                break
            else:
                quit()
        guess = input('\nMake a guess')
        user_guesses+=guess

        if guess not in random_word:
            chances-=1
            print(f'Wrong.You have {chances} more chances')
            if chances ==0:
                print('Game over.You lose.The word is', random_word)
                restart = input('Do you like to play again? Y or N')
                if restart == 'N':
                    quit()

