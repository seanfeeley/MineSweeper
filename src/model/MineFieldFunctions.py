import src.model.GameStates as states
import random


def generate_minefield(rows, columns, mines):
    minefield = generate_empty_minefield(rows, columns)
    minefield = add_mines_to_minefield(mines, minefield)
    return minefield


def generate_empty_minefield(rows, columns):
    minefield = []
    for row_index in range(0, rows):
        minefield.append([])
        for columns_index in range(0, columns):
            minefield[row_index].append(states.BLANK)
    return minefield


def add_mines_to_minefield(mines, minefield):
    mine_counter = 0
    while mine_counter < mines:
        random_row = random.randint(0, len(minefield)-1)
        random_column = random.randint(0, len(minefield[0])-1)
        if minefield[random_row][random_column] != states.MINE:
            minefield = add_mine_to_minefield(random_row,
                                              random_column,
                                              minefield)
            mine_counter += 1
    return minefield


def add_mine_to_minefield(row_index, column_index, minefield):
    minefield[row_index][column_index] = states.MINE
    attached_coords = get_attached_coords(row_index, column_index, minefield)
    for coord in attached_coords:
        minefield = increase_hint(coord[0], coord[1], minefield)
    return minefield


def increase_hint(row_index, column_index, minefield):
    value = minefield[row_index][column_index]
    # Since blank is 0 and the hint values increase from 1
    # we can just increment the value by 1
    if value >= states.BLANK:
        minefield[row_index][column_index] += 1
    return minefield


def get_blank_area(non_mines, minefield):
    row_index = non_mines[-1][0]
    column_index = non_mines[-1][1]
    attached_coords = get_attached_coords(row_index,
                                          column_index,
                                          minefield)
    for coord in attached_coords:
        if coord not in non_mines:
            coord_status = minefield[coord[0]][coord[1]]
            is_hint = coord_status >= states.HINT1
            is_blank = coord_status == states.BLANK
            if is_blank or is_hint:
                non_mines.append(coord)
            if is_blank:
                non_mines = get_blank_area(non_mines,
                                           minefield)

    return non_mines


def get_attached_coords(row_index, column_index, minefield):
    coords = []
    directions = [[-1, -1],
                  [0, -1],
                  [1, -1],
                  [-1, 0],
                  [1, 0],
                  [-1, 1],
                  [0, 1],
                  [1, 1]]
    for direction in directions:
        new_coord = [direction[0]+row_index, direction[1]+column_index]
        # print(new_coord)
        if (new_coord[0] >= 0
           and new_coord[1] >= 0
           and new_coord[0] < len(minefield)
           and new_coord[1] < len(minefield[0])):
            coords.append(new_coord)
    return coords
