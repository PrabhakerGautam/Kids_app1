import streamlit as st
import time
import numpy as np
st.set_page_config(page_title="Home",
                   layout='wide',
                   page_icon='./images/object.png')
# Create a Streamlit app
st.title(" Digit Classification Model Training ")

# Create a sidebar for user input
st.sidebar.header("User Input")

# Define the number of epochs for training
n_epochs = st.sidebar.slider("Number of Epochs", 1, 10, 5)

# Create a button to trigger model training
if st.sidebar.button("Train Model"):
    st.info("Training the model...")

    # Simulate loading animation
    for epoch in range(n_epochs):
        st.write(f"Epoch {epoch + 1}/{n_epochs}: Training in progress...")

        # Training code for each epoch goes here
        # This is a placeholder for training and should be replaced with your actual training code
        time.sleep(2)  # Simulating training for 2 seconds

    st.success("Model training completed!")

    # Optionally, you can add model evaluation and accuracy calculation here

# Add an animation while waiting for user input
st.write("Waiting for user input to trigger model training...")

# Optionally, you can add additional content and explanations
