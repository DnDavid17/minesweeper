from tkinter import *
from cell import Cell
import settings
import utils
root = Tk()

# Setarile pentru fereastra
root.configure(bg="antique white")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper proiect atestat')
root.resizable(False, False)

# titlu
top_frame = Frame(
    root,
    bg="old lace",
    width=settings.WIDTH,
    height=utils.height_prct(25)
                 )
top_frame.place(x=0, y=0)

# scoreboard
left_frame = Frame(
    root,
    bg="navajo white",
    width=utils.width_prct(25),
    height=utils.height_prct(75)
                  )
left_frame.place(x=0, y=utils.height_prct(25))

# plansa jocului
center_frame = Frame(
    root,
    bg="misty rose",
    width=utils.width_prct(75),
    height=utils.height_prct(75)
                    )
center_frame.place(x=utils.width_prct(25), y=utils.height_prct(25))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)

Cell.randomize_mines()
# Functionarea ferestrei
root.mainloop()
