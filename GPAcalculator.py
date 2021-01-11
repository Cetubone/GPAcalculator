def gTog(x):
    if x < 60 :
        return 0
    else:
        return (x-50)/10

print('\n','#'*40,sep='')
print('\n您好，欢迎使用本小程序\n请依次输入您各个科目的成绩，以这样的格式：\n\n成绩,学分\n\n请用英文逗号分隔\n用all结束输入得到GPA\n用stop退出\n')
print('#'*40,'\n')
while 1 :
    a=b=0
    while 1 :
        x=input()
        if x.isalpha() :
            if x=='stop':
                exit()
            if x=='all':
                break
        else:
            x=eval(x)
            a += gTog(x[0])*x[1]
            b += x[1]
    print('您的GPA为：{:.2f}'.format(a/b))

