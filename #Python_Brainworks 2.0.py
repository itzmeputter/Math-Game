#Python_Brainworks 2.0

#Introduction
name = input("What's your name?: ")
age = int(input("How old are you?: "))
print(f"Welcome, {name}.")
print("You have 3 lives, each time you answer wrong, you got deducted by 1 point. If you got 0 points then you start again.")
print("Rules: 1. If there's more than 1 answer, put a comma and put it in order. ex.(x-1)(x-2). answer = 1,2\n2. ** = tothe power of. ex. x**2 = x to the power of 2")
print("Select your level")
print("There's 5 levels: 1.Kindergarten 2.Easy 3.Moderate 4.Hard 5.Brainpower")
level = input("ENTER YOUR LEVEL: ")

#Quiz_Level 1
key1 = ["386","690","1132","photosynthesis","potential-kinetic","NaCl","Mn","producer","KCl","ultraviolet"]
questions1 = ["Question 1: 187 + 199","Question 2: 299 + 391 = ?","Question 3: 141 + 991 = ?","Question 4: What is photosynthesis?","Question 5: When an object falls down, the energy converted from which form to whihc form?","Question 6: What is a chemical formula of salt","Question 7: What is an element sign of Manganese","Question 8: What is the role of plants in a food chain","Question 9: What is a chemical formula of potassium chloride?","Question 10: What's the type of electromagnetic radiation from the sun"]
if level == "1":
    print("Let's go")
    life = 3
    for i in range(len(questions1)):
        print(questions1[i])
        answer = input("ENTER THE CORRECT ANSWER: ")
        answer = answer.replace(" ","")
        answer = answer.lower()
        correct = key1[i]

        if answer == correct:
            print("Correct")
        else:
            life -= 1
            print(f"Wrong! You have {life} chances left")
            if life == 0:
                print("GAME OVER!\nStart again, type 'start'\nQuit game, type 'quit")
                decision = input("What's your decision: ")
                if decision == "quit":
                    print("Thanks for playing\nSee you next time")
                    break
                else:
                    life = 3
                    print(f"Welcome back{name}")
                    continue

#Quiz_Level 2
key2 = ["4998","12335","36","7","2","-3",["-9,-8","-8,-9"],["-16,-12","-12,-16"],["-20,36","36,-20"],["-13,-30","-30,-13"]]
questions2 = ["Question 1: 2999 + 1999","Question 2: 5896 + 6439","Question 3: (84 + 36)/4 + 6","Question 4: 8x + 64 = 120 ","Question 5: 13x + 324 = 350 ","Question 6: (x + 3)**2 = 0, x = ? ","Question 7: (x + 9)(x + 8) = 0, x =? ","Question 8: (x + 16)(x + 12) = 0, x = ? ","Question 9: (x + 20)(36 - x) = 0, x = ? ","Question 10: (x + 13)(x + 30) = 0, x = ? "]
if level == "2":
    print("Let's go")
    life = 3   
    for i in range(len(questions2)):
        print(questions2[i])
        answer = input("ENTER THE CORRECT ANSWER: ")
        answer = answer.replace(" ","")
        answer = answer.lower()
        correct = key2[i]

        if isinstance(correct, list):
            if answer in correct:
                print("Correct")
            else:
                life -= 1
                print(f"Wrong! You have {life} chances left")
        else:
            if answer == correct:
                print("Correct")

            if life == 0:
                print("GAME OVER!\nStart again, type 'start'\nQuit game, type 'quit")
                decision = input("What's your decision: ")
                if decision == "quit":
                    print("Thanks for playing\nSee you next time")
                    break
                else:
                    life = 3
                    print(f"Welcome back{name}")
                    continue

#Quiz_Level 3
key3 = [["4,-9","-9,4"],["-10,16","16,-10"],["-13,17","17,-13"],["-24,34","34,-24"],["-78,90","90,-78"],"12","15 km/h","8","x**2 + 21x + 80","x**2 + 49x + 600"]
questions3 = ["Question 1: (x - 4)(x + 9) = 0, x = ?","Question 2: (x + 10)(x - 16) = 0, x = ?","Question 3: (x + 13)(x - 17) = 0, x = ?","Question 4: (x + 24)(x - 34) = 0, x = ?","Question 5: (x + 78)(x - 90) = 0, x = ?","12","15 km/h","8","x**2 + 21x + 80","x**2 + 49x + 600"]
if level == "3":
    print("Let's go")
    life = 3   
    for i in range(len(questions3)):
        print(questions3[i])
        answer = input("ENTER THE CORRECT ANSWER: ")
        answer = answer.replace(" ","")
        answer = answer.lower()
        correct = key3[i]

        if isinstance(correct, list):
            if answer in correct:
                print("Correct")
            else:
                life -= 1
                print(f"Wrong! You have {life} chances left")
        else:
            if answer == correct:
                print("Correct")

            if life == 0:
                print("GAME OVER!\nStart again, type 'start'\nQuit game, type 'quit")
                decision = input("What's your decision: ")
                if decision == "quit":
                    print("Thanks for playing\nSee you next time")
                    break
                else:
                    life = 3
                    print(f"Welcome back{name}")
                    continue

#Quiz_Level 4
questions4 = ["Question 1: y = x + 1\ny = 2x - 3\nx + y = ?","Question 2: y = x + 4\ny = -x - 2\nx + y = ?","Question 3: y = -2x - 4\ny = x - 4\nx + y = ?","Question 4: y = -x + 4\ny = 2x + 8\nx + y = ?","Question 5: y = -2 - x\ny = 2x + 13\nx + y = ?","Question 6: x**2 - 16 = 0, x + y = ?","Question 7: x**2 - 144 = 0, x + y = ?","Question 8: 4 - 25x**2 = 0, x + y = ?","Question 9: 4x**2 - 9 = 0, x + y = ?","Question 10: x**2 + 11x + 10 = 0, x + y = ?"]
key4 = ["9","-2","-4","4","-2",["4,-4","-4,4"],["12,-12","-12,12"],["2/5,-2/5","-2/5,2/5"],["1.5,-1.5","-1.5,1.5"],["10,11","11,10"]]
if level == "4":
    print("Let's go")
    life = 3   
    for i in range(len(questions4)):
        print(questions4[i])
        answer = input("ENTER THE CORRECT ANSWER: ")
        answer = answer.replace(" ","")
        answer = answer.lower()
        correct = key4[i]
        
        if isinstance(correct, list):
            if answer in correct:
                print("Correct")
            else:
                life -= 1
                if life == 0:
                    print("GAME OVER!\nStart again, type 'start'\nQuit game, type 'quit'")
                    decision = input("What's your decision: ")
                    if decision == "quit":
                        print("Thanks for playing\nSee you next time")
                        break
                    else:
                        life = 3
                        print(f"Welcome back {name}")
                else:
                    print(f"Wrong! You have {life} chances left")
        else:
            if answer == correct:
                print("Correct")
            else:
                life -= 1
                if life == 0:
                    print("GAME OVER!\nStart again, type 'start'\nQuit game, type 'quit'")
                    decision = input("What's your decision: ")
                    if decision == "quit":
                        print("Thanks for playing\nSee you next time")
                        break
                    else:
                        life = 3
                    print(f"Welcome back {name}")
                else:
                    print(f"Wrong! You have {life} chances left")
                    continue

#Quiz_Level 5
questions5 = ["Quetsion 1: y = 2x - 10\ny = 4x - 18\n x + y = ?","Question 2: y = 5 - 3x\ny = 10 - 6x\nx + y = ?","Question 3: y = x + 2\n3x + 2y = 19\nx + y = ?","Question 4: 4x + 3y = 7\n6x - 3y = -27\nx + y = ?","Question 5: 12x + 9y = 7\n7x - 2y = -8\nx + y = ?","Question 6: 5x**2 - 6x = 13x\nx = ?","Question 7: 9x**2 + 6x - 48 = 0\nx = ?","Question 8: 36x**2 + 39x = 12\nx = ?","Question 9: (2x + 3)**2 - (x + 1)**2 = 0\nx = ?","Question 10: (2x + 1)(x -2) = 7\nx = ?"]
key5 = ["2","5/3","8","3","1","0",["-8/3,2","2,-8/3"],["0.25,4/3","4/3,0.25"],"-2",["1.5,3","3,1.5"]]
if level == "5":
    print("Let's go")
    life = 3   
    for i in range(len(questions5)):
        print(questions5[i])
        answer = input("ENTER THE CORRECT ANSWER: ")
        answer = answer.replace(" ","")
        answer = answer.lower()
        correct = key5[i]
        
        if isinstance(correct, list):
            if answer in correct:
                print("Correct")
            else:
                life -= 1
                print(f"Wrong! You have {life} chances left")
        else:
            if answer == correct:
                print("Correct")

            if life == 0:
                print("GAME OVER!\nStart again, type 'start'\nQuit game, type 'quit")
                decision = input("What's your decision: ")
                if decision == "quit":
                    print("Thanks for playing\nSee you next time")
                    break
                else:
                    life = 3
                    print(f"Welcome back{name}")
                    continue