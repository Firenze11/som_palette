import functions
import classes

pic_file = "wisconsin.jpg"

s_o_m = functions.initialize_som()

functions.draw(s_o_m)

image = classes.Dataset(pic_file)

functions.train(image,s_o_m)

functions.save_som(s_o_m,pic_file)

functions.draw(s_o_m)

functions.reproduce(image,s_o_m,image.size[0],image.size[1])

import db_check

db_check.similar_som()