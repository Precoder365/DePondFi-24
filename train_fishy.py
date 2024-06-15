import yaml
from ultralytics import YOLO

data_yaml = dict(
    train ='train',
    val ='valid',
    test='test',
    nc =9,
    names =['Mouth','Eye','Top fin','Fish center','Bottom center','start point tail','top outline tail','mid outline tail','bottom outline tail']
)

with open('data.yaml', 'w') as outfile:
    yaml.dump(data_yaml, outfile, default_flow_style=True)

names =['Mouth','Eye','Top fin','Fish center','Bottom center','start point tail','top outline tail','mid outline tail','bottom outline tail']
M=list(range(len(names)))
class_map=dict(zip(M,names))

model = YOLO("yolov8x.pt")

model.train(data='config.yaml', epochs=1, imgsz=640)

