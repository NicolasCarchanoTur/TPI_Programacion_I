import csv
from typing import List, Dict
from utilidades import validar_int, formato_pais_valido

CSV_FIELDS = ['nombre', 'poblacion', 'superficie', 'continente']

def leer_paises_desde_csv(ruta: str) -> List[Dict]:
    paises = []
    try:
        with open(ruta, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            cabeceras = [h.strip().lower() for h in reader.fieldnames] if reader.fieldnames else []
            if any(c not in cabeceras for c in CSV_FIELDS):
                raise ValueError(f"El CSV debe contener las columnas: {CSV_FIELDS}. Encontrado: {cabeceras}")

            for i, row in enumerate(reader, start=2):
                try:
                    nombre = row.get('nombre', '').strip()
                    poblacion_raw = row.get('poblacion', '').strip()
                    superficie_raw = row.get('superficie', '').strip()
                    continente = row.get('continente', '').strip()

                    if not formato_pais_valido(nombre, continente):
                        print(f"Fila {i}: nombre o continente vacío. Se omite.")
                        continue

                    poblacion = validar_int(poblacion_raw)
                    superficie = validar_int(superficie_raw)

                    if poblacion is None or superficie is None:
                        print(f"Fila {i}: error en tipos numéricos. Se omite.")
                        continue

                    pais = {'nombre': nombre, 'poblacion': poblacion, 'superficie': superficie, 'continente': continente}
                    paises.append(pais)
                except Exception as e:
                    print(f"Error procesando fila {i}: {e}. Se omite.")
    except FileNotFoundError:
        print(f"Archivo no encontrado: {ruta}")
    except ValueError as ve:
        print(f"Error en formato del CSV: {ve}")
    except Exception as e:
        print(f"Error leyendo el CSV: {e}")
    return paises
