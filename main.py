spacer = '----------------------'
greeting = 'Welcome!'

print(spacer)
print(greeting)
print(spacer)

lives = 3 #how many questions you can get wrong before game over
correctQuestions = 0 #how many questions are succesfully answered
minCorrect = 3 #minimum of correct questions to win the game
maxCorrect = 5 #maximum of correct questions

def gameOver(remLives, correctQuestions, minCorrect, maxCorrect):
    if remLives < 1:
        if correctQuestions >= minCorrect:
            print("Well Done!")
            print("You've won the game with " + str(correctQuestions) + "/" + str(maxCorrect) + " correct questions.")

        else: 
            print("You've Lost!")
            print("You're out of lifes!")
            print("Only " + str(correctQuestions) + "/" + str(maxCorrect) + " correct questions.")
            print("Better luck next time.")
            exit()

    elif remLives > 0:
        if correctQuestions == maxCorrect:
            print("Great Job!")
            print("You got all of the questions correct.")
            print("Give yourself a pat on the back!")
        else:
            print("Well Done!")
            print("You've won the game with " + str(correctQuestions) + "/" + str(maxCorrect) + " correct questions.")


def Question1(lives, correctQuestions, minCorrect, maxCorrect):
    if lives > 0:
            
        question = 'What does CO2 Stand for?'
        correctAnswer = 'carbon dioxide'
        print(question)
        ans = input("> ")
        if ans == correctAnswer:
            print("Correct!")
            correctQuestions = correctQuestions + 1
            return lives, correctQuestions
        else: 
            print("Incorrect!")
            lives = lives - 1
            return lives, correctQuestions
    else:  gameOver(lives, correctQuestions, minCorrect, maxCorrect)
         
        
def Question2(lives, correctQuestions, minCorrect, maxCorrect):
    if lives > 0:
            
        question = 'What element is the C?'
        correctAnswer = 'carbon'
        print(question)
        ans = input("> ")
        if ans == correctAnswer:
            print("Correct!")
            correctQuestions = correctQuestions + 1
            return lives, correctQuestions
        else: 
            print("Incorrect!")
            lives = lives - 1
            return lives, correctQuestions
    else:  gameOver(lives, correctQuestions, minCorrect, maxCorrect)


def Question3(lives, correctQuestions, minCorrect, maxCorrect):
    if lives > 0:
            
        question = 'What element is the O?'
        correctAnswer = 'oxygen'
        print(question)
        ans = input("> ")

        if ans == correctAnswer:
            print("Correct!")
            correctQuestions = correctQuestions + 1
            return lives, correctQuestions

        else: 
            print("Incorrect!")
            lives = lives - 1
            return lives, correctQuestions
    else:  gameOver(lives, correctQuestions, minCorrect, maxCorrect)


def Question4(lives, correctQuestions, minCorrect, maxCorrect):
    if lives > 0:
            
        question = 'How much does CO2 weigh?'
        correctAnswer = 'c'
        print(question)
        print("a) 47 grams per mole")
        print("b) 50 grams per mole")
        print("c) 44 grams per mole")
        print("d) 50 grams per mole")
        ans = input("> ")
        if ans == correctAnswer:
            print("Correct!")
            correctQuestions = correctQuestions + 1
            return lives, correctQuestions
        else: 
            print("Incorrect!")
            lives = lives - 1
            return lives, correctQuestions
    else:  gameOver(lives, correctQuestions, minCorrect, maxCorrect)


def Question5(lives, correctQuestions, minCorrect, maxCorrect):
    if lives > 0:
            
        question = 'What happens when plants absorb CO2?'
        correctAnswer = 'a'
        print(question)
        print("a) They use it to make food through photosynthesis")
        print("b) They use it to make light through sunlight")
        print("c) They use it to make water through photosynthesis")
        print("d) They use it to make oxygen through sunlight")
        ans = input("> ")
        if ans == correctAnswer:
            print("Correct!")
            correctQuestions = correctQuestions + 1
            return lives, correctQuestions
        else: 
            print("Incorrect!")
            lives = lives - 1
            return lives, correctQuestions
    else:  gameOver(lives, correctQuestions, minCorrect, maxCorrect)



lives, correctQuestions = Question1(lives, correctQuestions, minCorrect, maxCorrect)

lives, correctQuestions = Question2(lives, correctQuestions, minCorrect, maxCorrect)

lives, correctQuestions = Question3(lives, correctQuestions, minCorrect, maxCorrect)

lives, correctQuestions = Question4(lives, correctQuestions, minCorrect, maxCorrect)

lives, correctQuestions = Question5(lives, correctQuestions, minCorrect, maxCorrect)

gameOver(lives, correctQuestions, minCorrect, maxCorrect)