#program to generate a binary number

num = int(input("enter the decimal number"))
res = ''
i =0
while (num>0):
    t = num%2
    res = res+ str(t)
    num =num//2
    i=i+1
    print("res ",res, "num",num)

#statement to convert a string to its reverse
print(res[::-1])

#array sorting
arr = [1,2,4,5,8,2,9,4,0]

arr.sort(reverse=True)


print(arr)
arr.append(19)
print(arr)

#performing recursion

#factorial
def fact_n(num):
    if(num ==1):
        return 1
    return (num * fact_n(num-1))

factn = input("enter fact number newline")
print(fact_n(int(factn)))


#left rotation
str1 ="abcdefrte"
str2 = str1[:3]
str3 = str1[3:]
print(str3+str2)