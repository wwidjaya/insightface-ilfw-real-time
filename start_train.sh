export CUDA_VISIBLE_DEVICES=0
export MXNET_CUDNN_AUTOTUNE_DEFAULT=0 
export USE_CUDA=0
echo "Insightface Model Training Ver. 1.7.1 R100 - Corrected - 800 Id - With Mask - 64 batch size"
python -u ./train_model.py --network r100 --loss arcface --dataset emore --per-batch-size 64
