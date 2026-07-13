score = 0
questions =[
    {
        "question": "1. What command creates a file?",
        "options":["A. python3", "B. rm", "C. createfile", "D. touch"],
        "answer": "D",
    },

    {
        "question": "2. On which day did we create our group chat this year?",
        "options": ["A. DAY 1", "B. DAY 7", "C. DAY 5", "D. DAY 2"],
        "answer": "D"
    },

    {
        "question": "3. A tower of pizza suddenly appears next to an Italian man's pizzeria, and a crazy pizza face threatens his business. What should the Italian man do?",
        "options": ["A. GO STOP HIM! or Call his gremlin rival to help out", "B. nah let him do it, he's already suffering from enough debt", "C. sleep it", "D. That's it summon the nukes"],
        "answer": "A",
        "correct_message": "That's Correct!\n",
        "incorrect_message": "That's Incorrect... maybe you should play Pizza Tower. Anyways, The correct answer was A!\n"
    },
    {
        "question": "4. How many times has Bowser canonically kidnapped Peach within the entire Mario franchise?",
        "options": ["A. IT'S OVER NINE THOUSAAAAAAAND!", "B. Like over 25 times at this point", "C. The ONE time. Super Mario Bros. 1 is the only canon game.", "D. Around 15-20"],
        "answer": "B"
    },
]
print("====Welcome to my quiz of awesomenes====\n")

for q in questions:
    print(q["question"])

    for option in q["options"]:
        print(option)

    response = input("Enter your Answer with the Keyboard (A,B,C or D)!").strip().upper()
    if response == q["answer"]:
        print("That's Correct!\n")
        score +=1
    else:
        print(f"That's Incorrect... the correct answer to this question was {q['answer']}!\n")
    
print("="*40)
print(f"This is your total score: {score}/{len(questions)}\n")
print(f"Play again for a better score!\n")

print(f"Thanks for Playingß!\n")