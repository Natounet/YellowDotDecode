import tkinter as tk
from tkinter import messagebox

class YellowDotDecoderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Yellow Dot Decoder")
        self.root.eval('tk::PlaceWindow . center')
        self.root.resizable(True, True)

        # Interface Widgets
        self.label = tk.Label(root, text="Click the grid to mark yellow dots")
        self.label.grid(row=0, column=0, columnspan=15, pady=10, sticky='n')

        # Create a grid of checkboxes to represent the yellow dot pattern
        self.grid_cols = 15  # Updated grid size to 15 columns
        self.grid_rows = 8  # Updated grid size to 8 rows
        self.checkbuttons = []
        self.check_vars = []
        for row in range(self.grid_rows):  # 8 rows for decoding
            row_vars = []
            row_buttons = []
            for col in range(self.grid_cols):
                var = tk.IntVar()
                chk = tk.Checkbutton(root, variable=var)
                chk.grid(row=row+1, column=col, padx=2, pady=2)
                row_vars.append(var)
                row_buttons.append(chk)
            self.check_vars.append(row_vars)
            self.checkbuttons.append(row_buttons)

        self.decode_button = tk.Button(root, text="Decode Pattern", command=self.decode_pattern)
        self.decode_button.grid(row=9, column=0, columnspan=15, pady=10)

        self.result_label = tk.Label(root, text="Decoded Information:")
        self.result_label.grid(row=10, column=0, columnspan=15, pady=10)

        self.result_text = tk.Text(root, height=10, width=80)
        self.result_text.grid(row=11, column=0, columnspan=15, pady=10)
        self.result_text.config(state=tk.NORMAL)

    def decode_pattern(self):
        # Decode the pattern based on the selected checkboxes
        selected_points = []
        for row in range(self.grid_rows):
            row_points = []
            for col in range(self.grid_cols):
                if self.check_vars[row][col].get() == 1:
                    row_points.append(1)
                else:
                    row_points.append(0)
            selected_points.append(row_points)
        
        # Process the selected points to decode the information
        decoded_info = ""
        columns = list(zip(*selected_points))  # Transpose rows to columns
        sn = ""
        minutes = ""
        hours = ""
        day = ""
        month = ""
        years = ""
        # Each column is read from top to bottom as an octet of seven bits, ignoring the first bit
        for col_num, column in enumerate(columns, start=1):
            column_bits = column[1:]  # Ignore the first bit (index 0)
            value = sum(bit * (2 ** (6 - idx)) for idx, bit in enumerate(column_bits))

           
            if 11 <= col_num <= 14:
                # Columns 14 to 11: Printer Serial Number in BCD
                sn = f"{value:02}" + sn
            elif col_num == 8:
                years += f"{value:02}"
            elif col_num == 7:
                month += f"{value:02}"
            elif col_num == 6:
                day += f"{value:02}"
            elif col_num == 5:
                hours = f"{value:02}"
            elif col_num == 2:
                minutes = f"{value:02}"

        decoded_info = f"{hours}:{minutes} {day}/{month}/{years} {sn}"

        # Show decoded information
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "HH:MM DD/MM/YY SN\n")
        self.result_text.insert(tk.END, decoded_info)

if __name__ == "__main__":
    root = tk.Tk()
    app = YellowDotDecoderApp(root)
    root.mainloop()