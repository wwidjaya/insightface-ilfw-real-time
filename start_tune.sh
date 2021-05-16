export CUDA_VISIBLE_DEVICES=0
export MXNET_CUDNN_AUTOTUNE_DEFAULT=0
export USE_CUDA=0
echo "Insightface Model Training Ver. 1.7.6 R100 - Tuned - 1000 Id - With Mask - 64 batch size"
python3 -u ./train_model.py --models-root './models/tuned' --network r100 --loss arcface --dataset emore --per-batch-size 64 --pretrained './models/model-r100-ii/model'