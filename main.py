from PIL import Image
import numpy as np

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


def elision_figure(input_matrix, filter):
    height = len(input_matrix)
    width = len(input_matrix[0])
    virtual_display = [[0 for x in range(width)] for y in range(height)]
    width_filter = max(len(x) for x in filter['template'])
    height_filter = len(filter['template'])
    count_of_cells = sum(len(x) for x in filter['template'])
    filter_y = int(filter['y'])
    filter_x = int(filter['x'])
    print(count_of_cells)
    for y in range(filter['y'], height - (height_filter - filter['y'])):
        for x in range(filter['x'], width - (width_filter - filter['x'])):
            if input_matrix[y][x] == filter['template'][filter_y][filter_x]:
                counter = 0
                for y_f in range(height_filter):
                    for x_f in range(len(filter['template'][y_f])):
                        if filter['template'][y_f][x_f] == input_matrix[y - filter_y + y_f][x - filter_x + x_f]:
                            counter += 1
                        else:
                            break
                if counter == count_of_cells:
                    virtual_display[y][x] = filter['template'][filter_y][filter_x]
    return virtual_display

result_elision = elision_figure(input_matrix=binary_matrix, filter=filter)
for y in result_elision:
    print(y)

r = np.array(result_elision)
image_array_restored = (1 - r) * 255
image_array_restored = image_array_restored.astype(np.uint8)
restored_image = Image.fromarray(image_array_restored, mode='L')
restored_image.save('elisionImage.png')