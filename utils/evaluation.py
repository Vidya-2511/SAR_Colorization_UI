import numpy as np
import tensorflow as tf
from skimage.metrics import structural_similarity as ssim

def calculate_metrics(original, generated):
    # Convert images to float32 to avoid type mismatch errors
    original = tf.convert_to_tensor(original, dtype=tf.float32)
    generated = tf.convert_to_tensor(generated, dtype=tf.float32)

    # Calculate MSE
    mse = tf.reduce_mean(tf.square(original - generated))

    # Handle division by zero in PSNR
    mse_value = mse.numpy() if isinstance(mse, tf.Tensor) else mse
    if mse_value == 0:
        psnr = float("inf")  # Assign infinity if MSE is 0
    else:
        psnr = 20 * np.log10(255 / np.sqrt(mse_value))

    # Convert tensors back to numpy for SSIM calculation
    original_np = original.numpy()
    generated_np = generated.numpy()
    
    # Compute SSIM with proper data range
    ssim_value = ssim(original_np, generated_np, data_range=generated_np.max() - generated_np.min())

    return psnr, ssim_value, mse_value
