# YOLO-ECNet

## Installation

conda virtual environment is recommended.

```bash
conda create -n yolo-ecnet python=3.8 -y
conda activate yolo-ecnet
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 --extra-index-url https://download.pytorch.org/whl/cu113
```

```bash
git clone https://github.com/your_username/YOLO-ECNet.git
cd YOLO-ECNet
pip install -e .
```
## Train & Validation

We provide `train.py` and `val.py` for model training and validation. The default model configuration is set to **YOLO11-ECNet**, and the main training and validation parameters have already been configured in the scripts.

Before running the scripts, please prepare your dataset in YOLO format and manually modify the dataset configuration path in `train.py` and `val.py`.

For example, open `train.py` and set the dataset path:

```python
data = "/path/to/data.yaml"
```

Then run the training script:

```bash
python train.py
```

After training, run the validation script:

```bash
python val.py
```

## Acknowledgement

Our code is built based on the [Ultralytics](https://github.com/ultralytics/ultralytics). Thanks for their great work!

