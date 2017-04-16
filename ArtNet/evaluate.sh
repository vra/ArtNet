INPUT_DIR=$1
CHECK_POINT_DIR=$2
echo $PWD
cd /home/yunfeng/Dev/git/ArtNet/fast-style-transfer
CUDA_VISIBLE_DEVICES= python evaluate.py --checkpoint $CHECK_POINT_DIR --in-path $INPUT_DIR --out-path data/outputs --allow-different-dimensions
