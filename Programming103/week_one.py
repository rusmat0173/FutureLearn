""" I joined this free course, and doing the exercise here:
    https://www.futurelearn.com/courses/programming-103-data/1/steps/629564

 """
try:
    with open("highscore.txt", "r") as f:
        print("The 10 highest scores previously were")
        highscore = f.read()
        print(highscore)
except:
    print("Creating a new highscore.txt file")
    f = open('highscore.txt', 'w')
    f.close()


scores = []
names = []
with open("highscore.txt", 'r') as file:
    for line in file:
        line = line.split(" "), # <= makes one string omto 2 strings in a list
        names.append(line[0])
        scores.append(int(line[1]))
print(names, scores)
