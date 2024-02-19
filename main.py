spacer = '----------------------'
greeting = 'Welcome!'

print(spacer)
print(greeting)
print(spacer)

lives = 3 #how many questions you can get wrong before game over
correctQuestions = 0 #how many questions are succesfully answered
minCorrect = 5 #minimum of correct questions to win the game
maxCorrect = 10 #maximum of correct questions

def gameOver(remLives, correctQuestions, minCorrect, maxCorrect):
    if remLives < 1:
        if correctQuestions >= minCorrect:
            print("Well Done!")
            print("You've won the game with " + str(correctQuestions) + "/" + str(maxCorrect) + " correct questions.")
            input("Press Enter to exit...")
            exit()

        else: 
            print("You've Lost!")
            print("You're out of lifes!")
            print("Only " + str(correctQuestions) + "/" + str(maxCorrect) + " correct questions.")
            print("Better luck next time.")
            input("Press Enter to exit...")
            exit()

    elif remLives > 0:
        if correctQuestions == maxCorrect:
            print("Great Job!")
            print("You got all of the questions correct.")
            print("Give yourself a pat on the back!")
            input("Press Enter to exit...")
        else:
            print("Well Done!")
            print("You've won the game with " + str(correctQuestions) + "/" + str(maxCorrect) + " correct questions.")
            input("Press Enter to exit...")

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

def Question6(lives, correctQuestions, minCorrect, maxCorrect):
    if lives > 0:
            
        question = 'Does CO2 stay in the air forever?'
        correctAnswer = 'b'
        print(question)
        print("a) Yes, it's imposible to remove it from the air")
        print("b) No, some gets absorbed by oceans and plants")
        print("c) No, the sunlight helps reduce it")
        print("d) Yes, we have to remove it manually")
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

def Question7(lives, correctQuestions, minCorrect, maxCorrect):
    if lives > 0:
            
        question = 'What is the easiest way to help with CO2?'
        correctAnswer = 'd'
        print(question)
        print("a) Stop throwing plastic in oceans")
        print("b) Buying more electric cars")
        print("c) Killing less animals")
        print("d) Planting trees")

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

def Question8(lives, correctQuestions, minCorrect, maxCorrect):
    if lives > 0:
            
        question = 'Where does CO2 come from?'
        correctAnswer = 'b'
        print(question)
        print("a) Animals and plants")
        print("b) Cars, factories, and burning fossil fuels")
        print("c) Humans")
        print("d) Phones, computers and firewood")

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

def Question9(lives, correctQuestions, minCorrect, maxCorrect):
    if lives > 0:
            
        question = 'Why is CO2 bad?'
        correctAnswer = 'a'
        print(question)
        print("a) It traps heat in the atmosphere, causing global warming and climate change")
        print("b) It minimises oxygen in the atmosphere, causing plants and animals to develop slower")
        print("c) It makes the atmosphere thicker, causing rain, flooding, global warming and climate change.")
        print("d) All of the above")

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

def Question10(lives, correctQuestions, minCorrect, maxCorrect):
    if lives > 0:
            
        question = 'How do we measure CO2?'
        correctAnswer = 'c'
        print(question)
        print("a) By mesasuring the amount of rain")
        print("b) By checking the colour of trees in summer")
        print("c) With special instruments called sensors")
        print("d) All of the above")

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

def Main(lives, correctQuestions, minCorrect, maxCorrect):

    lives, correctQuestions = Question1(lives, correctQuestions, minCorrect, maxCorrect) # type: ignore
    print(spacer)
    lives, correctQuestions = Question2(lives, correctQuestions, minCorrect, maxCorrect) # type: ignore
    print(spacer)
    lives, correctQuestions = Question3(lives, correctQuestions, minCorrect, maxCorrect) # type: ignore
    print(spacer)
    lives, correctQuestions = Question4(lives, correctQuestions, minCorrect, maxCorrect) # type: ignore
    print(spacer)
    lives, correctQuestions = Question5(lives, correctQuestions, minCorrect, maxCorrect) # type: ignore
    print(spacer)
    lives, correctQuestions = Question6(lives, correctQuestions, minCorrect, maxCorrect) # type: ignore
    print(spacer)
    lives, correctQuestions = Question7(lives, correctQuestions, minCorrect, maxCorrect) # type: ignore
    print(spacer)
    lives, correctQuestions = Question8(lives, correctQuestions, minCorrect, maxCorrect) # type: ignore
    print(spacer)
    lives, correctQuestions = Question9(lives, correctQuestions, minCorrect, maxCorrect) # type: ignore
    print(spacer)
    lives, correctQuestions = Question10(lives, correctQuestions, minCorrect, maxCorrect) # type: ignore
    print(spacer)
    gameOver(lives, correctQuestions, minCorrect, maxCorrect)


Main(lives, correctQuestions, minCorrect, maxCorrect)