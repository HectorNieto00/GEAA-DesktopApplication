from model.geaa_model import *
import tkinter as tk
from tkinter import ttk, filedialog
import itertools
import pandas as pd
from tkcalendar import DateEntry
from datetime import *

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)
    menu_inicio.add_command(label='Nomenclatura de Archivos', command=modificar_nomenclatura_archivos)
    menu_inicio.add_command(label='Insertar Ubicaciones', command=cargar_ubicaciones)
    menu_inicio.add_command(label='Insertar Datos', command=cargar_datos)
    menu_inicio.add_command(label='Listar Datos', command=listar_datos)
    menu_inicio.add_command(label='Crear Base de Datos', command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Base de Datos', command=eliminar_tabla)
    menu_inicio.add_command(label='Salir', command=root.destroy)
class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=800, height=600)
        self.root = root
        self.config(bg='#FFFFFF')
        self.grid(sticky='nsew')
        self.selected_vars = {}
        self.selected_ubi = {}
        self.campos_geaa()
        self.mostrar_datos()

    def campos_geaa(self):

        self.campos_frame = tk.Frame(self, width=1150, height=280)
        self.campos_frame.grid(row=0, column=0, columnspan=3, sticky='nsew', padx=10, pady=10)
        self.campos_frame.config(bg='#FFFFFF')
        self.campos_frame.grid_propagate(False)  # Evita que el frame cambie de tamaño automáticamente

        values = ['Temperatura Ambiental', 'Humedad Relativa', 'Presion del Aire o Atmosferica', 'Radiacion Solar Difusa',
        'Sumatoria de la hora de Radiacion Solar Difusa', 'Radiacion Solar Global',
        'Sumatoria de la hora de Radiacion Solar Global', 'Temperatura de Suelo a nivel 1', 'Temperatura de Suelo a nivel 2',
        'Temperatura de Suelo a nivel 3', 'Temperatura de Suelo a nivel 4', 'Temperatura de Suelo a nivel 5',
        'Temperatura de Suelo a nivel 6', 'Temperatura de Suelo a nivel 7', 'Precipitacion de lluvia',
        'Viento', 'Sensacion Termica', 'Bateria']
        ubicaciones = [
            'ALAO', 'ATILLO', 'CHOCAVI', 'CUMANDA', 'ESPOCH', 'MATUS', 'MULTITUD', 'QUIMIAG', 'SAN JUAN', 'TIXAN', 'TUNSHI', 'URBINA'
        ]
        # Label de cada campo
        self.label_fecha_inicio = tk.Label(self.campos_frame, text='Desde:')
        self.label_fecha_inicio.config(font=('Arial', 12, 'bold'), bg='#FFFFFF')
        self.label_fecha_inicio.grid(row=0, column=0, padx=10, pady=10)
        self.label_fecha_fin = tk.Label(self.campos_frame, text='Hasta:')
        self.label_fecha_fin.config(font=('Arial', 12, 'bold'), bg='#FFFFFF')
        self.label_fecha_fin.grid(row=0, column=2, padx=10, pady=10)
        self.label_variables = tk.Label(self.campos_frame, text='Variables:')
        self.label_variables.config(font=('Arial', 12, 'bold'), bg='#FFFFFF')
        self.label_variables.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        # Entry de cada campo
        self.date_entry = DateEntry(self.campos_frame, width=12, date_pattern='dd/mm/yyyy', background='darkblue',
                                    foreground='white', borderwidth=2)
        self.date_entry.grid(row=0, column=1, padx=10, pady=10)
        self.date_end = DateEntry(self.campos_frame, width=12, date_pattern='dd/mm/yyyy', background='darkblue',
                                    foreground='white', borderwidth=2)
        self.date_end.grid(row=0, column=3, padx=10, pady=10)
        self.variables_frame = tk.Frame(self.campos_frame, width=940, height=170)
        self.variables_frame.config(bg='#FFFFFF')
        self.variables_frame.grid(row=1, column=1, columnspan=3, sticky='nsew', padx=10, pady=10)
        self.variables_frame.grid_propagate(False)  # Evita que el frame cambie de tamaño automáticamente

        # Frame para variables con scrollbar
        self.scrollable_frame = tk.Frame(self.campos_frame, width=90, height=200, bg='#FFFFFF')
        self.scrollable_frame.grid(row=1, column=1, sticky='nsew', padx=10, pady=10)
        # Canvas Variables
        self.canvas = tk.Canvas(self.scrollable_frame, width=200, height=100, bg='#FFFFFF')
        self.canvas.config(bg="#FFFFFF")
        self.scrollbar_vertical = tk.Scrollbar(self.scrollable_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar_vertical.pack(side="right", fill="y")
        self.scrollable_canvas_frame = tk.Frame(self.canvas, bg='#FFFFFF')
        self.scrollable_canvas_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.canvas.create_window((0, 0), window=self.scrollable_canvas_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar_vertical.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        # Añadiendo Checkbuttons al scrollable_canvas_frame
        for idx, var in enumerate(values):
            self.selected_vars[var] = tk.IntVar()
            varible = tk.Checkbutton(self.scrollable_canvas_frame, text=var, variable=self.selected_vars[var])
            varible.config(font=('Arial', 10), bg='#FFFFFF')
            varible.grid(row=idx, column=0, padx=5, pady=5, sticky='w')

        # Frame para ubicaciones con scrollbar
        self.ubi_frame = tk.Frame(self.campos_frame, width=90, height=200, bg='#FFFFFF')
        self.ubi_frame.grid(row=1, column=2, sticky='nsew', padx=10, pady=10)
        # Canvas Ubicaciones
        self.canvas_ubi = tk.Canvas(self.ubi_frame, width=200, height=100, bg='#FFFFFF')
        self.canvas_ubi.config(bg="#FFFFFF")
        self.scrollbar_vertical_ubi = tk.Scrollbar(self.ubi_frame, orient="vertical", command=self.canvas_ubi.yview)
        self.scrollbar_vertical_ubi.pack(side="right", fill="y")
        self.ubi_canvas_frame = tk.Frame(self.canvas_ubi, bg='#FFFFFF')
        self.ubi_canvas_frame.bind(
            "<Configure>",
            lambda e: self.canvas_ubi.configure(
                scrollregion=self.canvas_ubi.bbox("all")
            )
        )
        self.canvas_ubi.create_window((0, 0), window=self.ubi_canvas_frame, anchor="nw")
        self.canvas_ubi.configure(yscrollcommand=self.scrollbar_vertical_ubi.set)
        self.canvas_ubi.pack(side="left", fill="both", expand=True)
        # Añadiendo Checkbuttons al scrollable_canvas_frame
        for idx, var in enumerate(ubicaciones):
            self.selected_ubi[idx] = tk.IntVar()
            varible = tk.Checkbutton(self.ubi_canvas_frame, text=var, variable=self.selected_ubi[idx])
            varible.config(font=('Arial', 10), bg='#FFFFFF')
            varible.grid(row=idx, column=0, padx=5, pady=5, sticky='w')

        # Buttons
        self.button_consultar = tk.Button(self.campos_frame, text='Consultar', command=self.mostrar_datos)
        self.button_consultar.config(width=20, font=('Arial',12,'bold'), fg='#FFFFFF', bg='#3333ff', cursor='hand2', activebackground='#6666ff', activeforeground='#FFFFFF', highlightthickness=3, bd=3)
        self.button_consultar.grid(row=2, column=0, padx=5, pady=5)
        self.button_cancelar = tk.Button(self.campos_frame, text='Cancelar', command=self.cancelar)
        self.button_cancelar.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#C84153', cursor='hand2', activebackground='#d36775', activeforeground='#FFFFFF', highlightthickness=3, bd=3)
        self.button_cancelar.grid(row=2, column=1, padx=5, pady=5)
        self.button_descargar = tk.Button(self.campos_frame, text='Descargar', command=self.descargar)
        self.button_descargar.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#359441', cursor='hand2', activebackground='#5da967', activeforeground='#FFFFFF', highlightthickness=3, bd=3)
        self.button_descargar.grid(row=2, column=2, padx=5, pady=5)

        # Configuración de grid
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

    def cancelar(self):
        for var in self.selected_vars.values():
            var.set(0)
        now = datetime.now()
        format = now.strftime('%d/%m/%Y')
        self.date_entry.set_date(format)

    def convert_date_format(self, date_str):
        try:
            # Si la fecha ya está en formato YYYY-MM-DD, solo devuélvela
            if len(date_str) == 10 and date_str[4] == '-' and date_str[7] == '-':
                return date_str
            # De lo contrario, convierte del formato DD/MM/YYYY a YYYY-MM-DD
            date_obj = datetime.strptime(date_str, '%d/%m/%Y')
            return date_obj.strftime('%Y-%m-%d')
        except ValueError as e:
            print(f"Error al convertir la fecha: {e}")
            return None
    def mostrar_datos(self):
        self.date = self.convert_date_format(self.date_entry.get())
        self.date1 = self.convert_date_format(self.date_end.get())
        print(self.date + 'aaaaaaaaaaaa')
        self.selected = [var for var, val in self.selected_vars.items() if val.get() == 1]
        self.selected_ubicaciones = [idx + 1 for idx, val in self.selected_ubi.items() if val.get() == 1]
        print(self.date)
        print(self.selected_ubicaciones)
        self.datos = listar_datos(self.date, self.date1, self.selected, self.selected_ubicaciones)
        if not self.datos:
            print("No se recuperaron datos.")
            # Configurar la tabla para que esté vacía
            self.num_columns = 3  # Número mínimo de columnas para mantener la estructura de la tabla
            self.columns = [f"Columna{i}" for i in range(self.num_columns)]

            # Crear un Frame contenedor para la tabla con barras de desplazamiento
            self.table_frame = tk.Frame(self, width=200, height=300)
            self.table_frame.grid(row=4, column=0, columnspan=3, sticky='nsew', padx=10, pady=10)
            self.table_frame.grid_propagate(False)  # Evita que el frame cambie de tamaño automáticamente

            # Crear la tabla Treeview
            self.tabla = ttk.Treeview(self.table_frame, columns=self.columns, show='headings')
            self.tabla.grid(row=0, column=0, sticky='nsew')

            # Crear barras de desplazamiento
            self.scrollbar_vertical = tk.Scrollbar(self.table_frame, orient=tk.VERTICAL, command=self.tabla.yview)
            self.scrollbar_vertical.grid(row=0, column=1, sticky='ns')
            self.scrollbar_horizontal = tk.Scrollbar(self.table_frame, orient=tk.HORIZONTAL, command=self.tabla.xview)
            self.scrollbar_horizontal.grid(row=1, column=0, sticky='ew')

            self.tabla.configure(yscrollcommand=self.scrollbar_vertical.set,
                                 xscrollcommand=self.scrollbar_horizontal.set)

            # Configurar encabezados de columnas
            for idx, col in enumerate(self.columns):
                self.tabla.heading(col, text=f"Columna {idx + 1}")
                self.tabla.column(col, width=100)

            # Configurar grid para el Frame contenedor
            self.table_frame.grid_rowconfigure(0, weight=1)
            self.table_frame.grid_columnconfigure(0, weight=1)

            self.grid_rowconfigure(4, weight=1)
            self.grid_columnconfigure(0, weight=1)
            self.grid_columnconfigure(1, weight=1)
            self.grid_columnconfigure(2, weight=1)

            return  # Salir de la función si no hay datos
        # Obtener el número de columnas y crear encabezados de columnas dinámicamente
        self.num_columns = len(self.datos[0])
        self.columns = [f"Columna{i}" for i in range(self.num_columns)]

        # Crear un Frame contenedor para la tabla con barras de desplazamiento
        self.table_frame = tk.Frame(self, width=200, height=300)
        self.table_frame.grid(row=4, column=0, columnspan=3, sticky='nsew', padx=10, pady=10)
        self.table_frame.grid_propagate(False)  # Evita que el frame cambie de tamaño automáticamente

        # Crear la tabla Treeview
        self.tabla = ttk.Treeview(self.table_frame, columns=self.columns, show='headings')
        self.tabla.grid(row=0, column=0, sticky='nsew')

        # Crear barras de desplazamiento
        self.scrollbar_vertical = tk.Scrollbar(self.table_frame, orient=tk.VERTICAL, command=self.tabla.yview)
        self.scrollbar_vertical.grid(row=0, column=1, sticky='ns')
        self.scrollbar_horizontal = tk.Scrollbar(self.table_frame, orient=tk.HORIZONTAL, command=self.tabla.xview)
        self.scrollbar_horizontal.grid(row=1, column=0, sticky='ew')

        self.tabla.configure(yscrollcommand=self.scrollbar_vertical.set, xscrollcommand=self.scrollbar_horizontal.set)

        self.colores_filas = ("gray", "white")
        for color in self.colores_filas:
            self.tabla.tag_configure(color, background=color)
        self.style_tabla = ttk.Style()
        self.style_tabla.configure("Treeview.Heading", font=("Arial", 10))
        self.tabla.tag_configure('fuente', font=("Arial", 10))

        # Configurar encabezados de columnas dinámicamente
        for idx, col in enumerate(self.columns):
            self.tabla.heading(col, text=f"Columna {idx + 1}")
            self.tabla.column(col, width=100)

        # Insertar los datos en la tabla
        self.colores = itertools.cycle(self.colores_filas)
        for row in self.datos:
            color = next(self.colores)
            self.tabla.insert("", tk.END, values=row, tags=('fuente', color))

        # Configurar grid para el Frame contenedor
        self.table_frame.grid_rowconfigure(0, weight=1)
        self.table_frame.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

    def descargar(self):
        # Extraer datos de la tabla
        rows = [self.tabla.item(item)['values'] for item in self.tabla.get_children()]
        columns = [self.tabla.heading(col, 'text') for col in self.tabla['columns']]

        # Crear DataFrame
        df = pd.DataFrame(rows, columns=columns)

        # Guardar en un archivo Excel
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                 filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
        if file_path:
            df.to_excel(file_path, index=False)
            tk.messagebox.showinfo("Información", "Datos exportados exitosamente a Excel")