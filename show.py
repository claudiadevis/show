from datetime import date

class Show:

    def __init__(self, titulo, tipo, esta_terminada = False, fecha_de_entrada = date.today()):
        self.titulo = titulo
        self.tipo = tipo
        self.esta_terminada = esta_terminada
        self.fecha_de_entrada = fecha_de_entrada
    
    def marcarTerminada(self):
        self.esta_terminada = True
    
if __name__ == '__main__':

    star_wars = Show('Star Wars','Película')
    avatar = Show('Avatar 2', 'Película')
    wormwood = Show('Wormwood', 'Documental')
    wire = Show('The wire','Una serie')

    mis_pelis = []
    mis_pelis.append(star_wars)
    mis_pelis.append(avatar)
    mis_pelis.append(wormwood)
    mis_pelis.append(wire)

    wire.marcarTerminada()

    for pelicula in mis_pelis:
        print(f'{pelicula.titulo} \t {pelicula.tipo} \t {pelicula.esta_terminada} \t {pelicula.fecha_de_entrada}')



    