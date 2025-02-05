def print_list(list2,n):
    for i in range(n):
        for j in range(n):
            print(list2[i][j],end=" ")
        print()
#-------------------------------------------------------------------------------------------------------------
def search(list2,no,n):
    for i in range(n):
        for j in range(n):
            if no==list2[i][j]:
                list2[i][j]="*"
#-------------------------------------------------------------------------------------------------------------
def bingo(list1,n):
    for i in range(n):
        for j in range(n):
            count=0
            if list1[0][0]=="*" and list1[1][1]=="*" and  list1[2][2]=="*" and list1[3][3]=="*" and list1[4][4]=="*":
                count+=1
            if list1[0][4]=="*" and list1[1][3]=="*" and  list1[2][2]=="*" and list1[3][1]=="*" and list1[4][0]=="*":
                count+=1
            if list1[0][0]=="*" and list1[0][1]=="*" and  list1[0][2]=="*" and list1[0][3]=="*" and list1[0][4]=="*":
                count+=1
            if list1[1][0]=="*" and list1[1][1]=="*" and  list1[1][2]=="*" and list1[1][3]=="*" and list1[1][4]=="*":
                count+=1
            if list1[2][0]=="*" and list1[2][1]=="*" and  list1[2][2]=="*" and list1[2][3]=="*" and list1[2][4]=="*":
                count+=1
            if list1[3][0]=="*" and list1[3][1]=="*" and  list1[3][2]=="*" and list1[3][3]=="*" and list1[3][4]=="*":
                count+=1
            if list1[4][0]=="*" and list1[4][1]=="*" and  list1[4][2]=="*" and list1[4][3]=="*" and list1[4][4]=="*":
                count+=1
            if list1[0][0]=="*" and list1[1][0]=="*" and  list1[2][0]=="*" and list1[3][3]=="*" and list1[4][0]=="*":
                count+=1
            if list1[0][1]=="*" and list1[1][1]=="*" and  list1[2][1]=="*" and list1[3][1]=="*" and list1[4][1]=="*":
                count+=1
            if list1[0][2]=="*" and list1[1][2]=="*" and  list1[2][2]=="*" and list1[3][2]=="*" and list1[4][2]=="*":
                count+=1
            if list1[0][3]=="*" and list1[1][3]=="*" and  list1[2][3]=="*" and list1[3][3]=="*" and list1[4][3]=="*":
                count+=1
            if list1[0][4]=="*" and list1[1][4]=="*" and  list1[2][4]=="*" and list1[3][4]=="*" and list1[4][4]=="*":
                count+=1
    
            if count==n: 
                return "BINGO"
     
    print_list(list1,n)
#------------------------------------------------------------------------------------------------------------
import random
print("enter number ")
n=int(input())
list1=[]
list2=[]
i=0
while i<25:
    num=random.randint(1,25)
    if num<=25:
        if num not in list1:
            list1.append(num)
            i+=1
        else:
            continue
    else:
        continue
start=0
stop=5
while stop<=25:
    l1=list1[start:stop]
    list2.append(l1)
    start=stop 
    stop+=5
print_list(list2,n)
count=0
for i in range(n**2):
    no=int(input("enter number"))
    search(list2,no,n)
    ult=bingo(list2,n)
    if ult=="BINGO":
        print("bingo you win")
        break




