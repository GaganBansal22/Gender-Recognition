# Gender Recognition

This repository contains a project for recognizing gender using a machine learning model. The project includes data processing, model training, and an interactive user interface.

## Repository Contents

- `Gender_Recognition.ipynb`: A Jupyter Notebook that includes the entire workflow for gender recognition, from data preprocessing to model evaluation.
- `gender_recognition.h5`: The trained model file saved in HDF5 format.
- `streanlitui.py`: A Python script for deploying the model using Streamlit to create an interactive user interface.

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/GaganBansal22/Gender-Recognition.git
   cd Gender_Recognition
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Jupyter Notebook**:
   Open `Gender_Recognition.ipynb` using Jupyter Notebook or Jupyter Lab to explore and run the code.

4. **Run the Streamlit app**:
   ```bash
   streamlit run streanlitui.py
   ```

## Usage

### Jupyter Notebook

The `Gender_Recognition.ipynb` notebook includes the following sections:

1. **Data Loading**: Load and preprocess the dataset.
2. **Model Building**: Define and compile the neural network model.
3. **Model Training**: Train the model on the dataset.
4. **Model Evaluation**: Evaluate the model performance and visualize the results.
5. **Model Saving**: Save the trained model for later use.

### Streamlit App

The Streamlit app (`streanlitui.py`) provides an interactive interface to upload images and get gender predictions using the trained model. Run the app using the command mentioned above and follow the instructions on the interface.

## Results

![accuracy](https://github.com/user-attachments/assets/bfe8f131-3560-46ec-ad12-764d950ce917)

![loss](https://github.com/user-attachments/assets/9e19f2d8-7275-4fdd-ba89-d7f6b081b23c)
