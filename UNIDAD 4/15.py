import tkinter as tk

class TaskManagerApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)
        self.task_entry.bind("<Return>", self.add_task_enter)  # Vinculamos el evento Return (Enter)

        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack()

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack()

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack()

        self.task_list = tk.Listbox(root, width=50)
        self.task_list.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def add_task_enter(self, event):
        self.add_task()

    def complete_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks[index] = f"Hecho: {self.tasks[index]}"
            self.task_list.delete(index)
            self.task_list.insert(index, self.tasks[index])

    def delete_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.task_list.delete(index)

if __name__ == "_main_":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()