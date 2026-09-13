#include <cuda_runtime.h>

__global__ void relu_kernel(const float* input, float* output, int N) {
    
    int workindex = blockDim.x * blockIdx.x + threadIdx.x;

    if(workindex < N)
    {
        output[workindex] = max(0.0f, input[workindex]);
    }
}

extern "C" void solve(const float* input, float* output, int N) {
    int threads = 256;
    int blocks = (N + threads - 1) / threads;
    relu_kernel<<<blocks, threads>>>(input, output, N);
    cudaDeviceSynchronize();
}