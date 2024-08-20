from .conexion_db import ConexionDB
from tkinter import messagebox
import pandas as pd
from pathlib import Path
import os

def crear_tabla():
    conexion = ConexionDB()

    tablas = [
        '''
            CREATE TABLE ubicacion (
                ubicacion_id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_ubicacion TEXT,
                longitud TEXT,
                latitud TEXT,
                altura TEXT
            );
        ''',
        '''
        CREATE TABLE datos_variables (
            dato_id INTEGER PRIMARY KEY AUTOINCREMENT,
            Date TEXT,
            Time TEXT,
            DimStat_TA_1h TEXT,
            status_Avg_Stat_TA_1h TEXT,
            Avg_Stat_TA_1h REAL,
            status_Max_Stat_TA_1h TEXT,
            Max_Stat_TA_1h REAL,
            status_Min_Stat_TA_1h TEXT,
            Min_Stat_TA_1h REAL,
            DimStat_RH_1h TEXT,
            status_Avg_Stat_RH_1h TEXT,
            Avg_Stat_RH_1h REAL,
            status_Max_Stat_RH_1h TEXT,
            Max_Stat_RH_1h REAL,
            status_Min_Stat_RH_1h TEXT,
            Min_Stat_RH_1h REAL,
            DimStat_PA_1h TEXT,
            status_Avg_Stat_PA_1h TEXT,
            Avg_Stat_PA_1h REAL,
            status_Max_Stat_PA_1h TEXT,
            Max_Stat_PA_1h REAL,
            status_Min_Stat_PA_1h TEXT,
            Min_Stat_PA_1h REAL,
            DimStat_SR_Dif_1h TEXT,
            status_Avg_Stat_SR_Dif_1h TEXT,
            Avg_Stat_SR_Dif_1h REAL,
            status_Max_Stat_SR_Dif_1h TEXT,
            Max_Stat_SR_Dif_1h REAL,
            status_Min_Stat_SR_Dif_1h TEXT,
            Min_Stat_SR_Dif_1h REAL,
            DimSum_SR_Dif_1h TEXT,
            status_Sum_Sum_SR_Dif_1h TEXT,
            Sum_Sum_SR_Dif_1h REAL,
            DimStat_SR_Glob_1h TEXT,
            status_Avg_Stat_SR_Glob_1h TEXT,
            Avg_Stat_SR_Glob_1h REAL,
            status_Max_Stat_SR_Glob_1h TEXT,
            Max_Stat_SR_Glob_1h REAL,
            status_Min_Stat_SR_Glob_1h TEXT,
            Min_Stat_SR_Glob_1h REAL,
            DimSum_SR_Glob_1h TEXT,
            status_Sum_Sum_SR_Glob_1h TEXT,
            Sum_Sum_SR_Glob_1h REAL,
            DimStat_TS_1h_TG1 TEXT,
            status_Avg_Stat_TS_1h_TG1 TEXT,
            Avg_Stat_TS_1h_TG1 REAL,
            status_Max_Stat_TS_1h_TG1 TEXT,
            Max_Stat_TS_1h_TG1 REAL,
            status_Min_Stat_TS_1h_TG1 TEXT,
            Min_Stat_TS_1h_TG1 REAL,
            DimStat_TS_1h_TG2 TEXT,
            status_Avg_Stat_TS_1h_TG2 TEXT,
            Avg_Stat_TS_1h_TG2 REAL,
            status_Max_Stat_TS_1h_TG2 TEXT,
            Max_Stat_TS_1h_TG2 REAL,
            status_Min_Stat_TS_1h_TG2 TEXT,
            Min_Stat_TS_1h_TG2 REAL,
            DimStat_TS_1h_TG3 TEXT,
            status_Avg_Stat_TS_1h_TG3 TEXT,
            Avg_Stat_TS_1h_TG3 REAL,
            status_Max_Stat_TS_1h_TG3 TEXT,
            Max_Stat_TS_1h_TG3 REAL,
            status_Min_Stat_TS_1h_TG3 TEXT,
            Min_Stat_TS_1h_TG3 REAL,
            DimStat_TS_1h_TG4 TEXT,
            status_Avg_Stat_TS_1h_TG4 TEXT,
            Avg_Stat_TS_1h_TG4 REAL,
            status_Max_Stat_TS_1h_TG4 TEXT,
            Max_Stat_TS_1h_TG4 REAL,
            status_Min_Stat_TS_1h_TG4 TEXT,
            Min_Stat_TS_1h_TG4 REAL,
            DimStat_TS_1h_TG5 TEXT,
            status_Avg_Stat_TS_1h_TG5 TEXT,
            Avg_Stat_TS_1h_TG5 REAL,
            status_Max_Stat_TS_1h_TG5 TEXT,
            Max_Stat_TS_1h_TG5 REAL,
            status_Min_Stat_TS_1h_TG5 TEXT,
            Min_Stat_TS_1h_TG5 REAL,
            DimStat_TS_1h_TG6 TEXT,
            status_Avg_Stat_TS_1h_TG6 TEXT,
            Avg_Stat_TS_1h_TG6 REAL,
            status_Max_Stat_TS_1h_TG6 TEXT,
            Max_Stat_TS_1h_TG6 REAL,
            status_Min_Stat_TS_1h_TG6 TEXT,
            Min_Stat_TS_1h_TG6 REAL,
            DimStat_TS_1h_TG7 TEXT,
            status_Avg_Stat_TS_1h_TG7 TEXT,
            Avg_Stat_TS_1h_TG7 REAL,
            status_Max_Stat_TS_1h_TG7 TEXT,
            Max_Stat_TS_1h_TG7 REAL,
            status_Min_Stat_TS_1h_TG7 TEXT,
            Min_Stat_TS_1h_TG7 REAL,
            Dim_Sum_PR_1h TEXT,
            status_Sum_Sum_PR_1h TEXT,
            Sum_Sum_PR_1h REAL,
            DimGenWind_1h_SDI12 TEXT,
            status_SpdMin_GenWind_1h TEXT,
            SpdMin_GenWind_1h REAL,
            status_WRun_GenWind_1h TEXT,
            WRun_GenWind_1h REAL,
            status_DirAvg_GenWind_1h TEXT,
            DirAvg_GenWind_1h REAL,
            status_DirMax_GenWind_1h TEXT,
            DirMax_GenWind_1h REAL,
            status_GustDir_GenWind_1h TEXT,
            GustDir_GenWind_1h REAL,
            status_GustH_GenWind_1h TEXT,
            GustH_GenWind_1h REAL,
            status_GustM_GenWind_1h TEXT,
            GustM_GenWind_1h REAL,
            status_SpdAvg_GenWind_1h TEXT,
            SpdAvg_GenWind_1h REAL,
            status_SpdMax_GenWind_1h TEXT,
            SpdMax_GenWind_1h REAL,
            DimStat_WindChill_1h TEXT,
            status_Avg_Stat_WindChill_1h TEXT,
            Avg_Stat_WindChill_1h REAL,
            status_Max_Stat_WindChill_1h TEXT,
            Max_Stat_WindChill_1h REAL,
            status_Min_Stat_WindChill_1h TEXT,
            Min_Stat_WindChill_1h REAL,
            DimQMBATT_Meas TEXT,
            status_meas_QMBATT_Meas TEXT,
            meas_QMBATT_Meas REAL,
            ubicacion_id INTEGER,
            FOREIGN KEY(ubicacion_id) REFERENCES Ubicacion(ubicacion_id)
        );
        '''
    ]

    try:
        for tabla in tablas:
            conexion.cursor.execute(tabla)
        conexion.cerrar_conexion()
    except Exception as e:
        messagebox.showwarning("Error", f"Ocurrió un error al crear las tablas: {str(e)}")
        conexion.cerrar_conexion()

def eliminar_tabla():
    conexion = ConexionDB()
    sql = 'DROP TABLE IF EXISTS peliculas'
    conexion.cursor.execute(sql)
    conexion.cerrar_conexion()

def cargar_ubicaciones():
    ubicaciones = [
        'ALAO', 'ATILLO', 'CHOCAVI', 'CUMANDA', 'ESPOCH', 'MATUS', 'MULTITUD', 'QUIMIAG', 'SAN JUAN', 'TIXAN', 'TUNSHI', 'URBINA'
    ]
    longitud = ["-78.5415915", "-78.5490996", "-78.6944718", "-79.1453299", "-78.6775198", "-78.5037299", "-78.9970056",
                "-78.5725507", "-78.7835603", "-78.7603694", "-78.6263025", "-78.7124203"]

    latitud = ["-1.86948947", "-2.186991", "-1.53265559", "-2.21017735", "-1.65460177", "-1.55575093", "-2.60966782",
               "-1.65965467", "-1.6376917", "-2.15763504", "-1.74752939", "-1.4886592"]

    altura = ["3064", "3467", "3486", "330", "2754", "2704", "1483", "2709", "3232", "3546", "2840", "3642"]

    conexion = ConexionDB()

    try:
        for idx, ubi in enumerate(ubicaciones):
            sql = 'INSERT INTO Ubicacion(nombre_ubicacion, longitud, latitud, altura) values(?,?,?,?)'
            conexion.cursor.execute(sql, (ubi, longitud[idx], latitud[idx], altura[idx]))
        conexion.cerrar_conexion()
    except Exception as e:
        messagebox.showwarning("Error", f"Ocurrió un error al insertar las ubicaciones: {str(e)}")
        conexion.cerrar_conexion()

def modificar_nomenclatura_archivos():
    base_path = Path(Path.home(), 'PycharmProjects', 'GEAA', 'Archivos')
    path_modificados = Path(Path.home(), 'PycharmProjects', 'GEAA', 'Modificados')
    archivos = os.listdir(base_path)
    todas_variables = ['Stat_TA_1h', 'Stat_RH_1h', 'Stat_PA_1h', 'Stat_SR_Dif_1h', 'Sum_SR_Dif_1h', 'Stat_SR_Glob_1h',
                       'Sum_SR_Glob_1h', 'Stat_TS_1h_TG1', 'Stat_TS_1h_TG2', 'Stat_TS_1h_TG3', 'Stat_TS_1h_TG4',
                       'Stat_TS_1h_TG5',
                       'Stat_TS_1h_TG6', 'Stat_TS_1h_TG7', 'Sum_PR_1h', 'QMBATT_Meas', 'GenWind_1h', 'GenWind_1h_SDI12',
                       'Stat_WindChill_1h', 'Stat_WindChill_1h_SDI12']
    for archivo in archivos:
        print(archivo)
        variables_nuevas, variables_no_archivo = [], []
        nombre_sin_extension = Path(archivo).stem
        data = pd.read_excel(base_path / archivo, header=None)
        # Guardar las variables del archivo - Verificar variables nuevas
        variables = []
        for col in data.iloc[0, :]:
            if pd.notna(col) and col not in variables:
                variables.append(col)
        for var in variables:
            if var not in todas_variables:
                variables_nuevas.append(var)
        for var in todas_variables:
            if var not in variables:
                variables_no_archivo.append(var)
        # print(f"Variables: {variables}{len(variables)}")
        print(f"Variables nuevas: {variables_nuevas}")
        print(f"Variables no estan en archivo: {variables_no_archivo}")

        # Eliminar la primera fila
        data = data.drop(data.index[0])

        # Reseteo los indices del DF
        data.reset_index(drop=True, inplace=True)
        # print(data)

        # Diccionario con las variables y posibles indices
        dic_variables = {
            'Stat_TA_1h': 6, 'Stat_RH_1h': 6, 'Stat_PA_1h': 6, 'Stat_SR_Dif_1h': 6, 'Sum_SR_Dif_1h': 2,
            'Stat_SR_Glob_1h': 6, 'Sum_SR_Glob_1h': 2, 'Stat_TS_1h_TG1': 6, 'Stat_TS_1h_TG2': 6, 'Stat_TS_1h_TG3': 6,
            'Stat_TS_1h_TG4': 6, 'Stat_TS_1h_TG5': 6, 'Stat_TS_1h_TG6': 6, 'Stat_TS_1h_TG7': 6, 'Sum_PR_1h': 2,
            'QMBATT_Meas': 2, 'GenWind_1h': 18, 'GenWind_1h_SDI12': 18, 'Stat_WindChill_1h': 6,
            'Stat_WindChill_1h_SDI12': 6
        }
        inicio = 2
        for var in variables:
            if var in dic_variables.keys():
                fin = inicio + dic_variables[var]
                for col in range(inicio, fin):
                    nom_col = data.columns[col]  # Nombre de la columna
                    if col + 1 < len(data.columns):
                        valor_col_derecha = data.iloc[0, col + 1]
                    else:
                        valor_col_derecha = ''
                    if data.at[0, nom_col] == 'status':
                        data.at[0, col] = f'{data.at[0, nom_col]}_{valor_col_derecha}_{var}'
                    else:
                        data.at[0, col] = f'{data.at[0, nom_col]}_{var}'
                inicio = fin
        data.to_excel(path_modificados / f"{nombre_sin_extension}_modificado.xlsx", index=False)
        print('exitoso')
def cargar_datos():
    conexion = ConexionDB()
    ubicaciones = {
        'ALAO': 1, 'ATILLO': 2, 'CHOCAVI': 3, 'CUMANDA': 4, 'ESPOCH': 5, 'MATUS': 6, 'MULTITUD': 7, 'QUIMIAG': 8,
        'SAN JUAN': 9, 'TIXAN': 10, 'TUNSHI': 11, 'URBINA': 12}
    nombres = [
        'Temperatura Ambiental', 'Humedad Relativa', 'Presion del Aire o Atmosferica', 'Radiacion Solar Difusa',
        'Sumatoria de la hora de Radiacion Solar Difusa', 'Radiacion Solar Global',
        'Sumatoria de la hora de Radiacion Solar Global', 'Temperatura de Suelo a nivel 1', 'Temperatura de Suelo a nivel 2',
        'Temperatura de Suelo a nivel 3', 'Temperatura de Suelo a nivel 4', 'Temperatura de Suelo a nivel 5',
        'Temperatura de Suelo a nivel 6', 'Temperatura de Suelo a nivel 7', 'Precipitacion de lluvia',
        'Viento', 'Sensacion Termica', 'Bateria']
    base_path = Path(Path.home(), 'PycharmProjects', 'GEAA', 'Modificados')
    archivos = os.listdir(base_path)
    archivo = archivos[0]
    print(archivo)
    archivo_excel = base_path / archivo
    data = pd.read_excel(archivo_excel, skiprows=[0])
    print(data)
    # Convertir la columna de fechas al formato YYYY-MM-DD
    if 'date' in data.columns:
        data['date'] = pd.to_datetime(data['date'], format='%m/%d/%y').dt.strftime('%Y-%m-%d')
    # Iterar sobre las filas del DataFrame para insertar en la tabla datos_variables
    for index, row in data.iterrows():
        fecha = row.get('date', None)
        hora = row.get('time', None)
        avg_stat_ta_1h = row.get('Avg_Stat_TA_1h', None)
        status_Avg_Stat_TA_1h = row.get('status_Avg_Stat_TA_1h', None)
        max_stat_ta_1h = row.get('Max_Stat_TA_1h', None)
        status_Max_Stat_TA_1h = row.get('status_Max_Stat_TA_1h', None)
        min_stat_ta_1h = row.get('Min_Stat_TA_1h', None)
        status_Min_Stat_TA_1h = row.get('status_Min_Stat_TA_1h', None)
        avg_stat_rh_1h = row.get('Avg_Stat_RH_1h', None)
        status_Avg_Stat_RH_1h = row.get('status_Avg_Stat_RH_1h', None)
        max_stat_rh_1h = row.get('Max_Stat_RH_1h', None)
        status_Max_Stat_RH_1h = row.get('status_Max_Stat_RH_1h', None)
        min_stat_rh_1h = row.get('Min_Stat_RH_1h', None)
        status_Min_Stat_RH_1h = row.get('status_Min_Stat_RH_1h', None)
        avg_stat_pa_1h = row.get('Avg_Stat_PA_1h', None)
        status_Avg_Stat_PA_1h = row.get('status_Avg_Stat_PA_1h', None)
        max_stat_pa_1h = row.get('Max_Stat_PA_1h', None)
        status_Max_Stat_PA_1h = row.get('status_Max_Stat_PA_1h', None)
        min_stat_pa_1h = row.get('Min_Stat_PA_1h', None)
        status_Min_Stat_PA_1h = row.get('status_Min_Stat_PA_1h', None)
        avg_stat_sr_dif_1h = row.get('Avg_Stat_SR_Dif_1h', None)
        status_Avg_Stat_SR_Dif_1h = row.get('status_Avg_Stat_SR_Dif_1h', None)
        max_stat_sr_dif_1h = row.get('Max_Stat_SR_Dif_1h', None)
        status_Max_Stat_SR_Dif_1h = row.get('status_Max_Stat_SR_Dif_1h', None)
        min_stat_sr_dif_1h = row.get('Min_Stat_SR_Dif_1h', None)
        status_Min_Stat_SR_Dif_1h = row.get('status_Min_Stat_SR_Dif_1h', None)
        sum_sum_sr_dif_1h = row.get('Sum_Sum_SR_Dif_1h', None)
        status_Sum_Sum_SR_Dif_1h = row.get('status_Sum_Sum_SR_Dif_1h', None)
        avg_stat_sr_glob_1h = row.get('Avg_Stat_SR_Glob_1h', None)
        status_Avg_Stat_SR_Glob_1h = row.get('status_Avg_Stat_SR_Glob_1h', None)
        max_stat_sr_glob_1h = row.get('Max_Stat_SR_Glob_1h', None)
        status_Max_Stat_SR_Glob_1h = row.get('status_Max_Stat_SR_Glob_1h', None)
        min_stat_sr_glob_1h = row.get('Min_Stat_SR_Glob_1h', None)
        status_Min_Stat_SR_Glob_1h = row.get('status_Min_Stat_SR_Glob_1h', None)
        sum_sum_sr_glob_1h = row.get('Sum_Sum_SR_Glob_1h', None)
        status_Sum_Sum_SR_Glob_1h = row.get('status_Sum_Sum_SR_Glob_1h', None)
        avg_stat_ts_1h_tg1 = row.get('Avg_Stat_TS_1h_TG1', None)
        status_Avg_Stat_TS_1h_TG1 = row.get('status_Avg_Stat_TS_1h_TG1', None)
        max_stat_ts_1h_tg1 = row.get('Max_Stat_TS_1h_TG1', None)
        status_Max_Stat_TS_1h_TG1 = row.get('status_Max_Stat_TS_1h_TG1', None)
        min_stat_ts_1h_tg1 = row.get('Min_Stat_TS_1h_TG1', None)
        status_Min_Stat_TS_1h_TG1 = row.get('status_Min_Stat_TS_1h_TG1', None)
        avg_stat_ts_1h_tg2 = row.get('Avg_Stat_TS_1h_TG2', None)
        status_Avg_Stat_TS_1h_TG2 = row.get('status_Avg_Stat_TS_1h_TG2', None)
        max_stat_ts_1h_tg2 = row.get('Max_Stat_TS_1h_TG2', None)
        status_Max_Stat_TS_1h_TG2 = row.get('status_Max_Stat_TS_1h_TG2', None)
        min_stat_ts_1h_tg2 = row.get('Min_Stat_TS_1h_TG2', None)
        status_Min_Stat_TS_1h_TG2 = row.get('status_Min_Stat_TS_1h_TG2', None)
        avg_stat_ts_1h_tg3 = row.get('Avg_Stat_TS_1h_TG3', None)
        status_Avg_Stat_TS_1h_TG3 = row.get('status_Avg_Stat_TS_1h_TG3', None)
        max_stat_ts_1h_tg3 = row.get('Max_Stat_TS_1h_TG3', None)
        status_Max_Stat_TS_1h_TG3 = row.get('status_Max_Stat_TS_1h_TG3', None)
        min_stat_ts_1h_tg3 = row.get('Min_Stat_TS_1h_TG3', None)
        status_Min_Stat_TS_1h_TG3 = row.get('status_Min_Stat_TS_1h_TG3', None)
        avg_stat_ts_1h_tg4 = row.get('Avg_Stat_TS_1h_TG4', None)
        status_Avg_Stat_TS_1h_TG4 = row.get('status_Avg_Stat_TS_1h_TG4', None)
        max_stat_ts_1h_tg4 = row.get('Max_Stat_TS_1h_TG4', None)
        status_Max_Stat_TS_1h_TG4 = row.get('status_Max_Stat_TS_1h_TG4', None)
        min_stat_ts_1h_tg4 = row.get('Min_Stat_TS_1h_TG4', None)
        status_Min_Stat_TS_1h_TG4 = row.get('status_Min_Stat_TS_1h_TG4', None)
        avg_stat_ts_1h_tg5 = row.get('Avg_Stat_TS_1h_TG5', None)
        status_Avg_Stat_TS_1h_TG5 = row.get('status_Avg_Stat_TS_1h_TG5', None)
        max_stat_ts_1h_tg5 = row.get('Max_Stat_TS_1h_TG5', None)
        status_Max_Stat_TS_1h_TG5 = row.get('status_Max_Stat_TS_1h_TG5', None)
        min_stat_ts_1h_tg5 = row.get('Min_Stat_TS_1h_TG5', None)
        status_Min_Stat_TS_1h_TG5 = row.get('status_Min_Stat_TS_1h_TG5', None)
        avg_stat_ts_1h_tg6 = row.get('Avg_Stat_TS_1h_TG6', None)
        status_Avg_Stat_TS_1h_TG6 = row.get('status_Avg_Stat_TS_1h_TG6', None)
        max_stat_ts_1h_tg6 = row.get('Max_Stat_TS_1h_TG6', None)
        status_Max_Stat_TS_1h_TG6 = row.get('status_Max_Stat_TS_1h_TG6', None)
        min_stat_ts_1h_tg6 = row.get('Min_Stat_TS_1h_TG6', None)
        status_Min_Stat_TS_1h_TG6 = row.get('status_Min_Stat_TS_1h_TG6', None)
        avg_stat_ts_1h_tg7 = row.get('Avg_Stat_TS_1h_TG7', None)
        status_Avg_Stat_TS_1h_TG7 = row.get('status_Avg_Stat_TS_1h_TG7', None)
        max_stat_ts_1h_tg7 = row.get('Max_Stat_TS_1h_TG7', None)
        status_Max_Stat_TS_1h_TG7 = row.get('status_Max_Stat_TS_1h_TG7', None)
        min_stat_ts_1h_tg7 = row.get('Min_Stat_TS_1h_TG7', None)
        status_Min_Stat_TS_1h_TG7 = row.get('status_Min_Stat_TS_1h_TG7', None)
        sum_sum_pr_1h = row.get('Sum_Sum_PR_1h', None)
        status_Sum_Sum_PR_1h = row.get('status_Sum_Sum_PR_1h', None)
        status_spdmin_genwind_1h = row.get('status_SpdMin_GenWind_1h', None)
        spdmin_genwind_1h = row.get('SpdMin_GenWind_1h', None)
        status_wrun_genwind_1h = row.get('status_WRun_GenWind_1h', None)
        wrun_genwind_1h = row.get('WRun_GenWind_1h', None)
        status_diravg_genwind_1h = row.get('status_DirAvg_GenWind_1h', None)
        diravg_genwind_1h = row.get('DirAvg_GenWind_1h', None)
        status_dirmax_genwind_1h = row.get('status_DirMax_GenWind_1h', None)
        dirmax_genwind_1h = row.get('DirMax_GenWind_1h', None)
        status_gustdir_genwind_1h = row.get('status_GustDir_GenWind_1h', None)
        gustdir_genwind_1h = row.get('GustDir_GenWind_1h', None)
        status_gusth_genwind_1h = row.get('status_GustH_GenWind_1h', None)
        gusth_genwind_1h = row.get('GustH_GenWind_1h', None)
        status_gustm_genwind_1h = row.get('status_GustM_GenWind_1h', None)
        gustm_genwind_1h = row.get('GustM_GenWind_1h', None)
        status_spdavg_genwind_1h = row.get('status_SpdAvg_GenWind_1h', None)
        spdavg_genwind_1h = row.get('SpdAvg_GenWind_1h', None)
        status_spdmax_genwind_1h = row.get('status_SpdMax_GenWind_1h', None)
        spdmax_genwind_1h = row.get('SpdMax_GenWind_1h', None)
        avg_stat_windchill_1h = row.get('Avg_Stat_WindChill_1h', None)
        status_Avg_Stat_WindChill_1h = row.get('status_Avg_Stat_WindChill_1h', None)
        max_stat_windchill_1h = row.get('Max_Stat_WindChill_1h', None)
        status_Max_Stat_WindChill_1h = row.get('status_Max_Stat_WindChill_1h', None)
        min_stat_windchill_1h = row.get('Min_Stat_WindChill_1h', None)
        status_Min_Stat_WindChill_1h = row.get('status_Min_Stat_WindChill_1h', None)
        status_meas_qmbatt_meas = row.get('status_meas_QMBATT_Meas', None)
        meas_qmbatt_meas = row.get('meas_QMBATT_Meas', None)

        sql = '''
        INSERT INTO datos_variables (
            Date, Time, DimStat_TA_1h, status_Avg_Stat_TA_1h, Avg_Stat_TA_1h, status_Max_Stat_TA_1h, Max_Stat_TA_1h, status_Min_Stat_TA_1h, Min_Stat_TA_1h,
            DimStat_RH_1h, status_Avg_Stat_RH_1h, Avg_Stat_RH_1h, status_Max_Stat_RH_1h, Max_Stat_RH_1h, status_Min_Stat_RH_1h, Min_Stat_RH_1h,
            DimStat_PA_1h, status_Avg_Stat_PA_1h, Avg_Stat_PA_1h, status_Max_Stat_PA_1h, Max_Stat_PA_1h, status_Min_Stat_PA_1h, Min_Stat_PA_1h,
            DimStat_SR_Dif_1h, status_Avg_Stat_SR_Dif_1h, Avg_Stat_SR_Dif_1h, status_Max_Stat_SR_Dif_1h, Max_Stat_SR_Dif_1h, status_Min_Stat_SR_Dif_1h, Min_Stat_SR_Dif_1h,
            DimSum_SR_Dif_1h, status_Sum_Sum_SR_Dif_1h, Sum_Sum_SR_Dif_1h,
            DimStat_SR_Glob_1h, status_Avg_Stat_SR_Glob_1h, Avg_Stat_SR_Glob_1h, status_Max_Stat_SR_Glob_1h, Max_Stat_SR_Glob_1h, status_Min_Stat_SR_Glob_1h, Min_Stat_SR_Glob_1h,
            DimSum_SR_Glob_1h, status_Sum_Sum_SR_Glob_1h, Sum_Sum_SR_Glob_1h,
            DimStat_TS_1h_TG1, status_Avg_Stat_TS_1h_TG1, Avg_Stat_TS_1h_TG1, status_Max_Stat_TS_1h_TG1, Max_Stat_TS_1h_TG1, status_Min_Stat_TS_1h_TG1, Min_Stat_TS_1h_TG1,
            DimStat_TS_1h_TG2, status_Avg_Stat_TS_1h_TG2, Avg_Stat_TS_1h_TG2, status_Max_Stat_TS_1h_TG2, Max_Stat_TS_1h_TG2, status_Min_Stat_TS_1h_TG2, Min_Stat_TS_1h_TG2,
            DimStat_TS_1h_TG3, status_Avg_Stat_TS_1h_TG3, Avg_Stat_TS_1h_TG3, status_Max_Stat_TS_1h_TG3, Max_Stat_TS_1h_TG3, status_Min_Stat_TS_1h_TG3, Min_Stat_TS_1h_TG3,
            DimStat_TS_1h_TG4, status_Avg_Stat_TS_1h_TG4, Avg_Stat_TS_1h_TG4, status_Max_Stat_TS_1h_TG4, Max_Stat_TS_1h_TG4, status_Min_Stat_TS_1h_TG4, Min_Stat_TS_1h_TG4,
            DimStat_TS_1h_TG5, status_Avg_Stat_TS_1h_TG5, Avg_Stat_TS_1h_TG5, status_Max_Stat_TS_1h_TG5, Max_Stat_TS_1h_TG5, status_Min_Stat_TS_1h_TG5, Min_Stat_TS_1h_TG5,
            DimStat_TS_1h_TG6, status_Avg_Stat_TS_1h_TG6, Avg_Stat_TS_1h_TG6, status_Max_Stat_TS_1h_TG6, Max_Stat_TS_1h_TG6, status_Min_Stat_TS_1h_TG6, Min_Stat_TS_1h_TG6,
            DimStat_TS_1h_TG7, status_Avg_Stat_TS_1h_TG7, Avg_Stat_TS_1h_TG7, status_Max_Stat_TS_1h_TG7, Max_Stat_TS_1h_TG7, status_Min_Stat_TS_1h_TG7, Min_Stat_TS_1h_TG7,
            Dim_Sum_PR_1h, status_Sum_Sum_PR_1h, Sum_Sum_PR_1h,
            DimGenWind_1h_SDI12, status_SpdMin_GenWind_1h, SpdMin_GenWind_1h, status_WRun_GenWind_1h, WRun_GenWind_1h,
            status_DirAvg_GenWind_1h, DirAvg_GenWind_1h, status_DirMax_GenWind_1h, DirMax_GenWind_1h,
            status_GustDir_GenWind_1h, GustDir_GenWind_1h, status_GustH_GenWind_1h, GustH_GenWind_1h,
            status_GustM_GenWind_1h, GustM_GenWind_1h, status_SpdAvg_GenWind_1h, SpdAvg_GenWind_1h,
            status_SpdMax_GenWind_1h, SpdMax_GenWind_1h, DimStat_WindChill_1h, status_Avg_Stat_WindChill_1h,
            Avg_Stat_WindChill_1h, status_Max_Stat_WindChill_1h, Max_Stat_WindChill_1h, status_Min_Stat_WindChill_1h,
            Min_Stat_WindChill_1h, DimQMBATT_Meas, status_meas_QMBATT_Meas, meas_QMBATT_Meas, ubicacion_id
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        values = [
            fecha, hora,
            nombres[0], status_Avg_Stat_TA_1h, avg_stat_ta_1h, status_Max_Stat_TA_1h, max_stat_ta_1h, status_Min_Stat_TA_1h, min_stat_ta_1h,
            nombres[1], status_Avg_Stat_RH_1h, avg_stat_rh_1h, status_Max_Stat_RH_1h, max_stat_rh_1h, status_Min_Stat_RH_1h, min_stat_rh_1h,
            nombres[2], status_Avg_Stat_PA_1h, avg_stat_pa_1h, status_Max_Stat_PA_1h, max_stat_pa_1h, status_Min_Stat_PA_1h, min_stat_pa_1h,
            nombres[3], status_Avg_Stat_SR_Dif_1h, avg_stat_sr_dif_1h, status_Max_Stat_SR_Dif_1h, max_stat_sr_dif_1h, status_Min_Stat_SR_Dif_1h, min_stat_sr_dif_1h,
            nombres[4], status_Sum_Sum_SR_Dif_1h, sum_sum_sr_dif_1h,
            nombres[5], status_Avg_Stat_SR_Glob_1h, avg_stat_sr_glob_1h, status_Max_Stat_SR_Glob_1h, max_stat_sr_glob_1h, status_Min_Stat_SR_Glob_1h, min_stat_sr_glob_1h,
            nombres[6], status_Sum_Sum_SR_Glob_1h, sum_sum_sr_glob_1h,
            nombres[7], status_Avg_Stat_TS_1h_TG1, avg_stat_ts_1h_tg1, status_Max_Stat_TS_1h_TG1, max_stat_ts_1h_tg1, status_Min_Stat_TS_1h_TG1, min_stat_ts_1h_tg1,
            nombres[8], status_Avg_Stat_TS_1h_TG2, avg_stat_ts_1h_tg2, status_Max_Stat_TS_1h_TG2, max_stat_ts_1h_tg2, status_Min_Stat_TS_1h_TG2, min_stat_ts_1h_tg2,
            nombres[9], status_Avg_Stat_TS_1h_TG3, avg_stat_ts_1h_tg3, status_Max_Stat_TS_1h_TG3, max_stat_ts_1h_tg3, status_Min_Stat_TS_1h_TG3, min_stat_ts_1h_tg3,
            nombres[10], status_Avg_Stat_TS_1h_TG4, avg_stat_ts_1h_tg4, status_Max_Stat_TS_1h_TG4, max_stat_ts_1h_tg4, status_Min_Stat_TS_1h_TG4, min_stat_ts_1h_tg4,
            nombres[11], status_Avg_Stat_TS_1h_TG5, avg_stat_ts_1h_tg5, status_Max_Stat_TS_1h_TG5, max_stat_ts_1h_tg5, status_Min_Stat_TS_1h_TG5, min_stat_ts_1h_tg5,
            nombres[12], status_Avg_Stat_TS_1h_TG6, avg_stat_ts_1h_tg6, status_Max_Stat_TS_1h_TG6, max_stat_ts_1h_tg6, status_Min_Stat_TS_1h_TG6, min_stat_ts_1h_tg6,
            nombres[13], status_Avg_Stat_TS_1h_TG7, avg_stat_ts_1h_tg7, status_Max_Stat_TS_1h_TG7, max_stat_ts_1h_tg7,status_Min_Stat_TS_1h_TG7, min_stat_ts_1h_tg7,
            nombres[14], status_Sum_Sum_PR_1h, sum_sum_pr_1h,
            nombres[15], status_spdmin_genwind_1h, status_wrun_genwind_1h, spdmin_genwind_1h, status_diravg_genwind_1h, wrun_genwind_1h, status_dirmax_genwind_1h, diravg_genwind_1h,
            status_gustdir_genwind_1h, dirmax_genwind_1h, status_gusth_genwind_1h, gustdir_genwind_1h, status_gustm_genwind_1h, gusth_genwind_1h, status_spdavg_genwind_1h,
            gustm_genwind_1h, status_spdmax_genwind_1h, spdavg_genwind_1h, spdmax_genwind_1h,
            nombres[16], status_Avg_Stat_WindChill_1h, avg_stat_windchill_1h, status_Max_Stat_WindChill_1h, max_stat_windchill_1h, status_Min_Stat_WindChill_1h, min_stat_windchill_1h,
            nombres[17], status_meas_qmbatt_meas, meas_qmbatt_meas,
            1
        ]
        conexion.cursor.execute(sql, values)

    conexion.cerrar_conexion()

def listar_datos(date, date_end, variables, ubicaciones):
    variable_column_map = {
        'Temperatura Ambiental': (
            'DimStat_TA_1h', 'status_Avg_Stat_TA_1h', 'Avg_Stat_TA_1h', 'status_Max_Stat_TA_1h', 'Max_Stat_TA_1h',
            'status_Min_Stat_TA_1h', 'Min_Stat_TA_1h'),
        'Humedad Relativa': (
            'DimStat_RH_1h', 'status_Avg_Stat_RH_1h', 'Avg_Stat_RH_1h', 'status_Max_Stat_RH_1h', 'Max_Stat_RH_1h',
            'status_Min_Stat_RH_1h', 'Min_Stat_RH_1h'),
        'Presion del Aire o Atmosferica': (
            'DimStat_PA_1h', 'status_Avg_Stat_PA_1h', 'Avg_Stat_PA_1h', 'status_Max_Stat_PA_1h', 'Max_Stat_PA_1h',
            'status_Min_Stat_PA_1h', 'Min_Stat_PA_1h'),
        'Radiacion Solar Difusa': (
            'DimStat_SR_Dif_1h', 'status_Avg_Stat_SR_Dif_1h', 'Avg_Stat_SR_Dif_1h', 'status_Max_Stat_SR_Dif_1h',
            'Max_Stat_SR_Dif_1h', 'status_Min_Stat_SR_Dif_1h', 'Min_Stat_SR_Dif_1h'),
        'Sumatoria de la hora de Radiacion Solar Difusa': (
            'DimSum_SR_Dif_1h', 'status_Sum_Sum_SR_Dif_1h', 'Sum_Sum_SR_Dif_1h'),
        'Radiacion Solar Global': (
            'DimStat_SR_Glob_1h', 'status_Avg_Stat_SR_Glob_1h', 'Avg_Stat_SR_Glob_1h', 'status_Max_Stat_SR_Glob_1h',
            'Max_Stat_SR_Glob_1h', 'status_Min_Stat_SR_Glob_1h', 'Min_Stat_SR_Glob_1h'),
        'Sumatoria de la hora de Radiacion Solar Global': (
            'DimSum_SR_Glob_1h', 'status_Sum_Sum_SR_Glob_1h', 'Sum_Sum_SR_Glob_1h'),
        'Temperatura de Suelo a nivel 1': (
            'DimStat_TS_1h_TG1', 'status_Avg_Stat_TS_1h_TG1', 'Avg_Stat_TS_1h_TG1', 'status_Max_Stat_TS_1h_TG1',
            'Max_Stat_TS_1h_TG1', 'status_Min_Stat_TS_1h_TG1', 'Min_Stat_TS_1h_TG1'),
        'Temperatura de Suelo a nivel 2': (
            'DimStat_TS_1h_TG2', 'status_Avg_Stat_TS_1h_TG2', 'Avg_Stat_TS_1h_TG2', 'status_Max_Stat_TS_1h_TG2',
            'Max_Stat_TS_1h_TG2', 'status_Min_Stat_TS_1h_TG2', 'Min_Stat_TS_1h_TG2'),
        'Temperatura de Suelo a nivel 3': (
            'DimStat_TS_1h_TG3', 'status_Avg_Stat_TS_1h_TG3', 'Avg_Stat_TS_1h_TG3', 'status_Max_Stat_TS_1h_TG3',
            'Max_Stat_TS_1h_TG3', 'status_Min_Stat_TS_1h_TG3', 'Min_Stat_TS_1h_TG3'),
        'Temperatura de Suelo a nivel 4': (
            'DimStat_TS_1h_TG4', 'status_Avg_Stat_TS_1h_TG4', 'Avg_Stat_TS_1h_TG4', 'status_Max_Stat_TS_1h_TG4',
            'Max_Stat_TS_1h_TG4', 'status_Min_Stat_TS_1h_TG4', 'Min_Stat_TS_1h_TG4'),
        'Temperatura de Suelo a nivel 5': (
            'DimStat_TS_1h_TG5', 'status_Avg_Stat_TS_1h_TG5', 'Avg_Stat_TS_1h_TG5', 'status_Max_Stat_TS_1h_TG5',
            'Max_Stat_TS_1h_TG5', 'status_Min_Stat_TS_1h_TG5', 'Min_Stat_TS_1h_TG5'),
        'Temperatura de Suelo a nivel 6': (
            'DimStat_TS_1h_TG6', 'status_Avg_Stat_TS_1h_TG6', 'Avg_Stat_TS_1h_TG6', 'status_Max_Stat_TS_1h_TG6',
            'Max_Stat_TS_1h_TG6', 'status_Min_Stat_TS_1h_TG6', 'Min_Stat_TS_1h_TG6'),
        'Temperatura de Suelo a nivel 7': (
            'DimStat_TS_1h_TG7', 'status_Avg_Stat_TS_1h_TG7', 'Avg_Stat_TS_1h_TG7', 'status_Max_Stat_TS_1h_TG7',
            'Max_Stat_TS_1h_TG7', 'status_Min_Stat_TS_1h_TG7', 'Min_Stat_TS_1h_TG7'),
        'Precipitacion de lluvia': (
            'Dim_Sum_PR_1h', 'status_Sum_Sum_PR_1h', 'Sum_Sum_PR_1h'),
        'Viento': (
            'DimGenWind_1h_SDI12', 'status_SpdMin_GenWind_1h', 'SpdMin_GenWind_1h', 'status_WRun_GenWind_1h', 'WRun_GenWind_1h',
            'status_DirAvg_GenWind_1h', 'DirAvg_GenWind_1h', 'status_DirMax_GenWind_1h', 'DirMax_GenWind_1h',
            'status_GustDir_GenWind_1h', 'GustDir_GenWind_1h', 'status_GustH_GenWind_1h', 'GustH_GenWind_1h',
            'status_GustM_GenWind_1h', 'GustM_GenWind_1h', 'status_SpdAvg_GenWind_1h', 'SpdAvg_GenWind_1h',
            'status_SpdMax_GenWind_1h', 'SpdMax_GenWind_1h'),
        'Sensacion Termica': (
            'DimStat_WindChill_1h', 'status_Avg_Stat_WindChill_1h',
            'Avg_Stat_WindChill_1h', 'status_Max_Stat_WindChill_1h', 'Max_Stat_WindChill_1h', 'status_Min_Stat_WindChill_1h',
            'Min_Stat_WindChill_1h'),
        'Bateria': (
            'DimQMBATT_Meas', 'status_meas_QMBATT_Meas', 'meas_QMBATT_Meas'),
    }
    print(date, date_end, variables, ubicaciones)
    columnas_comunes = ['u.nombre_ubicacion', 'u.altura', 'u.latitud', 'u.longitud', 'd.Date', 'd.Time']
    columnas_dinamicas = []
    for var in variables:
        if var in variable_column_map:
            columnas_dinamicas.extend(variable_column_map[var])
    columnas_str = ','.join(columnas_comunes + columnas_dinamicas)
    print(columnas_str)

    places = ['ALAO']
    u = {'ALAO': 1, 'ATILLO': 2}
    for ubi, j in u.items():
        if ubi in places:
            i = j

    conexion = ConexionDB()
    print("Fechas en la base de datos:")
    sql_check_dates = '''
            SELECT DISTINCT d.Date FROM datos_variables d ORDER BY d.Date LIMIT 10;
        '''
    conexion.cursor.execute(sql_check_dates)
    fechas_db = conexion.cursor.fetchall()
    print(fechas_db)
    # Construir la consulta SQL
    sql = f'''
        SELECT {columnas_str}
        FROM ubicacion AS u
        INNER JOIN datos_variables AS d ON u.ubicacion_id = d.ubicacion_id
        WHERE d.ubicacion_id = ? 
        AND d.Date >= ? AND d.Date <= ? 
    '''

    # Ejecutar la consulta
    try:
        conexion.cursor.execute(sql, (ubicaciones[0], date, date_end))
        datos = conexion.cursor.fetchall()
        print(f"Datos recuperados: {datos}")
    except Exception as e:
        print(f"Error en la consulta SQL: {str(e)}")
        datos = []
    conexion.cerrar_conexion()

    #print(datos)
    return datos
