# -*- coding:utf-8 -*-
# @Author: Peizhen Li
# @Desc: None

import numpy as np
from PickPlaceEnv import env
import matplotlib.pyplot as plt
# import moviepy
from moviepy.editor import ImageSequenceClip
from PIL import Image
import utils

# make sure the resource is ready
utils.try_load_all_assets()

"""
you can modify this cofig as long as the resources are provided.
If you are going to add objects other than "block" "bowl" "plane", you need to modify 
"load_obj_from_config" method in PickPlaceEnv.py
"""

config = {'pick':  ['yellow block', 'green block', 'blue block'],  # 'red block'
          'place': ['yellow bowl', 'green bowl', 'blue bowl',]}  # 'red bowl'

np.random.seed(42)
def show_init_setting():
	obs = env.reset(config)
	img = env.get_camera_image()
	im = Image.fromarray(img)
	im.save('outputs/init_env.png')
	print('init object pos: ', env.obj_name_to_pos)
	print('image shape: ', img.shape, type(img))
	plt.imshow(img)
	plt.show()

def show_img_top(image_size=(240, 240)):
	obs = env.reset(config)
	img = env.get_camera_image_top(image_size=image_size)
	im = Image.fromarray(img)
	im.save('outputs/top_env.png')
	plt.imshow(img)
	plt.show()

"""
You are free to modify the pick and place object name as long as they are in the above config dict
"""
def generate_fake_action(pick_obj_name='yellow block', place_obj_name='yellow bowl'):
	action = {'pick': env.obj_name_to_pos[pick_obj_name],
			  'place': env.obj_name_to_pos[place_obj_name]}
	return action

def execute_action():
	# reset env before execute an action
	env.reset(config)
	action = generate_fake_action()
	env.step(action)
	output_cached_video()


def output_cached_video():
	if not env.cache_video:
		print('No cached video, abort...')
	debug_clip = ImageSequenceClip(env.cache_video, fps=25)
	debug_clip.write_videofile('outputs/my_video.mp4')
	# clear cache
	env.cache_video = []


if __name__ == "__main__":
	show_img_top()
	# show_init_setting()
	# execute_action()
