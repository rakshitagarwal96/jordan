def main(b):
    sum=0
    original=b
    while(b!=0):
        rem=b%10
        sum=sum+rem**3
        b=b/10
    if(sum==original):
        print("armstrong no.")
    else:
        print("not armstrong")
a=input("Enter a no.")
main(a)
