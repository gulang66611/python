def f():
    while(True):
        try:
            n=int(input('请输入一个整数'))
            return n
        except ValueError as err:
            print('请重新输入！')
a=f()
b=f()
print(a,'+',b,'=',a+b)
print(a,'-',b,'=',a-b)
print(a,'*',b,'=',a*b)
print(a,'/',b,'=',int(a/b))