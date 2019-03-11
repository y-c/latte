import os
import sys
import numpy as np
# sys.path.append("..")
# from Mask_RCNN_2.mask_rcnn_demo import main

def get_mask_rcnn_labels(filename):
	ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
	os.system("python Mask_RCNN_2/mask_rcnn_demo.py --image_filename={}".format(filename))
	# bounded_indices = mask_rcnn_demo.main(filename)
	bounded_indices = np.fromfile(
					    os.path.join(ROOT_DIR, "Mask_RCNN_2/output/indices.bin"),
					    dtype=np.int)
	os.system("rm {}/Mask_RCNN_2/output/*.bin".format(ROOT_DIR))
	return bounded_indices.tolist()
	# os.system("rm classify/bounding_boxes/*.json")