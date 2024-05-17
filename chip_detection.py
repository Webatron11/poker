from ultralytics import YOLO
import requests
import pathlib

def chip_detection(url):
    r = requests.get(url)
    with open("temp.jpg",'wb') as f:
        f.write(r.content)
    model = YOLO('best.pt')
    results = model.predict(source=['temp.jpg'])
    pathlib.Path.unlink("temp.jpg") # Deletes the file

    ### There absolutely must be a better way to do this but this is how you you get the chip count by going through the boxes and counting them
    for r in results:
        boxes = r.boxes
        chips = [model.names[int(box.cls)] for box in boxes]
    chip_dict = {}
    for chip in set(chips):
        chip_dict[chip] = chips.count(chip)
    
    return chip_dict