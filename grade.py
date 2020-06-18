# Grade calculator based on valid scores by users
score = input("Enter Score: ")
flag = 0
try:
    valid_score = float(score)
    if 0.0<=valid_score<=1.0:
        flag = 1
except:
    print("Please enter a score between 0.0 and 1.0")
    quit()
if flag == 1:
    if valid_score >=0.9:
        print("A")
    elif valid_score>=0.8:
        print("B")
    elif valid_score>=0.7:
        print("C")
    elif valid_score>=0.6:
        print("D")
    else:
        print("F")
