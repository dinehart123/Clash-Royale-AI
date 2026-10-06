from ultralytics import YOLO
from PIL import Image

model = YOLO("copy-best.pt")

def get_troop_identify_prediction(frame):
    # frame is a np.array(screenshot)

    results = model(frame)
    return results


def get_troop_identify_prediction_bound_confidence(frame, confidence=0.5):
    # frame is a np.array(screenshot), confidence is float representing what confidence level model needs on guess to add it to results

    results = model(frame, confidence)
    return results


def test_troop_identify_prediction():
    img = Image.open("test-image.jpg").convert("RGB") # put test image here
    
    results = model(img)

    for box in results[0].boxes:
        troop_id = int(box.cls)
        label = model.names[troop_id]
        confidence = float(box.conf)
        x1, y1, x2, y2 = box.xyxy[0]
        print("---Box Result---")
        print(f"{label}: {confidence:.2f} at {x1:.0f}, {y1:.0f}")
        print("")


test_troop_identify_prediction()