import tkinter as tk
import random

class Item:
    """Information for each item."""

    def __init__(self, name, stock_level):
        """Initialise item with name and stock level."""
        self.name = name
        self.stock_level = stock_level

class Store:
    """A GUI app for managing store inventory."""

    def __init__(self, root):
        self.root = root
        self.root.title("THE ST0RE")
        self.items_list = []

        self.data_frame = tk.Frame(root)
        self.data_frame.pack()

        products = [
            "Full cream milk (2 L)",
            "Instant coffee (200 g)",
            "Corn flakes cereal (375 g)",
            "Long grain white rice (2 kg)",
            "Smartphone (128 GB, black)",
            "Laptop (15.6-inch, 8 GB RAM, 256 GB SSD)",
            "Wireless noise-cancelling headphones",
            "USB flash drive (64 GB, USB 3.0)",
            "Copy paper (A4, 500 sheets, white)",
            "Ballpoint pens (blue ink, 12-pack)",
            "Stapler (full-strip, 20-sheet capacity)",
            "Sticky notes (3x3 inch, yellow, 12-pack)",
            "Laundry detergent (liquid, 2 L)",
            "Paper towels (8 rolls)",
            "Rubbish bags (kitchen, 13 gallon, 90-pack)",
            "LED light bulbs (60 W equivalent, 4-pack)",
            "Shampoo (400 mL, classic clean)",
            "Whitening toothpaste (110 mL)",
            "Toothbrush (soft bristle, 2-pack)",
            "Hand soap (liquid, 250 mL pump bottle)"
        ]

        for name in products:
            stock = random.randint(1, 100)
            item = Item(name, stock)
            self.items_list.append(item)

        n = 0
        for item in self.items_list:
            name_label = tk.Label(self.data_frame, text=item.name)
            name_label.grid(row=n, column=0)

            stock_label = tk.Label(self.data_frame, text=item.stock_level)
            stock_label.grid(row=n, column=1)
            
            n += 1


    def sell(self):
        print("sell")

    def restock(self):
        print("restock")

if __name__ == "__main__":
    root = tk.Tk()
    store = Store(root)
    root.mainloop()