TITLE: Plant Seedling Classification using CNN in Keras

OVERVIEW
The project focuses on creating a CNN - (Convolutional Neural Network) model to classify any given image into 12 classes i.e., 12 plant species. It has been trained, validated and tested on a dataset of 4750 images and gives an accuracy of 72% on test data.
REQUIREMENTS
This project requires : 

~ A diverse and detailed dataset containing the images and their class or species name.
~ A deep learning model - CNN that takes in an image of a plant seedling as input and outputs a category from the 12 species it's trained on.
~ The code required for the model needs: 
~ Languages:
	~ Python
~ Libraries: 
~ Pandas (to manage dataframe),
~ Numpy (for numerous calculations),
~ Scikit Learn (for predicting accuracy etc),
~ Keras (for creating deep learning model),
~ Seaborn and Matplotlib ( for visualization of data and results)
~ An IDE to work on like Spyder or Google Colab

GUIDE TO USE
Make sure the python notebook and the h5 model file are in the same directory and the libraries mentioned above have been installed in preferably a new conda environment.
If you’re using google colabotary then, simply upload the h5 file to the same directory in which the python notebook is present.
Run the code cell which imports all the libraries.
Run the code cell under the ‘Loading Model’ heading.
Now load the image you want to predict on.
Pass the image in the custom predict function.
The output is the prediction.

CODE LIMITATIONS:
Since it was specifically asked to split the data such that the training set comprised only 50% of the data, the accuracy took a hit.
This was primarily because some classes already had very less instances of images available and the split reduced the training data even more. So the classification power of some classes became less than expected.

FURTHER WORK:
Since the data was provided in the form of a numpy file, Image data generators couldn’t be used as Image Datagens require the data to be present in a particular directory structure.
With the availability of the dataset in the raw form and with the training set comprising about 70% of the data, an accuracy of about 90% would be achievable.
