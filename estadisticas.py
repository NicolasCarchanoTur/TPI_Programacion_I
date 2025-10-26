from typing import List, Dict, Tuple
import statistics

def pais_con_mayor_menor_poblacion(paises: List[Dict]) -> Tuple[Dict, Dict]:
    if not paises:
        return None, None
    mayor = max(paises, key=lambda p: p['poblacion'])
    menor = min(paises, key=lambda p: p['poblacion'])
    return mayor, menor

def promedio_poblacion(paises: List[Dict]) -> float:
    if not paises:
        return 0.0
    return statistics.mean([p['poblacion'] for p in paises])

def promedio_superficie(paises: List[Dict]) -> float:
    if not paises:
        return 0.0
    return statistics.mean([p['superficie'] for p in paises])

def cantidad_por_continente(paises: List[Dict]) -> Dict[str, int]:
    conteo = {}
    for p in paises:
        c = p['continente']
        conteo[c] = conteo.get(c, 0) + 1
    return conteo
