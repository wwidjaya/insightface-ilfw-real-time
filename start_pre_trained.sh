export CUDA_VISIBLE_DEVICES=0
export MXNET_CUDNN_AUTOTUNE_DEFAULT=0
export USE_CUDA=0
echo "Insightface Model Training Ver. 1.7.6 R100 - Pretrained- 1200 Id - With Mask - 64 batch size"
python3 -u ./train_model.py --network r100 --loss arcface --dataset emore --per-batch-size 64 --pretrained './models/r100-arcface-emore/model'