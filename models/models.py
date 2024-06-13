#modelos para el proyecto Bitacora

#Clase flight
#atributos fecha, origen, destino, duracion, observacion, avion

#se agrega parrafo en master para hacer prueba
class Flight:
    def __init__(self, date, out, takeoff, landing, origin, destination, _in):
        self.date = date
        self.out = out  # Hora de salida
        self.takeoff = takeoff  # Hora de despegue
        self.landing = landing  # Hora de aterrizaje
        self.origin = origin
        self.destination = destination
        self._in = _in  # Hora de llegada al destino

    def calculate_total_hours(self):
        # Calcula la duracion total del vuelo en horas
        total_hours = (self.landing - self.takeoff).total_seconds() / 3600
        return total_hours

    def __str__(self):
        return f"Flight on {self.date} from {self.origin} to {self.destination} ({self.calculate_total_hours()} hours)"

# Ejemplo de uso
if __name__ == "__main__":
    from datetime import datetime, timedelta

    # Crear una instancia de Flight
    my_flight = Flight(
        date="2024-06-04",
        out=datetime(2024, 6, 4, 8, 0),  # Hora de salida
        takeoff=datetime(2024, 6, 4, 8, 30),  # Hora de despegue
        landing=datetime(2024, 6, 4, 11, 0),  # Hora de aterrizaje
        origin="SCL",
        destination="MIA",
        _in=datetime(2024, 6, 4, 12, 0),  # Hora de llegada al destino
    )

    # Imprimir detalles del vuelo
    print(my_flight)


#Clase aircraft
#Atributes Manufacter, tail number, Tipe of engines, Hp engines