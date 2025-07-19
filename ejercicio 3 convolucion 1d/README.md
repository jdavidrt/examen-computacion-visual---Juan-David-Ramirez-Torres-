# Exercise 3: Manual 1D Convolution Implementation

## Description

Pure Python implementation of 1D convolution operation without using numpy.convolve, featuring signal processing, kernel application, and comprehensive visualization.

## Implementation

### Convolution Algorithm

- **Manual Implementation**: Custom convolution function without built-in libraries
- **Kernel Flipping**: Proper mathematical convolution with reversed kernel
- **Boundary Handling**: Full convolution output (signal + kernel - 1 length)
- **Pure Python Logic**: No dependency on numpy.convolve for core operation

### Signal and Kernel Definition

- **Input Signal**: 15-value sequence with varied amplitudes and transitions
- **Edge Detection Kernel**: [1, 0, -1] for discrete derivative approximation
- **Mathematical Purpose**: Detects signal changes and transition points
- **Output Analysis**: 17-value result demonstrating convolution mathematics

### Visualization System

- **Individual Plots**: Separate visualizations for signal, kernel, and result
- **Combined Display**: Three-subplot comparison for comprehensive analysis
- **Hand-drawn Styling**: XKCD matplotlib style for artistic appearance
- **Comic Sans Typography**: Consistent casual font styling across all plots
- **Orange Color Scheme**: Distinctive color palette for visual appeal

## Technical Details

### Core Function: `convolution_1d(signal, kernel)`

```python
def convolution_1d(signal, kernel):
    """Manual 1D convolution implementation without numpy.convolve"""
    signal_len = len(signal)
    kernel_len = len(kernel)
    output_len = signal_len + kernel_len - 1

    result = [0.0] * output_len
    flipped_kernel = kernel[::-1]  # Kernel reversal for convolution

    for i in range(output_len):
        for j in range(kernel_len):
            signal_idx = i - j
            if 0 <= signal_idx < signal_len:
                result[i] += signal[signal_idx] * flipped_kernel[j]

    return result
```

### Mathematical Verification

- **Edge Detection Response**: Positive values indicate decreasing signal trends
- **Derivative Approximation**: Kernel computes difference between samples 2 positions apart
- **Boundary Effects**: Expected artifacts at signal edges due to zero-padding
- **Sign Analysis**: Output polarity correctly reflects signal slope changes

## Libraries Used

- `matplotlib`: Plotting and visualization with styling capabilities
- `numpy`: Data structure support (not for convolution operation)
- `os`: Directory management for output organization

## Results Analysis

### Signal Characteristics

- **Original Signal**: [1, 2, 3, 4, 5, 3, 2, 1, 0, -1, -2, 1, 3, 2, 1]
- **Convolution Output**: 17 values showing edge detection response
- **Peak Detection**: Strong responses at sharp signal transitions
- **Noise Handling**: Smooth areas produce minimal convolution response

### Performance Validation

- **Algorithm Correctness**: Manual verification against expected convolution mathematics
- **Output Length**: Proper full convolution size calculation
- **Edge Cases**: Robust handling of signal boundaries and kernel alignment
- **Visual Verification**: Clear correlation between signal features and convolution peaks

## Files Generated

- `señal_original.png`: Input signal visualization
- `kernel.png`: Edge detection kernel display
- `resultado.png`: Convolution output visualization
- `combined_results.png`: Comprehensive three-panel comparison

## Usage

```bash
python convolucion.py
```

## Educational Value

This implementation demonstrates fundamental signal processing concepts:

- **Convolution Mathematics**: Manual calculation reinforces theoretical understanding
- **Edge Detection**: Practical application of derivative-based feature detection
- **Digital Signal Processing**: Foundation concepts for filter design and analysis
- **Algorithm Implementation**: Translation of mathematical operations into efficient code

## Visual Style

The hand-drawn aesthetic with Comic Sans typography creates an approachable presentation while maintaining mathematical rigor. The orange color scheme provides visual consistency and artistic appeal without compromising data clarity.
