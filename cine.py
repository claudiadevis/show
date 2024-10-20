from datetime import date

class Show:

    def __init__(self, titulo, tipo, esta_terminada = False, fecha_de_entrada = date.today()):
        self.titulo = titulo
        self.tipo = tipo
        self.esta_terminada = esta_terminada
        self.fecha_de_entrada = fecha_de_entrada
    
    def marcarTerminada(self):
        self.esta_terminada = True


class Cine:

    def __init__(self,nombre,direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.pases = []

    def __str__(self):
        return f'Nombre: {self.nombre} \t Dirección: {self.direccion}'
    
    def verCartelera(self):
        for pase in self.pases:
            print(f'Cine: {self.nombre} \t Película: {pase.pelicula.titulo} \t Horario: {pase.hora}')
            

class Pelicula(Show):
    
    def __init__(self, titulo):
        super().__init__(titulo, tipo = 'film')
        self.pases = []

    def dondeLaVeo(self):
        print(f'Pelicula: {self.titulo}')
        for pase in self.pases:
            print(f'Cine: {pase.cine.nombre} \t Horarios: {pase.hora}')


class Pase:
    
    def __init__(self, cine, pelicula, hora):
        if not isinstance(cine, Cine):
            raise TypeError(f'{cine} no es un cine')
        if not isinstance(pelicula, Pelicula):
            raise TypeError(f'{pelicula} no es una película')

        self.hora = hora
        self.cine = cine
        self.pelicula = pelicula
        
    def añadirPase(self):
        self.pelicula.pases.append(self)
        self.cine.pases.append(self)
    
    def __repr__(self):
        return self.hora

if __name__ == '__main__':

    cinesa = Cine('Cinesa', 'Gran via')
    yelmo = Cine('Yelmo','Sol')
    blancanieves = Pelicula('Blancanieves')
    star_wars = Pelicula('Star Wars')

    pase_2130 = Pase(cinesa, blancanieves, '21:30')
    pase_1200 = Pase(yelmo, star_wars,'12:00')
    pase_1430 = Pase(cinesa, blancanieves, '14:30')

    pase_2130.añadirPase()
    pase_1200.añadirPase()
    pase_1430.añadirPase()

    print(blancanieves.pases)
    print(star_wars.pases)
    print(cinesa.pases)
    print(yelmo.pases)
    cinesa.verCartelera()
    yelmo.verCartelera()
    blancanieves.dondeLaVeo()