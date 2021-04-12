def p_allowed(cell_from, cell_to, white):
    black = not white

    x1, y1 = cell_from
    x2, y2 = cell_to

    if x1 == x2 and y1 == y2:
        return False

    if (y2 == 1 or y1 == 1) and white:
        return False
    if (y1 == 8 or y2 == 8) and black:
        return False

    if not borders(cell_from, cell_to):
        return False

    if white:
        if y1 == 2 and y2 == 4:
            return True
    else:
        if y1 == 7 and y2 == 5:
            return True

    if white:
        return x1 == x2 and y1 + 1 == y2
    else:
        return x1 == x2 and y1 - 1 == y2


def k_allowed(cell_from, cell_to):
    x1, y1 = cell_from
    x2, y2 = cell_to

    if x1 == x2 and y1 == y2:
        return False

    if not borders(cell_from, cell_to):
        return False

    # движение вперед и назад
    if x1 == x2:
        return x1 == x2 and (y1 + 1 == y2 or y1 - 1 == y2)

    # движение вправо, влево, по диагонали
    elif x1 + 1 == x2 or x1 - 1 == x2:
        return (x1 + 1 == x2 or x1 - 1 == x2) and (y1 == y2 or y1 + 1 == y2 or y1 - 1 == y2)


def b_allowed(cell_from, cell_to):
    x1, y1 = cell_from
    x2, y2 = cell_to

    if x1 == x2 and y1 == y2:
        return False

    if not borders(cell_from, cell_to):
        return False

    # движение по белым клеткам
    if (y1 + x1) == (y2 + x2) or abs(y1 - x1) == abs(y2 - x2):
        return True


def n_allowed(cell_from, cell_to):
    x1, y1 = cell_from
    x2, y2 = cell_to

    if x1 == x2 and y1 == y2:
        return False

    if not borders(cell_from, cell_to):
        return False

    # движение с верха "Г"
    if x1 + 1 == x2 or x1 - 1 == x2:
        return (x1 + 1 == x2 or x1 - 1 == x2) and (y1 + 2 == y2 or y1 - 2 == y2)

    # движение с низа "Г"
    elif x1 + 2 == x2 or x1 - 2 == x2:
        return (x1 + 2 == x2 or x1 - 2 == x2) and (y1 + 1 == y2 or y1 - 1 == y2)


def r_allowed(cell_from, cell_to):
    x1, y1 = cell_from
    x2, y2 = cell_to

    if x1 == x2 and y1 == y2:
        return False

    if not borders(cell_from, cell_to):
        return False

    # движение вверх и вниз
    if x1 == x2:
        return x1 == x2 and y1 != y2

    # движение влево и вправо
    else:
        return x1 != x2 and y1 == y2


def q_allowed(cell_from, cell_to):
    return k_allowed(cell_from, cell_to) or b_allowed(cell_from, cell_to) or r_allowed(cell_from, cell_to)


def borders(cell_from, cell_to):
    x1, y1 = cell_from
    x2, y2 = cell_to
    if y1 > 8 or y2 > 8 or y1 < 1 or y2 < 1:
        return False
    if x1 > 8 or x2 > 8 or x1 < 1 or x2 < 1:
        return False
    return True


def board_move_ok(cell_from, cell_to, board):
    return True
