import torch
from PIL import Image
import numpy as np

def read_and_process_file(f):
    im = Image.open(f)
    im = im.convert('L')
    im = im.resize((512,512))
    im = np.asarray(im)

    im_copy = im.copy()
    im_copy[im_copy>=239.8] = 1

    # im[im>=239.8] = 1 #239.8 is the mean of the dataset
    im_copy[im_copy!=1] = 0
    im_copy = im_copy.astype(np.float32) 
    

    return im_copy

def process_pil(im):

    im = im.convert('L')
    im = im.resize((512,512))
    im = np.asarray(im)

    im_copy = im.copy()
    im_copy[im_copy>=239.8] = 1

    # im[im>=239.8] = 1 #239.8 is the mean of the dataset
    im_copy[im_copy!=1] = 0

    im_copy = torch.from_numpy(im_copy).unsqueeze(0).unsqueeze(0).float()

    return im_copy
