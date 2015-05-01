Instructions:

Parameters that can be changed:
In "functions.py"
	N - number of iterations through each pixel
	neuron_w - width of SOM
	neuron_h - height of SOM
		* Note that the sum of neuron_w and neuron_h must be greater than or equal to 8 *
	som_dim - width and height (in pixels) of the printed SOM
	a0 - learning rate

In "run_som.py"
	pic_file - image file (.jpg/.jpeg/.bmp)

To run the code, run "run_som.py" with python. From there, an SOM map will be initialized and shown in the format of a randomized color grid. Then the image to be evaluated will show up and the training begins. After the number of iterations specified at the top of "functions.py", training finishes and the final SOM is shown. The program then recreates the image using the color palette in SOM, and the resulting SOM will be saved into "database.py". After that, the program will look through all the existing SOMs in "database.py" for the one most similar to the current image, and show that image.

It is recommended to not alter code in "database.py" and "database_index.py", as changing the values may make database searching and similar image return impossible.