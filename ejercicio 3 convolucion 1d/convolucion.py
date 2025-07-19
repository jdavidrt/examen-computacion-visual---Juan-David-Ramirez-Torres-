import numpy as np
import matplotlib.pyplot as plt
import os

# Set hand-drawn style and informal font
plt.xkcd(scale=0.5, length=50, randomness=1)
plt.rcParams['font.family'] = ['Comic Sans MS', 'Trebuchet MS', 'DejaVu Sans']
plt.rcParams['font.size'] = 11

def convolution_1d(signal, kernel):
    """
    Manual 1D convolution implementation without numpy.convolve
    """
    signal_len = len(signal)
    kernel_len = len(kernel)
    output_len = signal_len + kernel_len - 1
    
    # Initialize output array
    result = [0.0] * output_len
    
    # Flip kernel for convolution
    flipped_kernel = kernel[::-1]
    
    # Perform convolution
    for i in range(output_len):
        for j in range(kernel_len):
            signal_idx = i - j
            if 0 <= signal_idx < signal_len:
                result[i] += signal[signal_idx] * flipped_kernel[j]
    
    return result

def create_plots():
    """
    Generate signal, apply convolution and create visualizations
    """
    # Create directories
    os.makedirs('graficos', exist_ok=True)
    
    # Define input signal (15 values)
    signal = [1, 2, 3, 4, 5, 3, 2, 1, 0, -1, -2, 1, 3, 2, 1]
    
    # Define kernel (edge detection)
    kernel = [1, 0, -1]
    
    # Apply manual convolution
    convolution_result = convolution_1d(signal, kernel)
    
    # Plot original signal
    plt.figure(figsize=(10, 4))
    plt.stem(range(len(signal)), signal, basefmt=' ', linefmt='orange', markerfmt='o')
    plt.title('Original Signal')
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.5, linewidth=1.5, color='black')
    plt.axhline(y=0, color='black', linewidth=1.5)
    plt.axvline(x=0, color='black', linewidth=1.5)
    plt.tight_layout()
    plt.savefig('graficos/señal_original.png', dpi=150)
    plt.close()
    
    # Plot kernel
    plt.figure(figsize=(6, 4))
    plt.stem(range(len(kernel)), kernel, basefmt=' ', linefmt='orange', markerfmt='o')
    plt.title('Convolution Kernel [1, 0, -1]')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.grid(True, alpha=0.5, linewidth=1.5, color='black')
    plt.axhline(y=0, color='black', linewidth=1.5)
    plt.axvline(x=0, color='black', linewidth=1.5)
    plt.tight_layout()
    plt.savefig('graficos/kernel.png', dpi=150)
    plt.close()
    
    # Plot convolution result
    plt.figure(figsize=(12, 4))
    plt.stem(range(len(convolution_result)), convolution_result, basefmt=' ', linefmt='orange', markerfmt='o')
    plt.title('Convolution Result')
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.5, linewidth=1.5, color='black')
    plt.axhline(y=0, color='black', linewidth=1.5)
    plt.axvline(x=0, color='black', linewidth=1.5)
    plt.tight_layout()
    plt.savefig('graficos/resultado.png', dpi=150)
    plt.close()
    
    # Combined plot for comparison
    plt.figure(figsize=(15, 10))
    
    plt.subplot(3, 1, 1)
    plt.stem(range(len(signal)), signal, basefmt=' ', linefmt='orange', markerfmt='o')
    plt.title('Original Signal')
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.5, linewidth=1.5, color='black')
    plt.axhline(y=0, color='black', linewidth=1.5)
    plt.axvline(x=0, color='black', linewidth=1.5)
    
    plt.subplot(3, 1, 2)
    plt.stem(range(len(kernel)), kernel, basefmt=' ', linefmt='orange', markerfmt='o')
    plt.title('Kernel [1, 0, -1]')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.grid(True, alpha=0.5, linewidth=1.5, color='black')
    plt.axhline(y=0, color='black', linewidth=1.5)
    plt.axvline(x=0, color='black', linewidth=1.5)
    
    plt.subplot(3, 1, 3)
    plt.stem(range(len(convolution_result)), convolution_result, basefmt=' ', linefmt='orange', markerfmt='o')
    plt.title('Convolution Result')
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.grid(True, alpha=0.5, linewidth=1.5, color='black')
    plt.axhline(y=0, color='black', linewidth=1.5)
    plt.axvline(x=0, color='black', linewidth=1.5)
    
    plt.tight_layout()
    plt.savefig('graficos/combined_results.png', dpi=150)
    plt.show()
    
    # Print numerical results
    print("Original Signal:", signal)
    print("Kernel:", kernel)
    print("Convolution Result:", [round(x, 3) for x in convolution_result])
    print("\nPlots saved in 'graficos/' directory")

if __name__ == "__main__":
    create_plots()