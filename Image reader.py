import os
import shutil

# Specify input and output folder paths
input_folder = 'C:\\Users\\siddi\\Downloads\\archive\\Database1\\Database1'  # Replace with your input folder path
output_folder = 'C:\\Users\\siddi\\OneDrive\\Desktop\\ARMY\\Drones\\images'  # Replace with your output folder path

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# Copy images from input to output folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg','.JPEG', '.png')):  # Check for image extensions
        try:
            source_file = os.path.join(input_folder, filename)
            destination_file = os.path.join(output_folder, filename)
            shutil.copy(source_file, destination_file)

            print(f"Image {filename} copied successfully!")

        except Exception as e:
            print(f"Error copying {filename}: {e}")
