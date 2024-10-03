# Signature Forgery Detection

**Author-@sunilrathod098** (Danavath Sunil Rathod)

- This project is a **Signature Forgery Detection** system built using **Flask**, **PyTorch**, and **PIL** (Python Imaging Library). 
- The system allows users to upload an original signature image and a potentially forged signature image, and then determines whether the two images are identical or if the second image is forged.

## Features

- **Upload Signatures**: Users can upload both the original and the supposed fake signatures.
- **Forgery Detection**: The model predicts whether the second signature is a forgery or the same as the original.
- **Accuracy**: Displays the confidence and accuracy of the prediction.
- **Web Interface**: A clean, responsive UI built using HTML and CSS for ease of use.
  
## Technologies Used

- **Flask**: Backend framework for serving the web interface and handling file uploads.
- **PyTorch**: Used for model inference to detect signature forgery.
- **PIL (Python Imaging Library)**: For image processing and manipulation.
- **HTML/CSS**: For building the front-end interface.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Flask
- PyTorch
- Pillow (PIL)

You can install the required packages using the following commands:

pip install flask
pip install torch
pip install pillow



## Running the Application

- Clone the Repository:
- git clone https://github.com/sunilrathod098/signature_verification.git

- Navigate to the project directory:
- **cd signature-forgery-detection**

- Run the Flask application:
- python app.py

- Open a browser and navigate to **http://127.0.0.1:5000** to use the Signature Forgery Detection interface.

## Project Structure


= │Signature_Verification_Frogery_Detection
- |
- ├── app.py                     # Main application script
- ├── model.py                   # Model definition
- ├── utils.py                   # Utility functions for image processing- 
- ├── train.py                   # Script for training the model (if applicable)
- ├── static/                    # Static assets (CSS, JS, images)
- ├── templates/                 # HTML templates for Flask
- ├── sign_data/                 # Folder containing signature images (optional)
- └── model.pt                   # Pre-trained model file
- └── Readme.md
- └──Documentation_Project.md
## Example

- Upload two signature images.
- Click the Identify Forgery button.
- The system will output whether the signatures are the same or forged, along with the confidence level.


## Model Details
- The model is a neural network built using PyTorch, which has been trained on a dataset of signatures to recognize forgeries. The output is a softmax probability indicating the likelihood of forgery.

##Future Implementations

- *Real-time detection* using webcam input.
- *User authentication* for storing past verification results.
- *Mobile app* for signature detection on the go.
- *API development* for integration into external systems.

## Contributions
- Feel free to open issues or submit pull requests for improvements or bug fixes.

## License
- This project is licensed under the MIT License. See the LICENSE file for details.

## Instructions:

- Replace the placeholder GitHub URL (`https://github.com/sunilrathod098/signature_verification.git`).
- Add a screenshot of the web background interface in the `static/frogery.png` file as referenced in the `README.md`.


