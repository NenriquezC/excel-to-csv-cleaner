"""
Este archivo config.py sirve para centralizar toda la configuración de tu proyecto en un solo lugar. 
Es una excelente práctica que hace tu código más organizado y fácil de mantener.
¿Para qué sirve?
En lugar de tener valores "hardcodeados" (escritos directamente) en diferentes partes de tu código, los defines UNA VEZ aquí y
los usas en todo el proyecto.

🎯 CONFIG.PY - ¿Para qué sirve?
✅ CON config.py
Tienes UN SOLO LUGAR donde están TODOS los valores importantes.

Python
# src/config.py
input_dir = Path("input")
output_dir = Path("output")
output_file = "clean_data.csv"
max_files = 100
Ventajas:

Cambias UNA VEZ, afecta TODO

Quieres cambiar "input" → "datos_entrada"
Solo cambias en config.py
Automáticamente cambia en TODO el proyecto ✅
Sabes dónde buscar

¿Cuál es el nombre del archivo de salida? → Miras config.py
¿Cuántos archivos procesa? → Miras config.py
TODO está ahí 📋
No hay errores tontos

No escribes mal "input" en un archivo e "imput" en otro
No usas "100" en un lado y "50" en otro sin querer
TODO es consistente ✅
❌ SIN config.py
Los valores están regados por TODO el proyecto.

Python
# archivo1.py
input_folder = "input"
max_archivos = 100
output = "clean_data.csv"

# archivo2.py  
carpeta_entrada = "input"  # ¿Es la misma?
limite = 100  # ¿Es el mismo?
resultado = "clean_data.csv"  # ¿Es el mismo?

# archivo3.py
input_dir = "imput"  # 😱 ¡ERROR DE TYPO!
max_files = 50  # 🤔 ¿Por qué 50 y no 100?
output_file = "datos_limpios.csv"  # 🤨 ¿Diferente nombre?

"""

from __future__ import annotations #permite usar anotaciones de tikpos (type hints) sin problema de orden/imports  en python moderno
from dataclasses import dataclass #te deja definir una "config" como objeto simple, ordenado y facil de mantener
from pathlib import Path #rutas de archivos robustas (mejor que strings, funciona bien en windows/linux)

@dataclass (frozen=True)  #frozen=True significa inmutable, una vez creado no lo puedes cambiar accidentalmente
class Settings:
    #CONFIGURACION DE RUTAS
    #porque: estas son las carpetas del pipeline. Esta es la raiz del proyecto y el script debe saber donde leer/escribir
    input_dir: Path = Path("input")      # Carpeta donde están los archivos de entrada
    output_dir: Path = Path("output")    # Carpeta donde se guardan resultados
    logs_dir: Path = Path("logs")        # Carpeta para archivos de log

    #NOMBRES DE ARCHIVOS DE SALIDA
    output_clean_csv: str = "clean_data.csv"  # Archivo con datos limpios
    output_errors_csv: str = "errors.csv"     # Archivo con errores encontrados

    #EXTENSIONES PERMITIDAS
    excel_extensions: tuple[str, ...] = (".xlsx", ".xls")  # Formatos Excel válidos

#INSTANCIA GLOBAL
"""
🌍 INSTANCIA GLOBAL - ¿Para qué sirve?
✅ CON instancia global
Python
# src/config.py
SETTINGS = Settings()  # ⬅️ Se crea UNA VEZ aquí
Todos importan EL MISMO objeto:

Python
# archivo1.py
from src.config import SETTINGS  # Importa el objeto

# archivo2.py
from src.config import SETTINGS  # Importa EL MISMO objeto

# archivo3.py
from src.config import SETTINGS  # Importa EL MISMO objeto
Ventajas:

Todos usan lo MISMO

Todos ven los mismos valores
No hay confusión
Garantizado ✅
Más simple de escribir

Python
from src.config import SETTINGS
print(SETTINGS.input_dir)  # ¡Listo! 2 líneas
Usa menos memoria

1 objeto en lugar de 10
Más eficiente 🚀
❌ SIN instancia global
Python
# src/config.py
class Settings:
    input_dir = Path("input")
    
# NO hay instancia global
Cada archivo crea su propio objeto:

Python
# archivo1.py
from src.config import Settings
config = Settings()  # ⬅️ Objeto #1

# archivo2.py
from src.config import Settings
mi_config = Settings()  # ⬅️ Objeto #2 (diferente)

# archivo3.py
from src.config import Settings
ajustes = Settings()  # ⬅️ Objeto #3 (diferente)

"""
SETTINGS = Settings()  # Crea UNA instancia para todo el proyecto