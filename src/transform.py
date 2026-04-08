"""
Docstring for excel_to_csv_cleaner.src.transform
Transformaciones del pipeline (Excel crudo --> DataFrame usable)
"""
from __future__ import annotations
#Any es un tipo especial del módulo typing que significa "cualquier tipo". 
# Se usa en type hints (anotaciones de tipo) para indicar que una variable puede ser de cualquier tipo de dato.
from typing import Any
import re


def is_empty(value: Any) -> bool:
    """
    Devuelve True si el valor cuenta como 'vacío' para nuestro análisis.
    """
    if value is None:
        return True
    
    texto = str(value).strip().lower()
    valores_vacios = {"", "nan", "none"}  # set: rápido y limpio

    return texto in valores_vacios




def has_letters(value: Any) -> bool:
    """
    Devuelve True si el valor contiene al menos una letra (A-Z o acentos).
    Útil para detectar encabezados tipo: "Destination", "Distance (km)", etc.
    """
    # TODO: implementa
    raise NotImplementedError


def detect_header_row(raw_df, max_scan_rows: int = 30) -> int:
    """
    Detecta la fila más probable de encabezados en un DataFrame leído con header=None.
    Retorna el índice (int) de la fila candidata.
    """
    # TODO: implementa el scoring por fila
    raise NotImplementedError


