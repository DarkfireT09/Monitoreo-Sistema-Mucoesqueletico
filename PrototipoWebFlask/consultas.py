#Consultas necesarias para hacer las gráficas

#Consultas que van a aparecer en el resumen de datos:

def avg_pulso():
    return """SELECT AVG(pulso) FROM pulsometro""" #promedio de pulso cardiaco

def avg_actividad():
    return """SELECT AVG(porcentaje_activdad) FROM pulsometro""" #promedio de porcentaje de actividad física obtenida por el pulso cardiaco

def num_alertas():
    return """SELECT COUNT(mensaje) FROM notificaciones"""

def ultimo_pulso():
    return """SELECT pulso 
                FROM pulsometro
                WHERE fecha = (SELECT MAX(fecha) FROM pulsometro)"""

def ultima_actividad():
    return """SELECT porcentaje_activdad
                FROM pulsometro
                WHERE fecha = (SELECT MAX(fecha) FROM pulsometro)"""

#Consulta para el reporte de pulso

def reporte_pulso():
    return """SELECT fecha, pulso
                FROM pulsometro
                ORDER BY fecha ASC"""

#Consulta para el reporte de actividad física

def reporte_actividad():
    return """SELECT fecha, porcentaje_activdad
                FROM pulsometro
                ORDER BY fecha ASC"""



