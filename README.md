# Evaluation Metrics for Medical Image Segmentation

A collection of evaluation metrics commonly used in medical image segmentation tasks. 

## 📊 Supported Metrics

Currently, this repository includes the following metrics:
1. **Dice** (Dice Similarity Coefficient)
2. **Boundary Dice**
3. **HD95** (95% Hausdorff Distance)

**Supported Data Format:** `.tif`

## 📁 File Description

* `metrics.py` : Contains the core implementations of the evaluation metrics.
* `evaluate.py` : A Python script demonstrating how to run the evaluation pipeline.
* `evaluate.ipynb` : A Jupyter Notebook for interactive evaluation and visualization.
* `requirements.txt` : List of necessary Python dependencies.

## 🛠️ Installation

To install the required dependencies, run the following command:

### 1. Clone the repository
```bash
git clone https://github.com/enquanc/Medical-Image-Segmentation-Metrics
```

### 2. Enter the project directory
```bash
cd https://github.com/enquanc/Medical-Image-Segmentation-Metrics
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the evaluation
```bash
python evaluate.py
```