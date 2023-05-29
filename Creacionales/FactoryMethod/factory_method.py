# Clase base que declara el método de fábrica abstracto
class Creator:
    def factory_method(self):
        raise NotImplementedError

    # Otros métodos comunes
    def operate(self):
        product = self.factory_method()
        # Realizar operaciones adicionales con el producto


# Subclase que implementa el método de fábrica
class ConcreteCreator(Creator):
    def factory_method(self):
        return ConcreteProduct()


# Interfaz o clase base para los productos
class Product:
    def do_something(self):
        raise NotImplementedError


# Clase concreta de producto
class ConcreteProduct(Product):
    def do_something(self):
        print("Haciendo algo en ConcreteProduct")


# Uso del Factory Method
creator = ConcreteCreator()
creator.operate()
