import os
import subprocess
import random

from PIL import Image

from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
	return render(request, 'index.html')

def demo(request):
	if request.method == 'POST' and request.FILES['custom_img']:
		custom_img = request.FILES['custom_img']
		style_id = request.POST['style_id']
		tmp_dir, img_name = artwork(custom_img, style_id)
		render_dict = {'done': 1, 'tmp_dir': tmp_dir, 'img_name': img_name}

		return render(request, 'demo.html', render_dict) 
	else:
		return render(request, 'demo.html')

def artwork(img, style_id):
	SITE_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)))
	data_root_path = os.path.join(SITE_ROOT, '../fast-style-transfer/data/') 
	
	# Clean the inputs and outputs dir

	# Save the uploaded image to disk
	tmp_dir = str(random.random()).split('.')[1]
	while os.path.exists(data_root_path + 'inputs/' + tmp_dir):
		tmp_dir = str(random.random()).split('.')[1]
	tmp_whole_path=data_root_path + 'inputs/' + tmp_dir
	os.makedirs(tmp_whole_path)
	print(tmp_whole_path)
	print(tmp_dir)
	img_name = 'img' + tmp_dir + '.png'
	img_path = data_root_path + 'inputs/'+ tmp_dir + '/' + img_name


	with open(img_path, 'wb+') as dst:
		for chunk in img.chunks():
			dst.write(chunk)
	
	# Resize the image
	resized_max_size = 512
	img = Image.open(img_path)
	ratio = min(resized_max_size/float(img.size[0]), resized_max_size/float(img.size[1]))
	resized_size = (int(ratio * img.size[0]), int(ratio * img.size[1]))
	if max(img.size) > resized_max_size:
		img.resize(resized_size, Image.ANTIALIAS).save(img_path)
	# Run style transfer
	subprocess.call(['bash', SITE_ROOT + '/evaluate.sh', 'data/inputs/'+tmp_dir, 'checkpoints-dir/cp-s'+style_id])
	return tmp_dir, img_name
