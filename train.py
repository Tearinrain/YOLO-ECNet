from ultralytics import YOLO


if __name__ == '__main__':
    # dataset path
    TT100kPath = "datasets/TT100k/TT100k.yaml"

    # Load a model
    model = YOLO('ultralytics/cfg/models/11/yolo11-ECNet.yaml')

    # Train the model
    model.train(data=TT100kPath, 
                device=[0,1],
                pretrained=False,
                project='runs',
                name='TT100k',
                epochs=300, 
                imgsz=640,
                batch=32,
                seed=0,
                optimizer='SGD'
                )

