#encoding=utf8
#! /usr/bin/python
'''
img_name height width
'''
import os
# import sys
import glob
from PIL import Image

from config import TextDetectionConfig as cfg


def get_name_size(img_dir, namesize_file):
    ''' get name size
        img_dir 图片路径
        namesize_file name_size文件存放路径
    '''
    print img_dir
    print namesize_file
    with open(namesize_file, 'w') as nsfile:
        for imgpath in glob.glob(os.path.join(img_dir, '*' + cfg.suffix)):
            width, height = Image.open(imgpath).size
            img_name = os.path.splitext(os.path.basename(imgpath))[0]
            nsfile.write(img_name + ' ' + str(height) + ' ' + str(width) + '\n')


get_name_size(os.path.join(cfg.data_dir, cfg.dataset_name, cfg.train_img_dir),
              os.path.join(cfg.data_dir, cfg.dataset_name, 'train_name_size.txt'))
get_name_size(os.path.join(cfg.data_dir, cfg.dataset_name, cfg.test_img_dir),
              os.path.join(cfg.data_dir, cfg.dataset_name, 'test_name_size.txt'))
