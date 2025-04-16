from PIL import Image
import numpy as np
from functions import sealing_figure, elision_figure

image = Image.open('input.png').convert('L')
image_array = np.array(image)
binary_matrix = (image_array < 128).astype(int)

height = len(binary_matrix)
width = len(binary_matrix[0])

filter = {
    'x': int(1),
    'y': int(1),
    'template': [[1,1,1],
                 [1,1,1],
                 [1,1,1]],
}

for y in range(height):
    print(binary_matrix[y])

result_elision = elision_figure(input_matrix=binary_matrix, filter=filter)
for y in result_elision:
    print(y)

r = np.array(result_elision)
image_array_restored = (1 - r) * 255
image_array_restored = image_array_restored.astype(np.uint8)
restored_image = Image.fromarray(image_array_restored, mode='L')
restored_image.save('elisionImage.png')


result_sealing = sealing_figure(input_matrix=result_elision, filter=filter)
r = np.array(result_sealing)
image_array_restored = (1 - r) * 255
image_array_restored = image_array_restored.astype(np.uint8)
restored_image = Image.fromarray(image_array_restored, mode='L')
restored_image.save('sealingImage.png')