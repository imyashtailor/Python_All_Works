#pattern programming 
# 1.
# *****
# *****
# *****
# *****
# *****

# lines = 5

# for i in range(lines):
#     for j in range(lines):
#         print("*",end="")
#     print()

2.
# *
# **
# ***
# ****
# *****

# lines = 5
# for i in range(lines):
#     for j in range(i+1):
#         print("*",end="")
#     print()

3.
# *****
# ****
# ***
# **
# *

# lines = 5
# for i in range(lines):
#     for j in range(lines-i):
#         print("*",end="")
#     print()

4.
#     *
#    **
#   ***
#  ****
# *****

# lines = 5
# for i in range(lines):
#     for k in range(lines-(i+1)):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end="")
#     print()

5.
# *****
#  ****
#   ***
#    **
#     *

# lines = 5
# for i in range(lines):
#     for k in range(i):
#         print(" ",end="")
#     for j in range(lines-i):
#         print("*",end="")
#     print()

6.
#         *
#       *   *
#     *   *   *
#   *   *   *   *

lines = 5

# for i in range(lines):
#     for k in range(lines-(i+1)):
#         print(" ",end="")
#     for j in range(i+1):
#         print("* ",end="")
#     print()

7.
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * * 

# lines = 5
# for i in range(lines):
#     for k in range(lines-(i+1)):
#         print(" ",end="")
#     for j in range((i*2)+1):
#         print("*",end="")
#     print()

8.
    #     *
    #   *   *
    # *   *   *
    #   *   *
    #     *

lines = 6
for i in range(lines):
    for k in range(lines-(i+1)):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()

for p in range(lines):
    for m in range(p):
        print(" ",end="")
    for r in range(lines-p):
        print("* ",end="")
    print()




  