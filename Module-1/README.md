## Back-end Python course
### Workshop 1 - Basic Python Operations
The objective of this workshop is to practice the basic Python concepts reviewed in the previous class. Each exercise will allow you to put into practice the concepts seen in the previous slides.

* [Point 1 : The IMC](Workshops/Workshop1-BasicPythonOperations/elIMC/imc.py)
* [Point 2 : Leap years](Workshops/Workshop1-BasicPythonOperations/añosBisiestos/bisiestos.py)
* [Point 3 : Do you divide me?](Workshops/Workshop1-BasicPythonOperations/meDivide/meDivide.py)
* [Point 4 : Classifying words](Workshops/Workshop1-BasicPythonOperations/clasificandoPalabras/clasificandoPalabras.py)

### Workshop 2 - Functions and Modules
The objective of this workshop is to practice the basic Python concepts reviewed in the previous class. Each exercise will allow you to put into practice the concepts seen in the previous slides. Remember to put into practice the good programming practices discussed in the course. Comment and give meaningful names to functions and variables to make your code clear.

* [Point 1 : Circle area](Workshops/Workshop2-FunctionsModules/areaCirculo/circulo.py)
* [Point 2 : Square area](Workshops/Workshop2-FunctionsModules/areaCuadrado/modulo.py)
* [Point 3 : Shaded area](Workshops/Workshop2-FunctionsModules/areaCuadrado/README.md/#punto-3--el-área-sombreada)
* [Point 4 : Main menu](Workshops/Workshop2-FunctionsModules/consola.py)

### Workshop 3 - UML and Classes (POO)
The objective of this workshop is to practice the basic Python concepts reviewed in the previous class. Each exercise will allow you to put into practice the concepts seen in the previous slides. Remember to put into practice the good programming practices discussed in the course. Comment and give meaningful names to functions and variables to make your code clear.

* [Point 0 : Preparation](Workshops/Workshop3-UMLClasses/preparacion)

#### Statement
In the day care center, a new owner has decided to establish a record of the canine's diet. For this purpose, a record of the concentrates will be kept. Each concentrate will have a name, a price, a number of calories and an INVIMA registration. Apart from the getters (dar_x) it will also have 2 functions:

* **give_information:** returns a string in the form “Name ($Price)”.
* **calculate_profitability:** returns the result of dividing price/calories rounded to two decimal places.

The Nursery will have a list of the different concentrates available, while each dog will have 1 concentrate of its choice.

* [Point 1 : The new UML](Workshops/Workshop3-UMLClasses/nuevoUML/Diagrama_Guarderia.png)
* [Point 2 : The concentrate](Workshops/Workshop3-UMLClasses/concentrado/concentrado.py)
* [Point 3 :  Modify Nursery and Dog](Workshops/Workshop3-UMLClasses/preparacion)

### Workshop 3 - Heritage (POO)
The objective of this workshop is to practice the basic Python concepts reviewed in the previous class. Each exercise will allow you to put into practice the concepts seen in the previous slides. Remember to put into practice the good programming practices discussed in the course. Comment and give meaningful names to functions and variables to make your code clear.

* [Point 0 : Preparation](Workshops/Workshop4-HeritagePOO/preparacion)

#### Statement

Now we want to model two animals considered exotic, a Boa Constrictor and a Ferret. For this it is necessary to build a new exotic animal class, which includes the new attributes country_origin (str) and taxes (float). In addition to a new method called calculate_flete that multiplies the taxes by the weight of the animal to know what is the cost of importing this animal. The Boa Constrictor and the Ferret must have their own classes, the Boa makes the sound “Tsss!” while the Ferret makes “Eek Eek!”. Additionally, the Boa must have an attribute that allows it to count how many mice it has eaten, as well as a method that adds a mouse to that count. The Ferret must have no additional attributes or methods.

* [Point 1 : The new UML](Workshops/Workshop4-HeritagePOO/nuevoUML/Diagrama_Guarderia.png)
* [Point 2 : Exotic Animal](Workshops/Workshop4-HeritagePOO/animalExotico/animal_exotico.py)
* [Point 3 : Ferrets and Boa Constrictors](Workshops/Workshop4-HeritagePOO/huronesyBoas)