"""This program create an ajuastabeble GUI inventory."""
import tkinter as tk


class Item:
    """Information for each item."""

    def __init__(self, name, stock_level):
        """Create name and stock_level info."""
        self.name = name
        self.stock_level = stock_level


class Store:
    """A GUI app for managing store inventory."""

    def __init__(self, root):
        """Initialize the store inventory GUI application.

        Sets up the main window, input fields for adding
        new products, and displays a predefined list of
        items. Initializes internal data structures for
        tracking items and dynamically updating their
        stock levels. Also configures the layout, input
        validation, and error messaging UI components.
        """

        self.root = root
        self.root.title("THE ST0RE")
        self.items = []
        self.entries = []
        self.start_row = 2
        self.BLACK = "#1e1e1e"
        self.GREEN = "#008000"
        self.MAX_STOCK = 1000

        self.data_frame = tk.Frame(root)
        self.data_frame.pack(padx=10, pady=10)

        # Title
        tk.Label(self.data_frame, text="Product List", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=6, pady=(0, 10))

        # New prouct row
        tk.Label(self.data_frame, text="New Product:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.name_entry = tk.Entry(self.data_frame, width=25, bd=2, relief="solid")
        self.name_entry.grid(row=1, column=1, padx=5)

        self.stock_entry = tk.Entry(self.data_frame, width=5, bd=2, relief="solid")
        self.stock_entry.grid(row=1, column=2, padx=5)

        submit_button = tk.Button(self.data_frame, text="Submit", bd=2, relief="solid", command=self.new_item)
        submit_button.grid(row=1, column=3, padx=5)

        # List of preloaded data
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

        # Adding preloading data to class
        for name, stock in products:
            self.items.append(Item(name, stock))

        self.render_items()

        # Creating error lable
        self.error_label = tk.Label(self.root, fg="red", font=("Arial", 30, "bold"))
        self.error_label.pack(pady=5)

    def render_items(self):
        """Render the product list to the UI.

        starting in the second row,
        clears old data so when new items
        are added items rows don't break,
        then adds each item, they're
        buttons, and entry box.
        """
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

            # here the code repeats,
            # however it would not be more effienct
            # to have use a loop as it adds
            # unesacery complexity and removes
            # readibility
            tk.Button(self.data_frame, text="Add", command=lambda i=index: self.operate(i, "add")).grid(row=row_num, column=3)
            tk.Button(self.data_frame, text="Minus", command=lambda i=index: self.operate(i, "minus")).grid(row=row_num, column=5, padx=20)

            self.entries.append({
                "entry": entry,
                "stock_label": stock_label
            })

    def operate(self, product_index, operator):
        """Update stock level based on user input.

        adds or subtracts apporiate amount,
        input validates,
        """
        quantity_entry = self.entries[product_index]["entry"]
        try:
            amount = int(quantity_entry.get())
            if operator == "add":
                self.items[product_index].stock_level += amount
            else:
                self.items[product_index].stock_level -= amount
            new_stock = self.items[product_index].stock_level

            if new_stock < 0:  # ensuring stock isn't negative
                new_stock = 0
                self.items[product_index].stock_level = 0

            if new_stock >= self.MAX_STOCK:  # ensuring stock way to big
                new_stock = self.MAX_STOCK
                self.items[product_index].stock_level = self.MAX_STOCK

            self.entries[product_index]["stock_label"].config(text=str(new_stock))

            quantity_entry.config(bg=self.GREEN)
            quantity_entry.after(500, lambda: quantity_entry.config(bg=self.BLACK))  # waits .5s to change colour
            quantity_entry.delete(0, tk.END)
            self.error_label.config(text="")
        except ValueError:
            self.error_label.config(text="Enter a number")
            quantity_entry.config(bg="red")
            self.error_label.after(5000, lambda: self.error_label.config(text=""))
            self.error_label.after(500, lambda: quantity_entry.config(bg=self.BLACK))
            quantity_entry.after(500, lambda: quantity_entry.delete(0, tk.END))

    def new_item(self):
        """Add new item, and input validates and removes old input."""
        name = self.name_entry.get()
        stock = self.stock_entry.get()

        if len(name) < 3:  # ensures name is atleast 3 characters long
            self.name_entry.config(bg="red")
            self.name_entry.after(500, lambda: self.name_entry.config(bg=self.BLACK))
            self.error_label.config(text="Please enter a valid name (at least 3 characters)")
            self.error_label.after(3000, lambda: self.error_label.config(text=""))
            return

        if any(item.name.lower() == name.lower() for item in self.items):
            self.name_entry.config(bg="red")
            self.name_entry.after(500, lambda: self.name_entry.config(bg=self.BLACK))
            self.error_label.config(text="This product already exists.")
            self.error_label.after(3000, lambda: self.error_label.config(text=""))
            return

        try:
            stock = int(stock)
            if stock <= 0 or stock > self.MAX_STOCK:
                self.stock_entry.config(bg="red")
                self.stock_entry.after(500, lambda: self.stock_entry.config(bg=self.BLACK))
                self.error_label.config(text=f"Stock must be between 1 and {self.MAX_STOCK}.")
                self.error_label.after(3000, lambda: self.error_label.config(text=""))
                return
        except ValueError:
            self.stock_entry.config(bg="red")
            self.stock_entry.after(500, lambda: self.stock_entry.config(bg=self.BLACK))
            self.error_label.config(text="Please enter a valid number for stock level.")
            self.error_label.after(3000, lambda: self.error_label.config(text=""))
            return

        # If all validations pass, add the new item
        self.items.append(Item(name, stock))
        self.render_items()

        # Clear and highlight inputs
        self.name_entry.delete(0, tk.END)
        self.stock_entry.delete(0, tk.END)
        self.name_entry.config(bg=self.GREEN)
        self.stock_entry.config(bg=self.GREEN)
        self.name_entry.after(500, lambda: self.name_entry.config(bg=self.BLACK))
        self.stock_entry.after(500, lambda: self.stock_entry.config(bg=self.BLACK))
        self.error_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    store = Store(root)
    root.mainloop()
