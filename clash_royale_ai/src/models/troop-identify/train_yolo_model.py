from ultralytics import YOLO
import torch

if __name__ == "__main__":
    # TODO: next time use yolo11s.pt(small) instead of yolo11n.pt (nano) as initial model, also require GPU training
    model = YOLO("yolo11s.pt")

    if not torch.cuda.is_available():
        print("---GPU not available---")
        print("---Running Training on CPU (Please change to GPU if possible)---")
        print("---Device name: "+torch.cuda.get_device_name(0)+"---")

        model.train(
            data="dataset/data.yaml",
            epochs=50,
            imgsz=640,
            batch=16,
            name="clash_royale_troops_identifier"
        )

    else:
        print("---GPU available---")
        print("---Running Training on GPU (first recognized)---")
        print("---Device name: "+torch.cuda.get_device_name(0)+"---")

        model.train(
            data="dataset/data.yaml",
            epochs=50,
            imgsz=640,
            batch=16,
            device='cuda',
            name="clash_royale_troops_identifier"
        )