def giaithua(n):
    if n==1:
       return 1
    else:
       return (n*giaithua(n-1))
num=int(input("nhập số cần tính thứ 1 ! :"))
num1=int(input("nhập số cần tính thứ 2  ! :"))
num2=int(input("nhập số cần tính thứ 3 ! :"))
print("Giai thừa của ",num,",",num1,",",num2,"là",giaithua(num),',',giaithua(num1),',',giaithua(num2))
