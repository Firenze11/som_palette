import functions
import classes

s_o_m = functions.initialize_som()

functions.draw(s_o_m)

image = classes.Dataset("americangothic.jpg")

functions.train(image,s_o_m)

functions.draw(s_o_m)

functions.reproduce(image,s_o_m,image.size[0],image.size[1])