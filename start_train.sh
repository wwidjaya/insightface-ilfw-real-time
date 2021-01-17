export CUDA_VISIBLE_DEVICES=0
export MXNET_CUDNN_AUTOTUNE_DEFAULT=0 
export USE_CUDA=0
python -u ./train_model.py --network r100 --loss arcface --dataset emore --per-batch-size 2
