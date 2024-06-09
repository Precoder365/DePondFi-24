import os
import random
import shutil

data_path = "Images/"
keypoints_path = "Keypoints/"

# Path to destination folders
train_images_folder = os.path.join(data_path, 'train')
test_images_folder = os.path.join(data_path, 'test')
train_keypoints_folder = os.path.join(keypoints_path, 'train')
test_keypoints_folder = os.path.join(keypoints_path, 'test')

# Define a list of image extensions
image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']

# Create a list of image filenames in 'data_path'
imgs_list = [filename for filename in os.listdir(data_path) if os.path.splitext(filename)[-1] in image_extensions]

# Sets the random seed 
random.seed(42)

# Shuffle the list of image filenames
random.shuffle(imgs_list)

# Determine the number of images for each set
train_size = int(len(imgs_list) * 0.8)
test_size = int(len(imgs_list) * 0.2)

# Create destination folders if they don't exist
for folder_path in [train_images_folder, test_images_folder, train_keypoints_folder, test_keypoints_folder]:
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Copy image and keypoints files to destination folders
for i, img_file in enumerate(imgs_list):
    keypoint_file = os.path.splitext(img_file)[0] + '.txt'
    
    if i < train_size:
        dest_images_folder = train_images_folder
        dest_keypoints_folder = train_keypoints_folder
    else:
        dest_images_folder = test_images_folder
        dest_keypoints_folder = test_keypoints_folder

    shutil.copy(os.path.join(data_path, img_file), os.path.join(dest_images_folder, img_file))
    shutil.copy(os.path.join(keypoints_path, keypoint_file), os.path.join(dest_keypoints_folder, keypoint_file))

print("Dataset split completed!")
