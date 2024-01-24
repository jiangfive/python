# python

## 计算机相关知识

### 计算机硬件组成

Cpu：控制器：控制计算机

​	  	 运算器：数学运算和逻辑运算

​		   存储器：负责数据的存储

​		    内存：基于电工作

​			外存：基于磁工作

​			输入设备：

​			输出设备： 

### 操作系统

应用程序：爱奇艺 typora

操作系统：控制程序 macos -控制底层硬件

硬件是死的 计算机硬件的运行都受软件控制

软件：

​			1.应用软件：应用程序相关逻辑

​			2.系统软件 ：控制底层硬件

### 计算机系统三层结构

应用程序⟺操作系统⟺计算机硬件 

文件就是操作系统 提供给上层应用控制硬盘的功能

平台：操作系统➕硬件

服务器只是一个计算机

python很适合跨平台性 

### 扫盲 

1. cpu详解

   - cpu的分类和指令集

   - X86-64

      x86指的是cpu型号 64为cpu一次性能从取出的位数

     cpu具有向下兼容性

   - 内核态和用户态

   - 多线程和多核芯片

2. 存储器详解

   内存：RAM  ROM:BIOS 最基本的最简单的操作系统

   cmos：存取速度慢 断电数据丢失 耗电量低 

3. 硬盘详解

4. 操作系统的启动流程：BIOS basic input output system

   裸机：cpu

   ​			rom：充当内存 存放bios系统

   ​			cmos：充当硬盘

   装了其他操作系统后：

   1. 计算机加电
   2. bios 开始运行 检测硬件：cpu、内存、硬盘等
   3. bios读取cmos存储器中的参数，选择启动设备
   4. 从启动设备上读取第一个扇区的内容 （MBR主引导记录512字节，前446为引导信息，后64为分区信息，最后后个为标志位）
   5. 根据分区信息读入bootloader启动转载模块，启动操作系统
   6. 然后操作系统询问bios，以获得配置信息，对于每种设备，系统就会检查其设备驱动程序是否存在，如果没有，系统就会要求用户按照设备驱动程序。一旦有了全部的设备驱动程序，操作系统就会将他们调入内核

5. 密码破解和安全：操作系统的密码 


## python study

###  what is python

python 应用领域：web开发 网络编程 人工智能 云计算开发 爬虫开发 自动化运维、测试 科学运算 游戏开发 桌面开发

### pycharm快捷键

ctrl+？ 快速注释

pep8规范 可以格式化代码来避免 command  option l

shift 回车键 快速换行

### python入门 

一个python应用程序的运行步骤：python3 c:\a\b\1.py

1. 先启动python解释器
2. 解释器会发送系统调用 把1.py内容从硬盘调入内存 此时1.py内容全部为普通字符 没有任何语法意义
3. 解释器开始解释执行刚读入内存的1.py代码 开始识别python语法

python对文件后缀名没有影响 即使不是py也可以运行

环境安装：python3 -m pip install matplotlib

#### 编程语言 

- 机器语言—二进制 计算机能识别的文字 跨平台性差
- 汇编语言—用英文标签代表二进制
- 高级语言
  - 编译型：执行效率高 开发效率低 跨平台性低 不给源代码
  - 解释型：执行效率低 开发效率高 跨平台性高 给用户源代码
  - 混合型：java

#### 内存管理

- 栈区：存放变量名与内存地址的映射关系

- 堆区：存放变量值

  赋值、传参传递的都是栈区数据，都是引用传递

![内存管理](/Users/jiang5/Desktop/5/python/python picture/内存区.png)

若堆区被回收 则栈区也被回收了

##### 垃圾回收机制

垃圾回收机制:垃圾指的是变量值被绑定的变量名值为0时，无法被查找时是垃圾

引用计数机制;有缺陷的 因为容易导致容器之间进行循环引用 从而导致计数只留下间接引用但却无法取到值了即内存泄漏

![引用计数](/Users/jiang5/Desktop/5/python/python picture/引用计数.png)

```python
l1=[1,]
l2=[2,]
l1.append(l2)
l1.append(l1)#l1与l2之间发生循环引用
del l1#l1的直接引用减少 但还有l2对l1的直接引用
del l2#此时无法再取到值了 但计数并没有为0 
```

```python
x=10 #直接引用
l=["a",x] #间接引用 也算一次引用数 
```

##### 标记-清除

标记-清除：在内存不够用时python解释器自动启动：将整个程序停止，扫描堆区中是否有没被栈区直接引用的内容，若有则标记并清除

##### 分代回收

分代回收：基于引用计数机制，每次回收内存，都需要把所有对象的引用计数都遍历一遍，于是引入了分代回收 ：给回收内容分权重，再根据权重分频率检查引用计数值

##### 深浅copy

是为了让两个列表独立开

浅copy：把原列表的第一层内存地址不加区分完全原封不动copy给新列表

```python
lis1=[1,2,[3,4]]
lis2=lis1.copy()#列表浅拷贝
print(lis1,lis2)#copy后列表值相同
print(id(lis1[0]),id(lis1[1]),id(lis1[2]))
print(id(lis2[0]),id(lis2[1]),id(lis2[2]))#两个列表第一层内存地址相同
lis1[0]=5
print(lis1[0],lis2[0])#lis1不可变类型改变 但lis2没有变
lis1[2][0]=6
print(lis1[2][0],lis2[2][0])#可变类型变 lis2也跟着变 即没有两个列表并没有全部分开
```

深copy：能够区分开容器内可变类型和不可变类型的copy

 ```python
 import copy
 lis1=[1,2,[3,[4,5]]]
 lis3=copy.deepcopy(lis1)
 print(id(lis1[0]),id(lis1[1]),id(lis1[2]),id(lis1[2][1]))
 print(id(lis2[0]),id(lis2[1]),id(lis2[2]),id(lis2[2][1]))#不可变类型内存地址相同 可变类型内存地址不同 是所有嵌套内的可变类型容器内存地址都不同
 ```



### 变量与基本数据类型 

#### 转义

```python
a=r"jiangwu/t" //可以使其无法转义 同理多行字符串可以用r“”“ ”“”
```



#### 注释

多行注释：三引号

```python
'''
注释
'''
"""
注释
"""
```

单行注释：#

#### 变量

 ```python
 #变量是记录事物的变化
 #先定义后引用
 name = 'zhangyueyu'#定义 python中的变量定义与c不同 python是先给值赋予空间再让变量名指向变量值的内存地址就像c里面的引用一样 而c是给变量名赋予空间
 print(name)#引用
 a = 10
 b = a
 c = 10#引用计数的增加 此时指的是z指向x记录的地址
 a = 5#此时a记录的是另一片地址即5的地址
 print(a, b, c)
 print(id(a))#a的地址为4393755968
 print(id(b))#b的地址为4393756128
 print(id(c))#c的地址为4393756128
 del a#引用计数的减少 解除的是a与10的绑定
 name #这种会报错 因为变量名必须关联变量值
 'name'#这种不会报错
 #只要赋值 就会开创内存空间
 ```

1. 变量名：

   - 驼峰法：NameOfJiangwu name_of_jiangwu

   - 纯小写加下划线: name_of_jiangwu

2. 变量值：

   id：反映的是变量值的内存地址 print(id(变量名))

   type：变量值类型 print(type(变量名))   

   - 值相等的情况可能id不同
   - id相同的情况下，值一定相同

   is与==： 

   - is比较的是两个值的身份id是否相等

   - ==比较的是两个值它们的值是否相等

     ```python
     x="jiang"
     y="jiang"
     print(id(x), id(y))
     x is y #true
     x="jiang:"
     y="jiang:"
     print(id(x), id(y))
     x is y#false
     #出现这种情况是因为python解释器小整数池([-5,256]和一些字符串，但pycharm可能还有扩充)的原因 把常见的放一起了 避免过多的io操作
     x=10
     x=100#此时内存先开辟一片空间给100，再将x引用至100 即x与10的关系解除重新指向100
     ```

3. 常量 

   python中没有常量的概念 但在程序的开发中会涉及常量概念

   约定让全大写的变量为常量

#### 基本数据类型

1. ##### 整型 int

   ```python
   int("101010") #可以将纯数字的字符串转成整型
   ```

2. ##### 浮点型 float

   ```python
   float("3.12") #可以转成浮点型
   ```

   整型和浮点型可以互相运算 其他类型只能自类型运算

3. ##### 字符串类型 str

   字符串：用引号包含   引号：‘ ’、“ ”、‘’‘ ’‘’、“”“ ”“” 三引号可以多行字符串

   字符串的嵌套：外层用单则内层双 反之亦然 否则引号会被解释器错误匹配

   内置方法：

   ```python
   x="姜伍"+"张月瑜" #字符串相加（不推荐使用 因为str相加效率低）  
   y=('='*5)#字符串相乘 结果为=====
   str({"jiangwu":"zhangyueyu"})#可以将任意类型转换成字符串
   str_="jiangwu"
   #只能索引读 不能改字符串内子值
   print(str_[0]) #正取
   print(str_[-1]) #反取   
   
   str_2=str_1[0:5] #切片 结果仍是字符串 顾头不顾尾
   str_3=str_1[0:5:1]#1为切片
   str_4=str_1[5:0:-1]#反向步长 只能正走正步长 反走反步长
   str_5=str_1[:]#开头结尾可以不写参数
   
   msg="	jiangwu	"
   res=msg.strip() #去掉左右两边的字符 若不加参数 则去掉的空格 该函数只有一个参数 lstrip()只去掉左边，rstrip()只去掉右边
   string=".;'',jiangwu,,',[]'"
   string1=string.strip(".[];'',")#这样也能去掉
   
   #切分split：把一个字符串按照某种分隔符进行切分，得到的是一个列表 rsplit 是从右往左切分
   msg="jiang wu"
   res=msg.split() #该函数两个参数 不写参数 默认全部切分且切分标记为空格
   msg1="j.i.a.n.g.w.u"
   res1=msg1.split('.',2)#切分标记为','且从头开始只切分两个 输出为[j,i,a.n.g.w.u]
   
   #lower()、upper() 将字符串全部大写或小写 无参数
   msg='jiangWU'
   msg1=msg.lower()
   msg1=msg.upper()
   
   #startswith()、endswith()
   a='jiangwu is zhangyueyu boyfriend'
   print(a.startswith('jiang')) #参数数量为1 且不可忽略
   
   #str.join()：按照某个分隔符号把全是字符串的列表拼接成一个字符串  
   l=['j','i','a','n','g']
   print(''.join(l))
    
   #str.replace() 三个参数 一新一旧一规定几个旧的 默认数量为全改
   msg="jiangwu is zhangyueyu's lover，lover，lover"
   print(msg.replace("lover",'boyfriend',2)) #改掉2个lover 输出为jiangwu is zhangyueyu's boyfriend，boyfriend，lover
   
   #str.isdigit() 判断字符串是否都由数字组成 无参数
   print("123".isdigit())
   print("12.3".isdigit())
   
   #find、rfind、index、rindex、zfill、count
   a='jiangwu is zhangyueyu boyfriend'
   print(a.find("an"))#返回子字符串在字符串中的起始索引
   print(a.index("an"))#与find相同
   print(a.find("xxx"))#找不到返回-1
   print(a.index("xxx"))#找不到程序出错
   #str.count() #字符出现的次数
   msg="hello world"
   print(msg.count("o"))
   
   #center、ljust、rjust、zfill 
   #str.zfill() 无参数
   a='jiangwu'
   print(a.zfill(10)) #用0来补全不到十的长度 输出为000jiangwu 默认右对齐
   print("jiangwu".center(10,'*'))#输出为*jiangwu**
   print("jiangwu".rjust(10,'*'))#输出为***jiangwu 右对齐填充
   print("jiangwu".ljust(10,'*'))#左对齐填充 输出为jiangwu***
   #以上三个都是两个参数
   
   #expandtabs 设置制表符长度 一个参数
   msg='hello\tworld'
   print(msg.expandtabs(10))
   
   #captalize、swapcase、title
   print("hello world".swapcase())#大小写转换 HELLO WORLD
   print("hello world".capitalize())#字符串首字母大写 Hello world
   print("hello world".title())#字符串每个单词大写 Hello World
   
   #is系列
   print('abc'.islower())  # 是否是全小写
   print('ABC'.isupper())  # 是否是全大写
   print('Abc D'.istitle())  # 是否每个单词都大写
   print('Abc1'.isalnum())  # 是否全是字母和数字组成
   print('AbcD'.isalpha())  # 是否全是字母
   print('   '.isspace())  # 是否全是空格
   print('print'.isidentifier())  # 是否是标识符或者变量名命名正确
   #...
   
   #is 数字系列
   num1=b'4' #byte
   num2=u'4' #unicode python3中无需加u默认是unicode
   num3='四' #中文数字
   num4='Ⅳ' #罗马数字
   print(num1.isdigit()) #true
   print(num2.isdigit()) #true
   print(num3.isdigit()) #false
   print(num4.isdigit()) #false
   
   print(num1.isnumeric()) #程序错误
   print(num2.isnumeric()) #true
   print(num3.isnumeric()) #true
   print(num4.isnumeric()) #true
   
   print(num1.isdecimal()) #decimal意思是十进制 程序出错
   print(num2.isdecimal()) #true
   print(num3.isdecimal()) #false
   print(num4.isdecimal()) #false
   
   #字符串可以按照asci码大小 
   ```

4. ##### 列表类型 list

   List是有序的

   ```python
   a=10
   lis=["张月瑜",a]#lis[0]存的是"张月瑜"的内存地址 lis[1]存的是10的内存地址
   lover="张月瑜"
   lis=['姜伍',lover]
   lover="臭傻逼"
   print(lover,lis)#输出为 臭傻逼 姜伍 张月瑜 即不改变列表的内容
   ```

   作用：记录多个值，并且可以按照索引存取指定位置的值 索引反映的是顺序、位置，对值没有描述性的功能

   索引值对应值：索引反映的是位置，顺序索引从0开始，0代表第一个位置,可以倒着取 最后一个是-1

   定义：[1,2,3,...,["a","b"]]

   类型转换：

   ```python
   list() #凡是能够被for循环遍历的类型都可以当作参数传给list()：字符串、列表、字典 元组
   dic={'k1':1,'k2':2}
   a=list(dic)
   print(a)  #list化列表输出的是key
   ```

   内置方法：

   ```python
   #列表也可以比大小 原理和字符串一样 但是对应位置的元素必须是同种类型
   #索引：可读可写
   lis=[0,1,2]
   lis[0]=3 #索引存在 可读可改
   lis[3]=4 #索引不存在 程序报错
   
   #追加 append 参数为一
   lis=[0,1,2]
   lis.append(4) 
   
   #插入值 insert
   lis=[0,1,2]
   lis.insert(-1,3) #输出为[0, 1, 3, 2]
   lis.insert(0,3) #输出为[3, 0, 1, 2]
   lis.insert(10,3) #当参数大于或等于列表最大索引值时 和append一样 
   
   #extend 可以直接将另一个列表里的数据一个一个的添加到列表尾部 
   lis=[0,1,2]
   lis1=[3,4,5]
   for i in lis1:
       lis.append(i)
   print(lis) #以上代码可以用extend实现
   lis.extend(lis1)
   print(lis) 
   lis=[0,1,2]
   dic={'k':1,'k2':2}
   lis.extend(dic)
   print(lis) #输出为[0, 1, 2, 'k','k2']  字典进去话则是key进去
   
   #删除
   #方式一：del 通用删除方式，只是单纯删除，没有返回值
   #方式二：l.pop() 根据索引删除，会返回删除的值 若列表为空或索引超出则程序错误
   l=[1,2,3]
   del l[1]
   print(l)
   l.pop() #不指定索引删除最后一个元素
   l1=l.pop(0)
   print(l1)
   #方式三：l.remove() 根据元素名删除 返回的是None 注意返回None和无返回值是有区别的 l1=del(l[0]) 无返回值这样是会程序报错的 
   
   #切片  （顾头不顾尾）
   l=[1,2,3]
   #可以切片修改 改的是原列表
   print(id(l[:]),id(l)) #和浅copy一样
   print(l[0:3])
   print(::-1) #倒置
   
   #循环 循环时不要减少list里的数量 会混乱
   l=[1,2,3,4,5]
   for i in l:
     l.pop(1)
   print(l)   #这样改的话逻辑容易出错
   
   #l.count、l.index、l.clear(返回值为None)、l.reverse(返回值为None)  没有find
   
   #sort 列表元素必须是同种类型才可以排序 int和float除外 可以指定两个参数  sort(reserve=True)降序排 默认则是升序 
   
   ```

   ###### 列表生成式

   列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

   举个例子，要生成list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`可以用`list(range(1, 11))`：

   ```python
   >>> list(range(1, 11))
   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   ```

   但如果要生成`[1x1, 2x2, 3x3, ..., 10x10]`怎么做？方法一是循环：

   ```python
   >>> L = []
   >>> for x in range(1, 11):
   ...    L.append(x * x)
   ...
   >>> L
   [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
   ```

   但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：

   ```python
   >>> [x * x for x in range(1, 11)]
   [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
   ```

   写列表生成式时，把要生成的元素`x * x`放到前面，后面跟`for`循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。

   for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：

   ```python
   >>> [x * x for x in range(1, 11) if x % 2 == 0]
   [4, 16, 36, 64, 100]
   
   >>> [x if x % 2 == 0 else -x for x in range(1, 11)] #需要用到else的情况，应放前面
   [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
   ```

   还可以使用两层循环，可以生成全排列：

   ```python
   >>> [m + n for m in 'ABC' for n in 'XYZ']
   ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
   ```

5. ##### tuple 元组：是不可变的列表 只有读的需求时可以用元组

    ```python
    x=(10) #单独一个括号是包含的意思
    t=(10,) #这样才是元组 元组内存的也是内存地址 所以指的是元组存的内存地址不可变 
    t=(1,[1,2]) # t[0]，t[1]不可变 但t[1][1]可变 元组内元素可以是可变类型
    ```

   

6. ##### 字典类型 dict

   dict是无序的，用关键字对应值

   每一个value都有一个key对应 value可以是任意类型 key必须是不可变类型且不可以重复

   定义：dic={key:value,key:value}  key通常为字符串

   ```python
   student_info = [
       {"name": "姜伍", "age": 25, "tele": 17679225435},
       {"name": "张月瑜", "age": 26, "tele": 15179215521}]
   print(student_info[0], student_info[1])
   
   dic=dict(x=1,y=2)#输出为{'x': 1, 'y': 2}
   
   #将列表的内容变为字典 
   l = [[1, 'jiangwu'],
        (2, "zhangyueyu")]
   dic = dict()
   #一：
   for i in l 
       dic[i[0]] = i[1]
   #二：
   for m, n in l:
       dic[m] = n
   #三：
   dic=dict(l) #一行代码搞定  但是列表内的每个元素必须是两个值
   
   #快速初始化字典
   keys=(1,2,3)
   value=None
   #一：
   d={}
   for i in keys: 
     d[i]=value
   #二：
   d={}.fromkeys(keys,value)#空字典快速初始化
   
   #赋值 key存在 则修改  key不存在 则添加key
   
   #成员运算 根据key
   
   #删除
   #del 
   #pop 根据key删除 但返回值是value
   #popitem 无参数 返回值是一个元组
   
   #keys(),values(),键值对items() 返回的都是列表
   #python2 得到的是鸡蛋
   d={'k1':111,'k2':222}
   d.keys()#得到的是['k1','k2']
   d.values()#得到的是[111,222]
   d.items()#得到的是[('k1',111),('k2',222)]
   #python3 得到的老母鸡
   
   #其他内置
   d={1:2}
   d.clear() #返回值是None
   d.update({"k2":222,'k3':444,'k1':111}) #更新字典 返回值None
   d.get() #print(d[3]) 不存在报错  print(d.get(3)) 不存在返回None res=d.get(1) 返回值为2 若 res=d.get(5) 返回值为None 若 res=d.get(5，18) 则返回值为18
   d.setdefault() #d.setfault(1,2) key若有则啥都不干，不用管value  d.setfault(3,4) 若无 则d添加一项  返回值都是value
   ```

7. ##### 布尔类型 bool

   Flase：0 None 空

   用于记真假状态，通常用于条件判断

8. ##### 集合类型 set

   作用：用于关系运算、去重
   
   - 集合内元素必须为==不可变类型==
   - 集合内元素无序
   - 集合内元素==无重复==
   
   ```python
   #d={}这是空字典 而不是集合
   res=set('zhuangyueyu')
   print(res) #输出为{'y', 'e', 'n', 'h', 'z', 'a', 'u', 'g'} 
   res=set([1,2,[1,3]])
   print(res) #会报错  
   res=set([1,2,(1,3)]) 
   print(res) #{1, 2, (1, 3)} 元组可以
   ```
   
   内置方法：
   
   ```python
   #关系运算
   f1={'jiangwu','zhangyueyu','lu1'}
   f2={'lu1','zhangyueyu','po8'}
   print(f1&f2)
   print(f1.intersection(f2))#交集 
   print(f1|f2)
   print(f1.union(f2))#并集
   print(f1-f2)
   print(f1.difference.(f2))#差集
   print((f1-f2)|(f2-f1))
   print(f1.symmetric_difference(f2))#对称差集
   #父子集 
   s1={1,2}
   s2={1}
   s3={3}
   print(s1>s2)
   print(s1.issuperset())#true
   print(s3<s1)
   print(s3.issubset())#false
   
   #去重-基于集合对列表去重具有局限性 所以一般还是自己手写
   1.只针对不可变类型
   2.无法保证原来的顺序
   
   #其他内置方法
   discard() #超出索引不会报错
   remove()#超出索引报错
   s.difference_update(s1) == s=s.difference(s1)
   s.pop()
   s.add()
   s.isdisjoint()#判断有无共同
   ```

#### 可变不可变类型

可变类型：值变、id不变

> list、dict  指的是容器内的东西变 而不是容器变

不可变类型：值变、id变

> int、float、string都被设计成不可分割的整体，是不可变类型

### 输入、输出 即与用户交互

#### 输入

input：接受为字符串类型 其他类型需要用强制转换函数

```python
username=intput("请输入你的账号：")
```

#### 输出

```python
print("姜伍",end="")
print("张月瑜")#输出的是姜伍张月瑜
print("姜伍",end=" ")
print("张月瑜")#输出的是姜伍 张月瑜
```

字符串格式化输出：

%格式：速度最慢

%s可以接受任意类型 连列表字典都能接受 但%d只能接受int

```python
test="my name is %s ,my age is %d"%('姜伍',25)#使用% 按照位置一一对应 若只有一个%则可以不用加括号
test="jiangwushi%s"%"shuaig e"
test="my lover is %(name)s ,her age is %(age)d"%{"name":"张月瑜",'age':26}#利用字典类型来打破顺序固定
lover={"name":'张月瑜','age':26}
test="my lover is %(name)s ,her age is %(age)d"%{**lover}#使用**解构lover
print("张月瑜以后要对姜伍%s%%真诚"%100) #用%%可以解除%的意思获得单纯的%
```

str.format：速度中等 兼容性高 python2、3都能用 所以推荐这种

 ```python
 test="my name is {} ,my age is {}".format('姜伍',25)#按顺序
 test="my name is {0}{1} ,my age is {1}{1}{0}".format('姜伍',25)#可以按索引取
 test="my lover is {name} ,her age is {age}".format(name="张月瑜",age=26)#打破顺序
 lover={"name":'张月瑜','age':26}
 print("my lover is {name},her age is {age}".format(**lover))#使用**解构lover
 ```

f格式：速度最快 但兼容性差，python3 才推出

```python
x=input("your name:")
y=input("your age:")
test=f'我的名字是{x} 我的年纪是{y}'
print(test)
x="姜伍"
y="张月瑜"
print(f"{{{x}}}喜欢{{{y}}}")#输出为{姜伍}喜欢{张月瑜} 最外面括号使得第二个括号意义失效变成单纯的{}
```

f格式{}用法：

```python
f'{print("jiangwu")}'#输出为jiangwu  即{}能将字符串里的内容变成表达式
print(f'520+16') #输出为 520+16
print(f'{520+16}')#输出为536
```



填充与格式化：

左对齐：x<10 共十个字符 不够的用x凑

```python
print('{0:x<10}'.format("woshi"))#输出格式为woshixxxxx
```

右对齐：x>10

中间对齐：x^10

精度与进制：

```python
print("{salary:.3f}".format(salary=3.1415926))#四舍五入精确到小数点后三位
a=19873983734.381042804
print("%-2.5f"%a) #输出结果19873983734.38104是个字符串 -为左对齐 2为对齐宽度 5为精度
b="zhangyueyu"
b=("%5.2s"%b)
print(b)#输出为   zh 普通格式输出为右对齐
print("{:5.2s}".format(b))#输出结果为zh 字符串格式输出的话为左对齐
print("{0:b}".format(123))#转换成二进制 也可以没有0
print("{0:o}".format(9))#转换成八进制
print("{0:x}".format(15))#转化成十六进制
b=10101
d=int(b,2/8/16)#将二/八/十六进制转成十进制
a=5
print(bin(a),oct(a),hex(a)) #十进制转二、八、十六进制

#在Python中，采用的格式化方式和C语言是一致的，用%实现，举例如下：
>>> 'Hello, %s' % 'world'
'Hello, world'
>>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
'Hi, Michael, you have $1000000.'
#其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
```

### 练习

小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出`'xx.x%'`，只保留小数点后1位：

```
# -*- coding: utf-8 -*-

s1 = 72
s2 = 85
r = (s2-s1)/85*100

print('%.1f%%'%r)
print('{0:.1f}%'.format(r))
print(f'{r:.1f}%')
```

### 基本运算符

#### 算术运算

```python
10/3 #结果带小数
10//3 #结果只保存整数部分
10**2 #10的二次方
```

#### 比较运算

#### 赋值运算

```python
= #变量的赋值
+= #增量赋值
x=y=z=10 #链式赋值
m,n=n,m #交叉赋值
lis=[1,2,3,4,5]
a,b,c,d,e=lis #解压赋值 左右必须一一对应 多少都不行
a,b,*_=lis #取前两个值 后面其余被*整合到变量名为_的变量类型（此处为列表）中了
*_,a,b=lis #取后两个值
a,*_,b=lis #取两边的值 
若是解压字典 默认解压的是value
```

#### 逻辑运算

not、and、or 优先级：not>and>or 

#### 成员运算

```python
print("j" in "jiangwu) #判断子字符串是否在主串中
print(1 in [1,2]) #判断元素是否在列表中
print("k1" not in ["k1":1,"k2":2])字典的成员运算是判断key是否在字典中
```

#### 身份运算

is 判断id

== 判断值

#### 短路运算

偷懒原则：偷懒到哪个位置就把当前位置返回

### 流程控制

#### if

```python
if 条件：#语法1
    代码1
  	代码2#缩进四个空格
    
if 条件：#语法2
    代码1
  	代码2
else：
		代码3
  	代码4
    
if 条件1：#语法3
    代码1
  	代码2
elif 条件2： 
		代码3
  	代码4
else：
		代码5
```

#### 模式匹配

即c语言中的switch语句

```python
score = 'B'

match score:
    case 'A':
        print('score is A.')
    case 'B':
        print('score is B.')
    case 'C':
        print('score is C.')
    case _: # _表示匹配到其他任何情况
        print('score is ???.')
        
#match语句除了可以匹配简单的单个值外，还可以匹配多个值、匹配一定范围，并且把匹配后的值绑定到变量：
age = 15

match age:
    case x if x < 10:
        print(f'< 10 years old: {x}')
    case 10:
        print('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')
        
# 匹配列表

#match语句还可以匹配列表，功能非常强大。

#我们假设用户输入了一个命令，用args = ['gcc', 'hello.c']存储，下面的代码演示了如何用match匹配来解析这个列表：
args = ['gcc', 'hello.c', 'world.c']
# args = ['clean']
# args = ['gcc']

match args:
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')

```



#### 循环

##### while循环

```python
while 1:
    1+1#这种死循环会出现致命问题 因为cpu会一直高速工作 
while 1:
    print(1) #这种不会出现致命问题，因为在io操作时，cpu可以等待一会 即死循环本身是无害的
account="张月瑜"
password="姜伍"
while 1:
    input_=input("请输入您的账号：")
    input__=input("请输入您的密码：")
    if account==input_ and password==input__:
        print("登入成功")
        break
    else:
        print("登录失败，密码或用户名不正确，请重新输入")

#while + else：针对的是break 即while结束后运行并且是while没有被break打断结束的情况下才会运行
count_1=0
while count_1<3:
    account = input("请输入您的账号：")
    password = input("请输入您的密码：")
    count_1+=1
    if account=="jiangwu" and password=="zhangyueyu":
        print("登录成功，请选择您要进行的操作：")
        count_2=0
        while count_2<3:
            cmd=input()
            count_2+=1
            if cmd=="5":
                key=input("取钱成功，请按1退出：")
                if key=="1":
                    print("退出成功")
                    break
            else:
                print("请重新输入您的操作")
        else:
            print("您操作次数过多，已停止程序")
        break
    else:
        print("请重新输入您的账号密码") 
else:
    print("您输入次数过多，已关闭程序")
```

##### for循环

for循环在循环取值上更方便

```python
for 变量名 in 可迭代对象： 
		代码1
  	代码2  #可迭代对象可以是：列表、字典、字符串、元组、集合 
    
for i in [1,2,3]:
  print(i)
   
dic={"k1":1,"k2":2,"k3":3}
for i in dic:
  	print(i,dic[i]) #取出来的i是key
range(10) #其实是个列表[0,1,2,3,4,5,6,7,8,9]
range(1,9)#[1,2,3,4,5,6,7,8]
range(1,9,2) #[1,3,5,7] 2表示步长
#python3对range进行了空间上的优化 range(10)表示的是一个能生0到9的老母鸡 不需要像python2一样需要内存空间存列表
dic={1:1,2:2}
for i,j in dic.items():
    print(i,j)
```

for+break 和for+else 与while循环一样

### 函数

```python
def 函数名(x):
    if x >= 0:
        return x
    else:
        return -x
#默认参数
def power(x, n=2):#此处n=2为默认参数，一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
  #这样，当我们调用power(5)时，相当于调用power(5, 2)：而对于n > 2的其他情况，就必须明确地传入n，比如power(5, 3)。
  
 #可变参数
#在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。

#我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。

#要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下：

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#但是调用的时候，需要先组装出一个list或tuple：

>>> calc([1, 2, 3])
14
>>> calc((1, 3, 5, 7))
84
#如果利用可变参数，调用函数的方式可以简化成这样：

>>> calc(1, 2, 3)
14
>>> calc(1, 3, 5, 7)
84
#所以，我们把函数的参数改为可变参数：

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：

>>> calc(1, 2)
5
>>> calc()
0
#如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：

>>> nums = [1, 2, 3]
>>> calc(nums[0], nums[1], nums[2])
14
#这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：

>>> nums = [1, 2, 3]
>>> calc(*nums)

#关键字参数
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
#函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数：

>>> person('Michael', 30)
name: Michael age: 30 other: {}
#也可以传入任意个数的关键字参数：

>>> person('Bob', 35, city='Beijing')
name: Bob age: 35 other: {'city': 'Beijing'}
>>> person('Adam', 45, gender='M', job='Engineer')
name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
#关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：

>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, city=extra['city'], job=extra['job'])
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
#当然，上面复杂的调用可以用简化的写法：

>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, **extra)
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

#命名关键字参数

#对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。

#仍以person()函数为例，我们希望检查是否有city和job参数：

def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
#但是调用者仍可以传入不受限制的关键字参数：

>>> person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：

def person(name, age, *, city, job):
    print(name, age, city, job)
#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。

#调用方式如下：

>>> person('Jack', 24, city='Beijing', job='Engineer')
Jack 24 Beijing Engineer
#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：

def person(name, age, *args, city, job):
    print(name, age, args, city, job)
#命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：

>>> person('Jack', 24, 'Beijing', 'Engineer')
#Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
#TypeError: person() missing 2 required keyword-only arguments: 'city' and 'job'
#由于调用时缺少参数名city和job，Python解释器把前两个参数视为位置参数，后两个参数传给*args，但缺少命名关键字参数导致报错。

#命名关键字参数可以有缺省值，从而简化调用：

def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
#由于命名关键字参数city具有默认值，调用时，可不传入city参数：

>>> person('Jack', 24, job='Engineer')
Jack 24 Beijing Engineer
#使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：

def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass
  
 #参数组合

#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
```

### 生成器 generator

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator保存的是算法。

创建生成器方法：

1. 把列表的[]改成（）

   ```python
   >>> L = [x * x for x in range(10)]
   >>> L
   [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
   >>> g = (x * x for x in range(10))
   >>> g
   <generator object <genexpr> at 0x1022ef630>
   #我们可以直接打印出list的每一个元素，但我们怎么打印出generator的每一个元素呢？
   
   #如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值：
   
   >>> next(g)
   0
   >>> next(g)
   1
   >>> next(g)
   4
   >>> next(g)
   9
   >>> next(g)
   16
   >>> next(g)
   25
   >>> next(g)
   36
   >>> next(g)
   49
   >>> next(g)
   64
   >>> next(g)
   81
   >>> next(g)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   StopIteration
   #generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
   #当然，上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象：
   
   >>> g = (x * x for x in range(10))
   >>> for n in g:
   ...     print(n)
   ... 
   0
   1
   4
   9
   16
   25
   36
   49
   64
   81
   
   ```

2. 在函数中使用yield

   ```python
   def fib(max):
       n, a, b = 0, 0, 1
       while n < max:
           yield b
           a, b = b, a + b
           n = n + 1
       return 'done'
    fib(6)#此时这一个一个生成器
   
   ```

   

### 字符编码

- Unicode  兼容万国码且与万国码都有对应关系  内存中统一使用unicode

  - 采用16位对应一个中文字符（个别生僻字对应32，64位）

- utf-8

  - 英文 8位

  - 中文 24位

结论：

- 内存固定使用unicode，我们可以改变的是存入硬盘采用格式

  - 中+英：内存- unicode、硬盘-gbk
  - 万国符：内存-unicode、硬盘-utf-8

- 文本文件存取乱码问题

  - 存乱了，致命问题 因为就不知道存了什么在硬盘
  - 取乱了，小问题

- python解释器默认读文件的编码

  - python2默认：ascii
  - python3默认：utf-8
  - 在指定文件的首行写#coding：gbk（读文件的编码）就可以读取别的编码的内容了

- 编码、解码

  ```python
  x='姜伍'
  res=x.encode('gbk')
  b=res.decode('gbk')
  print(res,type(res),b)#输出为b'\xbd\xaa\xce\xe9' <class 'bytes'> 姜伍
  ```

  - 对于单个字符的编码，Python提供了`ord()`函数获取字符的整数表示，`chr()`函数把编码转换为对应的字符：
  
  ```python
  >>> ord('A')
  65
  >>> ord('中')
  20013
  >>> chr(66)
  'B'
  >>> chr(25991)
  '文'
  ```

### python面向对象

定义一个类Animals:

(1)**init**()定义构造函数，与其他面向对象语言不同的是，Python语言中，会明确地把代表自身实例的self作为第一个参数传入

(2)创建一个实例化对象 cat，**init**()方法接收参数

(3)使用点号 . 来访问对象的属性。

```python
class Animal:

    def __init__(self,name):
        self.name = name
        print('动物名称实例化')
    def eat(self):
        print(self.name +'要吃东西啦！')
    def drink(self):
        print(self.name +'要喝水 啦！')

cat =  Animal('miaomiao')
print(cat.name)
cat.eat()
cat.drink()
```

继承：

```python
class Person:        
    def __init__(self,name):
        self.name = name
        print ('调用父类构造函数')

    def eat(self):
        print('调用父类方法')
 
class Student(Person):  # 定义子类
   def __init__(self):
      print ('调用子类构造方法')
 
   def study(self):
      print('调用子类方法')

s = Student()          # 实例化子类
s.study()              # 调用子类的方法
s.eat()                # 调用父类方法
```

### Python JSON

JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式，易于人阅读和编写。

json.dumps 用于将 Python 对象编码成 JSON 字符串。

```py
import json
data = [ { 'b' : 2, 'd' : 4, 'a' : 1, 'c' : 3, 'e' : 5 } ]
json = json.dumps(data)
print(json)
```

```py
import json
data = [ { 'b' : 2, 'd' : 4, 'a' : 1, 'c' : 3, 'e' : 5 } ]
json = json.dumps(data)
print(json)
```

为了提高可读性，dumps方法提供了一些可选的参数。

sort_keys=True表示按照字典排序(a到z)输出。

indent参数，代表缩进的位数

separators参数的作用是去掉,和:后面的空格，传输过程中数据越精简越好

```py
import json
data = [ { 'b' : 2, 'd' : 4, 'a' : 1, 'c' : 3, 'e' : 5 } ]
json = json.dumps(data, sort_keys=True, indent=4,separators=(',', ':'))
print(json)
```

json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型。

```py
import json
jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
text = json.loads(jsonData)  #将string转换为dict
print(text)
```
