
# coding: utf-8

# In[199]:

import classes
import random
import math
from PIL import Image

# In[200]:

neuron_w = 4
neuron_h = 4
max_dist = 3 * pow(255,2)

a0 = 0.1 #initial learning rate

#TODO: round result vectors, so that colors have tuples of integers
'''
We did this! In the last loop of the code (last 10 lines)
'''
#TODO: maybe normalize vectors, so that it works with different kind of data - not really necessary

def initialize_som():
    out_map = []
    for i in range(neuron_h):
        out_map.append([])
        for j in range(neuron_w):
            temp_col =classes.Node((random.randint(0,255), random.randint(0,255), random.randint(0,255)), j, i)
            out_map[i].append(temp_col)
    return out_map


# In[201]:

def neighborhood(wn,cn,t,N):
    return math.exp(-sq_node_distance(wn,cn)/ (2 * radius(t,N) * radius(t,N)))


# In[202]:

def vec_distance(pv, n):    #pv: pixel vector (to be called with get_vector) , n: node
    return math.sqrt(math.pow(pv[0] - n.v[0], 2) + math.pow(pv[1] - n.v[1], 2) + math.pow(pv[2] - n.v[2], 2))


# In[203]:

def winner_node(pv, som):
    d_min = math.sqrt(max_dist)
    for column in som:
        for n in column:
            if vec_distance(pv, n) < d_min:
                winner = n
                d_min = vec_distance(pv, n)
    return winner


# In[204]:

def sq_node_distance(n0, n1):
    return math.pow(n0.x - n1.x, 2) + math.pow(n0.y - n1.y, 2)


# In[205]:

def update_node(pv,wn,cn,t,N):
    _a = a(t,N)
    _n = neighborhood(wn,cn,t,N)
    v = ()
    for i in xrange(len(pv)):
        new_dim = cn.get_v()[i] + _a * _n * (pv[i]-cn.get_v()[i])
        v = v + (new_dim,)
    cn.set_v(v)


# In[206]:

def update_som(som,pv,wn,t,N):
    for column in som:
        for cn in column:
            update_node(pv, wn,cn,t,N)


# In[207]:

def radius(t,N):
    return (neuron_w + neuron_h)/4 * math.exp(-t / (N / math.log( (neuron_w + neuron_h)/4) ))


# In[208]:

def a(t,N):
    return a0 * math.exp(-t / N)


# In[209]:


s_o_m = initialize_som()


# In[210]:



# In[211]:

image = classes.Dataset("cat.jpeg")


# In[212]:

def train (data,som):
    N = 5;
    for t in xrange(N):
        for i in xrange(len(data)):
            print "t: "+str(t)+", "+"i: "+str(i)
            pixel_v = data.get_vector(i)
            win_n = winner_node(pixel_v, som)
            update_som(som, pixel_v, win_n, t, N)
    print "training finished" 
    for i in range(neuron_h):
        for j in range(neuron_w):
            print som[i][j]

# In[142]:


train(image,s_o_m)

im3 = Image.new('RGB', (neuron_w,neuron_h), None)
pix3 = im3.load()

for i in range(neuron_h):
    for j in range(neuron_w):
        lst = list(s_o_m[i][j].get_v())
        tup = []
        for k in range(len(lst)):
            tup[len(tup):] = [int(round(s_o_m[i][j].get_v()[k]))]
        rgbtup = tuple(tup)
        pix3[j,i] = rgbtup



im3.show()




# In[Reproduction]:

def reproduce (data,fin_som,pic_w,pic_h,som_w,som_h):
    im4 = Image.new('RGB', (pic_w,pic_h), None)
    pix4 = im4.load()
    fin_array = []
    for i in xrange(len(data)):
        pixel_u = data.get_vector(i)
        win_u = winner_node(pixel_u,fin_som)
        fin_array
        for x in range(pic_w):
            for y in range(pic_h):
                lst = list(fin_som[x][y].get_v())
                tup = []
                for z in range(len(lst)):
                    tup[len(tup):] = [int(round(fin_som[x][y].get_v()[z]))]
                rgbtup = tuple(tup)
        pix4[i/pic_w,i%pic_w] = win_u.get_v()
    pix4.show()

reproduce(image,s_o_m,image.size[0],image.size[1],neuron_w,neuron_h)

'''
for x in range(image.size[0]):
    for y in range(image.size[1]):
        lst = list(s_o_m[i][j].get_v())
        tup = []
        for k in range(len(lst)):
            tup[len(tup):] = [int(round(s_o_m[i][j].get_v()[k]))]
        rgbtup = tuple(tup)
        pix4[x,y] = reproduce(image,s_o_m,image.size[0],image.size[1])
'''




