# Diseño software. Patrón Modelo-Vista-Controlador.
## Diagramas UML
### Diagrama parte estática:

```mermaid
classDiagram

    MedicationsModel --o Presenter
    PosologyModel --o  Presenter
    PatientModel --o  Presenter
    
    Presenter <-- View
    Presenter -->View:handler
    
    ModelException <-- PatientModel
    
    Patient <-- PatientModel
    
    Posology <-- PosologyModel
    ModelException <-- PosologyModel
    Medication <-- MedicationsModel
    ModelException <-- MedicationsModel
    Presenter --> Patient
    
    
    class View{
    
      presenter: Presenter
      widget: Gtk.Box
      
      +__init__(self: View)
      +show_loading_window(self: View) Gtk.Dialog
      +confirmDel(self: View, arg: Any, id: int, listType)
      +conexionError(self: View, message: String,funcion,*args)
      +show_ok(self: View)
      +show_error(self: View, message: String)
      +mostrarBuscarPaciente(self: View,srt: String) Gtk.Box
      +datosPaciente(s,n,surn,cod,meds,medsID,medsDate,medsDuration,medsDose,idMED) Gtk.Box
      +añadirMedicamento(self: View) Gtk.Box
      +datosPosología(self,name,posologiesID,posologiesHour,posologiesMinutes,idPos) Gtk.Box
      +añadirPosologia(self: View) Gtk.Box
      
    }
    
    
    
    class Presenter{
    
      view: View
      window: Gtk.ApplicationWindow
      currentWindow: int
      model: PatienteModel
      model: MedicationsModel
      model: PosologyModel
      patient: Patient
      medication: Medication
      
      +__init__(self: Presenter, window: Gtk.ApplicationWindow)
      +is_valid_patient(self: Presenter, id: int) Patient
      +obtenerDatosMedicamentos(self: Presenter) List, List, List, List, List
      +obtenerDatosPosologia(self: Presenter) List, List, List, List
      +run_in_thread(self: Presenter, target:, args: Any, callbacK:Any)
      +thread_finished(self: Presenter, result:, loading_dialog: Gtk.Dialog, callbacK:)
      +screen_switcher(self: Presenter, arg: Any, id:int)
      +mostrarBuscarPaciente(self: Presenter)
      +datosPaciente(self: Presenter)
      +anadirMedicamento(self: Presenter)
      +confirmarAnadirMedicamento(self: Presenter, arg: Any)
      + go_to_error(self: Presenter, arg: Any, strn: String)
      +updateMed(self: Presenter, arg: Any)
      +delMed(self: Presenter, args: Tuple)
      +listaPosologias(self: Presenter, args: Tuple)
      +delPos(self: Presenter, args: Tuple)
      +showRowData(self: Presenter, args: Tuple )
      +showRowDataPos(self: Presenter,idMED: int, rowID: int)
      +anadirPosologia(self: Presenter)
      +confirmarAnadirPosologia(self: Presenter, args: Tuple)
      +updatePos(self: Presenter, args: Tuple)
      
    }
    
    class MainWindow{
   
      +__init__(self:MainWindow, *args:, **kwargs:)
      
    }
    
    class MyApp{
    
      +__init__(self: MyApp, **kwargs:)
      +do_activate(self: MyApp)
      
    }
    

    class MedicationsModel{
    
        +__init__ (self: MedicationModel)
        +search_medication(self: MedcationModel, inpt: String)
        +get_Medications(self: MedicationModel, indice1: int, count: int, idPaciente: int) List
        +get_Medication(self: MedicationModel, idPaciente: int, idMed:int) Medication:
        +delete_Medications(self: MedicationModel, idPaciente: int, idMed: int)
        +add_Medication(self:MedicationModel, patient_id: int, name: String, dosage: float, start_date: String, treatment_duration: int)
        +update_Medications(self:MedicationModel, patient_id: int, idMed: int, name: String, dosage: float, start_date: String, treatment_duration: int)
        
    }
    
    class PatientModel{
    
        +__init__(self: PatientModel)
        +get_patient(self: PatientModel, idPaciente: int) Patient
        
    }
    
    
    class PosologyModel{
    
        +__init__(self: PosologyModel)
        +get_Posology(self: PatientModel, indice1: int, count: int, idPaciente: int, idMedicamento: int) List
        +update_posology(self: PatientModel, idPaciente: int, idMed: int, idPos:int, hour: int, minute: int)
        +delete_posology(self: PatientModel, idPaciente: int, idMed: int, idPos:int)
        +add_posology(self: PatientModel, patient_id: int, medication_id: int, hour: int, minute: int)
    }
    
    
    class ModelException{
    
        +__init__(self: ModelException, msg: Sring)
        
    }
    
    class Patient{
    
        +__init__(self: Patient, data: Dictionary)
        
    }
    
    class Posology{
    
        +__init__(self: Posology, data: Dictionary)
        
    }
    
    class Medication{
    
        +__init__(self: Medication, data: Dictionary)
        
    }
   
   
```

### Diagramas parte dinámica:


#### Dar de alta Medicamento y modificar medicamento:

Diagrama dinámico que ejemplifica como se añade un medicamento a un paciente determinado, después se modifica un medicamento y tras esto se deja de usar la aplicación.

```mermaid
sequenceDiagram
  Actor Customer as User
  
  Customer ->> MyApp:1.do_activate()
  activate Customer
  activate MyApp
  MyApp ->> MainWindow: 2.__init__()
  
  activate MainWindow
  MainWindow ->> Presenter: 3.self.set_child(presenter.view.widget)
  activate Presenter
  Presenter->> View:4.mostrarBuscarPaciente()
  activate View
  View -->> Customer: 5.<devuelve pantalla con buscador>
  
  Customer ->> View: 6.click botón "BUSCAR"
  View->> Presenter:7.screenswitcher(2)
  Presenter ->> Presenter: 8.datosPaciente()
  Presenter ->> Presenter: 9.is_valid_patient()
  Presenter ->> Presenter: 10.obtenerDatosMedicamento()
  Presenter->> View: 11.datosPaciente()
  View -->>Customer:12.<actualiza pantalla>
  Customer->>View: 13.click botón "AÑADIR MEDICAMENTOS"
  View ->> Presenter:14.screen_switcher(3)
  Presenter ->> Presenter: 15.anadirMedicamento()
  Presenter->> View: 16.anadirMedicamento()
  View -->> Customer: 17.
  Customer->> View: 18.click botón"CONFIRMAR"
  View ->> Presenter:19.confirmarAnadirMedicamento
  Presenter->> MedicationsModel: 20.searchMedication()
  activate MedicationsModel
  MedicationsModel-->> Presenter:21.
  Presenter->> MedicationsModel: 22.addMedication()
  MedicationsModel-->> Presenter:23.
  Presenter ->> Presenter: 24.screenswitcher(self.currentWindow)
  Presenter->> View: 25.datosPaciente()
  View -->>Customer: 26.
  Customer->>View: 27.click botón"CONFIRMAR"
  View ->> Presenter:28.updatedMed
  deactivate View
  Presenter->> MedicationsModel: 29.updateMedication()
  MedicationsModel-->> Presenter:30.
  deactivate MedicationsModel
  Presenter-->> MainWindow:31.
  deactivate Presenter
  MainWindow-->>MyApp:32.
  deactivate MainWindow
  deactivate MyApp
  deactivate Customer
  
  Note right of MedicationsModel: CASO DE USO: Dar de alta Medicamento + modificar medicamento
  

```




#### Dar de baja Medicamento/Posología:

Diagrama dinámico que ejemplifica como se elimina un medicamento, se consultan las posologías de un medicamento, se elimina una y tras esto se deja de usar la aplicación.

```mermaid

sequenceDiagram
  Actor Customer as User
  
  Customer ->> MyApp:1.do_activate()
  activate Customer
  activate MyApp
  MyApp ->> MainWindow: 2.__init__()
  
  activate MainWindow
  MainWindow ->> Presenter: 3.self.set_child(presenter.view.widget)
  activate Presenter
  Presenter->> View:4.mostrarBuscarPaciente()
  activate View
  View -->> Customer: 5.<devuelve pantalla con buscador>
  Customer ->> View: 6.click botón "BUSCAR"
  View->> Presenter:7.screenswitcher(2)
  Presenter ->> Presenter: 8.datosPaciente()
  Presenter ->> Presenter: 9.is_valid_patient()
  Presenter ->> Presenter: 10.obtenerDatosMedicamento()
  Presenter->> View: 11.datosPaciente()
  View-->> Customer:12.<actualiza pantalla>
  Customer->>View: 13.Botón "ELIMINAR"
  View ->> View: 14.confirmDel()
  View-->> Customer:15.<actualiza pantalla>
  Customer->>View: 16.Botón "CONFIRMAR"
  View ->> View: 17.confirmdelPres()
  View->> Presenter:18.delMed(idM)
  Presenter ->> MedicationsModel: 19.delete_Medications(idP, idM)
  activate MedicationsModel
  MedicationsModel -->> Presenter:20.
  deactivate MedicationsModel
  Presenter ->> Presenter: 21.screenswitcher(currentWindow)
  Presenter->> View:22.datosPaciente()
  View-->> Customer:23.<actualiza pantalla>
  Customer->>View: 24.Botón "VER POSOLOGÍAS"
  View ->> Presenter:25.screen_switcher(4)
  Presenter ->> Presenter: 26.listaPosología()
  Presenter ->> Presenter: 27.obtenerDatosPosología()
  Presenter ->>PosologyModel: 28.get_Posology (indice1, count, idP, idM)
  activate PosologyModel
  PosologyModel -->>Presenter:29.idMed, hoursPos,minutePos, idPos (List, List, List, List)
  Presenter->> View: 30.datosPosología()
  View-->> Customer:31.<actualiza pantalla>
  Customer->>View: 32.Botón "ELIMINAR"
  View ->> View: 33.confirmDel()
  View-->> Customer:34.<actualiza pantalla>
  Customer->>View: 35.Botón "CONFIRMAR"
  View ->> View: 36.delete_confirm_presed()
  View->> Presenter:37.delPos(idPo)
  deactivate View
  Presenter ->> PosologyModel:38.delete_posology(idP, idM, idPos)
  PosologyModel-->> Presenter:39.
  Presenter ->> Presenter: 40.screenswitcher(currentWindow)
  Presenter ->> Presenter: 41.listaPosología()
  Presenter ->> Presenter: 42.obtenerDatosPosología()
  Presenter ->>PosologyModel: 43.get_Posology (indice1, count, idP, idM)
  PosologyModel -->>Presenter:44.idMed, hoursPos,minutePos, idPos (List, List, List, List)
  deactivate PosologyModel
  Presenter-->> MainWindow:45.
  deactivate Presenter
  MainWindow-->>MyApp:46.
  deactivate Customer
  deactivate MainWindow
  deactivate MyApp 
  
  Note right of PosologyModel: CASO DE USO: Dar de baja Medicamento + dar baja posología
  
```


#### Alta y modificación Posología:

Diagrama dinámico que ejemplifica como se consultan posologías de un medicamento, se añade una posología, se modifica una posología y finalmente se deja de usar la aplicación.

```mermaid
sequenceDiagram
  Actor Customer as User
  
  Customer ->> MyApp:1.do_activate()
  activate Customer
  activate MyApp
  MyApp ->> MainWindow: 2.__init__()
  
  activate MainWindow
  MainWindow ->> Presenter: 3.self.set_child(presenter.view.widget)
  activate Presenter
  Presenter->> View:4.mostrarBuscarPaciente()
  activate View
  View -->> Customer: 5.<devuelve ventana con buscador>
  
  Customer ->> View: 6.click botón "BUSCAR"
  View->> Presenter:7.screenswitcher(2)
   Presenter ->> Presenter: 8.datosPaciente()
  Presenter ->> Presenter: 9.is_valid_patient()
  Presenter ->> Presenter: 10.obtenerDatosMedicamento()
  Presenter->> View: 11.datosPaciente()
  View -->> Customer:12.<actualiza ventana>
  Customer ->> View: 13.click Botón "VER POSOLOGÍAS"
  View ->> Presenter:14.screen_switcher(4)
  Presenter ->> Presenter: 16.listaPosología()
  Presenter ->> Presenter: 17.obtenerDatosPosología()
  Presenter ->>PosologyModel: 18.get_Posology (indice1, count, idP, idM)
  activate PosologyModel
  PosologyModel -->>Presenter:19.idMed, hoursPos,minutePos, idPos (List, List, List, List)
  Presenter->> View: 20.datosPosología()
  View-->>Customer: 21.<actualiza ventana>
  Customer->>View: 22.click botón "AÑADIR POSOLOGÍA"
  View ->> Presenter: 23.screenswitcher(5)
  Presenter ->> Presenter: 24.anadirPosologia()
  Presenter->> View:25.anadirPosologia()
  View-->>Customer: 26.<actualiza ventana>
  Customer->>View: 27.click botón "CONFIMAR"
  View ->> Presenter:28.confirmarAnadirPosologia()
  Presenter->>PosologyModel:29.addPosology(idP, idM, hour, min)
  PosologyModel --> Presenter:30.
  Presenter->>Presenter: 31.screenswitcher(currentWindow) 
  Presenter ->> Presenter: 32.listaPosología()
  Presenter ->> Presenter: 33.obtenerDatosPosología()
  Presenter ->>PosologyModel: 34.get_Posology (indice1, count, idP, idM)
  PosologyModel -->>Presenter:35.idMed, hoursPos,minutePos, idPos (List, List, List, List)
  Presenter->> View: 36.datosPosología()
  View-->>Customer: 37.<actualiza ventana>
  Customer->>View: 38.click botón "CONFIRMAR"
  View ->> Presenter: 39.updatePos(idPo)
  deactivate View
  Presenter ->> PosologyModel: 40.update_posology(idP, idM, hour, min)
  PosologyModel -->>Presenter: 41.
  deactivate PosologyModel


  Presenter-->> MainWindow:42.
  deactivate Presenter
  MainWindow-->>MyApp:43.
  deactivate Customer
  deactivate MainWindow
  deactivate MyApp 
  
  Note right of PosologyModel: CASO DE USO: Dar de alta posología + modificar una posología
  

```

#### Dar de alta Medicamento y modificar medicamento con Concurrencia:

Diagrama dinámico que ejemplifica como se añade un medicamento a un paciente determinado, después se modifica un medicamento y tras esto se deja de usar la aplicación.
Teniendo en cuenta el comportamiento concurrente de la aplicación.

```mermaid
sequenceDiagram
  Actor Customer as User
  
  Customer ->> MyApp:1.do_activate()
  activate Customer
  activate MyApp
  MyApp ->> MainWindow: 2.__init__()
  
  activate MainWindow
  MainWindow ->> Presenter: 3.self.set_child(presenter.view.widget)
  activate Presenter
  Presenter->> View:4.mostrarBuscarPaciente()
  activate View
  View -->> Customer: 5.<devuelve pantalla con buscador>
  
  Customer ->> View: 6.click botón "BUSCAR"
  View->> Presenter:7.screenswitcher(2)
  Presenter ->> Presenter: 8.datosPaciente()
  Presenter ->> Presenter: 9.is_valid_patient()
  Presenter ->> Presenter: 10.obtenerDatosMedicamento()
  Presenter->> View: 11.datosPaciente()
  View -->>Customer:12.<actualiza pantalla>
  Customer->>View: 13.click botón "AÑADIR MEDICAMENTOS"
  View ->> Presenter:14.screen_switcher(3)
  Presenter ->> Presenter: 15.anadirMedicamento()
  Presenter->> View: 16.anadirMedicamento()
  View -->> Customer: 17.
  Customer->> View: 18.click botón"CONFIRMAR"
  View ->> Presenter:19.confirmarAnadirMedicamento
  Presenter->> MedicationsModel: 20.run_in_thread(searchMedication)
  activate MedicationsModel
  MedicationsModel-->> Presenter:21.
  Presenter->> MedicationsModel: 22.run_in_thread(addMedication)
  MedicationsModel-->> Presenter:23.
  Presenter ->> Presenter: 24.screenswitcher(self.currentWindow)
  Presenter->> View: 25.datosPaciente()
  View -->>Customer: 26.
  Customer->>View: 27.click botón"CONFIRMAR"
  View ->> Presenter:28.updatedMed
  deactivate View
  Presenter->> MedicationsModel: 29.run_in_thread(updateMedication)
  MedicationsModel-->> Presenter:30.
  deactivate MedicationsModel
  Presenter-->> MainWindow:31.
  deactivate Presenter
  MainWindow-->>MyApp:32.
  deactivate MainWindow
  deactivate MyApp
  deactivate Customer
  
  Note right of MedicationsModel: CASO DE USO: Dar de alta Medicamento + modificar medicamento con Concurrencia.
  

```

#### Intento de inicio con errores:

Diagrama dinámico que ejemplifica como se intenta entrar en la aplicación con un código incorrecto y después de corregirlo se produce un error de conexión del que 
se recupera y finaliza mostrando la pantalla de medicamentos del paciente. Para finalizar el ejemplo el usuario sale de la aplicación. 

```mermaid
sequenceDiagram
  Actor Customer as User
  
  Customer ->> MyApp:1.do_activate()
  activate Customer
  activate MyApp
  MyApp ->> MainWindow: 2.__init__()
  
  activate MainWindow
  MainWindow ->> Presenter: 3.self.set_child(presenter.view.widget)
  activate Presenter
  Presenter->> View:4.mostrarBuscarPaciente()
  activate View
  View -->> Customer: 5.<devuelve pantalla con buscador>
  
  Customer ->> View: 6.Intro código paciente INCORRECTO + click botón "BUSCAR"
  
  View->> Presenter:7.screenswitcher(2)
  Presenter ->> Presenter: 8.datosPaciente()
  Presenter ->> View:9.show_error()
  View -->> Customer: 10.<muestra dialogo de Error>
  Customer->> View: 11.click botón "CERRAR"
  View -->> Customer: 12.<devuelve pantalla con buscador>
  
  Customer ->> View: 13.Intro código paciente CORRECTO + click botón "BUSCAR"
  View->> Presenter:14.screenswitcher(2)
  Presenter ->> Presenter: 15.datosPaciente()
  Presenter ->> View: 16.conexionError()
  View -->Customer: 17.<dialogo de error de conexión>
  Presenter ->> Presenter:18. run_in_thread(fetch_medications_data)
  Customer->> View: 19.click botón "Recargar"
  View->> Presenter:20.screenswitcher(2)
  Presenter ->> Presenter: 21.datosPaciente()
  Presenter ->> Presenter: 22.is_valid_patient(entryID)
  Presenter ->> Presenter: 23.obtenerDatosMedicamentos()
  
  Presenter->> View: 24.datosPaciente()
  View -->>Customer:25.<actualiza pantalla>
  Customer ->> View: 26.cierra aplicación
  View -->> Presenter: 27.
  
  deactivate View
  
  Presenter-->> MainWindow:28.
  deactivate Presenter
  MainWindow-->>MyApp:29.
  deactivate MainWindow
  deactivate MyApp
  deactivate Customer
  
  
  

```



