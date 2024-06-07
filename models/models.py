#modelos para el proyecto Bitacora

#Clase flight
#atributos fecha, origen, destino, duracion, observacion, avion
class Flight:
    def __init__(self, date, duration_hours, origin, destination):
        self.date = date
        self.duration_hours = duration_hours
        self.origin = origin
        self.destination = destination

    def calculate_total_hours(self):
        return self.duration_hours

    def __str__(self):
        return f"Flight on {self.date} from {self.origin} to {self.destination} ({self.duration_hours} hours)"

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia de Flight
    my_flight = Flight(date="2024-06-04", duration_hours=3.5, origin="SCL", destination="MIA")

    # Imprimir detalles del vuelo
    print(my_flight)
    print(f"Total de horas de vuelo: {my_flight.calculate_total_hours()} horas")


#Clase aircraft
#Atributes Manufacter, tail number, Tipe of engines, Hp engines