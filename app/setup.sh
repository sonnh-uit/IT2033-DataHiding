#!/bin/bash

install_gcc() {
    add-apt-repository ppa:ubuntu-toolchain-r/test
    apt install software-properties-common
    apt update
    apt install gcc-9
    apt install g++-9

}

cuda_toolkit() {
    wget https://developer.download.nvidia.com/compute/cuda/12.2.2/local_installers/cuda_12.2.2_535.104.05_linux.run
    sh cuda_12.2.2_535.104.05_linux.run
}

main () {
    install_gcc
    cuda_toolkit
}

main