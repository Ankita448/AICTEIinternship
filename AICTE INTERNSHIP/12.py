import gdown
print("gdown is installed and working!")


import gdown
import pandas as pd

# Define the file ID from the shared Google Drive link
file_id = "1VTcau-3BifmqJkxuYaMQUcE18D1T2mig"

# Construct the download URL
url = f"https://drive.google.com/uc?id={file_id}"

# Download the file (change "dataset.csv" to match your file type if needed)
output_file = "dataset.csv"
gdown.download(url, output_file, quiet=False)

# Load the dataset into a Pandas DataFrame
dataset = pd.read_csv(output_file)  # Assuming it's a CSV file
print(dataset.head())