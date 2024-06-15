DePondFi24 
==============================

"DePondFi'24" is notable for incorporating a wide array of underwater-specific obstacles in pond environment that significantly complicate visual recognition tasks. 
These challenges include refraction, color distortion, limited visibility range, absorption and scattering losses, image distortion, varied lighting conditions, and image noise.
Each challenge plays a crucial role in evaluating the robustness and precision of keypoint detection algorithms in pond environments.

The images in the dataset have undergone resizing as a form of augmentation and are provided at a resolution of 640p recorded at a frame rate of 60fps. 
This setup is designed to simulate realistic underwater conditions and is essential for developing and benchmarking key point detection.

Total no. of images = 560
Train Test Split -> 80:20

Key points
==============================
0- Mouth
1- Eye
2- Top fin
3- Fish center
4- Bottom center
5- start point tail 
6- top outline tail
7- mid outline tail
8- bottom outline tail

Annotation Rules:
==============================
Camera Angle: Fish facing directly towards the camera were excluded.
Distance: Fish that appeared too far from the camera were disregarded.
Visibility: Only fish where at least 75% of the structure was visible were included; others were neglected.
Size: Very small fish were excluded.
Clarity: Fish that were not clearly visible due to poor image quality or unfavorable conditions were excluded.

Quick start:
==============================
Load data into gdrive
Clone repo
Run on google colab DepondFi'24.ipynb

Inference Time:
==============================
1.208hrs; Specifications - Python-3.10.12 torch-2.3.0+cu121 CUDA:0 (Tesla T4, 15102MiB)


<i>Note: The dataset is not included in this repository as it is not intended for public sharing.</i>

