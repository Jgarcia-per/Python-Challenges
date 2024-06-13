<- [Readme](README.md#parte-2--objetos)

### Punto 6 | Construir el UML
A partir del enunciado construya un nuevo UML que refleje la construcción del mundo propuesta en el enunciado. Considere las relaciones de herencia y de asociación entre las diferentes clases. Para hacer un UML puede usar herramientas específicas como [Lucidchart](https://www.lucidchart.com/pages/es) o [draw.io (diagrams.net)](https://app.diagrams.net/), o simplemente hacerlas en Powerpoint o Paint.
### Punto 7 | Ingrediente
Construya la clase abstracta Ingrediente según la especificación del enunciado. En este caso la clase debe tener los atributos de precio, calorías, nombre, inventario y es_vegetariano. También debe tener la función de es_sano (Punto 1) y la función abstracta de abastecer. No olvide colocar todos los getters y los setters de los atributos.

### Punto 8 | Base y Complemento
Construya las clases Base y Complemento que heredan de la clase abstracta Ingrediente. Recuerde que en este caso la base tendrá el atributo extra sabor, mientras que los complementos tendrán la función extra renovar_inventario. Para las bases la función abastecer sumará 5 en el inventario, mientras que para los complementos se aumentará en 10. No olvide colocar el getter y el setter para el atributo sabor.

### Punto 9 | IProducto
Construya la interfaz Producto según la especificación del enunciado. En este caso la interfaz solamente tendrá las funciones abstractas calcular_costo, calcular_rentabilidad y calcular_calorias.

### Punto 10 | Copa y Malteada
Construya las clases Copa y Malteada que implementan la interfaz IProducto. Tanto Copa como Malteada tienen los atributos nombre y precio_publico. Tenga en cuenta las siguientes diferencias entre la implementación de ambas clases:
* Calcular el costo de una copa se hace simplemente sumando los ingredientes (Punto 3). Para las malteadas se sumarán 500 pesos por el uso de vasos plásticos.
* Calcular las calorías de una copa, es simplemente seguir la fórmula de sumar los ingredientes y multiplicar por 0.95 (Punto 2). Para las malteadas, se debe sumar y agregar 200 calorías, pues todas utilizan crema chantilly. No es necesario multiplicar por 0.95
* Las malteadas tienen un atributo de volumen, mientras que las copas tienen uno de tipo_vaso. Adicional a esto, calcular la rentabilidad (Punto 4) se implementa de la misma manera en ambas clases. No olvide agregar los getters y setters en ambas clases.

###  Punto 11 | Heladería
Construya la clase Heladería con todos los atributos, relaciones y funciones descritas en el enunciado. No olvide colocar la función que le permite determinar el producto más rentable (Punto 5).

### Punto 12 | Vender
Finalmente construya la función vender en la clase heladería, esta función debe seguir los siguientes pasos:
*  Recibe el nombre de un producto.
*  Verifica que dicho nombre de un producto sea igual a uno de los cuatro productos disponibles.
* Si lo anterior es correcto, verifica que haya existencias de los ingredientes para hacer dicho producto. Se necesita 1 de cada complemento y 0.2 de cada base para vender.
* Si sí hay existencia, resta de cada uno de los productos lo necesario para armar el producto.
* Si se vendió el producto, suma a las ventas del día el precio del producto.
*  Retorna True si fue posible venderlo, False de lo contrario.