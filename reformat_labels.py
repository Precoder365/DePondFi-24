import os

def append_values_to_labels(input_folder):
    files = os.listdir(input_folder)
    
    for file in files:
        input_filepath = os.path.join(input_folder, file)
        with open(input_filepath, 'r') as infile:
            lines = infile.readlines()
        
        with open(input_filepath, 'w') as outfile:
            for line in lines:
                line = line.strip() + ' 0.1 0.1\n'
                outfile.write(line)

if __name__ == '__main__':
    base_dir = r'C:\DEVELOPMENT\DePondFi-24\data\labels'
    train_folder = os.path.join(base_dir, 'train')
    val_folder = os.path.join(base_dir, 'val')
    
    append_values_to_labels(train_folder)
    append_values_to_labels(val_folder)

    print("Values have been appended to all label files.")
