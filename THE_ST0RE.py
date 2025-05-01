"""A simple inventory system for a store."""
import tkinter as tk


class Items:
    """Infomation for each item."""

    def __init__(self, name, stock_level) -> None:
        """Intizalize infomation about each item icluding name and amount."""
        self.name = name
        self.stock_level = stock_level


class Store:
    """A GUI application for collecting and displaying survey information.

    Users can enter find items, stock level, and log restock/selling of items.
    """

    def __init__(self, root):
        """Set up the main window and variables for the app."""
        self.root = root
        self.root.title("THE ST0RE")
        self.items_list = []

    def sell(self):
        """Remove item from stock_level count."""
        print("sell")

    def restock(self):
        """Add item from stock_level count."""
        print("restock")


if __name__ == "__main__":
    root = tk.Tk()
    store = Store(root)
    root.mainloop()
