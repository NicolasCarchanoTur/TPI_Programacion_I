from typing import List, Dict

def ordenar_por_nombre(paises: List[Dict], descendente: bool = False) -> List[Dict]:
    return sorted(paises, key=lambda p: p['nombre'].lower(), reverse=descendente)

def ordenar_por_poblacion(paises: List[Dict], descendente: bool = False) -> List[Dict]:
    return sorted(paises, key=lambda p: p['poblacion'], reverse=descendente)

def ordenar_por_superficie(paises: List[Dict], descendente: bool = False) -> List[Dict]:
    return sorted(paises, key=lambda p: p['superficie'], reverse=descendente)
