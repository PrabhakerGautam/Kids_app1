import streamlit as st
import subprocess
import os
from PIL import Image
import time

st.set_page_config(page_title="Home",
                   layout='wide',
                   page_icon='./images/object.png')






def main():
    st.title("Let's Generate DataSet for Computer Model ")
    
    st.subheader(" Press Draw Images below") 
    st.write("Start drawing on the Canvas Opening Shortly")
    st.write("Try save atleast 5 images for your particular digit ")
    
    if st.sidebar.button("Draw Images"):
        subprocess.Popen(["python", "ScreenApp.py"])
        
        
    if st.sidebar.button("Show Images"):
        time.sleep(5)
        st.success("Showing All Images")
        display_images() 
    
    if st.sidebar.button("Clear Images"):
       clear_images("./images_folder")    
    
        
    
   
def clear_images(folder_path):
    try:
        for filename in os.listdir(folder_path):
            if filename.endswith(".png"):
                file_path = os.path.join(folder_path, filename)
                os.remove(file_path)
        st.success("All images cleared successfully.")
    except Exception as e:
        st.error(f"Failed to clear images: {str(e)}")

def display_images():
    saved_images = [f for f in os.listdir("./images_folder") if f.endswith(".png")]
    if saved_images:
        st.subheader("Saved Images")
        num_columns = 4  # Number of columns in the grid
        rows = [saved_images[i:i + num_columns] for i in range(0, len(saved_images), num_columns)]

        for row in rows:
            st.write("".join([f"| {image_file} " for image_file in row]))
            for image_file in row:
                image_path = os.path.join("./images_folder", image_file)
                img = Image.open(image_path)
                st.image(img, caption=image_file, use_column_width=True)
# Streamlit app code...

if __name__ == "__main__":
    main()
