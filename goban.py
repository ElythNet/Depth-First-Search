import enum


class Status(enum.Enum):
    """
    Enum representing the Status of a position on a goban
    """
    WHITE = 1
    BLACK = 2
    EMPTY = 3
    OUT = 4


class Goban(object):
    def __init__(self, goban):
        self.goban = goban
        self.x_history = []
        self.y_history = []
        self.took = 1

    def get_status(self, x, y):
        """
        Get the status of a given position

        Args:
            x: the x coordinate
            y: the y coordinate

        Returns:
            a Status
        """
        if not self.goban or x < 0 or y < 0 or y >= len(self.goban) or x >= len(self.goban[0]):
            return Status.OUT
        elif self.goban[y][x] == '.':
            return Status.EMPTY
        elif self.goban[y][x] == 'o':
            return Status.WHITE
        elif self.goban[y][x] == '#':
            return Status.BLACK

    def already_checked(self, x, y):
        for i in range(0, len(self.x_history)):
            if self.x_history[i] == x and self.y_history[i] == y:
                return True
        return False

    def is_taken(self, x, y):
        current_status = self.get_status(x, y)
        self.x_history.append(x)
        self.y_history.append(y)
        if self.get_status(x - 1, y) == Status.EMPTY:
            return False
        elif self.get_status(x, y - 1) == Status.EMPTY:
            return False
        elif self.get_status(x + 1, y) == Status.EMPTY:
            return False
        elif self.get_status(x, y + 1) == Status.EMPTY:
            return False
        else:
            if not self.already_checked(x - 1, y) and self.get_status(x - 1, y) == current_status:
                if not self.is_taken(x - 1, y):
                    self.took = False
                    return False
            if not self.already_checked(x, y - 1) and self.get_status(x, y - 1) == current_status:
                if not self.is_taken(x, y - 1):
                    self.took = False
                    return False
            if not self.already_checked(x + 1, y) and self.get_status(x + 1, y) == current_status:
                if not self.is_taken(x + 1, y):
                    self.took = 0
                    return False
            if not self.already_checked(x, y + 1) and self.get_status(x, y + 1) == current_status:
                if not self.is_taken(x, y + 1):
                    self.took = 0
                    return False
            if not self.took:
                return False
            else:
                return True
