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
* `evaluate.ipynb` : A Jupyter Notebook demonstrating how to run the evaluation pipeline.

## 🛠️ Installation

To install the required dependencies, run the following command:

```bash
git clone https://github.com/enquanc/Medical-Image-Segmentation-Metrics

cd https://github.com/enquanc/Medical-Image-Segmentation-Metrics

pip install -r requirements.txt