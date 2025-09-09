# Curso 24/25. Práctica 2. Interfaces gráficas para aplicaciones de dispositivos móviles

## Welcome :wave:

- **Who is this for**: Grupos de prácticas de la asignatura _IPM_.

- **What you'll learn**: Implementación de interfaces gráficas con un
  paradigma quasi-declarativo, diseño e implementación de interfaces
  adaptativas, patrones arquitectónicos para el manejo del estado con
  interfaces gráficas, concurrencia con funciones asíncronas,
  _software testing_ a través de la interfaz gráfica.

- **What you'll build**: Construiréis una aplicación para dispositivos
  móviles.

- **Prerequisites**: Asumimos que os resultan familiares el lenguaje
  de programación _dart_ y la librería _flutter_.

- **How long**: Este assigment está formado por tres pasos o
  _tareas_. La duración estimada de cada tarea es de una semana
  lectiva.


La aplicación a desarrollar está dirigida a las personas usuarias del
sistema sanitario introducido en la primera práctica.

  - La usuaria puede consultar la medicación pautada por al médico.
    Tanto una consulta genérica como una consulta de la medicación
    pendiente en el siguiente período de tiempo: horas, día, ...
  
  - La usuaria puede marcar las tomas realizadas en cada momento.
	
  - [Opcional] La aplicación notifica a la usuaria 5 minutos antes de
    cada toma.
	
Otros requisitos:

  - El dispositivo de la usuaria puede ser tanto un teléfono
    inteligente como un reloj inteligente.


<details id=1>
<summary><h2>Tarea 1: Diseño de la interfaz</h2></summary>

### :wrench: Esta tarea tiene las siguientes partes:

  1. Identifica y documenta los casos de uso relevantes para las
     potenciales usuarias de la aplicación.
  
  2. Realizar un diseño de la interfaz de usuaria de la aplicación y
     añadir el diseño a este repositorio en un fichero _PDF_ con el
     nombre `diseño-iu.pdf`. El diseño tiene que ajustarse a las
     siguientes pautas:
	 
     - Al menos debe haber un diseño distinto para teléfonos móviles y
       otro para relojes.
	   
     - El diseño debe adaptarse a la configuración del dispositivo.
	 
     - El diseño tiene que incluir los elementos necesarios para la
       gestión de errores, proporcionar la retroalimentación necesaria
       a la usuaria durante las operaciones de E/S, ...
	 
  2. Seleccionar un patrón arquitectónico para gestionar el estado de
     la aplicación de manera que el componente de la _vista_ sea
     independiente del _estado/modelo_. El patrón debe ser adecuado
     para su aplicación con _flutter_.
	 
  3. Realizar un diseño software siguiendo el patrón seleccionado.
  
	  - El diseño tiene que cubrir los casos de uso de la aplicación.
	  
	  - El diseño se realiza usando el lenguaje _UML_ y debe incluir
        diagramas tanto para la parte estática como para la dinámica.
		
	  - La documentación del diseño se incorpora al fichero
        `diseño_sw.md` de este repositorio. El formato del fichero es
        la versión de _markdown_ [Github Flavored
        Markdown](https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax). Los
        diagramas UML se integran directamente en el fichero markdown
        usando
        [_Mermaid_](https://github.blog/2022-02-14-include-diagrams-markdown-files-mermaid/)
		

### :books: Objetivos de aprendizaje:

  - Diseño adaptativo.
  
  - Patrones arquitectónicos en IGUs.
  
</details>


<details id=2>
<summary><h2>Tarea 2: Implementación de la aplicación</h2></summary>

### :wrench: Esta tarea tiene las siguientes partes:

  1. Implementar la aplicación diseñada en la tarea anterior.
  
     - La implementación debe realizarse usando _flutter_.

  2. [Opcional] Implementar los distintos casos de uso identificados para 
     el manejo de las notificaciones.
	 
> :warning: Es muy importante capturar todo tipo de errores, en
> especial los relacionados con las operaciones de E/S e informar a la
> usuaria en todo momento.

> :warning: Actualmente flutter soporta múltiples plataformas: linux,
> web, android, ios, etc. Pero la práctica consiste en el desarrollo
> de una aplicación para dispositivos móviles. Tenéis que cercioraros
> de que la aplicación efectivamente funciona como se espera en
> android y/o ios. La defensa de la práctica también se realizará
> ejecutando la aplicación en alguna de dichas plataformas.

> :warning: El desarrollo software es iterativo. Durante esta tarea
> pueden ser necesarios cambios tanto en el diseño sw como en el
> diseño de la interfaz. Es importante actualizar los documentos de
> diseño afectados. También es importante que la modificación de los
> diseños se incluyan junto con el código relacionado en el mismo
> _commit_.


### :books: Objetivos de aprendizaje:

  - Uso de librerías para construir IGUs.
  
  - Programación dirigida por eventos

  - Uso de la concurrencia con funciones asíncronas.
  
  - Gestión de errores en la E/S.
  
</details>



<details id=3>
<summary><h2>Tarea 3: Test end2end</h2></summary>

### :wrench: Esta tarea tiene las siguientes partes:

  1. Siguiendo la documentación de diseño, implementar tests _end to
     end_ para los distintos caso de uso de la aplicación.
	 
  2. Implementar tests para las situaciones en que ocurren errores de
       E/S y errores de la usuaria.
	 
	 
### :books: Objetivos de aprendizaje:

  - Tests end to end a través de la interfaz gráfica.

</details>


<details id=X>
<summary><h2>Finish</h2></summary>

_Congratulations friend, you've completed this assignment!_

Una vez terminada la práctica no olvidéis revisar el contenido del
repositorio en Github y comprobar su correcto funcionamiento antes de
realizar la defensa.

</details>

