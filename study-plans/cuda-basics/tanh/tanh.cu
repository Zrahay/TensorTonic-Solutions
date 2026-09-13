#include <cuda_runtime.h>
#include <math.h>

__global__ void tanh_kernel(const float* input, float* output, int N) {
    int workindex = blockDim.x * blockIdx.x + threadIdx.x;

    if(workindex < N)
    {
        float x = input[workindex];
        float numerator = expf(x) - expf(-x);
        float denominator = expf(x) + expf(-x);

        output[workindex] = numerator / denominator;
    }
}

extern "C" void solve(const float* input, float* output, int N) {
    int threads = 256;
    int blocks = (N + threads - 1) / threads;
    tanh_kernel<<<blocks, threads>>>(input, output, N);
    cudaDeviceSynchronize();
}