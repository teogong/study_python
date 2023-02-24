#!/usr/bin/env python
# coding: utf-8

# ## zip

# In[15]:


# 요긴하게 써먹을 꺼
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3', 'b4']


# In[16]:


for a, b in  zip(alist, blist): 
    print(a,b)


# In[5]:


# 요긴하게 써먹을 꺼

alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3', 'b4']
clist = ['apple','mango','cherry']

for a, b, c in  zip(alist, blist, clist): # zip은 같은 인덱스는 묶이고 나머지 인덱스는 탈락
    print(a,b,c)


# In[7]:


a, b, c, = zip((1,2,3),(10,20,30),(100,200,300))
print(a,b,c)


# In[9]:


result = [sum(x) for x in  zip((1,2,3),(10,20,30),(100,200,300))]
print(result) # sum과 for문 한줄로 출력하기


# ### Random

# In[10]:


import random


# In[12]:


print(random.random())


# In[13]:


print(random.random())


# In[15]:


print(random.randrange(10))


# Random seed : 변하는 값  
# 가지고 seed 값(현재 시간, 기계값, 등등 time,merchine, ....) 이런것을 가지고 변하는 값 만듬

# In[6]:


import random
random.seed(10)  # seed 값을 고정해서 random하지 않게 하기


# In[5]:


for n in range(5):
    print(random.randrange(10))


# ### class

# In[13]:


class SoccerPlayer:
    #생성자 메소드 (클래스 안에 있는 것은 함수라고 안하고 메소드라 한다.)
    #self는 들어가있고 현재 함수 파라미터는 3개이다.
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number
    #self는 this랑 같음 
    
    def change_back_number(self, new_number):
        print('선수 등번호 변경 : From %d to %d' %(self.back_number ,new_number))
        self.back_number = new_number
    
    def __str__(self):  # __str__은 객체를 찍을때 정해줄 수 있다.
        return 'Hello, My name is %s. I play in %s in center.' % (self.name, self.position)


#  '\_\_str\_\_' 객체를 찍어줄때 정해줄수 있다.

# In[17]:


chaboom = SoccerPlayer("Chaboom", "CF", 11)

print("현재 선수의 등번호:", chaboom.back_number)
chaboom.change_back_number(9)
print("현재 선수의 등번호:", chaboom.back_number)
print()
print(chaboom)


# 상속

# In[18]:


class Bicycle:
    def __init__(self, wheel_size, color):
        self.wheel_size = wheel_size
        self.color = color

    def move(self, speed):
        print(f"자전거 시속 {speed}킬로미터로 전진")

    def turn(self, direction):
        print(f"자전거: {direction}회전")

    def stop(self):
        print(f"자전거({self.wheel_size}, {self.color}): 정지")


# In[25]:


class FoldingBicycle(Bicycle): #Bicycle에 자식 클래스는 FoldingBicycle
    def __init__(self, wheel_size, color, state):
        super().__init__(wheel_size, color)  #자식 클래스에서 부모 클래스 받을때 super()가 부모를 지칭
        self.state = state

    def fold(self):
        self.state = 'folding'
        print(f"자전거: 접기, state = {self.state}")

    def unfold(self):
        self.state = 'unfolding'
        print(f"자전거: 펴기, state = {self.state}")


# In[26]:


folding_bicycle = FoldingBicycle(27, 'white', 'unfolding')
folding_bicycle.move(20)
folding_bicycle.turn('right')
folding_bicycle.stop()
folding_bicycle.fold()
folding_bicycle.unfold()


# ### 모듈과 패키지
# #### 모듈
# ● 파이썬 프로그램 코드  
# ● 상수, 변수, 함수, 클래스 등을 포함

# In[5]:


import fah_converter


# In[2]:


celsius = float(input('Enter a celsius value:'))
fahrenheit = fah_converter.converter_to_f(celsius)
print("It's",fahrenheit, "degrees Farenheit")


# In[3]:


import fah_converter as fah
print(fah.converter_to_f(25))


# In[1]:


from fah_converter import converter_to_f # import해서 바로 사용 가능
# from fah_converter import converter_to_f * # 권장 안함, 단, 내가 만들고 잘알고 있을때
print(converter_to_f(25))


# #### 패키지  
# ● 모듈의 묶음  
# ● 모듈 파일이 포함될 폴더까지 포함

# In[5]:


# 예제) 인터넷에서 주식 정보를 가져와 데이터베이스에 저장, 필요한 정보를 계산
# 패키지 명: roboadvisor
# ● crawling: 주식 관련 데이터를 인터넷에서 가져옴
# ● database: 가져온 데이터를 데이터베이스에 저장
# ● analysis: 해당 정보를 분석, 의미있는 가치 추출

# my_package -- roboadvisor 	-- analysis
#   							-- crawling
#   							-- database


# In[8]:


import sys  ## 패스를 추가 해줘야한다.
print(sys.path) ### sys는 list로 되어 있다.


# In[2]:


import sys
sys.path.append('/Users/jungkihun/Documents/source/python/my_packge')
# 1방법
import roboadvisor.analysis.series #패키지.폴더.모듈
roboadvisor.analysis.series.series_test()


# In[5]:


import sys
sys.path.append('/Users/jungkihun/Documents/source/python/my_packge')
# 2 방법 : 패키지.폴더
from roboadvisor.analysis import series #패키지.폴더.모듈
series.series_test()


# In[6]:


import sys
sys.path.append('/Users/jungkihun/Documents/source/python/my_packge')
# 3 방법 : 패키지.폴더.모듈
from roboadvisor.analysis.series import series_test #패키지.폴더.모듈
series_test()


# In[2]:


import sys
sys.path.append('/Users/jungkihun/Documents/source/python/my_packge')
# 이것은 안되지만 되게 하는 방법이 있음, __init.py안에 __all__ = ['파일이름','파일이름'] 넣어주면 돌아간다.
import roboadvisor
roboadvisor.analysis.series.series_test()


# In[5]:


import sys
sys.path.append('/Users/jungkihun/Documents/source/python/my_packge')
# 모듈까지만  import 할수 있고 함수가 올수없다
import roboadvisor.analysis.series.series_test
series_test()


# In[3]:


import sys
sys.path.append('/Users/jungkihun/Documents/source/python/my_packge')
# 어떤 모듈을 사용할지 정의 해줘야한다. why? 폴더 안에 있는 필요한것 말고 전부다 가져와진다.
# __init__.py 파일 안에 ' __all__ = ['파일이름','파일이름'] ' 넣어줘야한다.
# 패키지안에 폴더는 잡아줘야안다.
from roboadvisor.analysis import *
series.series_test()


# In[4]:


import sys
sys.path.append('/Users/jungkihun/Documents/source/python/my_packge')
# 모든 모듈은 된다.
from roboadvisor.analysis.series import *
series_test()


# In[1]:


import sys
sys.path.append('/Users/jungkihun/Documents/source/python/my_packge')
# 이것은 안되지만 되게 하는 방법이 있음, __init.py안에 __all__ = ['파일이름','파일이름'] 넣어주면 돌아간다.
# 유니파이 설정하면됨
import roboadvisor
roboadvisor.analysis.series.series_test()


# In[1]:


import sys
sys.path.append('/Users/jungkihun/Documents/source/python/my_packge')
# 모든 모듈은 된다.
from roboadvisor.crawling.scrap import scrap_test
scrap_test()


# ### 예외처리

# In[2]:


for i in range(10):
    print(10/i) # 0으로 못 나눈다


# In[4]:


for i in range(10):
    try:
        print(10/i) 
    except ZeroDivisionError as e:
        print('0으로 나눴잖아....')
        print(e)


# In[8]:


for i in range(10):
    try:
        result = 10/i 
    except ZeroDivisionError as e:
        print('0으로 나눴잖아....')
        print(e)
    else: # if 사용하여 발생 안시키는것이 좋다
        print(result)
    


# In[13]:


for i in range(10):
    try:
        result = 10/i
        print(result)
    except ZeroDivisionError as e:
        print('0으로 나눴잖아....')
        print(e)
    finally: ## except에서 뭘 하든 항상실행
        print('여기는 항상 실행')
    


# In[15]:


while True:
    value = input('정수 입력:')
    for digit in value:
        if digit not in '0123456789':
            raise ValueError("똑바로 넣어!!!") # except 발생시키기 --> raise 명령어 사용
    print('입력한 숫자: ',int(value))


# \## 중간 중간 들어오는 값 체크할 경우  
# 개발할때 유용함

# In[23]:


def get_binary_number(deciaml_number):
    assert isinstance(deciaml_number,int),'숫자 아니잔어 바보야~~~~~~~~~~'  ## int 말고 다른 값이 들어오면 에러 
    return bin(deciaml_number)


# In[24]:


print(get_binary_number(13))


# In[25]:


print(get_binary_number('13'))


# In[ ]:




