import tensorflow as tf

hello = tf.constant('HEllo, Tensorflow')
sess = tf.Session()
print(sess.run(hello))

