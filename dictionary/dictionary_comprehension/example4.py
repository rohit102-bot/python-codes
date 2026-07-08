n=int(input("enter how many playes ?"))
players={input("enter name:"):input("enter score:") for i in range(n)}
players1={name:score for name,score in players.items()}
print(players1)