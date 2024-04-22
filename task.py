import cv2
import numpy as np

def blend_images(image1, image2, alpha):
    """
    Blend two images together using a given alpha value.
    """
    blended_image = cv2.addWeighted(image1, alpha, image2, 1 - alpha, 0)
    return blended_image

def main():
    # Load parent images
    parent1 = cv2.imread(r'C:\Users\Admin\Desktop\tanvi\Garg_TANVI\Parent1.jpg')
    parent2 = cv2.imread(r'C:\Users\Admin\Desktop\tanvi\Garg_TANVI\Parent2.jpg')

    # Resize images to the same dimensions
    parent1 = cv2.resize(parent1, (400, 400))
    parent2 = cv2.resize(parent2, (400, 400))

    # Blend images with equal weights
    blended_image = blend_images(parent1, parent2, 0.5)

    # Display the blended image
    cv2.imshow('Blended Image', blended_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
