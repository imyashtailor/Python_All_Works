1.
# 1
# 12
# 123
# 1234
# 12345

# lines = 5
# for i in range(lines):
#     for j in range(i+1):
#         print(j+1,end="")
#     print()

2.
# 1
# 23
# 456
# 78910

# lines = 4
# n=1
# for i in range(lines):
#     for j in range(i+1):
#         print(n,end="")
#         n+=1
#     print()

3.
# 5
# 45
# 345
# 2345
# 12345

# lines=5
# for i in range(lines,0,-1):
#     for j in range(lines-i+1):
#         print(i+j,end="")
#     print()

6.
# 0
# 10
# 010
# 1010
# 01010

lines = 5
for i in range(lines):
    for j in range(i+1):
        print((i+j)%2,end="")
    print()





