a=int(input("Enter first subject mark:-"))
b=int(input("Enter second subject mark:-"))
c=int(input("Enter third subject mark:-"))

sum=a+b+c
avg_score=sum/3

if avg_score>=90:
    grade='A'
elif avg_score>=80:
    grade='B'
elif avg_score>=70:
    grade='C'
elif avg_score>=60:
    grade='D'
else:
    grade='F'

print(f"\nAverage score:{avg_score}")
print(f"Final Grade:{grade}")