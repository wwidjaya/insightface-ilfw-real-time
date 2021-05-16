export CUDA_VISIBLE_DEVICES=0
export MXNET_CUDNN_AUTOTUNE_DEFAULT=0 
export USE_CUDA=0
echo "Insightface Model Verification Ver. 1.0 R100 - Tuned - 1000 Id - With Mask - 64 batch size"
python -u ./verify_model.py --batch-size 64 --model "./models/r100-arcface-emore/model,1"
