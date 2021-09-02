from gestion import pasar_genero,pasar_idioma

class Libro:
    def __init__(self,tit, gen, id, prec, isbn):
        self.titulo = tit
        self.genero = gen
        self.idioma = id
        self.precio = prec
        self.isbn = isbn

def write(libro):
    print("Titulo:", libro.titulo, end="  \t")
    print("Genero:", pasar_genero(libro.genero), end="  \t")
    print("Idioma:", pasar_idioma(libro.idioma), end="  \t")
    print("Precio:", libro.precio,"$", end="  \t")
    print("Codigo ISBN: ", libro.isbn )
