# MIT License
#
# Copyright (c) 2020 Wirianto Widjaya
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import os
import json

def set_search_path():
  sys.path.insert(1, "./ArcFace")
  sys.path.insert(1, "./ArcFace/symbol")
  sys.path.insert(1, "./ArcFace/common")
  sys.path.insert(1, "./modules")
  os.environ['MXNET_CUDNN_AUTOTUNE_DEFAULT'] = '0'
  os.environ['USE_CUDA'] = '1'

def read_setting():
  SETTINGS_FILENAME = "./settings.json"
  settings = {}

  if os.path.exists(SETTINGS_FILENAME):
    with open(SETTINGS_FILENAME, 'r') as f:
      settings = json.load(f)
  return settings


set_search_path()