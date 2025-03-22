from src.utils import read_yaml, create_directory
import argparse
import os
import logging
from tensorflow.keras.preprocessing import image
from keras_vggface.utils import preprocess_input
from keras_vggface.vggface import VGGFace
import numpy as np
import pickle
from tqdm import tqdm

# Logging Setup
logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(log_dir, 'running_logs.log'), 
    level=logging.DEBUG,  # Set to DEBUG for more verbose logging
    format=logging_str,
    filemode="a"
)

# Function to collect all image paths from directories
def collect_image_paths(root_dir):
    image_paths = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):  # Handles common image extensions
                image_paths.append(os.path.join(root, file))
    return image_paths

# Function to extract features from an image
def extractor(img_path, model):
    try:
        img = image.load_img(img_path, target_size=(224, 224))
    except Exception as e:
        logging.error(f"Error loading image: {img_path}. Error: {e}")
        return None  # Skip this file if there is an issue
    
    img_array = image.img_to_array(img)
    expanded_img = np.expand_dims(img_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img)

    result = model.predict(preprocessed_img).flatten()
    return result

# Main function to extract features
def feature_extractor(config_path, params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    artifacts = config['artifacts']
    artifacts_dir = artifacts['artifacts_dir']
    pickle_format_data_dir = artifacts['pickle_format_data_dir']
    img_pickle_file_name = artifacts['img_pickle_file_name']

    # Collect image paths from the dataset
    dataset_dir = os.path.join(artifacts_dir, "dataset")  # Root directory for your dataset
    filenames = collect_image_paths(dataset_dir)
    logging.info(f"Collected {len(filenames)} image paths from the dataset.")

    # Check if images were found
    if not filenames:
        logging.error("No images found in the dataset directory!")
        return

    model_name = params['base']['BASE_MODEL']
    include_tops = params['base']['include_top']
    input_shapes = params['base']['input_shape']
    poolings = params['base']['pooling']

    # Load VGGFace model
    model = VGGFace(model=model_name, include_top=include_tops, input_shape=(224, 224, 3), pooling=poolings)
    logging.info(f"Model {model_name} loaded successfully.")

    # Prepare feature extraction paths
    feature_extraction_dir = artifacts['feature_extraction_dir']
    extracted_features_name = artifacts['extracted_features_name']

    feature_extraction_path = os.path.join(artifacts_dir, feature_extraction_dir)
    create_directory(dirs=[feature_extraction_path])

    features_name = os.path.join(feature_extraction_path, extracted_features_name)

    features = []

    # Extract features for each image
    for file in tqdm(filenames, desc="Extracting features"):
        if os.path.exists(file):  # Ensure file exists before extracting features
            result = extractor(file, model)
            if result is not None:
                features.append(result)
            else:
                logging.warning(f"Skipping file {file} due to loading or prediction error.")
        else:
            logging.warning(f"File {file} does not exist. Skipping.")

    # Save features to pickle
    if features:
        pickle.dump(features, open(features_name, 'wb'))
        logging.info(f"Features extracted and saved to {features_name}.")
    else:
        logging.warning("No features were extracted. Check the logs for issues.")

# Entry point for running the script
if __name__ == '__main__':
    # Argument parser to accept paths for config and params
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args = args.parse_args()
    
    try:
        logging.info("stage_02 started: Feature_Extractor")
        feature_extractor(config_path=parsed_args.config, params_path=parsed_args.params)
        logging.info("stage_02 completed!")
    except Exception as e:
        logging.exception(e)
        raise e
