# Rúbricas

Las rúbricas nos ofrecen criterios y normas para la evaluación. A
continuación tenemos una serie de rúbricas relativas a distintos
aspectos y objetivos de aprendizaje de la práctica.

Por cada aspecto evaluable se presentan tres opciones, que en el orden
de aparición se corresponden con: mal, regular, bien.

## Diseño de la interfaz


Existe el diseño de la interfase.

    | En el repositorio no hay ningún pdf que contenga el diseño de la interfaz.


    | En el repositorio hay un pdf, pero contiene un diseño incompleto.


    | En el repositorio hay un pdf y contiene el diseño completo de la interfaz.


El diseño de la interfaz cubre los casos de uso.

    | El diseño de la interfaz no cubre los casos de uso especificados
    | para la aplicación.

    | El diseño de la interfaz algunos casos de uso, pero no todos.

    | El diseño de la interfaz cubre todos los casos de uso.


El diseño de la interfaz incluye la retroalimentación cuando hay E/S.

    | El diseño de la interfaz no tiene en cuenta mensajes de error, tiempos
    | de espera largos, ...

    | El diseño de la interfaz sólo tiene en cuenta parte de la
    | retroalimentación necesaria, usa formatos poco convencionales o mensajes
    | demasiado técnicos o con jerga.
    
    | El diseño de la interfaz incluye una retroalimentación adecuada para
    | todas las situaciones anómalas o no deseadas.
    
    
    
Calidad del diseño de la interfaz.

    | El diseño es pobre, usa elementos en contra de las convenciones, las
    | operaciones tienen más pasos de los necesarios, no se adapta al tamaño
    | de la ventana, ...
    
    | El diseño es correcto, pero existen puntos donde mejorar la usabilidad.
    
    | El diseño es correcto y usable.


## Repositorio

Se ha realizado un control de versiones.

    | Existe un único commit o todos los commit se realizaron el mismo día.
    
    | El número de commits es escaso y/o no refleja las versiones en la
    | evolución del desarrollo.
    
    | Los commits del repositorio se corresponden con las versiones y los
    | tiempos del desarrollo.
    
    
Las contribuciones son equitativas.
    
    | Todos los commits tienen la autoría de la misma persona.
    
    | La cantidad de trabajo indicada por los commits no es similar para 
    | todos los miembros del equipo.
    
    | Los commits se corresponden con una contribución equilibrada de los
    | miembros del equipo.
    

## Objetivo: Patrones arquitectónicos en IGUs

Existe un diseño software.

    | El repositorio no contiene ningún .md con el diseño software de la
    | aplicación, o no se corresponde con la implementación.
    
    | Existe un .md en el repositorio, pero sólo contiene un parte del diseño
    | software, o el diseño no está actualizado con la última versión de la
    | aplicación, o no está escrito en el lenguaje de mermaid.
    
    | Existe un .md en el repositorio que contiene el diseño software de la
    | última versión de la aplicación: se corresponde con la implementación y
    | cubre todos los aspectos implementados.
    

El diseño sw sigue el estándar UML.

    | El diseño sw no sigue el lenguaje definido por el estándar UML.
    
    | El diseño sw hace un uso incorrecto de algunos elementos de UML.
    | :nota:  es habitual un uso incorrecto de los distintos tipos de flechas
    | y conexiones.
    
    | El diseño sw se ajusta a lo establecido en UML.
    
    
El diseño sw cubre la parte estática y dinámica.

    | El diseño sw no incluye alguna o ninguna de las dos partes:
    | estática, dinámica.
    
    | El diseño sw incluye las dos partes, pero no se corresponden entre sí.
    
    | El diseño sw está completo y ambas partes son correctas.
    
    
El diseño sw separa la interfaz.

    | No existe un único componente encargado en exclusiva de crear y
    | actualizar la interfaz.
    
    | Existe un componente cuya responsabilidad es la interfaz, pero 
    | asume otras responsabilidades, depende de otros componentes y/o
    | existen otros componentes implicados en el manejo de la interfaz.
    
    | Existe un único componente cuya responsabilidad es la interfaz y
    | es independiente del resto de componentes.


El diseño sw cubre la gestión de errores.

    | En el diseño sw, especialmente la parte dinámica, no se contempla
    | la gestión de errores.
    
    | El diseño sw contempla la gestión de algunos errores, pero no todos.
    
    | El diseño sw contempla la gestión de errores.
    

El diseño sw cubre el funcionamiento concurrente.

    | En el diseño sw, especialmente la parte dinámica, no se contempla
    | la ejecución concurrente de las operación de E/S.
    
    | El diseño sw contempla la ejecución concurrente, pero no está completo.
    
    | El diseño sw contempla la ejecución concurrente en su totalidad.
    

## Objetivo: Uso de librerías para construir IGUs

Se ha usado al librería indicada.

    | La interfaz no se crea con Gtk+.
    
    | No se usa Gtk+ de manera convencional.
    
    | La interfaz se crea usando Gtk+ de la manera prevista por la librería.


Cada widget cumple su función natural.

    | Existen widget con un comportamiento anómalo. Por ejemplo checks que
    | lanzan acciones o buttons que no lazan acciones.
    
    | Algunas funciones podrían ser realizadas por widget más adecuados.
    
    | Todos los widgets cumplen su función habitual.
    

El layout se adapta a distintos tamaños de ventana, tamaños de fuente, ...

    | La interfaz no se adapta al tamaño de la ventana y/o de las fuentes.
    | Algunos elementos pueden quedar ocultos para ciertos tamaños.
    
    | La interfaz se adapta, pero el resultado desde el punto de vista del
    | diseño gráfico no es correcto.
    
    | La interfaz se adapta siguiendo las pautas del diseño de la interfaz.
    

## Objetivo: Programación dirigida por eventos

El flujo de ejecución está determinado exclusivamente por los eventos de la interfaz.

     | La aplicación tiene un programación poco habitual que interfiere en el
     | orden natural de procesado de eventos.
     
     | La aplicación intenta controlar el orden en que la usuaria interactúa con
     | la interfaz. Por ejemplo: abuso de diálogos y formularios.
     
     | La aplicación procesa los eventos en el momento en que se producen y
     | la usuaria tiene libertad para interactuar con la interfaz.
     

## Objetivo: Naturaleza concurrente de la interfaz

Las operaciones de E/S se realizan de forma concurrente.

    | La E/S se realiza de forma secuencial, bloqueando el hilo de ejecución
    | principal.
    
    | La E/S se realiza de forma concurrente, pero no se tienen en cuenta
    | los problemas de reentrada en la librería.
    
    | La E/S se realiza de forma concurrente, usando los mecanismos adecuados
    | para reentrar en la librería.
    
    
Las operaciones de E/S tiene el feedback adecuado.

    | No existe feedback cuando se realizan las operaciones de E/S.
    
    | El feedback no es adecuado o no es completo.
    
    | El feedback incluye todos los aspectos propios de la E/S: informar de
    | la situación de espera durante la operación, y del resultado al finalizar.


## Objetivo: Gestión de los errores en la E/S

Se capturan los errores de E/S.

    | No se capturan los errores de E/S. En caso de error la aplicación
    | termina de forma abrupta o muestra un comportamiento anómalo.
    
    | Se capturan algunos errores de E/S, pero no todos.
    
    | Se capturan todos los errores de E/S y se realizan las acciones 
    | necesarias.
    

Se informa a la usuaria de los errores.

    | La usuaria no recibe feedback en caso de error.
    
    | Los mensajes de error no son descriptivos, son difíciles de comprender,
    | o usan lenguaje técnico y jerga propia de la ingeniería de sw.
    
    | Los mensajes describe el error en un lenguaje sencillo de comprender
    | por parte de la usuaria.
    

Se ofrecen opciones en caso de error.

    | La información de error nunca incluye posibles acciones para continuar.
    
    | Sólo se ofrecen alternativas para algunos errores.
    
    | Ante un error, cuando es posible, se ofrece a la usuaria alternativas
    | para atajar el error.


## Objetivo: i18n

El idioma de la interfaz esta internacionalizado.

    | La implementación no incluye los mecanismos necesarios para
    | internacionalizar el texto de la interfaz.
    
    | Parte del texto está internacionalizado, pero no todo.
    
    | La implementación incluye los mecanismos de internacionalización
    | necesarios y todo el texto de la interfaz está internacionalizado.
    

Existe una localización a más de un idioma.

    | La interfaz no está localizada a ningún idioma excepto el usado en
    | el propio código fuente.
    
    | La interfaz está localizada varios idiomas, pero la localización no
    | está actualizada a la última versión de la aplicación, o la aplicación
    | no se adapta a la configuración de la usuaria.
    
    | La interfaz está localizada a varios idiomas, la localización está
    | actualizada a la última versión de la aplicación y el texto de la
    | interfaz se muestra en el idioma definido en la configuración de
    | la usuaria.


Las unidades están internacionalizadas (opcional).

    | Las cantidades se muestran según las unidades originales de la B.D.
    
    | Algunas cantidades se muestran adaptadas a la configuración de la 
    | usuaria.
    
    | Todas las cantidades se muestran adaptadas a la configuración de la
    | usuaria.



## Objetivo: QA

El programa funciona sin errores.

    | El programa presenta errores de ejecución.
	
    | En determinadas ocasiones el programa presenta algún error de ejecución,
	| pero no provoca corrupción de datos, ni impide continuar la ejecución 
	| del mismo.
	
    | El programa se ejecuta en todos los casos, estados y configuraciones
	| sin ningún error.
	
	
	
El desarrollo del proyecto está completo.

	| No se ha entregado algún entregable y/o el programa no implementa todos
	| los casos de uso.

    | Se han entregado todos los entregables, pero alguno no es correcto y/o
	| el programa no implementa algún caso de uso de forma errónea.
	
    | Se han creado y entregado todos los entregables requeridos y el programa
	| implementa todos los casos de uso especificados.
	
