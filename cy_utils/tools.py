import cv2
import numpy

def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()
def show_image(data: numpy.ndarray, tile="ouput", width=1920, height=1080):
    """
    Shaw image and wait until key hit by developer
    :param data:
    :param tile:
    :param width:
    :param height:
    :return:
    """
    cv2.namedWindow(tile, cv2.WINDOW_NORMAL)  # Create window with freedom of dimensions
    cv2.resizeWindow(tile, width, height)

    cv2.imshow(tile, data)  # Show image
    cv2.waitKey(0)
