# Rúbricas

Las rúbricas nos ofrecen criterios y normas para la evaluación. A
continuación tenemos una serie de rúbricas relativas a distintos
aspectos y objetivos de aprendizaje de la práctica.

Por cada aspecto evaluable se presentan tres opciones, que en el orden
de aparición se corresponden con: mal, regular, bien.


## Diseño de la interfaz


La documentación incluye los casos de uso.

    | En el repositorio no existe ningún pdf que describa los casos de uso de la interfaz.
	
	| En el repositorio hay un pdf, pero no contiene todos los casos de uso
	| contemplados en la aplicación, o la descripción no se corresponde con el
	| el diseño de la interfaz.
	
	| En el repositorio hay un pdf que enumera y describe los casos de uso. Ya
	| sea un pdf individual o dentro del mismo pdf que contiene el diseño de la
	| interfaz.
	
	
Existe el diseño de la interfaz.

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
    | operaciones tienen más pasos de los necesarios, no se adapta a la configuración
    | del dispositivo, ...
    
    | El diseño es correcto, pero existen puntos donde mejorar la usabilidad.
    
    | El diseño es correcto y usable.


El diseño es adaptativo.

    | El diseño no se adapta de ninguna manera a la configuración del
    | dispositivo.

    | El diseño se adapta en cierta manera, pero o bien no considera todos las configuraciones
    | especificados en los requisitos.

    | El diseño se adapta a la configuración del dispositivo y existe
    | al menos un diseño específico para cada configuración requerida.


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

    | La interfaz no se crea con flutter.
    
    | No se usa flutter de manera convencional.
    
    | La interfaz se crea usando flutter de la manera prevista por la librería.


Cada widget cumple su función natural.

    | Existen widgets con un comportamiento anómalo o no adecuados para una
	| pantalla táctil. Por ejemplo botones muy pequeños y/o próximos entre sí.
    
    | Algunas funciones podrían ser realizadas por widgets más adecuados.
    
    | Todos los widgets cumplen su función habitual.
    

El layout se adapta a distintos tamaños de ventana, tamaños de fuente, ...

    | La interfaz no se adapta a la configuración del dispositivo.
    
    | La interfaz se adapta, pero no existe una diferenciación entre teléfonos,
	| tablets, relojes, ...
    
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
    | los problemas de derivados de la ejecución concurrente.
    
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


## Objetivo: testing

Existen pruebas end2end.

    | No se ha implementado ninguna prueba software de tipo end2end.
	
	| Existe alguna prueba, pero es _brittle_ y/o no funciona en todos los casos.
	
	| Existe pruebas end2end y son fiables.
	
	
Se prueban los casos de uso positivos.

    | No existen pruebas para ningún caso de uso de la aplicación.
    
	| Existen pruebas, pero no para todos los casos de uso en los que la aplicación
	| tiene el comportamiento esperado.
	
	| Existen pruebas para todos los casos de uso en los que la aplicación
	| tiene el comportamiento esperado.


Existen pruebas negativas.

    | No existen pruebas para las situaciones en que se produce un error.
	
	| Existen pruebas, pero no para todas las situaciones en los que se produce un
	| error durante la ejecución de la aplicación.
	
	| Existen pruebas para todas las situaciones en que se produce un error, ya sea
	| un error de E/S o un error de la usuaria.


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
