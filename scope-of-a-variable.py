# """Local Scope
# Value can be accessed inside the function only """
# # """
# def fun ():
#     X=7; y=8; z=9
#     print(X+y)     #15
# fun()
#     # """
# """Global Scope of a Variable ,can be accessed by anyone """
# #"""
# a=2
# def bm():
#     a=4
#     b=3;c=5
#     print(a)    #4
#     print(b)    #3
# print(a)     #2
# bm()
# print(a)     #2
#"""
# """global is the keyword, which is need to be specified if we want to use
# the local variable as global variable."""
# #"""
# c=4
# def fun1():
#     a=3
#     global c,b
#     b=8
#     c=9
#     print(b)   #4
# print(c)       #8
# fun1()
# print(c)     #9
# print(b)     #8
# print(c)     #9
# #"""   
# """count the length of a string without using built-in function"""
# #"""
# def fn(st):
#     c=0
#     for i in st:
#         c+=1
#     return c     
# print(fn('python'))   #6
# #"""
# """ A guy having multiple names"""
# #"""
# def sc():
#     school='John'
#     print(f'Name in school is {school}')   #Name in school is John
# def cl():
#     college='max'
#     print(f'Name in college is {college}')    #Name in college is max
#     wk()
# def wk():
#     work='peter'
#     print(f' Name at work location is {work}')     #Name at work location is peter
#     sc()
# cl()
# #"""
