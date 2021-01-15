def gTog(x):
    if x < 60 :
        return 0
    else:
        return (x-50)/10

print('\n','#'*40,'\n您好，欢迎使用本小程序\n请依次输入您各个科目的成绩，以这样的格式：\n\nΦ 成绩,学分\n\n请用英文逗号分隔\n用all结束输入得到GPA\n用stop退出\n','#'*40,'\n',sep='')
while 1 :
    a=b=0
    while 1 :
        x=input('Φ ')
        if x.isalpha() or x == '' or str(type(eval(x)))!="<class 'tuple'>":
            if x=='stop':
                exit()
            if x=='all':
                break
            print('你在输些什么乱七八糟东西,重新输')
        else:
            x=eval(x)
            a += gTog(x[0])*x[1]
            b += x[1]
    if b == 0:
        print('你有成绩才能算GPA啊，啥也不输还算个pp')
    else:print('您的GPA为：{:.2f}'.format(a/b))
