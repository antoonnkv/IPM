# Curso 24/25. Práctica 1. Interfaces gráficas para aplicaciones de escritorio

## Welcome :wave:

- **Who is this for**: Grupos de prácticas de la asignatura _IPM_.

- **What you'll learn**: Implementación de interfaces gráficas,
  patrones arquitectónicos para el manejo del estado con interfaces
  gráficas, uso y necesidad de la concurrencia en interfaces
  gráficas, internacionalización de intefaces gráficas.

- **What you'll build**: Construiréis una aplicación con una interface
  gráfica de escritorio.

- **Prerequisites**: Asumimos que os resultan familiares el lenguaje de
  programación _python_ y la librería _Gtk+_.

- **How long**: Este assigment está formado por tres pasos o
  _tareas_. La duración estimada de cada tarea es de una semana
  lectiva.




<details id=1>
<summary><h2>Tarea 1: Diseño software e implementación</h2></summary>

### :wrench: Esta tarea tiene las siguientes partes:

  1. Evaluar los casos de uso y los diseños correspondientes
     realizados por cada uno de los miembros del equipo en la práctica
     individual. A partir de este material, crear un único conjunto de
     casos de uso y el diseño correspondiente de la interface de la
     aplicación que estáis desarrollando. Añadir el diseño a este
     repositorio en un fichero _PDF_ con el nombre `diseño-iu.pdf`

  2. Seleccionar un patrón arquitectónico para gestionar el estado de
     la aplicación de manera que el componente de la _vista_ sea
     independiente del _estado/modelo_.
	 
  3. Realizar un diseño software siguiendo el patrón seleccionado.
  
	  - El diseño tiene que cubir los casos de uso de la aplicación.
	  
	  - El diseño se realiza usando el lenguaje _UML_ y debe incluir
        diagramas tanto para la parte estática como para la dinámica.
		
	  - La documentación del diseño se incorpora al fichero
        `diseño_sw.md` de este repositorio. El formato del fichero es
        la versión de _markdown_ [Github Flavored Markdown](https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax). Los
        diagramas UML se integran directamente en el fichero markdow
        usando [_Mermaid_](https://github.blog/2022-02-14-include-diagrams-markdown-files-mermaid/)
		
  4. Implementar la aplicación siguiendo el diseño de la interface y
     el diseño software creados anteriormente.
	 
	   - El lenguaje de programación es python.
	   
	   - La librería gráfica es GTK, preferiblemente versión 4.
	   
	   - La estructura de módulos debe facilitar en lo posible el
         seguimiento del diseño sw. Se recomienda que, al menos, los
         componentes _vista_ y _estado/modelo_ esten en módulos o
         paquetes separados.
	   
	   - El servidor está disponible en el [repositorio del
         servidor](https://github.com/nbarreira/medications-backend).

### :books: Objetivos de aprendizaje:

  - Patrones arquitectónicos en IGUs.
  
  - Uso de librerías para construir IGUs.
  
  - Progamación dirigida por eventos


</details>


<details id=2>
<summary><h2>Tarea 2: Gestión de la concurrencia y la E/S en IGUs</h2></summary>

### :wrench: Esta tarea tiene las siguientes partes:

  1. Identificar las operaciones que pueden resultar erroneas y
     modificar la aplicación para gestionar esos errores e informar a
     la usuaria.
	 
	 > **TIP:** Muy probablemente son las peticiones al servidor.
	 
  2. Identificar las operaciones de E/S que pueden bloquear la
     interface e implementar una gestión concurrente de las mismas.
	 
	 > **TIP:** Siguen siendo las peticiones al servidor.
	 
> :warning: Estos cambios en la implementación deben ir acompañados
> del cambio correspondiente en el diseño sw y también podría ser
> necesario un cambio en el diseño de la interface gráfica de usuaria
> (_IGU_).


### :books: Objetivos de aprendizaje:

  - Naturaleza concurrente de las interfaces.
  
  - Uso de la concurrencia.
  
  - Gestión de errores en la E/S.
  
</details>



<details id=3>
<summary><h2>Tarea 3: Internacionalización</h2></summary>

### :wrench: Esta tarea tiene las siguientes partes:

  1. Internacionalizar la interface de usuaria para que se adapte a la
     configuración del _locale_ de la usuaria.
	 
  2. Para demostrar la validez de la implementación, localizar la
     interface a un idioma distinto del original.
	 
  3. [Opcional] Iternacionalizar la aplicación para mostrar las
     cantidades en las las unidades correspondientes a la
     configuración de la usuaria.

> :warning: No te olvides de las fechas.


### :books: Objetivos de aprendizaje:

  - Internacionalización de IGUs.

</details>


<details id=X>
<summary><h2>Finish</h2></summary>

_Congratulations friend, you've completed this assignment!_

Una vez terminada la práctica no olvidéis revisar el contenido del
repositorio en Github y comprobar su correcto funcionamiento antes de
realizar la defensa.

</details>

