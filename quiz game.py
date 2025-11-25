questions=("What is the biggest fish in the ocean?",
           "whats the sum of 40+60?",
           "What is the first element of periodic table?",
           "Whats the number of currency of bangladesh?")
options=(("A.salmon","B.Blue Whale","C.Sword fish","D.Tuna"),
         ("A.30","B.40","C.50","D.80"),
         ("A.H","B.Na","C.F","D.O"),
         ("A.Rupee","B.Taka","C.Dollar","D.yen"))
A=["B","D","A","B"]
k=[]
score=0
for i in range(len(questions)):
    print(questions[i])
    for j in range(len(options[i])):
        print(options[i][j])
    print("Answer:")
    answer=input().upper()
    k.append(answer)
    if k[i]==A[i]:
        print("CORRECT!")
        score+=1
    else:
        print("Wrong!!!")
        print(f"Right answer is {A[i]}")
print("---Result---")
print(f"Total score:{score}")




