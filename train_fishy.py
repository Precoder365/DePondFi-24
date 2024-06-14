from ultralytics import YOLO


model = YOLO('yolov8n-pose.pt') 

model.train(data='config.yaml', epochs=1, imgsz=640)

# import os
# import yaml
# from ultralytics import YOLO

# # Function to create data.yaml
# def create_data_yaml(data_dir):
#     data_yaml = {
#         'path': data_dir,
#         'train': 'images/train',
#         'val': 'images/val',
#         'nc': 9,
#         'names': ['mouth', 'eye', 'top_fin', 'fish_center', 'bottom_center', 'start_point_tail', 'top_outline_tail', 'mid_outline_tail', 'bottom_outline_tail'],
#         'kpt_shape': [9,2]
#     }
    
#     with open('data.yaml', 'w') as outfile:
#         yaml.dump(data_yaml, outfile, default_flow_style=False)

# # Main function
# if __name__ == '__main__':
#     base_dir = r'C:\DEVELOPMENT\DePondFi-24'
#     data_dir = os.path.join(base_dir, 'data')
    
#     # Create data.yaml
#     create_data_yaml(data_dir)
    
#     # Load YOLOv8 model
#     model = YOLO("yolov8n-pose.pt")
    
#     # Train the model
#     model.train(data='data.yaml', epochs=1, imgsz=640)
