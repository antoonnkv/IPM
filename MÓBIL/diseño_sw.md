# Diseño software
## Patrón Provider

<!-- ## Notas para el desarrollo de este documento
En este fichero debeis documentar el diseño software de la práctica.

> :warning: El diseño en un elemento "vivo". No olvideis actualizarlo
> a medida que cambia durante la realización de la práctica.

> :warning: Recordad que el diseño debe separar _vista_ y
> _estado/modelo_.
	 

El lenguaje de modelado es UML y debeis usar Mermaid para incluir los
diagramas dentro de este documento. Por ejemplo:

```mermaid
classDiagram
    class Model {
	}
	class View {
	}
	View ..> Gtk : << uses >>
	class Gtk
	<<package>> Gtk
```
-->

#### Diagrama parte estática (para móvil y reloj):
```mermaid
classDiagram

Model <.. _InicioState: << Listener >>
Model <.. _Pagina2State: << Listener >>
Model <.. ListaCompletaMedicamentos: << Listener >>
Model <.. _marcarMedState: << Listener >>
Model <.. _CheckState: << Listener >>

Model <.. _InicioStateReloj: << Listener >>
Model <.. _marcarMedStateReloj: << Listener >>
Model <.. ListaCompletaMedicamentosActivosReloj: << Listener >>
Model <.. _CheckStateReloj: << Listener >>

MedicationToday <-- Check  
_CheckState --o Check
_marcarMedState --o MarcarMed
_Pagina2State --o Pagina2 
_InicioState --o Inicio 

_InicioStateReloj --o LoginReloj
_marcarMedStateReloj --o MarcarMedReloj
_CheckStateReloj --o Check

Model --> dbItem
Model --> Patient
Model --> Medication
Model --> Posology
Model --> Intake
Model --> MedicationToday


ChangeNotifier <|-- Model

class MyApp  {
  maxDimension: double = 400.0 
  +build(context: BuildContext ): Widget
}


class ModelException{
  message: String 
  << constructor >>+ModelException(this.message: String)
}

class dbItem {
  data: Map<String, dynamic>
  << constructor >>+dbItem(this.data)
}

class Patient{
  id: int 
  name: String
  << constructor >>+Patient(db: dbItem)
}

class Medication{
  id: int
  name: String
  dosage: double
  start_date: String
  duration: int
  << constructor >>+Medication(db: dbItem)
}

class Posology{
  hour: int 
  minute: int
  << constructor >>+Posology(db: dbItem )
}


class Intake{
  date: DateTime ;
  << constructor >>+Intake(db: dbItem) 
}

class MedicationToday{
  med: Medication
  time: DateTime
  taken: boolean
  << constructor >>+MedicationToday(med1: Medication, taken1: bool, time1: DateTime)
}

class Model {
  _pat: Patient
  _intk: List<Intake>
  _pos: List<Posology>
  _medListToday: List<MedicationToday>
  _medList: List<Medication>
  _activeMedList: List<Medication>
  _notActiveMedList: List<Medication> 
  _dataSeleccionada: DateTime
  _semanas: List<DateTime> 

  +getPatient(patientId: String) async

  +getPatient1() async 

  +getMedList() async 
   
  +getPosList(medID: int) async 

  +getIntakeList(medID: int) async 


  +getMedicationsToday(date: DateTime) async 


  +getActiveMedications()

  +addIntake(medId: int, date: DateTime) async

  +actualizarSemanas() 

  +seleccionarData(date: DateTime ) async 

  +retrocederSemanas() async 

  +avanzarSemanas() async 

  +initHomepage() async 
}

class Inicio {
  +createState(): _InicioState 
}

class _InicioState {
  _controller: TextEditingController= TextEditingController() 
  _patientCode: String 

  +dispose():void 
  +build(context: BuildContext) Widget 

  +cuerpo(context: BuildContext) Widget


  +NombreApk1() Widget

  +NombreApk2() Widget 

  +CodigoPaciente() Widget 

  +botonLogin(context: BuildContext) Widget 
    
}

class Pagina2 {
  +createState() _Pagina2State
}

class _Pagina2State{
  _pagAct: int
  +build(context: BuildContext) Widget
  +_showDialog(context: BuildContext) void  
}



class ListaCompletaMedicamentos {
 
  +build(context: BuildContext) Widget 
    
}

class MarcarMed {

  +createState(): _marcarMedState 
}

class _marcarMedState{ 
  +initState(): void  
  +formatDate(date: DateTime): String 
  +build(context: BuildContext ): Widget   
  +calendario(): Widget 

}

class Check  {
  med: MedicationToday 
  today: DateTime 
  << constructor >>+Check()
  +createState(): _CheckState 
}

class _CheckState {
  +initState(): void
  +_mostrarDetallesMed(context: BuildContext, medt: MedicationToday) void  
  +_confirmarToma(context: BuildContext ) void
  +build(context:BuildContext) Widget 
}

class ListaCompletaMedicamentosActivosReloj {

   +build(context: BuildContext) Widget
   }


class LoginReloj  {
 
   +createState() _InicioState
}

class _InicioStateReloj  {
   _controller:  TextEditingController = TextEditingController();
   _patientCode: String
 
   +dispose() void 
   +build(context: BuildContext) Widget
   +cuerpo(context: BuildContext) Widget
  +NombreApk1() Widget
  +NombreApk2() Widget 
  +CodigoPaciente() Widget 
  +botonLogin(context: BuildContext) Widget
  
}
class MarcarMedReloj  {
  
   +createState()_marcarMedState
}

class _marcarMedStateReloj {

  
 +initState() void  
  +formatDate(date: DateTime) String 
  +build(context: BuildContext ) Widget   
  +calendario() Widget 
}

class _CheckStateReloj{
    +initState(): void
  +_mostrarDetallesMed(context: BuildContext, medt: MedicationToday) void  
  +_confirmarToma(context: BuildContext ) void
  +build(context:BuildContext) Widget 
}

```
### Diseño software para Teléfono inteligente
#### Diagramas parte dinámica:
- Diagrama dinámico que ejemplifica como se accede al calendario con las tomas diarias, se avanza semana y después se accede al histórico que contiene el listado genérico de medicamentos recetados, tras esto se deja de usar la aplicación.

```mermaid

sequenceDiagram
  Actor Customer as User

  Customer ->> MyApp:1.build()
  activate Customer
  activate MyApp
  MyApp ->> Inicio: 2.Inicio()
  activate Inicio
  
  Inicio ->> Inicio: 3.createState()
  Inicio ->> _InicioState:4._InicioState()
  deactivate Inicio
  activate _InicioState
  _InicioState ->> _InicioState:5.build()
  

  Customer ->> _InicioState: 6. Intro Código Paciente + click Login
  _InicioState ->> Model: 7.getPatient(codP)
  activate Model
  Model ->> Model :8.notifyListeners()
  Model -->> _InicioState:9.
  _InicioState ->> Model :10.getMedList()
  Model -->> _InicioState:11.
  _InicioState ->> Model :12.initHomePage()
  Model ->> Model :13.notifyListeners()
  Model ->> Model :14.actualizarSemanas()
  Model ->> Model :15.getMedicationsToday()
  Model -->> _InicioState:16.
  _InicioState ->> Model :17.getActivatedMedication()
  Model -->> _InicioState:18.
  deactivate Model
  _InicioState ->> Pagina2:19.Pagina2()
  activate Pagina2
  deactivate _InicioState
  Pagina2 ->> Pagina2: 20. createState()
  Pagina2 ->> _Pagina2State: 21. _Pagina2State()
  activate _Pagina2State
  deactivate Pagina2
  _Pagina2State ->>  _Pagina2State:22.build()

  Customer ->>  _Pagina2State: 23. click en icono tomas
   _Pagina2State ->>MarcarMed: 24.MarcarMed()
   activate MarcarMed
   deactivate _Pagina2State
   MarcarMed ->> MarcarMed: 25.createState()
   MarcarMed ->> _marcarMedState: 26._marcarMedState()

   deactivate MarcarMed
   activate _marcarMedState
   _marcarMedState ->>_marcarMedState:27.build()
   _marcarMedState->>_marcarMedState:28.calendario()

   Customer ->> _marcarMedState:29.click flecha navegar por calendario
  _marcarMedState ->>Model:30.avanzarSemanas()
  deactivate _marcarMedState
  activate Model
  Model ->> Model : 31.actualizarSemanas()
  Model ->> Model : 32.getMedicationsToday(dateSel)
  Model ->> Model : 33.getPosList()
  Model ->> Model : 34.getInatkeList()
  Model ->> Model : 35.notifyListeners()
  Model -->> _marcarMedState: 36.
  deactivate Model
  activate _marcarMedState
  _marcarMedState ->> Check : 37.Check()
  deactivate _marcarMedState
  activate Check
  Check ->> Check:38.build()
  
  Customer ->>  Check: 39. click en icono Histórico
  
  Check -->> _Pagina2State:40.
  deactivate Check
  activate _Pagina2State
  _Pagina2State ->> ListaCompletaMedicamentos: 41.ListaCompletaMedicamentos()
  activate ListaCompletaMedicamentos
  deactivate _Pagina2State
  ListaCompletaMedicamentos ->> Model: 42.get medList
  activate Model
  Model -->> ListaCompletaMedicamentos:43.
   deactivate Model
   deactivate Customer
   ListaCompletaMedicamentos  -->> MyApp:44.
   deactivate ListaCompletaMedicamentos
   
   deactivate MyApp



```

- Diagrama dinámico que ejemplifica como se accede al calendario con las tomas diarias, se marca una toma como realizada y tras esto se accede al detalle de una de las   tomas, finalmente se deja de utilizar la aplicación.

```mermaid

sequenceDiagram
  Actor Customer as User

  Customer ->> MyApp:1.build()
  activate Customer
  activate MyApp
  MyApp ->> Inicio: 2.Inicio()
  activate Inicio
  
  Inicio ->> Inicio: 3.createState()
  Inicio ->> _InicioState:4._InicioState()
  deactivate Inicio
  activate _InicioState
  _InicioState ->> _InicioState:5.build()
  

  Customer ->> _InicioState: 6. Intro Código Paciente + click Login
  _InicioState ->> Model: 7.getPatient(codP)
  activate Model
  Model ->> Model :8.notifyListeners()
  Model -->> _InicioState:9.
  _InicioState ->> Model :10.getMedList()
  Model -->> _InicioState:11.
  _InicioState ->> Model :12.initHomePage()
  Model ->> Model :13.notifyListeners()
  Model ->> Model :14.actualizarSemanas()
  Model ->> Model :15.getMedicationsToday()
  Model -->> _InicioState:16.
  _InicioState ->> Model :17.getActivatedMedication()
  deactivate Model
  _InicioState ->> Pagina2:18.Pagina2()
  activate Pagina2
  deactivate _InicioState
  Pagina2 ->> Pagina2: 19. createState()
  Pagina2 ->> _Pagina2State: 20. _Pagina2State()
  activate _Pagina2State
  deactivate Pagina2
  _Pagina2State ->>  _Pagina2State:21.build()

  Customer ->>  _Pagina2State: 22. click en icono tomas
   _Pagina2State ->>MarcarMed: 23.MarcarMed()
   activate MarcarMed
   deactivate _Pagina2State
   MarcarMed ->> MarcarMed: 24.createState()
   MarcarMed ->> _marcarMedState: 25._marcarMedState()
   deactivate MarcarMed
   activate _marcarMedState
   _marcarMedState ->>_marcarMedState:26.build()
   _marcarMedState->>_marcarMedState:27.calendario()

   Customer ->> _marcarMedState:28.click fecha
   _marcarMedState ->>Model:29.seleccionarDatat()
   activate Model
   Model ->> Model : 30.getMedicationsToday()
   Model ->> Model : 31.getPosList()
   Model ->> Model : 32.getIntakeList()
   Model ->> Model : 33.notifyListeners()
   Model -->> _marcarMedState:34.
   deactivate Model
   _marcarMedState ->> Check:35.Check()
   activate Check
   deactivate _marcarMedState
   Check ->> Check :36.build()
   Customer ->>  Check:37. Click checkbox toma
   Check ->> Check:38._confirmarToma()
   Customer ->> Check:39. Confirmar
   Check ->> Check:40. setState()
   Check ->> Model:41. addIntake()
   activate Model
   Model -->> Check:42.
   deactivate Model
   Customer ->>  Check:43. Click en toma
   Check ->> Check:44._mostrarDetallesMed(context, medToday)
   Check ->> Check:45.showDialog()
   Customer ->> Check:46. Cerrar
   
   deactivate Customer
   Check  -->> MyApp:47.
   deactivate Check
   deactivate MyApp



```
-------------

### Diseño software para Reloj inteligente
#### Diagrama parte dinámica:

- Diagrama dinámico que ejemplifica como se accede al calendario con las tomas del día actual, se marca una toma como realizada, se consulta el detalle de una toma, se consulta el histórico y finalmente se deja de utilizar la aplicación.

```mermaid
sequenceDiagram
  Actor Customer as User

  Customer ->> MyApp:1.build()
  activate Customer
  activate MyApp
  MyApp ->> Inicio: 2.LoginReloj()
  activate Inicio
  
  Inicio ->> Inicio: 3.createState()
  Inicio ->> _InicioState:4._InicioState()
  deactivate Inicio
  activate _InicioState
  _InicioState ->> _InicioState:5.build()
  

  Customer ->> _InicioState: 6. Intro Código Paciente + click Login
  _InicioState ->> Model: 7.getPatient(codP)
  activate Model
  Model ->> Model :8.notifyListeners()
  Model -->> _InicioState:9.
  _InicioState ->> Model :10.getMedList()
  Model -->> _InicioState:11.
  _InicioState ->> Model :12.initHomePage()
  Model ->> Model :13.notifyListeners()
  Model ->> Model :14.actualizarSemanas()
  Model ->> Model :15.getMedicationsToday()
  Model -->> _InicioState:16.
  _InicioState ->> Model :17.getActivatedMedication()
  Model -->> _InicioState:18.
  deactivate Model
  _InicioState ->> MarcarMedReloj:19.MarcarMedReloj()
  activate MarcarMedReloj
  deactivate _InicioState
  MarcarMedReloj ->> MarcarMedReloj: 20. createState()
  MarcarMedReloj ->> _marcarMedState: 21. _marcarMedState()
  activate  _marcarMedState
  deactivate MarcarMedReloj
  _marcarMedState ->> _marcarMedState:22.build()
  

   _marcarMedState->>_marcarMedState:23.calendario()

   _marcarMedState ->> Check:24.Check()
   activate Check
   deactivate _marcarMedState
   Check ->> Check :25.build()
   Customer ->>  Check:26. Click checkbox toma
   Check ->> Check:27._confirmarToma()
   Customer ->> Check:28. Confirmar
   Check ->> Check:29. setState()
   Check ->> Model:30. addIntake()
   activate Model
   Model -->> Check:31.
   deactivate Model
   Customer ->>  Check:32. Click en toma
   
   Check ->> Check:33._mostrarDetallesMed(context, medToday)
   Check ->> Check:34.showDialog()
   Customer ->> Check:35. Cerrar

    Customer ->>  Check:36. Click en icono histórico
   Check ->> ListaCompletaMedicamentosActivos:37.ListaCompletaMedicamentosActivos
   activate ListaCompletaMedicamentosActivos
   deactivate Check
   ListaCompletaMedicamentosActivos ->> ListaCompletaMedicamentosActivos:38.build()
   
   ListaCompletaMedicamentosActivos -->> MyApp:39.
   
   deactivate ListaCompletaMedicamentosActivos
   
   
   
   deactivate MyApp
```
-------------



