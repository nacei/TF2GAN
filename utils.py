# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import os

def check_dir(out_dir):
	if not os.path.exists(out_dir):
		os.mkdir(out_dir)

def imread(img_path, norm=True):
	img = plt.imread(img_path)
	return img / 255. if norm else img

def imsave(save_path, img):
	plt.imsave(save_path, img)

def imdenorm(img):
	return (img + 1.) / 2.

def montage(imgs):
	N, H, W, C = imgs.shape
	n = int(np.ceil(np.sqrt(N)))

	result = np.zeros((n * H, n * W, C))
	for i in range(N):
		r, c = i // n, i % n
		result[r * H: (r + 1) * H, c * W: (c + 1) * W] = imgs[i]

	return result