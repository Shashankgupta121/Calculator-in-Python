FIRST = int(input("ENTER YOUR FIRST NUMBER HERE: "))
SECOND = int(input("ENTER YOUR SECOND NUMBER HERE: "))
TO_DO = (input("WHAT TO DO WITH THESE TWO NUMBERS: "))
if TO_DO=="+":
    print(FIRST + SECOND)
elif TO_DO=="-":
    print(FIRST - SECOND)
elif TO_DO=="*":
    print(FIRST * SECOND)
elif TO_DO=="/":
    print(FIRST / SECOND )
else:
    print("SOMETHING IS WRONG")