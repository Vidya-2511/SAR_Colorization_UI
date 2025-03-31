import numpy as np
from skimage.metrics import structural_similarity as ssim

def calculate_metrics(original, generated):
    mse = np.mean((original - generated) ** 2)
    psnr = 20 * np.log10(255 / np.sqrt(mse))
    ssim_value = ssim(original, generated)
    return psnr, ssim_value, mse