import os
import tensorflow as tf
import random 
import numpy as np

flags = tf.app.flags
flags.DEFINE_string('data_dir', './', 'Root directory to raw pet dataset.')
FLAGS = flags.FLAGS



def main(_):
  relevant_path = FLAGS.data_dir #path for the image directory 

  DIR = os.listdir(relevant_path)  #derectory containing 

  arr_jpg = [x for x in DIR if x.endswith(".jpg")]

  names = [s.strip('.jpg') for s in arr_jpg]

  random.shuffle(names)  #shuffeling the names 

  end_index = len(names)
  print("Number of images :", end_index)

  y=int(np.round(0.8*end_index,0)) 
  
  trainval = names[0:y]
  test    = names[y:]

  thefile = open('trainval.txt', 'w')
  for item in trainval:
     thefile.write("%s\n" % item)

  

  thefile = open('test.txt', 'w')
  for item in test:
     thefile.write("%s\n" % item)


  thefile = open('list.txt', 'w')
  for item in  names:
     thefile.write("%s\n" % item)


if __name__ == '__main__':

  tf.app.run()
