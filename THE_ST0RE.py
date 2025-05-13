import tkinter as tk

class Item:
    """Information for each item."""

    def __init__(self, name, stock_level, item_index):
        """Initialise item with name and stock level."""
        self.name = name
        self.stock_level = stock_level
        self.item_index = item_index

class Store:
    """A GUI app for managing store inventory."""

    def __init__(self, root):
        self.root = root
        self.root.title("THE ST0RE")
        self.items_list = []

        self.data_frame = tk.Frame(root)
        self.data_frame.pack()
        self.entries = []

        products = {
            0: ["Full cream milk (2 L)", 5],
            1: ["Instant coffee (200 g)", 12],
            2: ["Corn flakes cereal (375 g)", 20],
            3: ["Long grain white rice (2 kg)", 23],
            4: ["Smartphone (128 GB, black)", 4],
            5: ["Laptop (15.6-inch, 8 GB RAM, 256 GB SSD)", 22],
            6: ["Wireless noise-cancelling headphones", 86],
            7: ["USB flash drive (64 GB, USB 3.0)", 23],
            8: ["Copy paper (A4, 500 sheets, white)", 2],
            9: ["Ballpoint pens (blue ink, 12-pack)", 91],
            10: ["Stapler (full-strip, 20-sheet capacity)", 7],
            11: ["Sticky notes (3x3 inch, yellow, 12-pack)", 42],
            12: ["Laundry detergent (liquid, 2 L)", 30],
            13: ["Paper towels (8 rolls)", 25],
            14: ["Rubbish bags (kitchen, 13 gallon, 90-pack)", 15],
            15: ["LED light bulbs (60 W equivalent, 4-pack)", 13],
            16: ["Shampoo (400 mL, classic clean)", 53],
            17: ["Whitening toothpaste (110 mL)", 3],
            18: ["Toothbrush (soft bristle, 2-pack)", 71],
            19: ["Hand soap (liquid, 250 mL pump bottle)", 100],
        }

        """Setting up preloaded products"""
        n = 0
        for index, (name, stock) in products.items():
            item = Item(name, stock, index)
            self.items_list.append(item)
            # print(f"{name}, {stock}, {index}")
            self.entries.append(0)
        n = 0
        for item in self.items_list:
            name_label = tk.Label(self.data_frame, text=item.name)
            name_label.grid(row=n, column=0)

            stock_label = tk.Label(self.data_frame, text=item.stock_level)
            stock_label.grid(row=n, column=1)
            add_button = tk.Button(self.data_frame, text="Add:", command=lambda i=item.item_index: self.add(i))
            add_button.grid(row=n, column= 2)
            add_entry = tk.Entry(self.data_frame)
            add_entry.grid(row=n, column=3)

            self.value_test(add_entry)

            self.entries[n]+= add_entry
 
            minus_button = tk.Button(self.data_frame, text="Minus:", command=lambda i=item.item_index: self.minus(i))
            minus_button.grid(row=n, column= 4)
            minus_entry = tk.Entry(self.data_frame)
            minus_entry = int(minus_entry)
            minus_entry.grid(row=n, column= 5)
            self.entries[n]-= minus_entry
            
            n += 1
        
    def add(self, product_no):
        print(f"stock, {product_no}")
        input = self.entries[product_no].get()
        print(f"number in box, {input}")

    def minus(self, product_no):
        print(f"sell, {product_no}")
        input = self.entries[product_no].get()
        print(f"number in box, {input}")
    
    def value_test(self, entry_widget):
        is_valid = False
        while not is_valid:
            try:
                value = int(entry_widget.get())
                is_valid = True
                return value
            except ValueError:
                # print("Invalid input: not an integer")
                is_valid = False
if __name__ == "__main__":
    root = tk.Tk()
    store = Store(root)
    root.mainloop()