scores = []
while True :
    score = input("Enter a score (or type 'done' to exit ): ")
    if score.lower() == "done" :
        break   
    scores.append(int(score))
avg = sum(scores) / len(scores)
print(f"The average score is {avg}")

