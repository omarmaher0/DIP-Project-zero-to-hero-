import streamlit as st
from PIL import Image
import cv2
import numpy as np
from Backend import *

#--------------implement Screen-------------
#--------First upload image-----------------
#-----------Convert image to array----------
#---------Second Choose Filter from box-----

def main():
    st.header("Welcome to our project for DIP")
    image_upload = st.file_uploader('Please upload an image file...',type=['jpg','png','jpeg'])
    if image_upload is not None:
        image = Image.open(image_upload)
        image_cv2 = np.array(image)

#------------convert BGR to RGB-------------

        image_cv2 = cv2.cvtColor(image_cv2,cv2.COLOR_BGR2BGRA)

        option = st.selectbox('Select your filter',('Select','Edge Detection','Grayscale','Negative Transformation','Gaussian Blur','Reduce Noise','Sharping'))
        st.write('You selected:',option)

#---------Choose from selectbox------------

        if option == 'Select':
            pass

#--------Edge Detection in selectionbox---
        elif option == 'Edge Detection':
            st.header('Input image')
            st.image(image)
            st.markdown('Image after Edge Detection')
            st.image(edge_detection(image_cv2))

# --------Gray Scale in selectionbox-----

        elif option == 'Grayscale':
            st.header('Input image')
            st.image(image)
            st.markdown('Image after Grayscale')
            st.image(gray_scale(image_cv2))

#------Negative Transformationin selectionbox----------

        elif option == 'Negative Transformation':
            st.header('Input image')
            st.image(image)
            st.markdown('Image after Negative Transformation')
            st.image(negative_transformation(image_cv2))

#------Gaussian Blur in selectionbox-------------------

        elif option =='Gaussian Blur':
            st.header('Input image')
            st.image(image)
            st.markdown('Image after Gaussian Blurring')
            st.image(Gaussian_Blur(image_cv2))

#--------Reduce Noise in selectionbox----------------

        elif option =='Reduce Noise':
            st.header('Input image')
            st.image(image)
            st.markdown('Image after Remove Noise')
            st.image(reduce_noise(image_cv2))

#-----------Sharping in selectionbox----------------

        elif option =='Sharping':
            st.header('Input image')
            st.image(image)
            st.markdown('Image after Sharping')
            st.image(sharp_image(image_cv2))

        else:
            pass

if __name__ =="__main__":
    main()