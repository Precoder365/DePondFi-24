import os

def modify_keypoint_files(input_folder):
    files = os.listdir(input_folder)
    
    for file in files:
        input_filepath = os.path.join(input_folder, file)
        with open(input_filepath, 'r') as infile:
            lines = infile.readlines()
        
        with open(input_filepath, 'w') as outfile:
            for i, line in enumerate(lines):
                label = i % 9  
                x, y = line.strip().split(',')
                outfile.write(f'{label} {x} {y}\n')

if __name__ == '__main__':
    base_dir = r'C:\DEVELOPMENT\DePondFi-24\data\labels'
    train_folder = os.path.join(base_dir, 'train')
    val_folder = os.path.join(base_dir, 'val')
    
    modify_keypoint_files(train_folder)
    modify_keypoint_files(val_folder)

    print("Keypoint files have been modified.")
