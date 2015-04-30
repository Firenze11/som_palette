import math
import database_index
from PIL import Image

def rgb_distance(a, b):
    return math.sqrt( (a[0]-b[0])*(a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1]) + (a[2] - b[2])*(a[2] - b[2]))

def similar_som():
	RGB_vals = []
	som = database_index.som
	for h in range(len(som)):
		var_R = 0
		var_G = 0
		var_B = 0
		for i in range(len(som[h][1])):
			for j in range(len(som[h][1][i])):
				if j == 0:
					var_R = var_R + som[h][1][i][j]
				elif j == 1:
					var_G = var_G + som[h][1][i][j]
				elif j == 2:
					var_B = var_B + som[h][1][i][j]
		RGB_vals.append((var_R/(som[h][2]),var_G/(som[h][2]),var_B/(som[h][2])))

	print RGB_vals



	#print vec_distance(RGB_vals[0],RGB_vals[1])
	a = len(som)
	som_num1 = som[a-1]

	im = Image.open(som_num1[0],'r')
	pix = im.load()
	im.show()

	distances = []
	for i in range(len(RGB_vals)-1):
		distances.append(rgb_distance(RGB_vals[len(RGB_vals)-1],RGB_vals[i]))
	print distances
	b = distances.index(min(distances))
	som_num2 = som[b]

	im2 = Image.open(som_num2[0],'r') #Can be many different formats.
	pix2 = im2.load()
	im2.show()

'''
som_im = Image.new('RGB', (10,10), None)
som_val = som_im.load()
for i in range(10):
    for j in range(10):
        som_val[i,j] = som11[1][10*i + j]
som_im.show()

def winner_node(pv, som):
    d_min = math.sqrt(max_dist)
    for column in som:
        for n in column:
            if vec_distance(pv, n) < d_min:
                winner = n
                d_min = vec_distance(pv, n)
    return winner
    '''