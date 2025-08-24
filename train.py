import torch
from ultralytics import YOLO
 
def main():

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Training on {device.upper()}")
 
    # Build YOLOv8n from scratch using config
    model = YOLO("/home/ankitr3/Desktop/yolov8n_training/Yolov8n_from_scratch/configs/yolov8n.yaml")
 
    # Train on COCO128 dataset
    model.train(
        data="configs/coco128.yaml",
        epochs=100,
        imgsz=640,
        device=0 if device == "cuda" else "cpu",
        pretrained=False,
        batch=16,
        workers=4
    )
    # Evaluate the model's performance on the validation set
    metrics = model.val()
if __name__ == "__main__":
    main()