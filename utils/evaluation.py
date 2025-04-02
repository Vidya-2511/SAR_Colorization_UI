import tensorflow as tf
import numpy as np
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim

def calculate_metrics(original, generated):
    original = np.array(original, dtype=np.float32)
    generated = np.array(generated, dtype=np.float32)

    psnr_value = psnr(original, generated, data_range=original.max() - original.min())
    ssim_value = ssim(original, generated, data_range=original.max() - original.min(), multichannel=True)
    mse_value = np.mean((original - generated) ** 2)  # ✅ Fix: Ensure correct MSE calculation

    return psnr_value, ssim_value, mse_value
