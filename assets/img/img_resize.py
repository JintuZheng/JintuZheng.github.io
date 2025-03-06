from skimage import io
import cv2

im = io.imread('profile.jpg')
im = cv2.resize(im, (int(im.shape[1]//2), int(im.shape[0]//2)))
io.imsave('profile.jpg', im)