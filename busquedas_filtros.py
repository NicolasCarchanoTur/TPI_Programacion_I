from typing import List, Dict

def buscar_por_nombre(paises: List[Dict], termino: str) -> List[Dict]:
    t = termino.strip().lower()
    return [p for p in paises if t in p['nombre'].lower()]

def filtrar_por_continente(paises: List[Dict], continente: str) -> List[Dict]:
    c = continente.strip().lower()
    return [p for p in paises if c in p['continente'].lower()]

def filtrar_por_rango_poblacion(paises: List[Dict], min_pob: int, max_pob: int) -> List[Dict]:
    return [p for p in paises if min_pob <= p['poblacion'] <= max_pob]

def filtrar_por_rango_superficie(paises: List[Dict], min_sup: int, max_sup: int) -> List[Dict]:
    return [p for p in paises if min_sup <= p['superficie'] <= max_sup]
