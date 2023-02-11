import tkinter as tk

import fill_formulare_medicale

#1234567891234

def on_submit():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    personal_id_no = personal_id_no_entry.get()
    result_label.config(text=f"Solicitarea a fost trimisa")

    fill_formulare_medicale.fill_document(first_name, last_name, personal_id_no)

root = tk.Tk()
root.title("Simple GUI")

first_name_label = tk.Label(root, text="Prenume:")
first_name_label.grid(row=0, column=0)

first_name_entry = tk.Entry(root)
first_name_entry.grid(row=0, column=1)

last_name_label = tk.Label(root, text="Nume:")
last_name_label.grid(row=1, column=0)

last_name_entry = tk.Entry(root)
last_name_entry.grid(row=1, column=1)

another_input_label = tk.Label(root, text="CNP:")
another_input_label.grid(row=2, column=0)

personal_id_no_entry = tk.Entry(root)
personal_id_no_entry.grid(row=2, column=1)

submit_button = tk.Button(root, text="Trimite", command=on_submit)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
