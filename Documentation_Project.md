# Project Documentation: Signature Forgery Detection


## Overview
- The Signature Forgery Detection project leverages deep learning techniques to identify forged signatures by comparing an original signature image against a suspected fake. The project uses Flask as the web framework, PyTorch for deep learning model implementation, and PIL (Python Imaging Library) for image processing. The system processes both images, predicts whether the second image is forged or not, and provides a result with accuracy and confidence levels.

## Key Features
- Upload and process two images: an original signature and a potentially forged one.
- Perform forgery detection using a pre-trained deep learning model.
- Display the result with a confidence score.
- Intuitive and user-friendly web interface.

## Technologies Used
- Flask: For building the web application and handling requests.
- PyTorch: For deep learning model (convolutional neural network) used to predict forgery.
- PIL (Pillow): For image processing.
- HTML/CSS/JavaScript: For the web interface.

## System Requirements
- Python 3.x
- Flask
- PyTorch
- Pillow
- Numpy

## Project Structure
- app.py: Main Flask application file to handle routes and image processing logic.
- model.py: Deep learning model implementation using PyTorch.
- utils.py: Helper functions for processing images.
- static/: Contains static resources such as images.
- templates/: Contains HTML templates for the web interface.

## How It Works
- The user uploads two signature images: one original and one fake.
- The server processes the images, resizes them, and converts them to grayscale.
- The images are passed through a pre-trained convolutional neural network (CNN).
- The model predicts whether the second image is forged or identical, displaying a confidence score.
Model Details
- The model used is a pre-trained CNN that has been fine-tuned for signature forgery detection.

### The model is a Convolutional Neural Network (CNN) with multiple layers:

- Three convolutional layers for feature extraction.
- Fully connected layers for decision-making.
- Uses ReLU activation functions and Dropout for regularization.
- Optimized using Adam optimizer and cross-entropy loss.
- Trained on a dataset of genuine and forged signatures.
- Fine-tuned for signature forgery detection.

## Training:

- The model was trained on a signature dataset using an Adam optimizer with cross-entropy loss.
- Training and test sets were processed to compute grayscale and color mean and standard deviations for normalization.

## Future Implementations
- `Real-time Signature Verification`: Extend the system to process signatures in real-time, possibly using webcam input.
- `Enhanced Model Training`: Incorporate more complex neural networks (e.g., ResNet) for improved accuracy.
- `User Management`: Add authentication and user profiles to store past verification results.
- `Mobile Integration`: Develop a mobile application to allow users to verify signatures on the go.
- `API Deployment`: Create an API for external systems to integrate signature forgery detection.