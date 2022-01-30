import tensorflow as tf

def create_model(LOSS_FUNCTION,OPTIMIZER,METRICS,NUM_CLASS):

    LAYERS =[tf.keras.layers.Flatten(input_shape=[28,28], name="InputLayer"),
            tf.keras.layers.Dense(300,activation='relu', name="HiddenLayer1"),
            tf.keras.layers.Dense(100,activation='relu', name="HiddenLayer2"),
            tf.keras.layers.Dense(NUM_CLASS,activation='softmax',name = "OuputLayer")]

    model_clf = tf.keras.models.Sequential(LAYERS)

    model_clf.summary()

    model_clf.compile(loss = LOSS_FUNCTION, optimizer = OPTIMIZER, metrics = METRICS)

    return model_clf            
