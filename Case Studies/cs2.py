# ''' 
#     The German mathematician Gottfried Leibniz developed the following method to approximate the value of n:
#     n/4 = 1 – 1/3 + 1/5 – 1/7 + ….
#     Write a program that allows the user to specify the number of iterations used in this approximation and 
#     that displays the resulting value. 
# '''

# n = int(input("Enter number of iteration: "))

# pi = 0
# deno = 1

# for i in range(n):
#     if i % 2 == 0:
#         pi += 1 / deno
#     else:
#         pi -= 1 / deno
#     deno += 2

# print("%0.2f" % pi)