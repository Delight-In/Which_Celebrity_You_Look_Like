from keras_vggface.utils import preprocess_input
from keras_vggface.vggface import VGGFace
from src.utils import read_yaml, create_directory
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
from PIL import Image
import os
import cv2
from mtcnn import MTCNN
import numpy as np
import logging

# Setup logging
logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(log_dir, 'app_logs.log'), 
    level=logging.INFO, 
    format=logging_str,
    filemode="a"
)

# Reading config and parameters
config = read_yaml('config/config.yaml')
params = read_yaml('params.yaml')

artifacts = config['artifacts']
artifacts_dir = artifacts['artifacts_dir']

# Upload image directory
upload_image_dir = artifacts['upload_image_dir']
uploadn_path = os.path.join(artifacts_dir, upload_image_dir)

# Pickle file directory and image pickle file
pickle_format_data_dir = artifacts['pickle_format_data_dir']
img_pickle_file_name = artifacts['img_pickle_file_name']

raw_local_dir_path = os.path.join(artifacts_dir, pickle_format_data_dir)
pickle_file = os.path.join(raw_local_dir_path, img_pickle_file_name)

# Feature extraction path and name
feature_extraction_dir = artifacts['feature_extraction_dir']
extracted_features_name = artifacts['extracted_features_name']

feature_extraction_path = os.path.join(artifacts_dir, feature_extraction_dir)
features_name = os.path.join(feature_extraction_path, extracted_features_name)

# Model parameters
model_name = params['base']['BASE_MODEL']
include_tops = params['base']['include_top']
input_shapes = params['base']['input_shape']
poolings = params['base']['pooling']

# Initialize MTCNN face detector and VGGFace model
detector = MTCNN()
model = VGGFace(model=model_name, include_top=include_tops, input_shape=(224, 224, 3), pooling=poolings)

# Load feature list and filenames from pickle files
feature_list = pickle.load(open(features_name, 'rb'))
filenames = pickle.load(open(pickle_file, 'rb'))

# Function to save uploaded image
def save_uploaded_image(uploaded_image):
    try:
        create_directory(dirs=[uploadn_path])

        with open(os.path.join(uploadn_path, uploaded_image.name), 'wb') as f:
            f.write(uploaded_image.getbuffer())
        logging.info(f"Image {uploaded_image.name} saved successfully.")
        return True
    except Exception as e:
        logging.error(f"Error saving image: {e}")
        return False

# Function to extract features from the uploaded image
def extract_features(img_path, model, detector):
    img = cv2.imread(img_path)
    
    if img is None:
        logging.error(f"Failed to load image: {img_path}")
        return None

    results = detector.detect_faces(img)
    
    if len(results) == 0:
        logging.error("No faces detected.")
        return None

    x, y, width, height = results[0]['box']
    face = img[y:y + height, x:x + width]

    # Extract features from the face region
    image = Image.fromarray(face)
    image = image.resize((224, 224))

    face_array = np.asarray(image)
    face_array = face_array.astype('float32')

    expanded_img = np.expand_dims(face_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img)
    result = model.predict(preprocessed_img).flatten()
    
    return result

# Function to recommend the most similar image
def recommend(feature_list, features):
    similarity = []
    
    if len(feature_list) == 0:
        logging.error("Feature list is empty.")
        return None

    for i in range(len(feature_list)):
        if features is None or feature_list[i] is None:
            logging.error(f"Invalid features at index {i}.")
            continue
        similarity.append(cosine_similarity(features.reshape(1, -1), feature_list[i].reshape(1, -1))[0][0])

    if len(similarity) == 0:
        logging.error("No similarity values computed.")
        return None

    index_pos = sorted(list(enumerate(similarity)), reverse=True, key=lambda x: x[1])[0][0]
    return index_pos

# Streamlit app setup
st.title('To whom does your face match?')

uploaded_image = st.file_uploader('Choose an image')

if uploaded_image is not None:
    # Save the image
    if save_uploaded_image(uploaded_image):
        # Load the image and display
        display_image = Image.open(uploaded_image)
        st.image(display_image, caption="Uploaded Image", use_column_width=True)

        # Extract features from the uploaded image
        features = extract_features(os.path.join(uploadn_path, uploaded_image.name), model, detector)
        
        if features is not None:
            # Recommend similar image based on cosine similarity
            index_pos = recommend(feature_list, features)

            if index_pos is not None:
                predicted_actor = " ".join(os.path.basename(filenames[index_pos]).split('_'))
                st.header(f"Seems like {predicted_actor}")

                # Display the predicted celebrity image
                st.image(filenames[index_pos], width=300)
            else:
                st.error("Unable to recommend a match.")
        else:
            st.error("Failed to extract features from the uploaded image.")
