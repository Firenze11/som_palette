
# coding: utf-8

# In[3]:

from PIL import Image

class Dataset:
    def __init__ (self, filename):
        im = Image.open(filename,'r') #Can be many different formats.
        pix = im.load()
        #print im.size #Get the width and hight of the image for iterating over
        im.show()
        im.thumbnail((40,30))
        
        self.size = im.size
        self._vectors = []
        self._labels = []
        
        for j in xrange(im.size[1]):
            for i in xrange(im.size[0]):
                self._vectors.append(pix[i,j])
                self._labels.append((i,j))

    def __len__ (self):
        return len (self._vectors)
    
    def __str__ (self):
        return str (self._vectors)

    def __getitem__ (self, key):
        return (self._vectors[key], self._labels[key])

    def size (self):
        return self.size

    def vectors (self):
        return self._vectors
    
    def labels (self):
        return self._labels
    
    def get_vector (self, point):
        return self._vectors[point]
    
    def get_label (self, point):
        return self._labels[point]

#a = Dataset("cat.jpeg")
#print a.size
#print a[4]
#print a.get_vector(4)
#print a.get_label(4)



class Node:
    def __init__ (self, _v, _x, _y):
        self.v = _v
        self.x = _x
        self.y = _y
    
    def __str__ (self):
        return str (self.v)
    
    def set_v (self, v):
        new_v = ()
        for i in xrange(len(v)):
            new_dim = int(round(v[i]))
            new_v = new_v + (new_dim,)
        self.v = new_v
        
    def get_v (self):
        return self.v
        
    def set_pos (self, pos):
        self.x = pos[0]
        self.y = pos[1]
        
    def get_pos (self):
        return (self.x, self.y)

'''    
class SOM:
    def __init__ (self, w, h)
        self.node = []
        for i in range(h):
            self.node.append([])
            for j in range(w):
                temp_node = new Node((random.randint(0,255), random.randint(0,255), random.randint(0,255)), j, i)
                self.node[i].append(temp_node)
                
    
    def __len__ (self):
        return (len (self.node), len (self.node[0])
    
    def __str__ (self):
        return str ("som")

    def __getitem__ (self, i, j):
        return (self.node[i][j])
'''


# In[ ]:



