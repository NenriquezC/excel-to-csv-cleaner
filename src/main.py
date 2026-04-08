"""
Orquestador del pipeline (el “director de orquesta”)

"""
from __future__ import annotations
import logging #logging: para registrar qué pasó (clientes aman eso).
from pathlib import Path #Path: rutas.
import pandas as pd # pandas: concatenación y exportación.
#Nota importante: el punto . significa “importa desde el paquete src”.
from .config import SETTINGS #modulo interno
from .io_excel import find_excel_files, read_excel_file #m odulo interno

#FUNCION_1:LOGGING
def setup_logging(logs_dir: Path) -> None:
    logs_dir.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(logs_dir / "app.log", encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )


def main() -> int:
    setup_logging(SETTINGS.logs_dir)
    logging.info("Inicio del pipeline: Excel -> CSV limpio")
    #si no hay archivos, el programa no puede hacer nada. Devuelve código 1 (fallo controlado).
    excel_files = find_excel_files(SETTINGS.input_dir, SETTINGS.excel_extensions)
    if not excel_files:
        logging.warning("No se encontraron Excel en /input. Agrega al menos 1 archivo .xlsx")
        return 1

    logging.info("Excel encontrados: %s", ", ".join(f.name for f in excel_files))
    """
    Por qué:
    guardas cada DataFrame leído en una lista.
    agregas __source_file para trazabilidad:
    Si después hay una fila mala, sabes de qué Excel salió.
    esto es oro en proyectos reales.
    """
    frames: list[pd.DataFrame] = []
    for file in excel_files:
        logging.info("Leyendo: %s", file.name)
        df = read_excel_file(file)
        if df is None:
            raise RuntimeError(f"read_excel_file devolvió None para: {file.name}")
        df["__source_file"] = file.name  # trazabilidad (muy útil)
        frames.append(df)

    raw = pd.concat(frames, ignore_index=True) #une todos los DataFrames en uno solo.
    logging.info("Filas totales leídas (raw): %d", len(raw))
    logging.info("Columnas raw: %s", list(raw.columns))
    #crea output/ si no existe y exporta CSV.
    #Esto por ahora es “salida provisional” para validar que todo funciona
    SETTINGS.output_dir.mkdir(parents=True, exist_ok=True)
    out_path = SETTINGS.output_dir / SETTINGS.output_clean_csv
    raw.to_csv(out_path, index=False, encoding="utf-8")

    logging.info("Salida provisional generada: %s", out_path.resolve())
    logging.info("Fin OK (por ahora solo concatenación). Siguiente: normalizar + limpiar + validar.")
    #código de salida 0 = ejecución OK.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())