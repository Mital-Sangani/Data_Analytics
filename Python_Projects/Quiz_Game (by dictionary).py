quiz = {
    1: {
        "que": "Most popular programming language?",
        "options": ["Java", "Python", "C++", "JavaScript"],
        "ans": "B"
    },
    2: {
        "que": "Most favourite cricketer?",
        "options": ["Virat Kohli", "Rohit Sharma", "MS Dhoni", "Sachin Tendulkar"],
        "ans": "C"
    },
    3: {
        "que": "Who is the Prime Minister of India?",
        "options": ["Rahul Gandhi", "Amit Shah", "Narendra Modi", "Arvind Kejriwal"],
        "ans": "C"
    },
    4: {
        "que": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "ans": "C"
    },
    5: {
        "que": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "ans": "B"
    },
    6: {
        "que": "Who wrote 'Hamlet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Leo Tolstoy"],
        "ans": "B"
    },
    7: {
        "que": "Which is the longest river in the world?",
        "options": ["Amazon", "Ganges", "Nile", "Yangtze"],
        "ans": "C"
    },
    8: {
        "que": "What is the square root of 64?",
        "options": ["6", "7", "8", "9"],
        "ans": "C"
    },
    9: {
        "que": "Which gas do plants absorb from the atmosphere?",
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        "ans": "C"
    },
    10: {
        "que": "Who discovered gravity?",
        "options": ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Nikola Tesla"],
        "ans": "B"
    }
}

for i in range(1, len(quiz) + 1):
    print(f"Que. ({i}) {quiz[i]['que']}")
    print("A.", quiz[i]['options'][0])
    print("B.", quiz[i]['options'][1])
    print("C.", quiz[i]['options'][2])
    print("D.", quiz[i]['options'][3])
    
    ans = input("Enter your answer (A/B/C/D): ").strip().upper()
    if ans == quiz[i]['ans']:
        print("Right answer!!")
    else:
        print("Wrong answer!")
    print()
