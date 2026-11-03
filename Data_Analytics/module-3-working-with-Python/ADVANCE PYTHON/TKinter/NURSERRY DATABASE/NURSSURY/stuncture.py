"""Nursery inventory manager using Tkinter and MySQL.

Install the dependency first with: pip install -r requirements.txt
"""

from __future__ import annotations

import os
import tkinter as tk
from datetime import date
from tkinter import messagebox, ttk

try:
    import mysql.connector
    from mysql.connector import Error
except ImportError:
    mysql = None
    Error = Exception
else:
    mysql = mysql.connector


class NurseryApp(tk.Tk):
    FIELDS = (("Plant name", "plant_name"), ("Category", "category"),
              ("Quantity", "quantity"), ("Unit price", "unit_price"),
              ("Supplier", "supplier"), ("Received (YYYY-MM-DD)", "received_date"))
    COLUMNS = ("id", "plant_name", "category", "quantity", "unit_price", "supplier", "received_date", "notes")

    def __init__(self):
        super().__init__()
        self.title("Greenhouse | Nursery Inventory")
        self.geometry("1120x700")
        self.minsize(940, 580)
        self.configure(bg="#eef5ef")
        self.connection, self.selected_id = None, None
        self.vars = {key: tk.StringVar() for _, key in self.FIELDS}
        self.search_var, self.status_var = tk.StringVar(), tk.StringVar(value="Connect to MySQL to begin.")
        self._build_style()
        self._build_ui()
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.after(200, self.open_connection_dialog)

    def _build_style(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Title.TLabel", background="#eef5f3", foreground="#194d33", font=("Segoe UI", 24, "bold"))
        style.configure("Sub.TLabel", background="#eef5ef", foreground="#5f7165", font=("Segoe UI", 10))
        style.configure("Card.TFrame", background="white")
        style.configure("Card.TLabel", background="white", foreground="#294536", font=("Segoe UI", 10))
        style.configure("Primary.TButton", background="#287a4b", foreground="white", font=("Segoe UI", 10, "bold"), padding=(14, 8))
        style.map("Primary.TButton", background=[("active", "#1d6039")])
        style.configure("Secondary.TButton", background="#e4efe6", foreground="#24533a", font=("Segoe UI", 10), padding=(12, 8))
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=30, background="white", fieldbackground="white")
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"), background="#dcebe0", foreground="#214b32", padding=8)
        style.map("Treeview", background=[("selected", "#b9ddc4")], foreground=[("selected", "#173f29")])

    def _build_ui(self):
        header = ttk.Frame(self, padding=(28, 22, 28, 10)); header.pack(fill="x")
        ttk.Label(header, text="Greenhouse", style="Title.TLabel").pack(anchor="w")
        ttk.Label(header, text="A simple place to keep your nursery stock organised.", style="Sub.TLabel").pack(anchor="w", pady=(2, 0))
        body = ttk.Frame(self, padding=(28, 8, 28, 20)); body.pack(fill="both", expand=True)
        body.columnconfigure(1, weight=1); body.rowconfigure(0, weight=1)
        form = ttk.Frame(body, style="Card.TFrame", padding=20); form.grid(row=0, column=0, sticky="nsw", padx=(0, 18))
        ttk.Label(form, text="Plant details", style="Card.TLabel", font=("Segoe UI", 14, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 14))
        for row, (label, key) in enumerate(self.FIELDS, 1):
            ttk.Label(form, text=label, style="Card.TLabel").grid(row=row * 2 - 1, column=0, sticky="w", pady=(4, 2))
            ttk.Entry(form, textvariable=self.vars[key], width=29, font=("Segoe UI", 10)).grid(row=row * 2, column=0, sticky="ew", pady=(0, 5))
        ttk.Label(form, text="Notes", style="Card.TLabel").grid(row=13, column=0, sticky="w", pady=(4, 2))
        self.notes = tk.Text(form, width=29, height=4, font=("Segoe UI", 10), relief="solid", borderwidth=1, highlightthickness=0)
        self.notes.grid(row=14, column=0, sticky="ew", pady=(0, 12))
        buttons = ttk.Frame(form, style="Card.TFrame"); buttons.grid(row=15, column=0, sticky="ew")
        ttk.Button(buttons, text="Save plant", style="Primary.TButton", command=self.save).pack(side="left")
        ttk.Button(buttons, text="Clear", style="Secondary.TButton", command=self.clear_form).pack(side="right")
        right = ttk.Frame(body); right.grid(row=0, column=1, sticky="nsew"); right.rowconfigure(1, weight=1)
        tools = ttk.Frame(right); tools.grid(row=0, column=0, sticky="ew", pady=(0, 10)); tools.columnconfigure(1, weight=1)
        ttk.Label(tools, text="Inventory", font=("Segoe UI", 14, "bold"), foreground="#294536", background="#eef5ef").grid(row=0, column=0, sticky="w", padx=(0, 15))
        ttk.Entry(tools, textvariable=self.search_var, font=("Segoe UI", 10)).grid(row=0, column=1, sticky="ew")
        ttk.Button(tools, text="Search", style="Secondary.TButton", command=self.load_records).grid(row=0, column=2, padx=(8, 0))
        ttk.Button(tools, text="Refresh", style="Secondary.TButton", command=self._reset_search).grid(row=0, column=3, padx=(8, 0))
        table_frame = ttk.Frame(right, style="Card.TFrame", padding=10); table_frame.grid(row=1, column=0, sticky="nsew"); table_frame.columnconfigure(0, weight=1); table_frame.rowconfigure(0, weight=1)
        self.tree = ttk.Treeview(table_frame, columns=self.COLUMNS, show="headings", selectmode="browse")
        headings = ("ID", "Plant", "Category", "Qty", "Price", "Supplier", "Received", "Notes")
        widths = (50, 145, 100, 60, 75, 115, 100, 180)
        for col, heading, width in zip(self.COLUMNS, headings, widths):
            self.tree.heading(col, text=heading); self.tree.column(col, width=width, anchor="center" if col in {"id", "quantity", "unit_price", "received_date"} else "w")
        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview); scrollbar.grid(row=0, column=1, sticky="ns"); self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.bind("<<TreeviewSelect>>", self.select_record)
        actions = ttk.Frame(right); actions.grid(row=2, column=0, sticky="e", pady=(10, 0))
        ttk.Button(actions, text="Delete selected", style="Secondary.TButton", command=self.delete).pack(side="right")
        ttk.Label(actions, text="Select a row to edit it.", foreground="#5f7165", background="#eef5ef", font=("Segoe UI", 9)).pack(side="right", padx=14)
        ttk.Label(self, textvariable=self.status_var, anchor="w", background="#194d33", foreground="white", font=("Segoe UI", 9), padding=(28, 7)).pack(fill="x", side="bottom")

    def open_connection_dialog(self):
        if mysql is None:
            messagebox.showerror("MySQL connector missing", "Install it with:\n\npip install -r requirements.txt")
            return
        dialog = tk.Toplevel(self); dialog.title("Connect to MySQL"); dialog.transient(self); dialog.grab_set(); dialog.resizable(False, False); dialog.configure(bg="white")
        frame = ttk.Frame(dialog, style="Card.TFrame", padding=22); frame.pack(fill="both", expand=True)
        ttk.Label(frame, text="MySQL connection", style="Card.TLabel", font=("Segoe UI", 15, "bold")).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 4))
        ttk.Label(frame, text="The database and inventory table will be created automatically.", style="Card.TLabel").grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 14))
        defaults = {"Host": os.getenv("NURSERY_DB_HOST", "localhost"), "Port": os.getenv("NURSERY_DB_PORT", "3306"), "User": os.getenv("NURSERY_DB_USER", "root"), "Password": os.getenv("NURSERY_DB_PASSWORD", ""), "Database": os.getenv("NURSERY_DB_NAME", "nursery_db")}
        entries = {}
        for row, (label, value) in enumerate(defaults.items(), 2):
            ttk.Label(frame, text=label, style="Card.TLabel").grid(row=row, column=0, sticky="w", pady=4, padx=(0, 12))
            entry = ttk.Entry(frame, width=30, show="*" if label == "Password" else ""); entry.insert(0, value); entry.grid(row=row, column=1, pady=4); entries[label] = entry
        def connect():
            try:
                db_name = entries["Database"].get().strip()
                if not db_name.replace("_", "").isalnum(): raise ValueError("Database name may contain only letters, numbers, and underscores.")
                self.connection = mysql.connect(host=entries["Host"].get(), port=int(entries["Port"].get()), user=entries["User"].get(), password=entries["Password"].get())
                cursor = self.connection.cursor(); cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`"); cursor.execute(f"USE `{db_name}`")
                cursor.execute("""CREATE TABLE IF NOT EXISTS plants (id INT AUTO_INCREMENT PRIMARY KEY, plant_name VARCHAR(100) NOT NULL, category VARCHAR(80), quantity INT NOT NULL DEFAULT 0, unit_price DECIMAL(10,2) NOT NULL DEFAULT 0, supplier VARCHAR(100), received_date DATE, notes TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
                self.connection.commit(); cursor.close(); dialog.destroy(); self.status_var.set(f"Connected to MySQL • database: {db_name}"); self.load_records()
            except (Error, ValueError) as exc: messagebox.showerror("Connection failed", str(exc), parent=dialog)
        ttk.Button(frame, text="Connect", style="Primary.TButton", command=connect).grid(row=7, column=1, sticky="e", pady=(16, 0)); dialog.bind("<Return>", lambda _event: connect()); entries["Host"].focus_set()

    def _cursor(self):
        if not self.connection or not self.connection.is_connected(): messagebox.showwarning("Not connected", "Connect to MySQL first."); return None
        return self.connection.cursor()

    def _record_values(self):
        name = self.vars["plant_name"].get().strip()
        if not name: raise ValueError("Plant name is required.")
        try: quantity, price = int(self.vars["quantity"].get() or 0), float(self.vars["unit_price"].get() or 0)
        except ValueError as exc: raise ValueError("Quantity must be a whole number and price must be a number.") from exc
        if quantity < 0 or price < 0: raise ValueError("Quantity and price cannot be negative.")
        received = self.vars["received_date"].get().strip() or None
        if received:
            try: date.fromisoformat(received)
            except ValueError as exc: raise ValueError("Use YYYY-MM-DD for the received date.") from exc
        return (name, self.vars["category"].get().strip(), quantity, price, self.vars["supplier"].get().strip(), received, self.notes.get("1.0", "end-1c").strip())

    def save(self):
        cursor = self._cursor()
        if not cursor: return
        try:
            values = self._record_values()
            if self.selected_id is None:
                cursor.execute("INSERT INTO plants (plant_name, category, quantity, unit_price, supplier, received_date, notes) VALUES (%s, %s, %s, %s, %s, %s, %s)", values); message = "Plant added to inventory."
            else:
                cursor.execute("UPDATE plants SET plant_name=%s, category=%s, quantity=%s, unit_price=%s, supplier=%s, received_date=%s, notes=%s WHERE id=%s", values + (self.selected_id,)); message = "Plant record updated."
            self.connection.commit(); self.status_var.set(message); self.clear_form(); self.load_records()
        except (Error, ValueError) as exc: messagebox.showerror("Could not save", str(exc))
        finally: cursor.close()

    def load_records(self):
        cursor = self._cursor()
        if not cursor: return
        try:
            term = self.search_var.get().strip(); query, params = "SELECT id, plant_name, category, quantity, unit_price, supplier, received_date, notes FROM plants", ()
            if term: query += " WHERE plant_name LIKE %s OR category LIKE %s OR supplier LIKE %s"; params = (f"%{term}%",) * 3
            cursor.execute(query + " ORDER BY id DESC", params); self.tree.delete(*self.tree.get_children())
            for record in cursor.fetchall():
                values = list(record); values[4] = f"{float(values[4]):.2f}"; values[6] = values[6].isoformat() if values[6] else ""; self.tree.insert("", "end", values=values)
            self.status_var.set(f"{len(self.tree.get_children())} record(s) shown.")
        except Error as exc: messagebox.showerror("Could not load records", str(exc))
        finally: cursor.close()

    def select_record(self, _event=None):
        selected = self.tree.selection()
        if not selected: return
        values = self.tree.item(selected[0], "values"); self.selected_id = int(values[0])
        for index, (_, key) in enumerate(self.FIELDS, 1): self.vars[key].set(values[index])
        self.notes.delete("1.0", "end"); self.notes.insert("1.0", values[7]); self.status_var.set(f"Editing plant record #{self.selected_id}.")

    def delete(self):
        if self.selected_id is None: messagebox.showinfo("Choose a record", "Select a plant record to delete."); return
        if not messagebox.askyesno("Delete plant", "Delete the selected plant record?"): return
        cursor = self._cursor()
        if not cursor: return
        try: cursor.execute("DELETE FROM plants WHERE id=%s", (self.selected_id,)); self.connection.commit(); self.status_var.set("Plant record deleted."); self.clear_form(); self.load_records()
        except Error as exc: messagebox.showerror("Could not delete", str(exc))
        finally: cursor.close()

    def clear_form(self):
        for var in self.vars.values(): var.set("")
        self.notes.delete("1.0", "end"); self.selected_id = None; self.tree.selection_remove(self.tree.selection())

    def _reset_search(self): self.search_var.set(""); self.load_records()

    def close(self):
        if self.connection and self.connection.is_connected(): self.connection.close()
        self.destroy()


if __name__ == "__main__": NurseryApp().mainloop()
