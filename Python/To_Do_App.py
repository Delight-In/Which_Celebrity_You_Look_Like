import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x400")
        
        self.tasks = []  # List to hold tasks

        # GUI Elements
        self.task_input = tk.Entry(self.root, width=35)
        self.task_input.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", width=20, command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Task", width=20, command=self.delete_task)
        self.delete_button.grid(row=1, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(self.root, width=40, height=10)
        self.task_listbox.grid(row=1, column=0, padx=10, pady=10)

        self.update_task_listbox()

    def add_task(self):
        task = self.task_input.get().strip()
        if task:  # Only add if there's some input
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_input.delete(0, tk.END)  # Clear input field
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]  # Get selected task index
            task_to_delete = self.tasks[task_index]
            del self.tasks[task_index]
            self.update_task_listbox()
            messagebox.showinfo("Deleted", f"Task '{task_to_delete}' has been deleted.")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def update_task_listbox(self):
        """Updates the listbox with current tasks."""
        self.task_listbox.delete(0, tk.END)  # Clear current items in the listbox
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)  # Insert updated task list

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
