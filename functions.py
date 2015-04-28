import classes
import random
import math
from PIL import Image

N = 5;
neuron_w = 4
neuron_h = 4 # (neuron_w + neuron_h) must be greater than or equal to 8
max_dist = 3 * 255 * 255
som_dim = 400

a0 = 0.1 #initial learning rate

#TODO: maybe normalize vectors, so that it works with different kind of data - not really necessary

def initialize_som():
    out_map = []
    for i in range(neuron_h):
        out_map.append([])
        for j in range(neuron_w):
            temp_col =classes.Node((random.randint(0,255), random.randint(0,255), random.randint(0,255)), j, i)
            out_map[i].append(temp_col)
    return out_map

def neighborhood(d2, r2):
    return math.exp(-d2 / (2 * r2))

def vec_distance(pv, n):    #pv: pixel vector (to be called with get_vector) , n: node
    return math.sqrt( (pv[0]-n.v[0])*(pv[0]-n.v[0]) + (pv[1]-n.v[1])*(pv[1]-n.v[1]) + (pv[2] - n.v[2])*(pv[2] - n.v[2]))

def winner_node(pv, som):
    d_min = math.sqrt(max_dist)
    for column in som:
        for n in column:
            if vec_distance(pv, n) < d_min:
                winner = n
                d_min = vec_distance(pv, n)
    return winner

def sq_node_distance(n0, n1):
    return (n0.x - n1.x) * (n0.x - n1.x) + (n0.y - n1.y) * (n0.y - n1.y)

def update_node(pv,wn,cn,t):
    _r = radius(t)
    _r2 = _r * _r
    _d2 = sq_node_distance(wn,cn)
    if (_d2 < _r2):
        _a = a(t)
        _n = neighborhood(_d2,_r2)
        v = ()
        for i in xrange(len(pv)):
            new_dim = cn.get_v()[i] + _a * _n * (pv[i]-cn.get_v()[i])
            v = v + (new_dim,)
        cn.set_v(v)

def update_som(som,pv,wn,t):
    for column in som:
        for cn in column:
            update_node(pv, wn,cn,t)

def radius(t):
    return (neuron_w + neuron_h)/4 * math.exp(-t / (N / math.log( (neuron_w + neuron_h)/4) ))

def a(t):
    return a0 * math.exp(-t / N)

def train (data,som):
    for t in xrange(N):
        for i in xrange(len(data)):
            print "t: "+str(t)+", "+"i: "+str(i)
            pixel_v = data.get_vector(i)
            win_n = winner_node(pixel_v, som)
            update_som(som, pixel_v, win_n, t)
    print "training finished" 

def draw (som):
    for i in range(neuron_w):
        for j in range(neuron_h):
            print som[j][i]
    som_im = Image.new('RGB', (neuron_w,neuron_h), None)
    som_val = som_im.load()
    for i in range(neuron_w):
        for j in range(neuron_h):
            som_val[i,j] = som[j][i].get_v()
    som_im2 = som_im.resize((som_dim,som_dim))
    som_im2.show()

def reproduce (data,fin_som,pic_w,pic_h):
    new_im = Image.new('RGB', (pic_w,pic_h), None)
    new_data = new_im.load()
    for i in xrange(len(data)):
        pixel_u = data.get_vector(i)
        win_u = winner_node(pixel_u,fin_som)
        new_data[i%pic_w,i/pic_w] = win_u.get_v()
    new_im.show()


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




