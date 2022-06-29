Data augumentation for traffic signal end-to-end ml model

Whenever we are dealing with data we always come across new terms that makes us thirst to learn whatever it is,it maybe a tabular form of data or it maybe the dta that deals with images likewise here I came across a new word called data augumentation.

Data Augumentation:
     The techniques used to increase the amount of data by adding slightly modified copies of already existing data or newly created synthetic data from existing data.In simple words,adding of new data with the help of existing data.It is mostly quite possible only in image form of dataset.
     
The model here involves many different python libraries like,
  OS
  CV2
  image
  tensorflow.keras and it's most needed libraries that deals with image (that takes us next path to deep learning)
  
  At sometime epochs are given to iterate the model that takes most of the time to train the given model.
  Images are getting preprocessed so that it will be easy to augument the new data at the needed form.
  
  In the end the whole model is loaded by using the library called tensorflow and cv2 along with numpy to reshape the image models.
  
  
  The frontend of the model is develped and deployed through the same python library called streamlit where the respective names are given to predict the given image that is augumented.
