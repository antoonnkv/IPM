# Curso 24/25. Práctica 3. Interfaces gráficas para aplicaciones web

## Welcome :wave:

- **Who is this for**: Grupos de prácticas de la asignatura _IPM_.

- **What you'll learn**: Implementación de interfaces gráficas usando
  lenguajes propios de la Web. Diseño mobile-first, adaptativo y
  accesible.

- **What you'll build**: Construiréis una interfaz para aplicaciones
  web.

- **Prerequisites**: Asumimos que os resultan familiares el
  funcionamiento de una aplicación web y las herramientas básicas para
  desarrolladores web.

- **How long**: Este assigment está formado por tres pasos o
  _tareas_. La duración estimada de cada tarea es de una semana
  lectiva.


La práctica se engloba en el mismo sistema sanitario al que pertenecen
las aplicaciones desarrolladas en las prácticas anteriores.  Consiste
en el desarrollo de una aplicación web que permita al personal
sanitario consultar los informes de seguimiento de las personas
usuarias del sistema sanitario.

Los requisitos funcionales son los siguientes:

  - La aplicación permite obtener el informe asociado a una persona
    durante un período de tiempo.
	
  - Los informes incluyen información tanto de la medicación pautada
    como del registro de las tomas realizadas en el período de tiempo
    establecido.
	
  - El informe tiene que permitir identificar con el mínimo esfuerzo
    posible los errores y desviaciones de la posología asignada.
	
  - La aplicación permite consultar, al menos, los siguientes períodos
    de tiempo: el último mes, los últimos _n_ días o el período entre
    dos fechas establecidas por la usuaria.

Los requisitos no funcionales son los siguientes:

  - No se empleará ninguna librería ni framework.
  
  - Todo el código, html, css y javascript, debe seguir los estándares
    correspondientes. Este requisito no se cumple si los validadores
    correspondientes informan de algún error.
	
  - Los documentos html siguen los principios del _html semántico_.
  
  - Toda la aplicación sigue los máximos estándares de accesibilidad
    posibles.
	
  - La aplicación es _crossbrowser_. Para cumplir este requisito es
    suficiente comprobarlo en tres navegadores basados en motores de
    rendering distintos.
	
  - El diseño de la interfaz es adaptativo. En este requisito tenemos
    que tener en cuenta que hemos identificado que las futuras
    usuarias de la aplicación disponen, fundamentalmente, de tres
    tipos de dispositivos: teléfono inteligente, tablet y ordenador de
    sobremesa.

No son requisitos funcionales de la aplicación:

  - Autenticación de la usuaria.

	

<details id=1>
<summary><h2>Tarea 1: Implementar la interfaz</h2></summary>

En este ejercicio implementaras únicamente la parte correspondiente a
la interfaz. No debes implementar ningún tipo de funcionalidad de la
aplicación. Los datos mostrados en el informe son estáticos y forman
parte del documento.

### :wrench: Esta tarea tiene las siguientes partes:

  1. Identifica y documenta los casos de uso necesarios para cubrir
     los requisitos de la aplicación. Añade al repositorio un fichero
     _PDF_ con el nombre `casos-de-uso.pdf` donde se recopilen los
     casos de uso identificados.
  
  2. Diseña la interfaz de la aplicación siguiendo estas pautas:

	 - La interfaz tiene que cubrir los casos de uso planteados en la
       descripción de la práctica.

     - El diseño tiene que estar dirigido únicamente a dispositivos
       móviles, en concreto a _smartphones_.

     - El diseño tiene que involucrar un único documento o página
       web.

  3. Añade al repositorio un fichero _PDF_ con el nombre
     `diseño-iu.pdf` donde se muestre el diseño que vas a implementar.

  4. Implementa el diseño empleando los lenguajes _html5_ y _css3_
     siguiendo las pautas del W3C:
	 
       - Usa html semántico.
	 
       - Separa el contenido (html5) de la presentación (css3).
	 
	   - La implementación debe seguir las normas de accesibilidad [WCAG
         2](https://www.w3.org/WAI/standards-guidelines/wcag/).

     Recuerda que no debes usar ninguna librería o framework CSS.
	   

### :books: Objetivos de aprendizaje:

  - Diseño _mobile-first_.
  
  - Uso de estándares web.
  
  - HTML semántico.
  
  - Accesibilidad web.
  
</details>


<details id=2>
<summary><h2>Tarea 2: Diseño adaptativo</h2></summary>

En esta tarea tienes que asegurarte de cumplir el requisito no
funcional _crossbrowser_: todas las características de los lenguajes
html5 y css3 que emplees hasta el final de la práctica están
disponibles en, al menos, tres navegadores basados en motores de
rendering distintos y en alguna versión anterior al comienzo del curso
académico actual.

### :wrench: Esta tarea tiene las siguientes partes:

  1. Extiende el diseño de la interfaz de manera que pueda mejorar
     paulatinamente adaptándose a la configuración del navegador web.
	 
	 Considera, al menos, los casos base típicos: _smartphone_,
     _tablet_, _desktop_.
	 
  2. Modifica la implementación de la tarea anterior de manera que la
     interfaz adapte el diseño a la configuración del navegador según
     el diseño elegido.
	 
	 La implementación debe seguir las mismas pautas del ejercicio
     anterior.
	 
  3. Comprueba que efectivamente todas las características de los
     lenguajes html y css cumplen el requisito _crossbrowser_ que
     hemos definido.
	 
	 
### :books: Objetivos de aprendizaje:

  - _Responsive design_.
  
  - Compatibilidad _cross-browser_.
  
</details>



<details id=3>
<summary><h2>Tarea 3: WAI-ARIA</h2></summary>

### :wrench: Esta tarea tiene las siguientes partes:

En esta tarea tienes que asegurarte de que tu implementación se 
ajuste a las normas de accesibilidad en aplicaciones Web
[WAI-ARIA](https://www.w3.org/WAI/standards-guidelines/aria/).
	 
  1. Para determinar las necesidades de la implementación ten en
     cuenta la lista de casos de uso. Antes de implementar ninguna
     funcionalidad, documenta las actualizaciones y cambios de estado
     por los que transita la interfaz y las reglas del WAI-ARIA
     pertinentes.
	 
  2. Implementa los casos de uso siguiendo los resultados del paso
     anterior.
	 
	 Para este paso no puedes utilizar ninguna librería de javascript,
     sólo _vanilla javascript_.
	 
	 
### :books: Objetivos de aprendizaje:

  - Accesibilidad en aplicaciones web.
  
  - Javascript y HTML dinámico.

</details>


<details id=X>
<summary><h2>Finish</h2></summary>

_Congratulations friend, you've completed this assignment!_

Una vez terminada la práctica no olvidéis revisar el contenido del
repositorio en Github y comprobar su correcto funcionamiento antes de
realizar la defensa.

</details>

