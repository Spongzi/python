# Python 自学

## 第一天

### 认识变量

```python
print(pow(3,0.5))
print(pow(3,0.5)*pow(3,0.5))
print(pow(3,0.5)*pow(3,0.5)==3)
print("pow(3,0.5)*pow(3,0.5)==3")

def add(x,y = 0,z=1):
    s=x-y+z
    return s
ad=add(y=100,x=200,z=300)
print(ad)

txt='haoABC'
for ch in "ABC":
    txt=txt.replace(ch,"*")
print(txt)


def f(n):
    s=1
    i=1
    while i<=n:
        s=s*i
        i=i=1
        return s
print(f(5))


for i in "AB":
    for k in range(2):
        print(i,end=" ")


for item in range(10):
    print(item)
else:
    print("For Over")


score = int(input("请输入一个0~100的整数:"))
if score>=85:
    print("nb")
if score<60:
    print("sb")
if (score>=60) and (score<85):
    print("还可以")
```

### 水仙花的练习

```python
i=100;r=0;s=0;t=0;

for i in range(1000):
    if i<100:
        continue
    r=i//100
    s=(i-r*100)//10
    t=i-r*100-s*10
    if i==(r**3+s**3+t**3):
        print("i= "+str(i))
    i+=1

#判断一个数字是不是水仙花
x=int(input("请输入一个三位数字:"))
x1=x//100         #求出百位数
x2=(x-x1*100)//10#求出十位数
x3=x-x1*100-x2*10#求出个位数
if x==x1**3+x2**3+x3**3:
    print("这个数字是水仙花")
else:
    print("不是水仙花")
```

第二天   字符串

r代表着使用的原始字符所有的\n或者\t都不可以使用

```python
print("hello \n world")
s = r'hello \n world'
print(s)
```

定义长字符串可以用"""XXXXXXXX""

eg:

```python
s = """
    《早发白帝城》
朝辞白帝彩云间，千里江陵一日还。
两岸猿声啼不住，轻舟已过万重山。
"""
print(s)
```

字符串可以通过int（）或者float（）实现转换成数字，转化成功返回数字否则引发异常。

```
a="AB"
print(int(a,16))#表示用16进制来转换
```

可以用str实现数字转化成字符串

```
a=str(123)
print(a)
print(type(a))
```

可以使用format方法进行格式化字符串,要想将表达式的计算结果插入到字符串中，需要使用占位符，对于占位符，使用一对大括号表示

```
i=32
s="i*i={}".format(i*i)
print(s)
s="{0}*{0}={1}".format(i,i*i)
print(s)
```

格式化控制符

```
money=5834.5678
name="Tony"
print("{0:s}年龄{1:d},工资是{2:g}元".format(name,20,money))#这里的g可以代表十进制整数型或者浮点型
```

字符串find方法可以用于查找子字符串，如果字符串中没有这个字符，那么返回值为-1

```
s_str="Hello World"
print(s_str.find("e"))
print(s_str.find('m'))
```

字符串替换，则可以使replace(old,new[,count])，count参数代表替换old子字符串个数，如果省略count则是全部替代

```
text = "AB CD EF GH HJ"
a=text.replace(' ','|',2)
print(a)
a=text.replace(' ','|')
print(a)
```

字符串的分割split()，split(sep=None,maxsplit=-1)表示sep子字符串分割字符串str，maxsplit最大分割次数，省略则代表不限制分割字数

```
a=text.split(" ")
print(a)
a=text.split(' ',maxsplit=2)
print(a)

s="hello world"
print(s[-5:])
```

::用于建立列表逆序

```
print("world"[::-1])
s='python'
print("{0:3}".format(s))
```

