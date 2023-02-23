#!/usr/bin/env python
# coding: utf-8

# In[1]:


kor_score = [60, 65, 85, 100, 90]
eng_score = [75, 80, 90, 85, 100]
math_score = [100, 90, 70, 90, 85]
term_score = [kor_score, eng_score, math_score]


#   
# math_backup_score는 math_score의 주소 값을 stack에 가지고 있어서 heap 영역에 값을 변경하면 같이 변경되고 즉 같은 객체를 공유하고 있다.

# In[2]:


math_backup_score = math_score
print(term_score)


# In[3]:


math_score[0] = 0


# In[4]:


print(math_score)


# In[5]:


print(math_backup_score)


# reverse() 리스트 자체가 갱신된다.

# In[6]:


a = [1, 10, 5, 7 , 6]


# In[7]:


a.reverse()


# In[8]:


print(a)


# sort() 순서대로 정렬, 기본이 언센딩sort

# In[9]:


a.sort()
print(a)


# 디센딩sort

# In[10]:


a.sort(reverse=True)
print(a)


# sorted가 sort새로운 리스트를 생성한고, 기존에 있는것은 건드리지 않는다.

# In[11]:


a = [3, 2, 1, 4]
b = sorted(a)
print(a,b)


# 파이썬 스타일은 reverse=True 붙여쓴다

# In[12]:


b = sorted(a, reverse=True)
print(a,b)


# count()안에 있는거 세줌

# In[13]:


a = [1,2,2,4,4,4,5]


# In[14]:


print(a.count(2))
print(a.count(4))
print(a.count(5))


# In[15]:


appetizer = ['egg', 'salad', 'bread', 'soup', 'canape']
main_dish = ['fish', 'lamb', 'pork', 'beef', 'chicken']
dessert = ['apple', 'ice cream', 'pudding', 'cookies', 'cake']

order = [appetizer, main_dish, dessert]
jane = [order[0][:-2], main_dish[1::3], dessert[1:3]]
del jane[2]
jane.extend([order[2][0:1]])


# In[16]:


print(jane)


# if 문 

# In[17]:


my_age = int(input("Input your age"))
if my_age < 30:
    print('Welcome to the Club')
else:
    print("Oh! you ar not allowed")


# In[18]:


score = int(input('Enter your score'))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade ='F'
    
print(grade)


# ### one line if  
# 한 라인은 if 짜는 방법

# In[19]:


a = 9
b = a * 10 if a % 2 == 0 else a + 10
print(b)


# ### for 문  
# in 다음에는 list가 온다 순서대로 값이 직접 들어온다 for in 형태

# In[20]:


for n in [1,2,3,4,5]:
    print('No',n)


# range는 0부터 5찍전 까지 출력

# In[21]:


for n in range(5):
    print('No',n)


# In[22]:


for n in range(1,6):
    print('No',n)


# In[23]:


for n in range(1,6,2):
    print('No',n)


# In[24]:


for n in  'abcdf':
    print('No',n)


# In[25]:


for n in ['banana',  'pineapple','mango']:
    print(n)


# In[26]:


for n in ['banana',  'pineapple','mango']:
    for k in n:
        print(k)
    print()   


# In[42]:


i = 1 
while i < 10:
    print(i)
    i += 1


# In[43]:


for i in range(10):
    if i == 5:
        break
    print(i)
print('End of program')


# In[45]:


for i in range(10):
    if i == 5:
        continue
    print(i)
print('End of program')


# In[51]:


print("몇단? ")
dan = input()
print("구구단", dan, "단 계산")
int_dan = int(dan)
for i in range(1,10):
    result = int_dan * i
    print (dan," X ",i,' = ',result )


# In[56]:


sentence = 'I love you'
reverse_sentence = ''
for char in sentence:
    reverse_sentence = char + reverse_sentence
print(reverse_sentence)


# 십진수를 이진수로 변환  
# 내 코드  

# In[13]:


decunak = 14
# 십진수를 이진수로 변환
result = ''
while decunak > 0 :
    for i in range(0,4):
        i+=1
        decunak = int(decunak / 2)
        print('%s' %str(decunak % 2))
        result =  result + str(decunak % 2)
print(result)


# 선생님 코드

# In[1]:


decimal = 14
result  = ''
while decimal > 0:
    remainder = decimal % 2
    decimal //= 2
    result = str(remainder) + result
print(result)


# 
# # 함수
# def 함수이름 (인자1, 인자2, ...옵션):  
#         실행문1 
#         실행문2    
#         return 반환값(옵션)

# In[1]:


def calculate_rectangle_area(x,y):
    return x*y


# In[2]:


rec_width  =10
rec_height = 20
print(calculate_rectangle_area(rec_width,rec_height))


#     대표적으로 레퍼런스 넘기는 예제 --> 함수 내부에서는 동일한 객체 사용  
#                  stack | heap  
#     shopping_list[100] | 100['bean', 'salt','beef']  
#             goods[100] | [2001,2]

# In[4]:


def shopping_cart(goods):
    goods.append('coupon')
    goods = [ 1, 2]
    print('In shopping_cart:', goods)


# In[5]:


shopping_list = ['bean', 'salt','beef']
shopping_cart(shopping_list)
print('I bouht:',shopping_list)


# x 와 t는 함수 내에서만 존재하는 변수,  따라서 접근이 불가능하다. 
# 
# 함수 안에서는 a가 300이 찍히는데 밖에 서는 10임 :   
# java나 c는 타입을 정해줘서 글로벌에서 접근이 불가능함 but 파이썬은 특별한 문법 제공
# 

# In[12]:


def test(x):
    print(x)
    t = 20
    a = 300
    print('In funtion:',t, a)


# In[13]:


a = 10 
test(a)
print('In Global a' , a)
# print('In Global t' , t)


# 지역 변수 s를 안만들어서 접근이 가능하나  
# 함수 내에서 s에 변수 값을 집어 넣으면 로컬 변수가 된다.  
# global 키워드로 지정해서 쓰면 함수 내에 변수 접근 가능

# In[17]:


def f():
    global s
    s = 'I love Doosan!'
    print(s)


# In[18]:


s = 'I love hanhwa!'
f()
print(s)


# ### 함수 파라미터
# 
# print('Hello {0}, my name is {1}' . format(your_name, my_name))  
# {0} ,{1} 인덱스

# In[19]:


def print_name(my_name, your_name):
    print('Hello {0}, my name is {1}' . format(your_name, my_name))


# In[20]:


print_name('Tom', 'Jane')


# 이름 지정하면 순서 바뀌어도 된다

# In[22]:


print_name(your_name ='Jane',my_name ='Tom' )


# 디폴드 벨류 정해주기  
# 디폴트 주면 리버스가 True아니면 false

# In[23]:


def print_name(my_name, your_name='Jane'):
    print('Hello {0}, my name is {1}' . format(your_name, my_name))


# In[24]:


print_name('Tom', 'Jane')


# In[25]:


print_name('Tom')


# In[26]:


print_name('Tom', 'Kate')


# 디폴드 값은 뒤에서 부터 줄수있다 앞에서 부터는 못준다

# In[28]:


def print_name(my_name = 'Tom', your_name):
    print('Hello {0}, my name is {1}' . format(your_name, my_name))


# 

# sentence = 'I love you'
# reverse_sentence = ''
# for char in sentence:
#     reverse_sentence = char + reverse_sentence
# print(reverse_sentence)

# In[33]:


s = "BLACK LIVES MATTER"
print(s.upper()) # 대문자
print(s.lower()) # 소문자
print(s.title()) # 제목 
print(s.capitalize()) # 첫글자만 대문자
print(s.count("T")) # 갯수 출력
print(s.startswith("B")) #

k = "123"
print(k.isdigit())


# In[32]:


print(1, 2, 3)
print("%d %d %d" %(1, 2, 3))   # C언어
print("%s--%s--%s" %('abc','def', 'ghi')) # C언어
print("{} {} {}".format('abc', 'def', 'ghi')) # 인덱스
print("{1} {0} {2}".format('abc', 'def', 'ghi')) # 인덱스
print(f"{'def'} {'abc'} {'ghi'}") # 인덱스 빼고 바로 찍어줌 'f'를 사용
print("{0:>10s}".format('python')) # 10칸 잡아서 오른쪽 정렬
print("{0:<10s}".format('python')) # 10칸 잡아서 왼쪽 정렬
print(f"{'python':>10s}")
print(f"{'python':<10s}")


# In[36]:


items = 'zero one two three'.split() # 띄어쓰기 인식해서 list에 담아줌
print(items) 


# In[39]:


examples = 'python,javascript,sql' 
print(examples.split(',')) # ',' 주면 ,로 구별해라


# In[43]:


a, _, b = examples.split(',') # 언패킹 바로사용
print(a,b)


# In[44]:


colors = ['red','blue','green','yellow']


# In[47]:


result = ''.join(colors) # join은 다 붙혀줌
print(result)


# In[48]:


result = ' '.join(colors) # join은 다 붙혀줌
print(result)


# In[49]:


result = ','.join(colors) # join은 다 붙혀줌
print(result)


# In[50]:


result = '_'.join(colors) # join은 다 붙혀줌
print(result)


# # 특별한 자료구조
# 
# ## Tuple

# In[51]:


t = (1,2,3)
print(t+t)


# In[52]:


print(t*2)


# In[55]:


print(t[1])


# In[58]:


t[1] = 100 # 이미 만들어진 Tuple은 안 바뀜


# In[59]:


print(type(t))


# In[60]:


t2 = (10)
print(type(t2))


# In[61]:


t2 = (10,) # 원소가 하나있을때는 ',' 써줘야한다
print(type(t2))


# In[62]:


s = set([1,2,3,1,2,3]) #중복 데이터 없어줌
print(s)


# In[65]:


s1 = set([1, 2, 3, 4, 5])
s2 = set([3, 4, 5, 6, 7])

print(s1.union(s2)) # 합집합
print(s1 | s2) # 합집합

print(s1.intersection(s2)) # 교집합
print(s1 & s2) # 교집합

print(s1.difference(s2)) # 차집합
print(s1-s2) # 차집합


# # Dictionary  
# 키: 벨류 , 키: 벨류 ,키: 벨류 ,키: 벨류 

# In[66]:


student_info = {20190001:'Tom', 20190002:'Jane', 20190003:'Mike', 20190004:'Jessica'}


# In[67]:


print(student_info[20190001])


# In[79]:


student_info[20190001] = 'Kate'
print(student_info)


# 이해못함

# In[73]:


country_code = {'USA':1, 'Korea':82, 'China':86, 'Malaysia':60}
print(country_code)

print(country_code.keys())

country_code['German'] = 49
print(country_code)

print(country_code.values())
print(country_code.items())
print()

for k, v in country_code.items():
    print('Key:', k)
    print('Value:', v)

print('Korea' in country_code.keys())
print(85 in country_code.values())


# In[78]:


for k,v in country_code.items(): # 투플을 바로 언팩킹한다.
    print(k,v)


# In[80]:


from collections import OrderedDict


# 나중에 합시다

# In[81]:


d = dict()
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['a'] = 400
print(d)


# 익명구현 객체를 표현하기 위해 람다 채용 : 자바  
# 익명구현 함수를 표현하기 위해 람다 채용 : 파이썬 

# In[82]:


def f(x,y):
    return x+y


# In[85]:


print(f(1,4))


# In[86]:


f1 = lambda x,y : x+y  # 파이썬은 제약사항이 있다 한줄뿐이 사용 못한다.
print(f1(1,4))


# In[88]:


print((lambda x,y : x+y)(1,4)) # 변수 안 거치고 사용가능


# In[89]:


f = lambda n, m: n if n%2 == 0 else m
print(f(1, 3))
print()
print(f(2, 3))


# In[94]:


def makeFunc(n):
    return lambda a : a % n == 1 # 함수를 제작해서 리턴 해줌

isOdd = makeFunc(2) # lambda a : a % 2 == 1 ,함수를 만들어주는 것
print(isOdd(3))  # 함수를 호출 할때만 값을 넣을 수 있다.
print(isOdd(4))


# In[106]:


# from collections import OrderedDict


# In[96]:


d = dict()
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['a'] = 400
print(d)


# In[97]:


def first_out(x):
    return x[0]


# In[98]:


od = OrderedDict(sorted(d.items()),key=first_out)


# In[99]:


print(od)


# In[101]:


od = OrderedDict(sorted(d.items(),key=lambda x:x[0])) #키 순서대로
print(od)


# In[103]:


od = OrderedDict(sorted(d.items(),key=lambda x:x[1])) #벨류 순서대로
print(od)


# In[105]:


od = OrderedDict(sorted(d.items(),key=lambda x:x[1], reverse = True)) #내림차순으로 정렬
print(od)


#  k

# In[114]:


s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 5)]
d = dict()
for k, v in s:
    d[k].append(v) # k값이 존재해야지 append로 들어갈수 있음


# In[115]:


s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 5)]
d = dict()
for k, v in s:
    try:
        d[k].append(v) # k값이 존재해야지 append로 들어갈수 있음
    except KeyError:
        d[k] = list()
        d[k].append(v)


# In[116]:


print(d)


# In[117]:


from collections import defaultdict


# In[118]:


d = defaultdict(list)
for k, v in s:
    d[k].append(v)


# In[119]:


print(d)


# In[121]:


print(d.items())  # 함수 호출해서 기본 값으로 만들어준다


# In[123]:


d = defaultdict(lambda : 100) #100을 디폴트로 넣고 싶으면 람다를 사용하면됨
print(d['name'])


# # 연습  

# In[125]:


text = """A press release is the quickest and easiest way to get free publicity. If
 well written, a press release can result in multiple published articles about your 
firm and its products. And that can mean new prospects contacting you 
asking you to sell to them. ….""".lower().split()


# In[126]:


print(text)


# In[182]:


word_count = defaultdict(lambda: 0)
for word in text:
    word_count[word] += 1
    
print(word_count.items())


# In[183]:


# 내가 한거
od = OrderedDict(sorted(word_count.items(),key=lambda x:x[1], reverse = True))
print(od)


# In[184]:


# 선생님이 알려주신거
for k, v in OrderedDict(sorted(word_count.items(), key=lambda t: t[1], reverse=True)).items():
    print(k, v)


# ### List  Comprehension

# In[185]:


result = []
for i in range(10):
    result.append(i)
    
print(result)


# In[186]:


result = [i for i in range(10)] #0-9 까지 추가 , 내부적으로 성능이 좋음
print(result)


# In[187]:


result = []
for i in range(10):
    if i % 2 == 0:
        result.append(i)
    
print(result)


# In[190]:


result = [i for i in range(10) if i %2 ==0] # if저거 일때만 적용하겠다
print(result)


# In[191]:


result = []
for i in range(10):
    if i % 2 == 0:
        result.append(i)
    else:
        result.append(99)
    
print(result)


# In[204]:


result = [i if i %2 ==0 else 99 for i in range(10)] # else 가 있으면 for문 앞으로 끄집어내야한다.
print(result)


# In[207]:


result = []
word1 = 'Hello'
word2 = 'World'
for i in word1:
    for k in word2:
        result.append(i+k)
        
print(result)


# In[208]:


result = [i + j for i in word1 for j in word2]  # 안에 쓰고 밖에쓴다
print(result)


# In[209]:


case1 = ['A', 'B', 'C']
case2 = ['A', 'B', 'C']


# In[210]:


result = []
for i in case1:
    for j in case2:
        if i != j:
            result.append(i+j)

print(result)


# In[212]:


result = [ i + j for i in case1 for j in case2 if i != j]
print(result)


# In[218]:


for v in ['tic','tac','toe']:  # 값에 인덱스가 필요한 경우???
    print(v)


# In[217]:


## 요긴하게 쓸거
for i,v in enumerate(['tic','tac','toe']):  # 값에 인덱스가 필요한 경우
    print(i,v)


# In[ ]:




