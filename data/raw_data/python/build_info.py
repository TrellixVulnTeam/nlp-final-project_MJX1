
# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Generates a Python module containing information about the build."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

is_cuda_build = True

cuda_version_number = '10.0'
cudnn_version_number = '7'
msvcp_dll_name = 'msvcp140.dll'
nvcuda_dll_name = 'nvcuda.dll'
cudart_dll_name = 'cudart64_100.dll'
cudnn_dll_name = 'cudnn64_7.dll'
