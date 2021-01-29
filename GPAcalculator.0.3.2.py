def gTog(x):
    if x < 60 : 
        return 0
    else: 
        return (x-50)/10
#将成绩分数转化成绩点


def printScore(x):
    print('═'*45)
    for k,v in x.items():
        if k!=0:
            print('{:^30}'.format(' 序号:{:<5}分数:{:<5}学分:{:<3}'.format(k,v[0],v[1])))
    print('═'*45)
#打印储存在字典中的成绩数据{序号：（分数，学分）}


def idtf(x):

    x=str(x)
    x=x.replace('，',',')
    n=x.find(',')

    noL="?!;:'\"*\\()%#@~/-+。？！～、：＃；％＊—…＆·￥（）‘’“”[]｛｝[]"
    for let in noL:
        if let in x:
            return 'none'
    
    if n==0 or n==(len(x)-1) :
        return 'none'

    if x.isdigit():
        key=0
        for num in x[:]:
            if num=='0':
                key+=1
            else:break
        return eval(x[key:])

    if x.isalpha():
        if x=='exit' or x=='gpa' or x=='GPA' or x=='list' or x=='edit' or x=='done' or x=='clear':return x
        else:return 'none'
    elif x=='':
        return 'none'

    if n<1 or x.count(',')!=1:
        return 'none'
    else:
        if x[:n].count('.')>1 or x[n:].count('.')>1:return 'none'

        if x[0]=='.':
            x='0'+x
        if x[n+1]=='.':
            x=x[:n+1]+'0'+x[n+1:]

        for num in x:
            if num.isalpha():return 'none'
        key=0
        if n!=1:
            for num in x[:n]:
                if num=='0':
                    key+=1
                elif num=='.':
                    key-=1;break
                else:
                    break
            x=x[key:]
        key=n+1
        for num in x[n+1:]:
            if num=='0':
                key+=1
            elif num=='.':
                key-=1;break
            else:
                break
        x=x[:n+1]+x[key:]
        return eval(x)
#对用户输入内容进行处理
#返回命令字符串，返回整数，返回元组，其他返回'none'
    

print('━'*50,'\n',
      '   您好，欢迎使用本小程序\n',
      '   请以这样的格式输入成绩和学分数据：\n\n',
      '   Φ 成绩,学分\n\n',
      '   指令：\n',
      '   GPA ----计算GPA\n',
      '   exit----退出程序\n',
      '   list----查看已输入数据\n',
      '   edit----进入修改模式修改已输入数据\n',
      '   done----完成并退出修改\n\n',
      '   #如果出现表格混乱请将字体调至黑体\n',
      '━'*50,'\n',sep='',end='')

dir_info={};Nob=1;a=b=0
#dir_info储存成绩数据，Nob储存输入数据，a为GPA计算式分子，b为分母
#GPA=∑(绩点*学分)/∑(学分)

while 1:
    
    order=idtf(input('Φ '))

    if str(type(order))=="<class 'tuple'>":
        dir_info[Nob]=order
        Nob+=1
#如果用户输入元组，则视为成绩数据存入字典

    if order=='exit': exit()#输入exit推出程序
    elif order=='none' or str(type(order))=="<class 'int'>":
        print('Δ----请正确输入数据----Δ')

    elif order=='gpa' or order=='GPA':
        if Nob==1:print('Δ----请先输入数据----Δ')
        else:
            for nob in range(1,Nob):
                a+=gTog(dir_info[nob][0])*dir_info[nob][1]
                b+=dir_info[nob][1]
            print('┄'*45,
                  '\n您的GPA为：{:.2f}\n'.format(a/b),
                  '┄'*45,'\n',
                  sep='',end='')
#输入gpa或GPA，用字典中的数据计算GPA并输出

    elif order=='list':
        if Nob==1:print('Δ----请先输入数据----Δ')
        else:
            printScore(dir_info)
#打印字典中的数据
            
    elif order=='clear':
        dir_info={};Nob=1;a=b=0
        print('数据已清空√')
#清空字典数据

    elif order=='edit':
        if Nob==1:print('Δ----请先输入数据----Δ')
        else:
            printScore(dir_info)
            while 1:
                print('请输入需修改的数据序号或指令：')
                order=idtf(input('δ '))
                if str(type(order))=="<class 'int'>" and 0<order<Nob:
                    data=idtf(input('\n请输入新数据\n({})δ '.format(order)))
                    if str(type(data))=="<class 'tuple'>":
                        dir_info[order]=data
                        print('\n修改成功√')
                        printScore(dir_info)
                    elif data=='exit':exit()
                    else:print('Δ----请正确输入数据----Δ')
                elif order=='done':break
                elif order=='exit':exit()
                else:print('Δ----请正确输入数据----Δ')
#edit进入修改模式，done推出修改模式，
