
import tensorflow as tf

mnist =tf.keras.datasets.fashion_mnist

class myCallback(tf.keras.callbacks.Callback):
    def epoch_end(self, epoch, logs = None):
        if logs.get('accuracy') > 0.95:
            print("\nReached 95% accuracy so cancelling training!")
            self.model.stop_training = True
callbacks = myCallback()
#訓練，テスト分割
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

#正規化
training_images = training_images / 255.0
test_images = test_images / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape = (28, 28)),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dense(10,activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss = 'sparse_categorical_crossentropy', 
              metrics=['accuracy'])

model.fit(training_images, training_labels, epochs=50,
          callbacks =[callbacks])

model.evaluate(test_images, test_labels)


classifications = model.predict(test_images)
print(classifications[0])
print(test_labels[0])

