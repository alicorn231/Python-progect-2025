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
        self.items = []
        self.entries = []
        self.start_row = 2
        self.black = "#1e1e1e"

        self.data_frame = tk.Frame(root)
        self.data_frame.pack(padx=10, pady=10)

        tk.Label(self.data_frame, text="Product List", font=("Arial", 16, "bold")).grid(
            row=0, column=0, columnspan=6, pady=(0, 10)
        )

        # Header row
        tk.Label(self.data_frame, text="New Product:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.name_entry = tk.Entry(self.data_frame, width=25, bd=2, relief="solid")
        self.name_entry.grid(row=1, column=1, padx=5)

        self.stock_entry = tk.Entry(self.data_frame, width=5, bd=2, relief="solid")
        self.stock_entry.grid(row=1, column=2, padx=5)

        submit_button = tk.Button(self.data_frame, text="Submit", bd=2, relief="solid", command=self.new_item)
        submit_button.grid(row=1, column=3, padx=5)

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

        for name, stock in products:
            self.items.append(Item(name, stock))

        self.render_items()

        self.error_label = tk.Label(self.root, fg="red", font=("Arial", 30, "bold"))
        self.error_label.pack(pady=5)

    def render_items(self):
        """Render the product list to the UI."""
        start_row = 2
        for widget in self.data_frame.winfo_children():
            info = widget.grid_info()
            if info["row"] >= self.start_row:
                widget.destroy()
        
        self.entries.clear()
        for index, item in enumerate(self.items):
            row_num = index + start_row
            row_num = index + self.start_row
            tk.Label(self.data_frame, text=item.name).grid(row=row_num, column=1, padx=10)
            stock_label = tk.Label(self.data_frame, text=str(item.stock_level))
            stock_label.grid(row=row_num, column=2, padx=10)

            entry = tk.Entry(self.data_frame, width=5)
            entry.grid(row=row_num, column=4)

            tk.Button(self.data_frame, text="Add", command=lambda i=index: self.operate(i, "add")).grid(row=row_num, column=3)
            tk.Button(self.data_frame, text="Minus", command=lambda i=index: self.operate(i, "minus")).grid(row=row_num, column=5, padx=20)

            self.entries.append({
                "entry": entry,
                "stock_label": stock_label
            })

    def operate(self, product_index, operator):
        """Update stock level based on user input."""
        quantity_entry = self.entries[product_index]["entry"]
        try:
            amount = int(quantity_entry.get())
            if operator == "add":
                self.items[product_index].stock_level += amount
            else:
                self.items[product_index].stock_level -= amount
            new_stock = self.items[product_index].stock_level
            if new_stock < 0:
                new_stock = 0
                self.items[product_index].stock_level = 0
            self.entries[product_index]["stock_label"].config(text=str(new_stock))

            quantity_entry.config(bg="#008000")  # Set the initial background to dark
            quantity_entry.after(500, lambda: quantity_entry.config(bg=self.black))
            quantity_entry.delete(0, tk.END)
            self.error_label.config(text="")
        except ValueError:
            self.error_label.config(text="Enter a number")
            quantity_entry.config(bg="red")
            self.error_label.after(5000, lambda: self.error_label.config(text=""))
            self.error_label.after(500, lambda: quantity_entry.config(bg=self.black))
            quantity_entry.after(500, lambda: quantity_entry.delete(0, tk.END))

    def new_item(self):
        name = self.name_entry.get()
        stock = self.stock_entry.get()
        if len(name) < 3:
            self.name_entry.config(bg="red")
            self.name_entry.after(500, lambda: self.name_entry.config(bg=self.black))
            self.error_label.config(text="Please enter a valid name (at least 3 characters)")
            self.error_label.after(3000, lambda: self.error_label.config(text=""))
            return
            

        try:
            stock = int(stock)  # Convert stock to an integer
            self.items.append(Item(name, stock))  # Add the new item
            self.render_items()  # Re-render the list with the new item
            self.name_entry.delete(0, tk.END)  # Clear the name entry
            self.stock_entry.delete(0, tk.END)  # Clear the stock entry
            self.stock_entry.config(bg="Green")
            self.name_entry.config(bg="Green")
            self.stock_entry.after(500, lambda: self.stock_entry.config(bg=self.black))
            self.name_entry.after(500, lambda: self.name_entry.config(bg=self.black))
        except ValueError:
            self.stock_entry.config(bg="red")
            self.stock_entry.after(500, lambda: self.stock_entry.config(bg=self.black))
            self.error_label.config(text="Please enter a valid number for stock level.")
            self.error_label.after(3000, lambda: self.error_label.config(text="")) 
if __name__ == "__main__":
    root = tk.Tk()
    store = Store(root)
    root.mainloop()