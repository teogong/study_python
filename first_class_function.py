#!/usr/bin/env python
# coding: utf-8

# In[3]:


def double_func(x):
    return x*2


# In[4]:


print(double_func(3))


# In[5]:


a = double_func
print(double_func) #함수를 넘겨줄수도 있고
print(a)


# In[6]:


print(a(10))


# In[10]:


def make_double_list(func,args):
    result = []
    for i in args:
        result.append(func(i))  #함수를 파라미터로 넘겨줄 수도 있다.
        
    return result


# In[9]:


input_list  = [ 1,2,3,4,5]
double_list = make_double_list(double_func,input_list)
print(double_list)


# In[11]:


def square(x):
    return x * x

def reflect(x):
    return -x


# In[12]:


square = make_double_list(square,input_list)
reflect = make_double_list(reflect,input_list)
print(square)
print(reflect)


# In[15]:


print('Hello ', end='') # 디폴트 값 end='\n'
print('World')


# In[26]:


import time
def log_formatter(msg):
    def log_message():
        time_str = time.strftime('%c', time.localtime(time.time()))
        print(time_str, end='')
        print(' ===> ', end='')
        print(msg) 
        
    return log_message
# 함수도 리턴이 가능하다.


# In[27]:


log_msg = log_formatter('test log')
print(log_msg) #함수를 리턴 해줌


# ● 종료된 이후에도 참조가 가능? log_message 를 클로저(closure) 라 함  
# ● 클로저는 다른 함수의 지역변수값을 그 함수가 종료된 후에도 기억

# In[30]:


log_msg()


# In[31]:


del log_formatter


# In[32]:


print(log_formatter)


# In[34]:


log_msg()   # closure 이다


# ### Closure  
# ● first class function을 지원하는 언어의 네임 바인딩 기술  
# ● 어떤 함수를 함수 자신이 가지고 있는 환경과 함께 저장한 레코드  
# ● 함수가 가진 프리변수(free variable)를 클로저가 만들어지는 당시의 값과 레퍼런스에 매핑하는 역할  
# ● 자신의 영역 밖에서 호출된 함수의 변수값과 레퍼런스를 복사하고 저장  
#   
# ** free variable  
# 코드블럭 안에서 사용은 되지만 그 코드블럭안에서 정의되지 않은 변수  

# In[37]:


def outer_func():
    msg = 'Good Morning!'
    
    def inner_func():
        print(msg)
    return inner_func() # return 함수() ==> 실행, return 함수 ==> 실행X


# In[36]:


outer_func()


# In[38]:


def outer_func():
    msg = 'Good Morning!'
    
    def inner_func():
        print(msg)
    return inner_func


# In[40]:


func = outer_func()
func()


# In[49]:


print(dir(func)) ##dir()변수나 메소드를 보여준다, closure를 내부에 뭐가 있나 보자


# In[43]:


print(type(func.__closure__)) # 튜플


# In[44]:


print(func.__closure__) #첫번째 항목만 있는 튜플


# In[45]:


print(func.__closure__[0])


# In[47]:


print(dir(func.__closure__[0]))


# In[48]:


print(func.__closure__[0].cell_contents)


# ### Decorator

# In[169]:


import time


# In[50]:


def log_formatter(msg):
    def log_message():
        time_str = time.strftime('%c', time.localtime(time.time()))
        print(time_str, end='')
        print(' ===> ', end='')
        print(msg) 
        
    return log_message


# In[56]:


test_log_msg = log_formatter('test log')
runtime_log_msg = log_formatter('runtime log')


# In[57]:


test_log_msg()
runtime_log_msg()


# In[58]:


def log_decorator(param_func):  #함수 실행하는것으로 변경
    def log_message():
        time_str = time.strftime('%c', time.localtime(time.time()))
        print(time_str, end='')
        print(' ===> ', end='')
        return param_func()
        
    return log_message


# In[59]:


def test_log_msg():
    print('This is test log.....')
    
def runtime_log_msg():
    print('This is runtime log.....')


# In[60]:


test_log = log_decorator(test_log_msg)


# In[61]:


runtime_log = log_decorator(runtime_log_msg)


# In[66]:


test_log() # 로그를 꾸며주는 힘수


# In[67]:


runtime_log() # 로그를 꾸며주는 힘수


# In[68]:


test_log_msg() # 그대로 출력


# In[69]:


runtime_log_msg() # 그대로 출력


# In[165]:


# @ 이것은 파이썬에서는 Decorator의미
@log_decorator # closure가 되는 함수 만들어줌
def test_log_msg(): # 함수 선언
    print('This is test log.....')


# In[74]:


@log_decorator 
def runtime_log_msg():
    print('This is runtime log.....')


# In[75]:


test_log_msg()


# In[76]:


runtime_log_msg()


# In[77]:


@log_decorator 
def runtime_log_msg(hote, ip):
    print(f'This is runtime log from {host}: {ip}')


# In[78]:


runtime_log_msg('localhost','192.168.34')


# In[168]:


def log_decorator(param_func):  #함수 실행하는것으로 변경
    def log_message(*args, **kargs):
        time_str = time.strftime('%c', time.localtime(time.time()))
        print(time_str, end='')
        print(' ===> ', end='')
        return param_func(*args, **kargs)
        
    return log_message


# In[148]:


@log_decorator # closure가 되는 함수 만들어줌
def test_log_msg(): # 함수 선언
    print('This is test log.....')


# In[149]:


@log_decorator 
def runtime_log_msg(host, ip):
    print(f'This is runtime log from {host}: {ip}')


# In[150]:


test_log_msg()


# In[151]:


runtime_log_msg('localhost','192.168.34')


# *변수, **변수

# In[103]:


def f1(a,b , *args):  # *변수 : 나머지 인자를 패킹해서 받아라, 일반 리스트 패킹
        print(a)
        print(b)
        print(args)
        i, j, k = args
        print(i,j,k)


# In[104]:


f1(1,2,3,4,5)


# In[166]:


def key_variale_length(**args): #딕션어리로 패킹
    print(args)
    print("First value is {first}".format(**args))
    print(f"First value is {args.get('first')}")
    print("Second value is {second}".format(**args))
    print("Third value is {third}".format(**args))


# In[105]:


#a = {'first' : 3, 'second' :4,'third':5}
key_variale_length(first=3,second=4,third=5)


# ### Generator

# In[132]:


def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result


# In[133]:


my_nums = square_numbers([1, 2, 3, 4, 5])  # 리소스가 낭비된다.


# In[134]:


print(my_nums)


# In[160]:


def square_numbers(nums):
    for i in nums:
        yield i * i  #원하는 메뉴를 만들수 있는 Generator를 가지고 만든다. 
#커피사장님이 100잔을 주문 받았다 
# 우유 커피콩, 물, 컵 다 따로 가져가서 거기서 만들어주는것이 Generator같은 거


# In[161]:


my_nums = square_numbers([1, 2, 3, 4, 5])


# In[162]:


print(my_nums)  # Generator객체가 튀어나옴


# In[164]:


#print(next(my_nums)) 
# 내부적으로는 next() 함수를 이용해서 출력한다.
for i in my_nums:
    print(i)


# In[ ]:




