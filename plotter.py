import matplotlib.pyplot as plt

def create_plot_keras(history, colors:list=["b","r"], metric:str="accuracy", validation:bool=False):
    """
    Create plot for your keras model learning history.
    """
    if metric == "accuracy":
        plt.plot(history.history["accuracy"], color=colors[0], label="accuracy")
        if validation:
            plt.plot(history.history["val_accuracy"], color=colors[1], label="val_accuracy")
        plt.legend()
        plt.show()
    elif metric == "loss":
        plt.plot(history.history["loss"], color=colors[0], label="loss")
        if validation:
            plt.plot(history.history["val_loss"], color=colors[1], label="val_loss")
        plt.legend()
        plt.show()
    else:
        print("Metric not found.")
