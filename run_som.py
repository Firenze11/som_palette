import functions
import classes

s_o_m = functions.initialize_som()

functions.draw(s_o_m)

image = classes.Dataset("cat.jpeg")

functions.train(image,s_o_m)

functions.draw(s_o_m)