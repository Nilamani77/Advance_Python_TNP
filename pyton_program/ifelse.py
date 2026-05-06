# mark = float(input("Enter your mark: "))

# if mark >= 90:
#     print("Grade A")
# elif mark >= 80:
#     print("Grade B")
# elif mark >= 70:
#     print("Grade C")
# elif mark >= 60:
#     print("Grade D")
# else:
#     print("Fail")

# i=1
# while i<=100:
#     print(i)
#     i+=1
  
# i=100
# while i>0:
#     print(i)
#     i-=1
   
# n=int(input("Enter a number"))
# for k in range(1,n+1):
#     print(k*k)

# n=5
# for i in range(1,n+1):
#     print("*"*5)

# n=5
# for i in range(1,n+1):
#     print("*"*i)

# n=int(input("Enter a number:-"))
# for i in range(1,11):
#     print(n,"x",i,"=",n*i)

# n=5
# for i in range(n,0,-1):
#     print("*"*i)
 
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

# for i in range(1,6):
#     print(str(i)*i)

# for i in range(5,0,-1):
#     print(' ' * (5-i),end=' ')
#     for j in range(i):
#         print('*',end=" ")
#     print()
   

for i in range(1,6):
    print(' ' * (5-i),end=' ')
    for j in range(i):
        print("*",end=" ")
    print()
