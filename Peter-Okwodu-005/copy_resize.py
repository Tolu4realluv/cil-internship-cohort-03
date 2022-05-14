import cv2
# A function that copies and resizes an image
def _copy_obj(obj):
    """copies an object

    Return:
        copied object"""
    temp = None

    # check if object is a list or tuple
    if (isinstance(obj, list) == True) or (isinstance(obj, tuple) == True):
            temp = obj[:]

    # check if object is a dictionary or a set
    elif (isinstance(obj, dict) == True) or (isinstance(obj, set) == True):
        temp = obj.copy()

    else:
        temp = obj

    return (temp)


# A function that resizes images using resize from opencv module
def _resize_jpg(img = None, height = None, width = None, percent = None):
    """Resizes an jpg object
    Args:
        obj: image to resize
        height: width to resize the image by (optional)
        width: height to resize the image by (optional)
        percent: percentage to resize the image by (optional)
    Return:
        resized image
    """
    new_width = int(img.shape[1] * percent/100)
    new_height = int(img.shape[0] * percent/100)
    dim = (width, height)
    # check if an image is passed
    if (img == None):
        return "Input error: No image have been passed to function"

    # priotizes resizing by percent if both percent and height/width param are passed
    elif (percent != None) and (height != None or width != None):
        resized_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        return (resized_img)

    # check if user wants to resize by only height
    elif (percent == None and width == None) or (height != None):
        new_height = height
        new_width = img.shape[1]
        dim = (width, height)
        resized_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        return (resized_img)

    # check if user wants to resize by only width
    elif (percent == None and height == None) or (width != None):
        new_width = width
        new_height = img.shape[0]
        dim = (width, height)
        resized_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        return (resized_img)

    # check if user wants to resize by both height and width
    elif (percent == None) and (height != None and width != None):
        new_height = height
        new_width = width
        dim = (width, height)
        resized_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        return (resized_img)

    # resizes by percent
    else:
        resized_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        return (resized_img)
