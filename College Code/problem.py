print("\n\t\t\t Missionaries & Cannibals problem")
print("Problem Rule: \n1. The boat can carry at most two people\n2. If cannibals num greater than missionaries then the cannibals would eat the missionaries\n3. The boat cannot cross the river by itself with no people on board")

leftM = 3
leftC = 3
rightM =0
rightC = 0
inM =0
inC =0
n =0
print(" Left  |  Right")
print("",leftM,"",leftC , " | " , rightM,"",rightC)
while(True):
    while(True):
        print(" M  C  |   M  C ")
        inM = int(input("Enter Missionaries: "))
        inC = int(input("Enter Cannibals: "))