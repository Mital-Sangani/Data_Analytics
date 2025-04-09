import random 

ipl_team_list = ["RR","RCB","KKR","CSK","GT"]

menu = """
                    IPL 2025
             TOP 5 IPL TEAMS ARE :
"""
print(menu)

# ------------variable zone:------------------------------

my_team_ball = 0
opp_team_ball = 0

my_team_score = 0
opp_team_score = 0

my_team_wicket = 0
opp_team_wicket = 0

score_list = [0,1,2,4,6,"Wicket","no_ball","wide",1,2,4,6]
# --------------------------------------------------------------------

for team in ipl_team_list:
    print(team, end=" ! ")
print()

my_team = input("Enter your team : ").upper()

opp_team = random.choice(ipl_team_list)

while opp_team == my_team:
    opp_team = random.choice(ipl_team_list)

print(f"MY TEAM : {my_team}")
print(f"OPP TEAM : {opp_team}")
print("\n------------------------------\n")

print("\n------------------------------\n")

toss_time = input("TOSS TIME : Press H for Head and T for Tails : ").upper()

if toss_time == "H":
    print("Your Choics is Head")
else : 
    print("Your choice is Tails")

toss_list = ["Head","Tails"]

print("------------------------------")

actul_toss = random.choice(toss_list)

if toss_time == actul_toss[0]:
    print("You won the TOSS ! ")
    
    menu1 = """
            CHOOSE YOUR PLAY SELECTION
            
                1) batting
                2) bowling
                
                press 1 or 2
    """
    print(menu1)
    input1 = int(input("Enter your play selection choice : "))
    if input1 == 1:
        print("You selecte batting first")
        
        while my_team_ball < 6 :
            score = random.choice(score_list)
            if score in [0,1,2,4,6,]:
                my_team_ball += 1
                my_team_score += score
                print(f"it's {score} run ")
                print()
                print(F"{my_team} score : {my_team_score}/{my_team_wicket} over : (0.{my_team_ball})")
            elif score == "Wicket":
                my_team_wicket += 1
                my_team_ball += 1
                print(f"it's wicket")
                print()
                print(F"{my_team} score : {my_team_score}/{my_team_wicket} over : (0.{my_team_ball})")
            else:
                my_team_score += 1
                print(f"it's {score} ")
                print()
                print(f"{my_team} score : {my_team_score}/{my_team_wicket} over : (0.{my_team_ball})")
            input("press enter for hit the ball ")
            print()
        print("-------------1st ininig completed-------------")
        input("-------------Pree Enter to start 2nd ining")
        input("-------------now it's your turn to bowling-------------")
        while opp_team_ball < 6 :
            score = random.choice(score_list)
            if score in [0,1,2,4,6,]:
                opp_team_ball += 1
                opp_team_score += score
                print(f"it's {score} run ")
                print()
                print(F"{opp_team} score : {opp_team_score}/{opp_team_wicket} over : (0.{opp_team_ball})")
            elif score == "Wicket":
                opp_team_wicket += 1
                opp_team_ball += 1
                print(f"it's wicket")
                print()
                print(F"{opp_team} score : {opp_team_score}/{opp_team_wicket} over : (0.{opp_team_ball})")
            else:
                opp_team_score += 1
                print(f"it's {score} ")
                print()
                print(f"{opp_team} score : {opp_team_score}/{opp_team_wicket} over : (0.{opp_team_ball})")
            input("press enter to throw the next ball")
            print()
        print(f"-------------{my_team} : {my_team_score}/{my_team_wicket} || {opp_team} : {opp_team_score}/{opp_team_wicket}-------------")
        if my_team_score > opp_team_score:
            win = my_team_score - opp_team_score
            print(f"---------------{my_team} won with {win} run---------------")
        else :
            win = opp_team_score - my_team_score
            print(f"---------------{opp_team} won with {11-opp_team_wicket} wicket---------------")        
    else:
        print("you selecte bowling first")
        input("Press Enter to start the bowling")
        
        while opp_team_ball < 6 :
            score = random.choice(score_list)
            if score in [0,1,2,4,6,]:
                opp_team_ball += 1
                opp_team_score += score
                print(f"it's {score} run ")
                print()
                print(F"{opp_team} score : {opp_team_score}/{opp_team_wicket} over : (0.{opp_team_ball})")
            elif score == "Wicket":
                opp_team_wicket += 1
                opp_team_ball += 1
                print(f"it's wicket")
                print()
                print(F"{opp_team} score : {opp_team_score}/{opp_team_wicket} over : (0.{opp_team_ball})")
            else:
                opp_team_score += 1
                print(f"it's {score} ")
                print()
                print(f"{opp_team} score : {opp_team_score}/{opp_team_wicket} over : (0.{opp_team_ball})")
            input("press enter to throw the ball")
            print()
        print("-------------1st ininig completed-------------")
        input("-------------Pree Enter to start 2nd ining:")
        input("-------------now it's your turn to batting-------------")
        while my_team_ball < 6 :
            score = random.choice(score_list)
            if score in [0,1,2,4,6,]:
                my_team_ball += 1
                my_team_score += score
                print(f"it's {score} run ")
                print()
                print(F"{my_team} score : {my_team_score}/{my_team_wicket} over : (0.{my_team_ball})")
            elif score == "Wicket":
                my_team_wicket += 1
                my_team_ball += 1
                print(f"it's wicket")
                print()
                print(F"{my_team} score : {my_team_score}/{my_team_wicket} over : (0.{my_team_ball})")
            else:
                my_team_score += 1
                print(f"it's {score} ")
                print()
                print(f"{my_team} score : {my_team_score}/{my_team_wicket} over : (0.{my_team_ball})")
            input("press enter for hit the ball ")
            print()
        print(f"-------------{my_team} : {my_team_score}/{my_team_wicket} || {opp_team} : {opp_team_score}/{opp_team_wicket}-------------")
        if my_team_score > opp_team_score:
            win = my_team_score - opp_team_score
            print(f"---------------{my_team} won with {11-my_team_wicket} wicket---------------")
        else :
            win = opp_team_score - my_team_score
            print(f"---------------{opp_team} won with {win} run---------------")     
else:
    print(f"{opp_team} won the TOSS ! ")
    list1 = ["batting" , "bowling"]
    choos = random.choice(list1)
    print(f"{opp_team} selecte {choos} first")
    
    if choos == "batting" :        
        while opp_team_ball < 6 :
            score = random.choice(score_list)
            if score in [0,1,2,4,6,]:
                opp_team_ball += 1
                opp_team_score += score
                print(f"it's {score} run ")
                print()
                print(F"{opp_team} score : {opp_team_score}/{opp_team_wicket} over : (0.{opp_team_ball})")
            elif score == "Wicket":
                opp_team_wicket += 1
                opp_team_ball += 1
                print(f"it's wicket")
                print()
                print(F"{opp_team} score : {opp_team_score}/{opp_team_wicket} over : (0.{opp_team_ball})")
            else:
                opp_team_score += 1
                print(f"it's {score} ")
                print()
                print(f"{opp_team} score : {opp_team_score}/{opp_team_wicket} over : (0.{opp_team_ball})")
            input("press enter to throw ball")
            print()
        print("-------------1st ininig completed-------------")
        input("-------------Pree Enter to start 2nd ining:")
        input("-------------now it's your turn to batting-------------")
        while my_team_ball < 6 :
            score = random.choice(score_list)
            if score in [0,1,2,4,6,]:
                my_team_ball += 1
                my_team_score += score
                print(f"it's {score} run ")
                print()
                print(F"{my_team} score : {my_team_score}/{my_team_wicket} over : (0.{my_team_ball})")
            elif score == "Wicket":
                my_team_wicket += 1
                my_team_ball += 1
                print(f"it's wicket")
                print()
                print(F"{my_team} score : {my_team_score}/{my_team_wicket} over : (0.{my_team_ball})")
            else:
                my_team_score += 1
                print(f"it's {score} ")
                print()
                print(f"{my_team} score : {my_team_score}/{my_team_wicket} over : (0.{my_team_ball})")
            input("press enter for hit the ball ")
            print()
        print(f"-------------{my_team} : {my_team_score}/{my_team_wicket} || {opp_team} : {opp_team_score}/{opp_team_wicket}-------------")
        if my_team_score > opp_team_score:
            win = my_team_score - opp_team_score
            print(f"---------------{my_team} won with {11-my_team_wicket} wicket---------------")
        else :
            win = opp_team_score - my_team_score
            print(f"---------------{opp_team} won with {win} run---------------")
    else :
        while my_team_ball < 6 :
            score = random.choice(score_list)
            if score in [0,1,2,4,6,]:
                my_team_ball += 1
                my_team_score += score
                print(f"it's {score} run ")
                print()
                print(F"{my_team} score : {my_team_score}/{my_team_wicket} over : (0.{my_team_ball})")
            elif score == "Wicket":
                my_team_wicket += 1
                my_team_ball += 1
                print(f"it's wicket")
                print()
                print(F"{my_team} score : {my_team_score}/{my_team_wicket} over : (0.{my_team_ball})")
            else:
                my_team_score += 1
                print(f"it's {score} ")
                print()
                print(f"{my_team} score : {my_team_score}/{my_team_wicket} over : (0.{my_team_ball})")
            input("press enter for hit the ball ")
            print()
        print("-------------1st ininig completed-------------")
        input("-------------Pree Enter to start 2nd ining:")
        input("-------------now it's your turn to bowling-------------")
        while opp_team_ball < 6 :
            score = random.choice(score_list)
            if score in [0,1,2,4,6,]:
                opp_team_ball += 1
                opp_team_score += score
                print(f"it's {score} run ")
                print()
                print(F"{opp_team} score : {opp_team_score}/{opp_team_wicket} over : (0.{opp_team_ball})")
            elif score == "Wicket":
                opp_team_wicket += 1
                opp_team_ball += 1
                print(f"it's wicket")
                print()
                print(F"{opp_team} score : {opp_team_score}/{opp_team_wicket} over : (0.{opp_team_ball})")
            else:
                opp_team_score += 1
                print(f"it's {score} ")
                print()
                print(f"{opp_team} score : {opp_team_score}/{opp_team_wicket} over : (0.{opp_team_ball})")
            input("press enter to throw the next ball")
            print()
        print(f"-------------{my_team} : {my_team_score}/{my_team_wicket} || {opp_team} : {opp_team_score}/{opp_team_wicket}-------------")
        if my_team_score > opp_team_score:
            win = my_team_score - opp_team_score
            print(f"---------------{my_team} won with {win} run---------------")
        else :
            win = opp_team_score - my_team_score
            print(f"---------------{opp_team} won with {11-opp_team_wicket} ---------------")        