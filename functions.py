
# coding: utf-8

# In[199]:

import classes
import random
import math


# In[200]:

def initialize_som(w, h):
    out_map = []
    for i in range(h):
        out_map.append([])
        for j in range(w):
            temp_col =classes.Node((random.randint(0,255), random.randint(0,255), random.randint(0,255)), j, i)
            out_map[i].append(temp_col)
    return out_map


# In[201]:

def neighborhood(wn,cn,t,w,h,N):
    return math.exp(-node_distance(wn,cn) * node_distance(wn,cn)/ (2 * radius(t,w,h,N) * radius(t,w,h,N)))


# In[202]:

def vec_distance(pv, n):    #pv: pixel vector (to be called with get_vector) , n: node
    return math.sqrt(math.pow(pv[0] - n.v[0], 2) + math.pow(pv[1] - n.v[1], 2) + math.pow(pv[2] - n.v[2], 2))


# In[203]:

def winner_node(pv, som):
    d_min = math.sqrt(195075)
    for column in som:
        for n in column:
            if vec_distance(pv, n) < d_min:
                winner = n
                d_min = vec_distance(pv, n)
    return winner


# In[204]:

def node_distance(n0, n1):
    return math.sqrt(math.pow(n0.x - n1.x, 2) + math.pow(n0.y - n1.y, 2))


# In[205]:

def update_node(pv,wn,cn,t,w,h,N):
    _a = a(t,N)
    _n = neighborhood(wn,cn,t,w,h,N)
    v = ()
    for i in xrange(len(pv)):
        new_dim = cn.get_v()[i] + _a * _n * (pv[i]-cn.get_v()[i])
        v = v + (new_dim,)
    cn.set_v(v)


# In[206]:

def update_som(som,pv,wn,t,w,h,N):
    for column in som:
        for cn in column:
            update_node(pv, wn,cn,t,w,h,N)


# In[207]:

def radius(t,w,h,N):
    return (w+h)/4 * math.exp(-t / (N / math.log( (w+h)/4) ))


# In[208]:

def a(t,N):
    return 0.1 * math.exp(-t / N)


# In[209]:

s_o_m = initialize_som(5,6)


# In[210]:

print s_o_m


# In[211]:

image = classes.Dataset("cat.jpeg")


# In[212]:

def train (data,som,w,h):
    N = 100;
    for t in xrange(N):
        for i in xrange(len(data)):
            pixel_v = data.get_vector(i)
            win_n = winner_node(pixel_v,som)
            update_som(som,pixel_v,win_n,t,w,h,N)
        


# In[142]:

train(image,s_o_m,5,6)


# In[ ]:



