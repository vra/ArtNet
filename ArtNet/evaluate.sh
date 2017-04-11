INPUT_DIR=$1
cd fast-style-transfer
CUDA_VISIBLE_DEVICES= python evaluate.py --checkpoint cp-dir/ --in-path $INPUT_DIR --out-path data/outputs --allow-different-dimensions
