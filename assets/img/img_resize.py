from skimage import io
import cv2

im = io.imread('ucas_logo.jpg')
im = cv2.resize(im, (int(im.shape[1]//2), int(im.shape[0]//2)))
io.imsave('ucas_logo.jpg', im)