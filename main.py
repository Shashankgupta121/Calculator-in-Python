FIRST = int(input("ENTER YOUR FIRST NUMBER HERE: "))
SECOND = int(input("ENTER YOUR SECOND NUMBER HERE: "))
TO_DO = (input("WHAT TO DO WITH THESE TWO NUMBERS: "))
if TO_DO=="+":
    print("THE ANSWER IS: " + str(FIRST + SECOND))
    print("CODE FINISED :)")
elif TO_DO=="add":
    print("THE ANSWER IS: " + str(FIRST + SECOND))
    print("CODE FINISED :)")
elif TO_DO == "-":
    print("THE ANSWER IS: " + str(FIRST - SECOND))
    print("CODE FINISED :)")
elif TO_DO == "cut":
    print("THE ANSWER IS: " + str(FIRST - SECOND))
    print("CODE FINISED :)")
elif TO_DO=="*":
    print("THE ANSWER IS: " + str(FIRST * SECOND))
    print("CODE FINISED :)")
elif TO_DO=="mul":
    print("THE ANSWER IS: " + str(FIRST * SECOND))
    print("CODE FINISED :)")
elif TO_DO=="/":
    print("THE ANSWER IS: " + str(FIRST / SECOND ))
    print("CODE FINISED :)")
elif TO_DO=="divide":
    print("THE ANSWER IS: " + str(FIRST / SECOND ))
    print("CODE FINISED :)")
else:
    print("SOMETHING IS WRONG")
