def elision_figure(input_matrix, filter):
    height = len(input_matrix)
    width = len(input_matrix[0])
    virtual_display = [[0 for x in range(width)] for y in range(height)]
    width_filter = max(len(x) for x in filter['template'])
    height_filter = len(filter['template'])
    count_of_cells = sum(len(x) for x in filter['template'])
    filter_y = int(filter['y'])
    filter_x = int(filter['x'])
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

def sealing_figure(input_matrix, filter):
    height = len(input_matrix)
    width = len(input_matrix[0])
    virtual_display = [[0 for x in range(width)] for y in range(height)]
    width_filter = max(len(x) for x in filter['template'])
    height_filter = len(filter['template'])
    filter_y = int(filter['y'])
    filter_x = int(filter['x'])
    for y in range(filter['y'], height - (height_filter - filter['y'])):
        for x in range(filter['x'], width - (width_filter - filter['x'])):
            if input_matrix[y][x] == filter['template'][filter_y][filter_x]:
                for y_f in range(height_filter):
                    for x_f in range(len(filter['template'][y_f])):
                        if virtual_display[y - filter_y + y_f][x - filter_x + x_f] != 1:
                            virtual_display[y - filter_y + y_f][x - filter_x + x_f] = filter['template'][y_f][x_f]
    return virtual_display