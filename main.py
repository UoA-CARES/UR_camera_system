
from cares_lib.vision.Camera import Camera
from cares_lib.vision.STagDetector import STagDetector
from cares_lib.vision.ArucoDetector import  ArucoDetector

def camera_test():

    camera_matrix     = '/home/david_lab/Desktop/camera_matrix.txt'
    camera_distortion = '/home/david_lab/Desktop/camera_distortion.txt'

    camera_id = 0
    camera = Camera(camera_id, camera_matrix, camera_distortion)

    image = camera.get_frame()
    print(image.shape)

if __name__ == '__main__':
    camera_test()

