from ultralytics import YOLO

# モデルのロード
model = YOLO("yolov8n.pt")

# 予測の実行
results = model.predict(source=0, show=True)
