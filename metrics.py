import numpy as np
from scipy.ndimage import binary_dilation
from medpy.metric.binary import hd95

# 3D Dice

def calculate_3d_dice(pred, gt):
    """
    Calculate 3D Volume Dice。
    Input pred and gt are 3D NumPy array (0 as background，1 as foreground)。
    """
    
    pred = np.asarray(pred, dtype=bool)
    gt = np.asarray(gt, dtype=bool)

    # Compute Intersection and Union voxel summation
    intersection = np.logical_and(pred, gt).sum()
    total_voxels = pred.sum() + gt.sum()

    # Special Case when Denominator is 0
    if total_voxels == 0:
        return 1.0

    dice_score = (2.0 * intersection) / total_voxels
    return dice_score


# Boundary Dice

def get_3d_boundary(mask, dilation_iters=1):
    """
    Extract 3D the boundary of the mask。
    Pratice: Dilate mask in 3D space, then compute XOR with original mask that will leave the mask edge shell。
    dilation_iter : Control the thickness of the boundary (default = 1)
    """
    # Build 3D structure element (3x3x3 matrics of all ones)
    struct = np.ones((3, 3, 3))
    
    # Doing 3D dilation
    dilated_mask = binary_dilation(mask, structure=struct, iterations=dilation_iters)
    
    # XOR computation：Find the boundary after 3D dilation
    boundary = np.logical_xor(dilated_mask, mask)
    return boundary

def calculate_3d_boundary_dice(pred, gt, dilation_iters=1):
    """
    Compute 3D Boundary Dice。
    """
    pred_boundary = get_3d_boundary(pred, dilation_iters)
    gt_boundary = get_3d_boundary(gt, dilation_iters)

    intersection = np.logical_and(pred_boundary, gt_boundary).sum()
    total_boundary_voxels = pred_boundary.sum() + gt_boundary.sum()

    if total_boundary_voxels == 0:
        return 1.0

    return (2.0 * intersection) / total_boundary_voxels

# HD95
def calculate_3d_hd95(pred, gt, voxel_spacing):
    """
    Calculates the 3D HD95. The `voxel_spacing` must be provided to convert 
    the distance into real physical units (e.g., mm).
    The format of `voxel_spacing` is typically a tuple, such as 
    (Z_spacing, Y_spacing, X_spacing) -> (1.0, 1.0, 1.0).
    """
    pred = np.asarray(pred, dtype=bool)
    gt = np.asarray(gt, dtype=bool)

    # Failsafe: If either the prediction or the ground truth is empty, HD95 cannot be calculated.
    # Usually, a NaN or a large penalty value is returned.
    if pred.sum() == 0 or gt.sum() == 0:
        print("Warning: Encountered an empty prediction or ground truth. Unable to calculate HD95.")
        return np.nan 

    # Calculate using MedPy, passing the 3D arrays and spacing directly.
    distance = hd95(result=pred, reference=gt, voxelspacing=voxel_spacing)
    return distance