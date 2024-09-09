from flask import Flask, request, render_template, redirect
from io import BytesIO
from PIL import Image
import torch
from utils import process_pil
from model import Network
import warnings

    # Ignore FutureWarnings from PyTorch
warnings.filterwarnings("ignore", category=FutureWarning)

    # # Initialize the Flask app with a custom static folder
    # app = Flask(__name__, static_folder='your_static_folder')
app = Flask(__name__, static_folder='static')


    # Initialize and load the model
net = Network()
net.load_()  # Use the method for loading the model weights

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original = request.files.get('original')
        fake = request.files.get('fake')

        if not original or not fake:
            return redirect('/')

            # Open images
        original_image = Image.open(BytesIO(original.read()))
        fake_image = Image.open(BytesIO(fake.read()))

            # Process images
        original_image = process_pil(original_image)
        fake_image = process_pil(fake_image)

            # Make predictions
        pred = torch.softmax(net(original_image, fake_image).squeeze(), 0)  # get probabilities
        out = pred.argmax()

            # Prepare result message
        result =f'<div style="display: flex; flex-direction: column; align-items: center; text-align: center;">' \
                f'<span style="color: {"red" if out == 1 else "green"}; font-size: 24px;">{"Forged" if out == 1 else "Same"}</span><br>' \
                f'<span style="color: {"red" if out == 1 else "green"}; font-size: 24px;">Accuracy Score=0.9536-------------------Confidence: {pred.max() * 100:.2f}%</span></div>'

        return result

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
