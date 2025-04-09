class fonts :
    END = '\033[0m'
    BOLD = '\033[1m'
def question1 ():
    print(fonts.BOLD + """ 1). Who is Current Prime Minister Of India ? """ + fonts.END)
    print("""    A. Narenda Modi
    B. Indira Gandhi
    C. Rahul Gandhi
    D. Amit Shah""")
    choice = input("Enter Your Choice Here : ").upper()
    ans = "A"
    return choice,ans
    
def question2 ():
    print(fonts.BOLD + """ 2). Who wrote the Indian national anthem? """ + fonts.END)
    print("""    A) Rabindranath Tagore
    B. Bankim Chandra Chatterjee
    C. Sarojini Naidu
    D. Subramania Bharati""")
    choice = input("Enter Your Choice Here : ").upper()
    ans = "A"
    return choice,ans
    
def question3 ():
    print(fonts.BOLD + """ 3). Which of these elements is found in water? """ + fonts.END)
    print("""    A. Oxygen
    B. Helium
    C. Argon
    D. Neon""")
    choice = input("Enter Your Choice Here : ").upper()
    ans = "A"
    return choice,ans
    
def question4 ():
    print(fonts.BOLD + """ 4). Which is the largest continent by area? """ + fonts.END)
    print("""    A. Africa
    B. Asia
    C. Europe
    D. North America""")
    choice = input("Enter Your Choice Here : ").upper()
    ans = "B"
    return choice,ans
    
def question5 ():
    print(fonts.BOLD + """ 5). What is the smallest bone in the human body? """ + fonts.END)
    print("""    A. Femur
    B. Stapes
    C. Ulna
    D. Tibia""")
    choice = input("Enter Your Choice Here : ").upper()
    ans = "B"
    return choice,ans
    
def question6 ():
    print(fonts.BOLD + """ 6). Which Nobel Prize category was established most recently? """ + fonts.END)
    print("""    A. Physics
    B. Peace
    C. Literature
    D. Economic Sciences""")
    choice = input("Enter Your Choice Here : ").upper()
    ans = "D"
    return choice,ans
       
def question7 ():
    print(fonts.BOLD + """ 7). What is the chemical symbol for the element gold? """ + fonts.END)
    print("""    A. Au
    B. Ag
    C. Pb
    D. Fe""")
    choice = input("Enter Your Choice Here : ").upper()
    ans = "A"
    return choice,ans
     
def question8 ():
    print(fonts.BOLD + """ 8). Who was the first woman to win a Nobel Prize? """ + fonts.END)
    print("""   A. Marie Curie
    B. Mother Teresa
    C. Rosalind Franklin
    D. Ada Lovelace""")
    choice = input("Enter Your Choice Here : ").upper()
    ans = "A"
    return choice,ans
     
def question9 ():
    print(fonts.BOLD + """ 9). Which country is home to the Great Barrier Reef? """ + fonts.END)
    print("""    A. Australia
    B. Canada
    C. Brazil
    D. South Africa""")
    choice = input("Enter Your Choice Here : ").upper()
    ans = "A"
    return choice,ans
     
def question10 ():
    print(fonts.BOLD + """ 10). Which is the largest island in the world by area? """ + fonts.END)
    print("""    A. Borneo
    B. Madagascar
    C. Greenland
    D. New Guinea""")
    choice = input("Enter Your Choice Here : ").upper()
    ans = "C"
    return choice,ans
    
def ans_check (choice,ans):
    return choice == ans    
   
score = 0
questions = [question1,question2,question3,question4,question5,question6,question7,question8,question9,question10]

for question in questions:
   choice,ans = question()
   
   if ans_check (choice,ans):
       score += 20
       print("Correct!")
       print()     
   else:
       score -= 20
       break
    
print(f"Your final score is: {score}")