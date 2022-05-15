from PIL import Image
img = Image.open("white dog.jpg")
resized_img = img.resize((500, 300))
resized_img.save("resized_img.jpg")

