export CUDA_VISIBLE_DEVICES=0
export MXNET_CUDNN_AUTOTUNE_DEFAULT=0 
export USE_CUDA=0
echo "Insightface Model Training Ver. 1.7.7 R100 - 100 Id - Without Mask - 64 batch size"
python -u ./train_model.py --models-root './models/scratch' --network r100 --loss arcface --dataset emore --per-batch-size 64
