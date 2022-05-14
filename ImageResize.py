# I'll run pip install opencv-python (to first install the opencv library)
# i'll first import the python image library
import cv2

# to assign a variable to our image path
path = "cecureintel/toluwase" 

# to read the image
image = cv2.imread(path)

# to know the current size of our image 
print(image.shape)

# to resize the image width and height, we set a variable and desired dimensions
width, height = 600, 600

imageResize = cv2.resize(image,(width, height))

# to show the resized image saved with a new variable name
cv2.imshow("toluwase Resized", imageResize)
cv2.waitkey(0)
