#训练
from ultralytics import YOLO
import ultralytics.nn.tasks
import torch
torch.serialization.add_safe_globals(['ultralytics.nn.tasks.DetectionModel'])
# 设置PyTorch全局配置
torch.serialization.add_safe_globals([
    'ultralytics.nn.tasks.DetectionModel',
    # 'torch.optim.SGD',  # 添加优化器类
    'torch.optim.Adam'
])
model = YOLO('./yaml/PC2f_MPF_yolov8n.yaml')
results = model.train(data='/home/lyric/ir_rgb/TwoStream_Yolov8/data/drone2.yaml',batch=16,epochs=100)
# 临时允许加载自定义模型
