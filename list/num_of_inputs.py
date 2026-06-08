scores=[]
n=int(input("enter the number of players: "))

for i in range(n):
    s=int(input("enter the scores :"))
    scores.append(s)

print(scores)
print(f"minimum score is : {min(scores)}")
print(f"maximum score is : {max(scores)}")
print(f"sum of all scores is : {sum(scores)}")