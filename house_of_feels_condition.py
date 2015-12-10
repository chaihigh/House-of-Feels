class Condition:
    """Define a Condition.

    attributes: is_fulfilled (boolean)"""

    def __init__(self, is_fulfilled=False):
        """Store the attribute.

        Condition[, boolean] -> None"""

        self.is_fulfilled = is_fulfilled

happy_aidan = Condition()
