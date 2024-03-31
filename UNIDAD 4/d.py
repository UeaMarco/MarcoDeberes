

    self.delete_button = ttk.Button(self.entry_frame, text="Eliminar")
    self.delete_button.grid(row=2, column=2, padx=5, pady=5)



    self.tree = ttk.Treeview(self.root, columns=("Fecha", "Hora", "Descripción" ))
    self.tree.pack(pady=20)

    self.tree.heading("Fecha", text="Fecha")
    self.tree.heading("Hora", text="Hora")
    self.tree.heading("Descripción", text="Descripción")


    self.time_entry.delete(0, tk.END)
    self.desc_entry.delete(0, tk.END)

    def delete_event(self):

        selected_item = self.tree.selection()[0]
        self.tree.delete(selected_item)
if __name__ == "__main__":

         self.time_label.grid(row=0, column=2, padx=5, )

















    root = tk.Tk()
    app = Agenda(root)
    root.mainloop()