# NombrePatterns

<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/MateoBarrera/design-patterns-es">
    <img src="../../src/MB_lila_dev.png" alt="Logo MB" width="80" height="80">
  </a>

  <h3 align="center">Design Patterns (es): NombrePatterns</h3>

  <p align="center">
    Basado en el proyecto <a href="https://refactoring.guru/es">Refactoring.guru</a>
    <br />
    <a href="https://github.com/MateoBarrera/design-patterns-es"><strong>Explorar »</strong></a>
    <br />
    <br />
    <a href="https://github.com/MateoBarrera">Autor</a>
    ·
    <a href="https://github.com/MateoBarrera/design-patterns-es/issues">Reportar Bug</a>
    ·
    <a href="https://github.com/MateoBarrera/design-patterns-es/issues">Solicitar Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#descripción">Descripción</a></li>
    <li><a href="#estructura">Estructura</a></li>
    <li><a href="#pseudocódigo">Pseudocódigo</a></li>
    <li><a href="#aplicabilidad">Aplicabilidad</a></li>
    <li><a href="#adicionales">Adicionales</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## Descripción

**Factory Method**, también conocido como método fábrica o constructor virtual, es un patrón de diseño creacional que se utiliza en la creación de objetos. Proporciona una interfaz para crear objetos en una clase base denominada **superclase**, pero permite que las subclases alteren el tipo de objetos que se crearán.

El objetivo principal del **Factory Method** es abstraer la lógica de creación de objetos y permitir la flexibilidad en la creación de instancias de objetos de diferentes tipos sin acoplar el código a clases concretas. Esto significa que las subclases pueden proporcionar su propia implementación del método de fábrica y, de esta manera, controlar qué clase concreta se instancia.

<p align="right">(<a href="#readme-top">Regresar al inicio</a>)</p>

<!-- GETTING STARTED -->

## Estructura

El **Factory Method** se compone de dos elementos principales: la clase base o superclase que declara el método de fábrica abstracto, y las subclases que implementan ese método y proporcionan su propia implementación de creación de objetos.

[![Estructura][estructura]][estructura-url]

<p align="right">(<a href="#readme-top">Regresar al inicio</a>)</p>

## Pseudocódigo

```
// Clase base que declara el método de fábrica abstracto
Clase Base {
    método abstracto factoryMethod() -> Producto

    // Otros métodos comunes
    método operar() {
        Producto producto = factoryMethod()
        // Realizar operaciones adicionales con el producto
    }
}

// Subclase que implementa el método de fábrica
Clase Concreta extends Base {
    método factoryMethod() -> Producto {
        retornar nuevo ProductoConcreto()
    }
}

// Interfaz o clase base para los productos
Interfaz Producto {
    método hacerAlgo()
}

// Clase concreta de producto
Clase ProductoConcreto implements Producto {
    método hacerAlgo() {
        mostrar "Haciendo algo en ProductoConcreto"
    }
}

// Uso del Factory Method
variable base: Base = new Concreta()
base.operar()
```

En este pseudocódigo, la clase _Base_ declara el método de fábrica abstracto **factoryMethod()**. La subclase _Concreta_ implementa ese método y devuelve una instancia de **ProductoConcreto**. La interfaz _Producto_ define los métodos que deben implementar todas las clases de productos.

Luego, en el uso del **Factory Method**, se crea una instancia de la subclase Concreta y se llama al método operar() de la clase base Base. Dentro de ese método, se utiliza el método factoryMethod() para obtener una instancia de Producto (en este caso, ProductoConcreto) y se realizan operaciones adicionales con el producto.

<p align="right">(<a href="#readme-top">Regresar al inicio</a>)</p>

<!-- USAGE EXAMPLES -->

## Aplicabilidad

El **Factory Method** se utiliza cuando se necesita una flexibilidad en la creación de objetos y se desea desacoplar el código de la creación de instancias de clases concretas. Esto permite un código más modular y más fácil de mantener y extender en el futuro.

<p align="right">(<a href="#readme-top">Regresar al inicio</a>)</p>

<!-- ROADMAP -->

## Adicionales

Para tips de aplicación, guía de como implementarlo, pros/contras y relaciones con demás patrones de diseño visite [Refactory.guru][estructura-url].

<p align="right">(<a href="#readme-top">Regresar al inicio</a>)</p>

## Licencia

Distribuido bajo la licencia MIT. Para mas información visite `LICENSE.txt` .

<p align="right">(<a href="#readme-top">Regresar al inicio</a>)</p>

<!-- CONTACT -->

## Contacto

Mateo Barrera- [@materile_19](https://twitter.com/materile_19) - mateobarrerazapata@gmail.com

Enlace del proyecto: [https://github.com/MateoBarrera/design-patterns-es](https://github.com/MateoBarrera/design-patterns-es)

<p align="right">(<a href="#readme-top">Regresar al inicio</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- examples -->

[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/MateoBarrera/design-patterns-es/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/MateoBarrera/design-patterns-es/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/MateoBarrera/design-patterns-es/stargazers

<!-- examples -->

<!-- main -->

[watchers-shield]: https://img.shields.io/github/watchers/MateoBarrera/design-patterns-es?style=for-the-badge
[watchers-url]: https://github.com/MateoBarrera/design-patterns-es
[issues-shield]: https://img.shields.io/bitbucket/issues-raw/MateoBarrera/design-patterns-es?style=for-the-badge
[issues-url]: https://github.com/MateoBarrera/design-patterns-es/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/MateoBarrera/design-patterns-es/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/mateobarrerazapata
[python-shield]: https://img.shields.io/badge/python-3.10.6-green?style=for-the-badge&logo=python
[python-url]: https://www.python.org/

<!-- main -->

[estructura]: src/structure.png
[estructura-url]: https://refactoring.guru/es/design-patterns/factory-method
