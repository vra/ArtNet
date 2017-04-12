INPUT_DIR=$1
cd fast-style-transfer
CUDA_VISIBLE_DEVICES= python evaluate.py --checkpoint checkpoints-dir/cp-s1/ --in-path $INPUT_DIR --out-path data/outputs --allow-different-dimensions
