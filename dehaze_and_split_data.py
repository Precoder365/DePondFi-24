import os
import cv2
import natsort
import shutil
import random
from lab_stretch import lab_stretching
from rgb_stretch import rgb_stretching

def process_image(input_folder, output_folder):
    files = os.listdir(input_folder)
    files = natsort.natsorted(files)

    for file in files:
        input_filepath = os.path.join(input_folder, file)
        if os.path.isfile(input_filepath):
            img = cv2.imread(input_filepath)

            img = rgb_stretching(img)
            img = lab_stretching(img)

            output_filepath = os.path.join(output_folder, file)
            cv2.imwrite(output_filepath, img)

def split_dataset(images_folder, keypoints_folder, train_images_folder, val_images_folder, train_labels_folder, val_labels_folder, split_ratio=0.8, seed=42):
    random.seed(seed)  
    images = natsort.natsorted(os.listdir(images_folder))
    random.shuffle(images)
    
    train_size = int(len(images) * split_ratio)
    train_images = images[:train_size]
    val_images = images[train_size:]

    for image in train_images:
        image_path = os.path.join(images_folder, image)
        label_path = os.path.join(keypoints_folder, image.replace('.jpg', '.txt'))
        
        if os.path.exists(image_path) and os.path.exists(label_path):
            shutil.move(image_path, train_images_folder)
            shutil.move(label_path, train_labels_folder)

    for image in val_images:
        image_path = os.path.join(images_folder, image)
        label_path = os.path.join(keypoints_folder, image.replace('.jpg', '.txt'))

        if os.path.exists(image_path) and os.path.exists(label_path):
            shutil.move(image_path, val_images_folder)
            shutil.move(label_path, val_labels_folder)

if __name__ == '__main__':
    base_dir = r'C:\DEVELOPMENT\DePondFi-24'
    raw_images_folder = os.path.join(base_dir, r"DePondFi'24_Train\Images")
    keypoints_folder = os.path.join(base_dir, r"DePondFi'24_Train\Keypoints")
    preprocessed_images_folder = os.path.join(base_dir, "Preprocessed_images")
    train_images_folder = os.path.join(base_dir, r"data\images\train")
    val_images_folder = os.path.join(base_dir, r"data\images\val")
    train_labels_folder = os.path.join(base_dir, r"data\labels\train")
    val_labels_folder = os.path.join(base_dir, r"data\labels\val")

    if not os.path.exists(preprocessed_images_folder):
        os.makedirs(preprocessed_images_folder)
    
    if not os.path.exists(train_images_folder):
        os.makedirs(train_images_folder)

    if not os.path.exists(val_images_folder):
        os.makedirs(val_images_folder)

    if not os.path.exists(train_labels_folder):
        os.makedirs(train_labels_folder)

    if not os.path.exists(val_labels_folder):
        os.makedirs(val_labels_folder)

    process_image(raw_images_folder, preprocessed_images_folder)
    split_dataset(preprocessed_images_folder, keypoints_folder, train_images_folder, val_images_folder, train_labels_folder, val_labels_folder)

    shutil.rmtree(preprocessed_images_folder)
    shutil.rmtree(os.path.join(base_dir, r"DePondFi'24_Train"))
