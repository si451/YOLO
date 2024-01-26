import os
import shutil
import random

# Folder paths
#image_folder = 'C:\\Users\\siddi\\OneDrive\\Desktop\\ARMY\\Drones\\images' 
label_folder = 'C:\\Users\\siddi\\OneDrive\\Desktop\\ARMY\\Fighter jets\\Labels\\train'

# Create train, validation, and test folders
#os.mkdir('train_images')
#os.mkdir('val_images')
#os.mkdir('test_images')
os.mkdir('train_labels')
os.mkdir('val_labels')
os.mkdir('test_labels')

# Get list of all images and labels
#images = os.listdir(image_folder)
labels = os.listdir(label_folder)  # Uncomment if using a separate labels folder

# Shuffle with the same seed
#random.seed(230)
#random.shuffle(images)
random.seed(230)
random.shuffle(labels)

# Split datasets 70% - 15% - 15%
#split_train = int(0.7 * len(images))
#split_val = int(0.85 * len(images))

#train_images = images[:split_train]
#val_images = images[split_train:split_val]
#test_images = images[split_val:]
split_train = int(0.7 * len(labels))
split_val = int(0.85 * len(labels))
train_labels = labels[:split_train]  # Uncomment if using a separate labels folder
val_labels = labels[split_train:split_val]
test_labels = labels[split_val:]

# Move images and labels to respective folders
#for image in train_images:
    #shutil.move(os.path.join(image_folder, image), os.path.join('train_images', image))

#for image in val_images:
    #shutil.move(os.path.join(image_folder, image), os.path.join('val_images', image))

#for image in test_images:
    #shutil.move(os.path.join(image_folder, image), os.path.join('test_images', image))

# Uncomment and adjust the following lines if using a separate labels folder:
for label in train_labels:
    shutil.move(os.path.join(label_folder, label), os.path.join('train_labels', label))

for label in val_labels:
     shutil.move(os.path.join(label_folder, label), os.path.join('val_labels', label))

for label in test_labels:
     shutil.move(os.path.join(label_folder, label), os.path.join('test_labels', label))
