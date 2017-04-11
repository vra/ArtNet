import os
import subprocess
import random

from PIL import Image

from django.http import HttpResponse
from django.shortcuts import render 

def process(request):
	if request.method == 'POST' and request.FILES['custom_img']:
		custom_img = request.FILES['custom_img']
		img_name = artwork(custom_img)
		render_dict = {'done': 1, 'img_name': img_name}

		return render(request, 'process.html', render_dict) 
	else:
		return render(request, 'process.html')

def artwork(img):
	data_root_path = 'fast-style-transfer/data/'
	
	# Clean the inputs and outputs dir

	# Save the uploade image to disk
	tmp_dir = str(random.random()).split('.')[1]
	while os.path.exists(data_root_path + 'inputs/' + tmp_dir):
		tmp_dir = str(random.random()).split('.')[1]
	os.makedirs(data_root_path + 'inputs/' + tmp_dir)
	img_name = 'img' + tmp_dir + '.png'
	img_path = data_root_path + 'inputs/'+ tmp_dir + '/' + img_name


	with open(img_path, 'wb+') as dst:
		for chunk in img.chunks():
			dst.write(chunk)
	
	# Resize the image
	resized_max_size = 1024
	img = Image.open(img_path)
	ratio = min(resized_max_size/float(img.size[0]), resized_max_size/float(img.size[1]))
	resized_size = (int(ratio * img.size[0]), int(ratio * img.size[1]))
	if max(img.size) > resized_max_size:
		img.resize(resized_size, Image.ANTIALIAS).save(img_path)
	# Run style transfer
	subprocess.call(['bash', 'ArtNet/evaluate.sh', 'data/inputs/'+tmp_dir])
	return img_name
