import random  
print("\t\t    Welcome to the Magic-8-Ball Mini Program\n\tIn this game, you'll ask the Magic 8-Ball a yes-or-no question, \nand I'll provide a whimsical or mysterious response, just like the classic toy. \n\t\t\tGo ahead and ask your question!")
eng_answers=["Yes, absolutely!", "No way", "Outlook is hazy", "Ask again later", 'Signs point to yes',"Most likely","Very doubtful","Ask again later","Without a doubt","My sources say no"]
fil_answers=["Omsimmmm", "Aba malay natin", "Pwede?", "Hindi", "Oo naman", "Imposible", "Huwag ka na umasa!", "Siguro??", "Mukhang malabo"]
ques_type= input("Choose if your want to ask a yes-or-no Tagalog or English question.\n[Type Filipino or English]\n>> ").capitalize()


if ques_type=="English":
    question= input("Type your question here: ")
    print(random.choice(eng_answers))
elif ques_type=="Filipino":
    question= input("Type your question here: ")
    print(random.choice(fil_answers))
else:
    print("Just enter Tagalog or English lol")
