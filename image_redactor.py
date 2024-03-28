from PIL import Image, ImageFilter

img = Image.open('example.jpg')

new_size = (img.width // 2, img.height // 2)
resized_img = img.resize(new_size)
filtered_img = resized_img.filter(ImageFilter.SMOOTH)

filtered_img.save('result_image.jpg')
