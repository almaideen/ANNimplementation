import tensorflow as tf

def create_model(LOSS_FUNCTION,OPTIMIZER,METRICS,NUM_CLASS):

    LAYERS =[tf.keras.layers.Flatten(input_shape=[28,28], name='Input Layer'),
            tf.keras.layers.Dense(300,activation='relu', name='Hidden Layer1'),
            tf.keras.layers.Dense(100,activation='relu', name='Hidden Layer2'),
            tf.keras.layers.Dense(NUM_CLASS,activation='softmax',name = 'Ouput Layer')]

    model_clf = tf.keras.model.Sequential(LAYERS)

    model_clf.summary()

    model_clf.compile(loss = LOSS_FUNCTION, optimizer = OPTIMIZER, metrics = METRICS)

    return model_clf            
