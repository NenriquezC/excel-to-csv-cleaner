"""
Docstring for excel_to_csv_cleaner.src.io_excel
io_excel.py solo se encarga de “encontrar y leer” datos. No transforma, no valida. Eso es diseño limpio.
"""

from __future__ import annotations
from pathlib import Path #Path: manejar rutas bien.
from typing import Iterable
import pandas as pd #pandas: para leer Excel en DataFrame.

#FUNCION_1:ENCONTRAR EXCELS
def find_excel_files(input_dir: Path, extensions: tuple[str, ...]) -> list[Path]:
    """
    Encuentra archivos Excel dentro de input_dir (no recursivo).
    Devuelve una lista ordenada para resultados deterministas.
    """
    #Por qué: error temprano y claro si el usuario borró la carpeta o ejecuta desde un lugar incorrecto.
    #Un programador serio falla rápido y con mensaje claro.
    if not input_dir.exists():
        raise FileNotFoundError(f"No existe la carpeta de entrada: {input_dir.resolve()}")
    #busca todos los archivos en esa carpeta con esas extensiones (no recursivo).
    #glob("*{ext}") es “muestrame todo lo que termine con .xlsx”.
    files: list[Path] = []
    for ext in extensions:
        files.extend(input_dir.glob(f"*{ext}"))

    #Por qué: orden determinista. Si tienes 10 archivos, siempre los procesa en el mismo orden → resultados repetibles.    
    return sorted(files)

#FUNCION_2:LEER UN EXCEL
def read_excel_file(path: Path) -> pd.DataFrame:
    """
    Lee un Excel y devuelve un DataFrame.

    Regla de contrato:
    - Devuelve SIEMPRE un DataFrame.
    - Si no puede, lanza un error con contexto (nombre de archivo).
    """
    #pandas se encarga de leer el Excel y devolver DataFrame.
    try:
        #df = pd.read_excel(path, sheet_name=0)  # primera hoja
        df = pd.read_excel(path, header = None) 
    #si falla, lanzas un error con contexto (“qué archivo falló”).
    except Exception as exc:
        raise RuntimeError(f"Error leyendo Excel '{path.name}': {exc}") from exc
    if df is None:
        raise RuntimeError(f"Lectura inválida: pandas devolvió None para '{path.name}'")

    if not isinstance(df, pd.DataFrame):
        raise RuntimeError(
            f"Lectura inválida: se esperaba DataFrame, se recibió {type(df).__name__} en '{path.name}'"
        )

    return df