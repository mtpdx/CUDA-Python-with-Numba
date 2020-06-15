# Add your completed `cuda_histogram` kernel definition here and save before running the assessment.
from numba import cuda
@cuda.jit
def cuda_histogram(x, xmin, xmax, histogram_out):
    '''Increment bin counts in histogram_out, given histogram range [xmin, xmax).'''
    idx = cuda.grid(1)
    stride = cuda.gridsize(1)
    
    nbins = histogram_out.shape[0]
    bin_width = (xmax - xmin) / nbins
    
    for i in range(idx, x.shape[0], stride):
        bin_number = np.int32((x[i] - xmin)/bin_width)
        if bin_number >= 0 and bin_number < histogram_out.shape[0]:
            cuda.atomic.add(histogram_out, bin_number, 1)
    pass  # Replace this with your implementation
