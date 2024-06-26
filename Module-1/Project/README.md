## La heladería
### Objetivo general
El objetivo de este Proyecto es practicar todos los conceptos trabajados en este módulo 1. Cada punto le permitirá poner en práctica los conceptos vistos en clase. Recuerde poner en práctica las buenas prácticas de programación discutidas en el curso. Comente y ponga nombres significativos a las funciones y variables para que su código sea claro. Este proyecto debe ser resuelto de forma individual.
### Objetivos específicos
1. Practicar el manejo de diferentes tipos de datos y de variables.
2. Practicar la construcción de funciones propias para resolver requerimientos.
3. Practicar los conceptos base de la Programación Orientada a Objetos
4. Implementar clases con herencia y clases abstractas.
5. Practicar buenas prácticas de programación

## Enunciado
Una heladería muy popular está buscando digitalizar su menú y parte de su manejo de inventario. Para esto ha decidido contar con nuestra ayuda. La heladería tiene dos conceptos principales: Productos e Ingredientes. A partir de los ingredientes que pueden ser bases o complementos, es posible armar productos, que pueden ser Copas o Malteadas.
Cada Ingrediente tiene un precio, número de calorías por porción, un nombre, un contador para su inventario y un indicador de si es o no vegetariano. Para cada ingrediente se debe saber si es sano o no, según las regulaciones del departamento de salud. También debe ser posible reabastecerlos cuando sea necesario. Como ya se mencionó en el párrafo anterior, los ingredientes pueden ser bases o complementos. Las bases son las que sirven como ingrediente principal de los productos, así que adicional a lo descrito, tendrán como característica adicional su sabor. Por otra parte, los complementos sufren en algunos casos de baja rotación de inventario, así que debe ser posible bajar su inventario a 0 con una sola instrucción. 
Por otra parte, tenemos los productos. Cada producto está compuesto por 3 ingredientes, realmente no tiene relevancia si son bases o complementos. Por regulación del departamento de salud es necesario poder calcular las calorías del producto y tener esta información a la mano. Para la heladería es importante saber el costo de un producto a partir de los ingredientes y la rentabilidad del mismo. Como ya lo mencionamos hay 2 tipos de productos, copas y malteadas. Si bien ambos productos tendrán su nombre y su precio al público, las copas tendrán un tipo de vaso y las malteadas un volumen en onzas.
Finalmente, la heladería. Por su nivel de operaciones, la heladería tiene solo 4 productos a la vez en cualquier debido momento. Sin embargo, la cantidad de ingredientes en los libros de inventario puede ser ilimitada. Al jefe le interesan realmente solo dos tareas, en primer lugar, saber cuál es el producto que más rentabilidad le genera a la heladería, y una función que le permita vender un producto, revisando previamente si se tienen los ingredientes para armarlo. A parte de sus relaciones y funciones, la heladería tiene un contador que permite llevar la cuenta de las ventas del día.

### Parte 1 | Funciones
La primera parte de este proyecto consiste en construir funciones que nos serán útiles para el funcionamiento de nuestra heladería. Cree un archivo llamado funciones.py y desarrolle en él las siguientes funciones.
* [Archivo explicación funciones](FUNCTIONS.md)

### Parte 2 | Objetos
La segunda parte de este proyecto consiste en implementar el sistema de la Heladería en un sistema de Objetos que representen el problema descrito en el enunciado. Las funciones definidas en la parte 1 le serán de mucha utilidad para construir este mundo, pero deberá modificarlas ligeramente para que sean coherentes con el sistema propuesto.
* [Archivo explicación objetos](OBJECTS.md)