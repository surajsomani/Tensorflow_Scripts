from tflearn.data_utils import image_preloader
import tensorflow as tf
X, Y = image_preloader(image_shape=(128, 128), mode='folder','/tmp/data',categorical_labels=True, normalize=True)



