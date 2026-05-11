from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO("/root/autodl-tmp/yolo11/runs/TT100k/weights/best.pt")
    TT100kPath = "datasets/TT100k/TT100k.yaml"

    # Validate the model
    validation_results = model.val(
                                data=TT100kPath,
                                imgsz=640, 
                                batch=16,
                                device=0,
                                )