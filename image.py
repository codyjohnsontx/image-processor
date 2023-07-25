from PIL import Image, ImageFilter
img = Image.open('./Pokedex/cristofer-maximilian-yk8mvocj6ye-unsplash.jpg')




print(img.size)
img.thumbnail((400,200))
img.save('thumbnail.jpg')