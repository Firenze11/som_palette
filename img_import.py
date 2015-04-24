from PIL import Image

class Dataset:
    def __init__ (self, filename):
        im = Image.open(filename,'r') #Can be many different formats.
        pix = im.load()
        print im.size #Get the width and hight of the image for iterating over
        im.show()
        
        self._data = []
        self._labels = []
        
        for j in xrange(im.size[1]):
            for i in xrange(im.size[0]):
                self._data.append(pix[i,j])
                self._labels.append((i,j))

    def __len__ (self):
        return len (self._data)
    
    def __str__ (self):
        return str (self._data)

    def __getitem__ (self, key):
        return (self._data[key], self._labels[key])

    def data (self):
        return self._data
    
    def labels (self):
        return self._labels
    
    def get_data (self, point):
        return self._data[point]
    
    def get_label (self, point):
        return self._labels[point]

a = Dataset("cat.jpeg")
print a[4]
print a.get_data(4)
print a.get_label(4)

#printing result:
#(259, 194)
#((238, 191, 137), (4, 0))
#(238, 191, 137)
#(4, 0)