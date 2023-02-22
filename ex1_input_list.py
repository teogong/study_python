#!/usr/bin/env python
# coding: utf-8

# # input 사용법
# - input() 
# - input('Enter name')

# In[7]:


print('Enter name')
name = input()
print("Good morning", name)


# In[9]:


name = input('Enter name')
print("Good morning", name)


# 
# # list 
# 파이썬은 배열이 없고 다 리스트입니다  
# 파이썬은 리스트는 객체고  힙에 생긱고  
# 저건 단지 레퍼렌스만 가지고 있는다

# In[10]:


color = ['red','blue','green']
print(color[0])
print(color[1])


# len 길이를 리턴해주는 함수

# In[11]:


print(len(color))


# 전체를 찍어줌

# In[12]:


print(color)


# 다른 list 와 다른점은 list안에 다른형식을 다집어 넣을수있다.

# In[13]:


list01 = [1,2,'Three',4.0,True]
print(list01)


# In[15]:


cities = ['서울','부산','인천','대구','대전','광주','울산','수원']


# 맨 뒤에서 직전까지만 출력

# In[16]:


print(cities[0:6])


# 처음 시작할때는 앞에 생략가능

# In[17]:


print(cities[:6])


# 끝까지 할때는 뒤에 생략가능

# In[18]:


print(cities[2:])


# cities = ['서울','부산','인천','대구','대전','광주','울산','수원']  
# 마이너스 인덱스 지원함

# In[19]:


print(cities[-7:])


# In[21]:


print(cities[:-2])


# 처음부터 끝까지 출력

# In[22]:


print(cities[:])


# In[23]:


print(cities)


# cities = ['서울','부산','인천','대구','대전','광주','울산','수원']  
# 1부터 7까지 인데 2개씩 뛰어라

# In[24]:


print(cities[1:7:2])


# In[25]:


print(cities[::-1])


# In[27]:


print(cities[::2])


# In[28]:


color1 = ['red','blue','green']
color2 = ['orange','black','white']


# list 사측연산

# In[29]:


add_color = color1+color2
print(add_color)


# In[30]:


mul_color = color1*2
print(mul_color)


# In[31]:


print('===============================================')


# In[32]:


print('='*40)


# color1 = ['red','blue','green']  
# color2 = ['orange','black','white']  
# 특정 항목에 list에 있는지 확인할때 in연산자 사용

# In[33]:


print('blue' in color1)


# In[35]:


print('orange' in color1)


# 맨 마지막에 항목추가하는것이 append이다

# In[36]:


color1.append('purple')
print(color1)


# list로 여러개 추가할때는 extend

# In[37]:


color2.extend(['purple','pink'])
print(color2)


# insert 원하는 위치에 넣는것 그러나 내부적으로 퍼포먼스가 떨어짐

# In[38]:


color2.insert(1,'magenta')
print(color2)


# list 삭제 방법

# In[39]:


color2.remove('magenta')
print(color2)


# 인덱스 삭제 (글로벌 스페이스에서 변수를 날려버릴때 사용)

# In[40]:


del color2[0]
print(color2)


# In[41]:


a= 100
print(a)


# In[43]:


del(a)
print(a)


# 값 변경

# In[44]:


color2[1] = 'red'
print(color2)


# 패킹 언패킹 

# In[45]:


color = ['red','blue','green'] #packing


# In[47]:


a, b, c = color  #unpacking
print(a,b,c)  #단 변수 갯수가 다르면 에러 발생


# In[48]:


a, _, b = color #안박고 싶은때는 _ 사용해서 갯수 맞쳐줘야한다.
print(a,b)


# 2차원 list  
# 앞에 인덱스가 row  
# 뒤에 인덱스가 column

# In[51]:


kor_score = [60, 65, 85, 100, 90]
eng_score = [75, 80, 90, 85, 100]
math_score = [100, 90, 70, 90, 85]
term_score = [kor_score, eng_score, math_score]


# In[52]:


print(term_score)


# In[53]:


print(term_score[0])


# In[54]:


print(term_score[0][2])


# In[ ]:




