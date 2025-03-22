# Project Name: Which Bollywood Celebrity You look like

A Deep learning based streamlit web app which can tell with which bollywood celebrity your face resembles.

In this project, you will discover the problem of face recognition and how deep learning methods can achieve superhuman performance to identify similar faces.

This is a methods of identifying similar faces check various aspects on pictures, including: face shape, nose, eyes and mouth; face position in the picture; skin color (including the lighting of the photo); color and hair and cosine_similarity.

# Dataset has been used:
https://www.kaggle.com/sushilyadav1998/bollywood-celeb-localized-face-dataset


# STEPS to run this project:

You can also use others images instead of bollywood actress

## STEP 01: 
Clone the repository

```bash
git clone 
```

## STEP 02: 
Create an environment

```bash
conda create -n env python=3.8 -y
```

## STEP 03: 
Install the requirements

```bash
pip install -r requirements.txt
```

## STEP 04: 
Download the data from the link and keep it in your project directory. Make sure all the actress folder should be in just one folder called data.

## STEP 05: 
Just execute this command one time if you are not changing the data

```bash
python run.py
```

## STEP 06: 
Now to start the webapp run the following command

```bash
streamlit run app.py
```
