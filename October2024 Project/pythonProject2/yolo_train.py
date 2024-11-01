from ultralytics import YOLO
# Загружаем предобученную модель YOLOv8
model = YOLO('best.pt') # Выберите размер модели: n, s, m, l, x
# Запускаем обучение
model.train(data='config.yaml', epochs=60, batch=16, imgsz=640)