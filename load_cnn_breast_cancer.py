import numpy as np
import pandas as pd
import tensorflow as tf
import os
import re
import random
import time # just to see how fast/slow things run

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from scipy.misc import imread
from sklearn.model_selection import train_test_split
from PIL import Image

class ManualError(Exception):
    pass

def restore_model(x_test_file_path):
    '''
    x_test_file_path is a string, i.e. the file path of one picture

    returns an int, 0 or 1, which predicts the malignancy of a breast cell culture
    
    '''
    assert isinstance(x_test_file_path, str)
    
    loaded_graph = tf.Graph()
    

    image = imread(x_test_file_path)

    if np.shape(image) != (50, 50, 3):
        image = image.resize((50, 50))

    if np.shape(image) != (50, 50, 3):
        print('Picture is not in colour!')
        raise ManualError
    
    
    with tf.Session(graph=loaded_graph) as sess:
        sess.run(tf.global_variables_initializer())
        
        model = tf.train.import_meta_graph('conv_nn_breast_cancer_IMPROVED.meta')
        model.restore(sess, tf.train.latest_checkpoint('./'))
        
        x_   = loaded_graph.get_tensor_by_name('x:0')
        out_ = loaded_graph.get_tensor_by_name('out:0')
        
        pred_labels = np.argmax(out_.eval({x_: np.array([image])}))
    
    return pred_labels




