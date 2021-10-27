
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved

# Install: PyTorch (we assume 1.5.1 but VISSL works with all PyTorch versions >=1.4)
!pip install torch==1.5.1+cu101 torchvision==0.6.1+cu101 -f https://download.pytorch.org/whl/torch_stable.html

# install opencv
!pip install opencv-python

# install apex by checking system settings: cuda version, pytorch version, python version
import sys
import torch
version_str="".join([
    f"py3{sys.version_info.minor}_cu",
    torch.version.cuda.replace(".",""),
    f"_pyt{torch.__version__[0:5:2]}"
])
print(version_str)

# install apex (pre-compiled with optimizer C++ extensions and CUDA kernels)
!pip install apex -f https://dl.fbaipublicfiles.com/vissl/packaging/apexwheels/{version_str}/download.html

# install VISSL
!pip install vissl

import vissl
import tensorboard
import apex
import torch
