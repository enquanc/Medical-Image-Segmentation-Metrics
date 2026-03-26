import numpy as np
import tifffile as tiff
from metrics import *

gt_path = 'your_gt_path' # Input your ground truth image file paths
pred_path = 'your_pred_path' # Input your prediction image file paths

# Read Image
gt = tiff.imread(gt_path)
pred = tiff.imread(pred_path)

# Check shape
print('Brain shape : ', gt.shape)
print('Hippo shape : ', pred.shape)

# real physical units
spacing = (1.0, 1.0, 1.0) 

# Dice
iou_score = calculate_3d_dice(pred, gt)
print(f"3D Dice: {iou_score:.4f}")

# Boundary Dice
biou_score = calculate_3d_boundary_dice(pred, gt, dilation_iters=1)
print(f"3D Boundary Dice: {biou_score:.4f}")

# HD95
hd95_distance = calculate_3d_hd95(pred, gt, voxel_spacing=spacing)
print(f"3D HD95 (mm): {hd95_distance:.4f}")

