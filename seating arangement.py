
a=[[6,7,18,19,30,31,42,43,54,55,66,67,78,79,90,91,102,103],
   [5,8,17,20,29,32,41,44,53,56,65,68,77,80,89,92,101,104],
   [4,9,16,21,28,33,40,45,52,57,64,69,76,81,88,93,100,105],
   [3,10,15,22,27,34,39,46,51,58,63,70,75,82,87,94,99,106],
   [2,11,14,23,26,35,38,47,50,59,62,71,74,83,86,95,98,107],
   [1,12,13,24,25,36,37,48,49,60,61,72,73,84,85,96,97,108]]

for j in range(int(input())):
    n=int(input())
    r= n%12
    if r==0:
        print(n-11, end=" ")
        print("WS")
    elif r==1:
        print(n+11, end=" ")
        print("WS")
    if r==2:
        print(n+9, end=" ")
        print("MS")
    elif r==11:
        print(n-9, end=" ")
        print("MS")
    if r==3:
        print(n+7, end=" ")
        print("AS")
    elif r==10:
        print(n-7, end=" ")
        print("AS")
    if r==4:
        print(n+5, end=" ")
        print("AS")
    elif r==9:
        print(n-5, end=" ")
        print("AS")
    if r==5:
        print(n+3, end=" ")
        print("MS")
    elif r==8:
        print(n-3, end=" ")
        print("MS")
    if r==6:
        print(n+1, end=" ")
        print("WS")
    elif r==7:
        print(n-1, end=" ")
        print("WS")



        










