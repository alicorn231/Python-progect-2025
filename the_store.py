import tkinter as tk

class Item:
    """Information for each item."""
    def __init__(self, name, stock_level):
        self.name = name
        self.stock_level = stock_level

class Store:
    """A GUI app for managing store inventory."""

    def __init__(self, root):
        self.root = root
        self.root.title("THE ST0RE")
        self.items_list = []
        self.entries = []

        self.data_frame = tk.Frame(root)
        self.data_frame.pack()

        # List of (name, stock) tuples
        products = [
            ("Full cream milk (2 L)", 5),
            ("Instant coffee (200 g)", 12),
            ("Corn flakes cereal (375 g)", 20),
            ("Long grain white rice (2 kg)", 23),
            ("Smartphone (128 GB, black)", 4),
            ("Laptop (15.6-inch, 8 GB RAM, 256 GB SSD)", 22),
            ("Wireless noise-cancelling headphones", 86),
            ("USB flash drive (64 GB, USB 3.0)", 23),
            ("Copy paper (A4, 500 sheets, white)", 2),
            ("Ballpoint pens (blue ink, 12-pack)", 91),
            ("Stapler (full-strip, 20-sheet capacity)", 7),
            ("Sticky notes (3x3 inch, yellow, 12-pack)", 42),
            ("Laundry detergent (liquid, 2 L)", 30),
            ("Paper towels (8 rolls)", 25),
            ("Rubbish bags (kitchen, 13 gallon, 90-pack)", 15),
            ("LED light bulbs (60 W equivalent, 4-pack)", 13),
            ("Shampoo (400 mL, classic clean)", 53),
            ("Whitening toothpaste (110 mL)", 3),
            ("Toothbrush (soft bristle, 2-pack)", 71),
            ("Hand soap (liquid, 250 mL pump bottle)", 100),
        ]

        # Create item objects
        for name, stock in products:
            self.items_list.append(Item(name, stock))

        # Create UI for each item
        for index, item in enumerate(self.items_list):
            tk.Label(self.data_frame, text=item.name).grid(row=index, column=0)
            stock_label = tk.Label(self.data_frame, text=str(item.stock_level))
            stock_label.grid(row=index, column=1)

            add_entry = tk.Entry(self.data_frame, width=5)
            add_entry.grid(row=index, column=3)
            tk.Button(self.data_frame, text="Add:", command=lambda i=index: self.operate(i, "add")).grid(row=index, column=2)

            minus_entry = tk.Entry(self.data_frame, width=5)
            minus_entry.grid(row=index, column=5)
            tk.Button(self.data_frame, text="Minus:", command=lambda i=index: self.operate(i, "minus")).grid(row=index, column=4)

            self.entries.append({
                "add": add_entry,
                "minus": minus_entry,
                "stock_label": stock_label
            })

    def operate(self, product_index, operator):
        """Update stock level based on user input."""
        entry_widget = self.entries[product_index][operator]
        try:
            amount = int(entry_widget.get())
            if operator == "add":
                self.items_list[product_index].stock_level += amount
            else:
                self.items_list[product_index].stock_level -= amount
            new_stock = self.items_list[product_index].stock_level
            self.entries[product_index]["stock_label"].config(text=str(new_stock))
        except ValueError:
            print("Invalid input: please enter an integer")

if __name__ == "__main__":
    root = tk.Tk()
    store = Store(root)
    root.mainloop()