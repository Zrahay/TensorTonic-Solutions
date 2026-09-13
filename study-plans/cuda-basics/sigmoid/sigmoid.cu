#include <cuda_runtime.h>
#include <math.h>

__global__ void sigmoid_kernel(const float* input, float* output, int N) {
    int workindex = blockDim.x * blockIdx.x + threadIdx.x;

    if(workindex < N)
    {
        float x = input[workindex];
        output[workindex] = 1.0f / (1.0f + expf(-x));
    }
}

extern "C" void solve(const float* input, float* output, int N) {
    int threads = 256;
    int blocks = (N + threads - 1) / threads;
    sigmoid_kernel<<<blocks, threads>>>(input, output, N);
    cudaDeviceSynchronize();
}