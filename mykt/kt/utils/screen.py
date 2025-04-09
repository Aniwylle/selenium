from PIL import Image, ImageChops

def compare_images(image1_path, image2_path): 
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)
    
    diff = ImageChops.difference(image1, image2)

    if diff.getbbox() is None:
        return True
    return False