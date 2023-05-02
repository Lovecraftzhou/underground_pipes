# YOLOv7 Pipe defect 



## Prepare
```text
    ### create virtual env 
    conda create -n yolov7-pipe python=3.8 
    ### requirements
    pip install -r requirements.txt
    ### Download related version Pytorch 
    pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117
```

## GUI
```text1
    ### change to the yolov7-GUI folder
    python main.py
```

## Train
```text
    python train.py --batch-size 32 --data data/pipe_enhance.yaml --hyp data/hyp.scratch.yaml
```





## Reference
- [WongKinYiu/yolov7](https://github.com/WongKinYiu/yolov7)
- [PyQt5-YOLOv5](https://github.com/Javacr/PyQt5-YOLOv5)
- [YOLOv7-Predict-with-UI](https://github.com/swiminggay/YOLOv7-Predict-with-UI)
- [Python Qt](https://www.byhy.net/tut/py/gui/qt_01/)
- [yolov7-Pyside6](https://github.com/SwimmingLiu/yolov7-Pyside6)

