import pygame
import pygame_menu
import sorting
import random

print_delay = 0.1
item_amount = 100
func = ""


def create_sort_menu(width, height, screen):
    # Create a menu
    menu = pygame_menu.Menu('Sorting Visualizer', width, height, theme=pygame_menu.themes.THEME_BLUE)

    # Create a list of tuples for the dropdown
    sorting_algorithms = [(name, name) for name in sorting.sorting_functions.keys()]

    # Create a dropdown for the sorting algorithm
    menu.add.dropselect('Sorting Algorithm :', sorting_algorithms,
                        default=0,
                        onchange=lambda value, index: set_sorting_function(value))

    # Create a slider for the sorting speed
    menu.add.range_slider('Sorting Speed (lower is faster):', default=print_delay, range_values=[0, 1], increment=0.001,
                          onchange=lambda value: set_sort_speed(float(value)))

    # Create a text input for the amount of items to sort
    menu.add.range_slider('Amount of Items :', default=item_amount, range_values=[10, 1000], increment=10,
                          onchange=lambda value: set_amount_of_items(int(value)))

    def start_sorting():
        sort(width, height, screen)

    # Add a button to start sorting
    menu.add.button('Start Sorting', start_sorting)

    # Add a button to quit the program
    menu.add.button('Quit', pygame_menu.events.EXIT)

    return menu


def set_sort_speed(value):
    global print_delay

    print_delay = value
    # print(f"Sorting Speed: {value}")


def set_amount_of_items(value):
    global item_amount
    item_amount = value
    # print(f"Amount of Items: {value}")


def set_sorting_function(value):
    global func
    func = value
    # print(f"Sorting function: {value}")


def sort(width, height, screen):
    if func == "":
        return
    heightMap = []
    rect_width = int(width / item_amount)
    for x in range(0, width, rect_width):
        heightMap.append(random.randrange(int(height / 10), height))

    pygame.display.set_caption(func[0][0])
    sorting.show(heightMap, rect_width, screen, 0, [])
    sorting.sorting_functions[func[0][0]](heightMap, rect_width, screen, print_delay)
    pygame.time.wait(2000)
