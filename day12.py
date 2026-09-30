# n = int(input())
# a = 0
# b = 1 
# for i in range(n):
#     print(a)
#     a, b = b, a+b


# s = input()
# rev ='' 

# for i in range(len(s)-1, -1, -1):
#     rev += s[i]
# print(rev)


# n = 1324
# count = 0
# while n > 0:
#     n //= 10
#     count += 1
# print(count)

n=int(input())
rev=0
while n > 0:
    rev = rev*10 + n%10
    n //= 10
print(rev)