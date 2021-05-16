export CUDA_VISIBLE_DEVICES=0
export MXNET_CUDNN_AUTOTUNE_DEFAULT=0 
export USE_CUDA=0
echo "Insightface Model Verification Ver. 1.2 R100 - PreTrained - 100 Id - Without Mask - 64 batch size"
python -u ./verify_model.py --batch-size 64 --model "./models/model-r100-ii/model,1"
