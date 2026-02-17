# 查看模型信息

from ultralytics import YOLO
model = YOLO('./yaml/PC2f_MPF_yolov8n.yaml')
model.info()