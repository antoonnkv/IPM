```mermaid
flowchart TD
    A[Buscador paciente] -->|Paciente encontrado| B(Datos paciente)
    A -->|Error al buscar| C(Ventana emergente error busqueda)
    C --> A
    B --> |Click en volver|A
    B --> |Boton de eliminar| D(Ventana emergente de confirmacion)
    D --> B
    B --> |Click en añadir medicamento|E(Añadir medicamento)
    B --> |Parámetro inválido o medicamento no seleccionado al confirmar|F(Ventana emergente error al modificar/Ver posologia)
    F --> B
    B --> |Click en ver posologias|G(Lista de posologías)
    G --> |Click en volver|B
    E --> |Medicamento añadido o click en volver|B
    E --> |Se intenta añadir un medicamento con parámetros no válidos|I(Ventana emergente error parámetros no válidos)
    I --> E
    G --> |No se ha seleccionado una posologia o los parámetros no son válidos al clickear confirmar|J(Ventana emergente error al modificar)
    J --> G
    G --> |Click en añadir posología|K(Añadir posología)
    K --> |Posología añadida o click en volver|G
    K --> |Parámetro inválido al añadir|L(Ventana emergente error parámetros no válidos)
    L --> K
    X(Ventana cualquiera) --> |Error de conexion con la base de datos al realizar una accion|Z(Ventana emergente error de conexión)
    Z --> X
