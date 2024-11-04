"""
File: babygraphics.py
Name: Quill
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt',
    'data/full/baby-2020.txt'
]
CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010, 2020]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    # Calculate each interval width on x
    interval_width = (width - 2 * GRAPH_MARGIN_SIZE) / (len(YEARS))
    # Calculate x coordinate for each year
    x = GRAPH_MARGIN_SIZE + interval_width * year_index
    return x


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    # Draw the top horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    # Draw the bottom horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    # Draw the year line
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    # Initialize color index
    i = 0
    # Loop through each name in lookup_names
    for name in lookup_names:
        if name in name_data:
            color = COLORS[i % len(COLORS)]
            i += 1
            # Loop through each year to get x, y
            for j in range(len(YEARS)-1):
                year = YEARS[j]
                x = get_x_coordinate(CANVAS_WIDTH, j)

                if str(year) in name_data[name]:
                    rank = int(name_data[name][str(year)])
                    y = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE) * rank / 1000
                else:
                    rank = '*'
                    y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE

                # Loop through each year to get x_next, y_next
                next_year = YEARS[j + 1]
                next_x = get_x_coordinate(CANVAS_WIDTH, j + 1)

                if str(next_year) in name_data[name]:
                    next_rank = int(name_data[name][str(next_year)])
                    next_y = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * next_rank / 1000
                else:
                    next_rank = '*'
                    next_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE

                canvas.create_line(x, y, next_x, next_y, width=LINE_WIDTH, fill=color)
                canvas.create_text(x+TEXT_DX, y, text=f'{name} {rank}', anchor=tkinter.SW, fill=color)

            # Add last year text label
            last_year = YEARS[-1]
            last_x = get_x_coordinate(CANVAS_WIDTH, len(YEARS)-1)

            if str(last_year) in name_data[name]:
                rank = int(name_data[name][str(last_year)])
                last_y = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2*GRAPH_MARGIN_SIZE) * rank / 1000
            else:
                last_rank = '*'
                last_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE

            canvas.create_text(last_x+TEXT_DX, last_y, text=f'{name} {rank}', anchor=tkinter.SW, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
