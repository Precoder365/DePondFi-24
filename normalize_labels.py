import os

def normalize_labels(input_folder):
    files = os.listdir(input_folder)
    
    for file in files:
        input_filepath = os.path.join(input_folder, file)
        with open(input_filepath, 'r') as infile:
            lines = infile.readlines()
        
        with open(input_filepath, 'w') as outfile:
            for line in lines:
                parts = line.strip().split()
                label = parts[0]
                x = float(parts[1]) / 640
                y = float(parts[2]) / 640
                # Write the normalized values back to the file without the 0.1 0.1 part
                outfile.write(f'{label} {x:.6f} {y:.6f}\n')

if __name__ == '__main__':
    base_dir = r'C:\DEVELOPMENT\DePondFi-24\data\labels'
    train_folder = os.path.join(base_dir, 'train')
    val_folder = os.path.join(base_dir, 'val')
    
    normalize_labels(train_folder)
    normalize_labels(val_folder)

    print("Labels have been normalized.")
