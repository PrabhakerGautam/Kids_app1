import streamlit as st
import torch
from PIL import Image
import numpy as np
st.set_page_config(page_title="Home",
                   layout='wide',
                   page_icon='./images/object.png')

# Load the saved model
model_path = './models/mnist1_model.pth'
loaded_model = torch.load(model_path, map_location=torch.device('cpu'))

# Define a function to preprocess the input image
def preprocess_image(image):
    image = image.convert('L')  # Convert to grayscale
    image = image.resize((28, 28))
    image = np.array(image) / 255.0  # Normalize pixel values
    image = image.astype(np.float32)
    image = torch.from_numpy(image)
    image = image.view(1, 1, 28, 28)  # Reshape to match the model's input shape
    return image

# Create a Streamlit app
st.title("MNIST Digit Classification App")
st.write("Upload an image and click the 'Classify' button to predict the digit.")



import subprocess

if st.sidebar.button("Draw Images"):
    subprocess.Popen(["python", "Prediction.py"])
        
# Upload an image
drawn_image = './test_images/my_image.png'

# Create a button to classify the uploaded image
if st.button("Classify"):
    if drawn_image is not None:
        # Preprocess the uploaded image
        image = Image.open(drawn_image)
        processed_image = preprocess_image(image)

        # Perform inference using the loaded model
        with torch.no_grad():
            output = loaded_model(processed_image)
            predicted_class = torch.argmax(output, 1).item()

        # Display the classification result
        st.write(f"Predicted Digit: {predicted_class}")

# Optional: You can add further customization and features to the app.

