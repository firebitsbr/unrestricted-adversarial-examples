import tensorflow as tf
from unrestricted_advex import eval_kit
from unrestricted_advex.mnist_baselines import mnist_utils

flags = tf.app.flags
FLAGS = flags.FLAGS

flags.DEFINE_string("model_dir", "/tmp/two-class-mnist/vanilla",
                    "Where to load the model to attack from")
flags.DEFINE_integer("num_datapoints", 128,
                    "How many datapoints to evaluate on")
flags.DEFINE_integer("batch_size", 128,
                    "Batch size to use during evaluation")



def main(_):
  mnist = mnist_utils.mnist_dataset(one_hot=False)
  eval_kit.evaluate_two_class_mnist_model(
    mnist_utils.np_two_class_mnist_model(FLAGS.model_dir),
    mnist_utils.two_class_iter(
      images=mnist.test.images, labels=mnist.test.labels,
      num_datapoints=FLAGS.num_datapoints, batch_size=FLAGS.batch_size),
    model_name='datapoints_'+str(FLAGS.num_datapoints))


if __name__ == "__main__":
  tf.app.run()
