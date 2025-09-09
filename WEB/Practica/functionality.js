const URL = "http://localhost:8000";

///////////// EXCEPCIÓN DE LA BASE DE DATOS Y OBJETO GENÉRICO DE LA BD /////////////

class ModelException {
    constructor(message) {this.message = message;}
}
  
class dbItem {
    constructor(data) {this.data = data;}
}



///////////// OBJETOS CON LOS QUE TRABAJAN LAS FUNCIONES /////////////
  
class Patient{
    constructor(db) {
        this.id = db.data['id'];
        this.name = db.data['name'];
    }
}
  
class Medication{
    constructor(db) {
        this.id = db.data['id'];
        this.name = db.data['name'];
        this.dosage = db.data['dosage'];
        this.date = db.data['start_date'];
        this.duration = db.data['treatment_duration'];
    }
}
  
class Posology{
    constructor(db) {
        this.hour = db.data['hour'];
        this.minute = db.data['minute'];
    }
}
  
class Intake{
    constructor(db) {this.date = db.data['date'];}
}
  
class MedicationToday{
    constructor(med, intake, desv, date) {
        this.med = med;
        this.intake = intake;
        this.desv = desv;
        this.date = date;
    }
}



///////////// FUNCIONES GENERICAS DE OBTENCION DE DATOS DE LA BD /////////////

async function getData(endpoint, ID, ClassType, errorMsg) {
    try {
        let url = URL + endpoint.replace(":ID1", ID);
        let response = await fetch(url);
        if (!response.ok) {
            displayError("Error de servidor: " + errorMsg);
            throw new ModelException("Error obteniendo: " + errorMsg);
        }
        let data = await response.json();
        if (data === null || data === undefined) {
            displayError("Datos no válidos: " + errorMsg);
            throw new ModelException("Error obteniendo: " + errorMsg);
        }
        return new ClassType(new dbItem(data));
    } catch (error) {
        if (error instanceof ModelException) throw error;
        displayError("Error inesperado: " + errorMsg);
        throw new ModelException("Error inesperado al obtener: " + errorMsg);
    }
}

async function getDataList(endpoint, ID1, ID2, ClassType, errorMsg) {
    let itemList = [];
    try {
        let url = URL + endpoint.replace(":ID1", ID1).replace(":ID2", ID2 || '');
        let response = await fetch(url);
        if (!response.ok) {
            displayError("Error de servidor: " + errorMsg);
            throw new ModelException(errorMsg);
        }

        let data = await response.json();
        for (let item of data) itemList.push(new ClassType(new dbItem(item)));
        return itemList;
    } catch (error) {
        if (error instanceof ModelException) throw error;
        displayError("Error inesperado: " + errorMsg);
        throw new ModelException("Error inesperado.");
    }
}



///////////// FUNCIONES DE OBTENCION DE DATOS LEGIBLES DE LA BASE DE DATOS /////////////

async function getPatient(ID) {
    return await getData("/patients?code=:ID1", ID, Patient, "paciente");
}

async function getMedications(ID) {
    return await getDataList("/patients/:ID1/medications", ID, null, Medication, "Error obteniendo medicaciones del paciente");
}

async function getIntakes(patID, medID) {
    return await getDataList("/patients/:ID1/medications/:ID2/intakes", patID, medID, Intake, "Error obteniendo tomas del medicamento");
}

async function getPosologies(patID, medID) {
    return await getDataList("/patients/:ID1/medications/:ID2/posologies", patID, medID, Posology, "Error obteniendo posologias del medicamento");
}



///////////// FUNCIONES AUXILIARES /////////////

function isOnInterval(dateS1, dateE1, dateS2, dateE2) {   
    return((dateS2 <= dateE1 && dateE2 >= dateS1) || (dateS1 <= dateE2 && dateE1 >= dateS2));
}

function calculateDesviation(date, theoricalDates) {
    const parsedDate = new Date(date.date);
    const intakeHours = parsedDate.getHours();
    const intakeMinutes = parsedDate.getMinutes();
    const intakeTimeInMinutes = intakeHours * 60 + intakeMinutes;
    
    let min = Infinity;
    let posology = null;
    
    for (const time of theoricalDates) {
        let theoricalTime = time.hour * 60 + (time.minute - 60);
        if (theoricalTime > intakeTimeInMinutes) theoricalTime -= 24 * 60;
        let difference = intakeTimeInMinutes - theoricalTime;
        if (Math.abs(difference) < min) {
            min = Math.abs(difference);
            posology = time;
        }
    }
    return posology;
}



///////////// OPERACIONES CON DATOS DE LA BASE DE DATOS /////////////

async function getActiveMedications(ID, startDate, endDate) {
    let actvMedList = [];
    let medList = await getMedications(ID);
    for (const med of medList){
        let medStartDate = new Date(med.date);
        let medEndDate = new Date(medStartDate);
        medEndDate.setDate(medEndDate.getDate() + med.duration);
        if (isOnInterval(new Date(startDate), new Date(endDate), medStartDate, medEndDate))actvMedList.push(med);
    }
    return actvMedList;
}

async function getDayIntakes(date, ID, idMed) {
    let intakes = await getIntakes(ID, idMed);
    let intksToday = [];
    let intkDate;
    for (const item of intakes) {
        intkDate = new Date(item.date);
        if (intkDate.toISOString().split('T')[0] == date.toISOString().split('T')[0]) intksToday.push(item);
    }
    return intksToday;  
}     

async function getIntakesToday(ID, startDate, endDate) {
    let medsTdy = [];
    let medList = await getActiveMedications(ID, startDate, endDate);
    let startDateObj = new Date(startDate);
    let endDateObj = new Date(endDate);
    let posologies = [];
    let intks = [];
    let medStartDate;
    let medEndDate;
    let taken;
    let auxDate;
    let dailyIntakes;
    let numPosologies;
    for (const med of medList) {
        posologies = await getPosologies(ID, med.id);
        medStartDate = new Date(med.date);
        medEndDate = new Date();
        medEndDate.setDate(medStartDate.getDate() + med.duration); 

        for (let date = new Date(startDateObj); date <= endDateObj; date.setDate(date.getDate() + 1)) {
            if(date < medStartDate || date > medEndDate) continue;
            intks = await getDayIntakes(date, ID, med.id);
            numPosologies = posologies.length;
            dailyIntakes = intks.length;
            if(dailyIntakes == 0) {
                for (const pos of posologies){
                    auxDate = new Date(date);
                    auxDate.setHours(pos.hour);
                    auxDate.setMinutes(pos.minute);
                    medsTdy.push(new MedicationToday(med, -1, pos, auxDate));
                }
                continue;
            }
            
            for (const pos of posologies) {
                taken = false;
                auxDate = new Date(date);
                auxDate.setHours(pos.hour);
                auxDate.setMinutes(pos.minute);
                for (const intk of intks) {
                    if (taken) continue;
                    if (pos == calculateDesviation(intk, posologies)) {
                        taken = true;
                        medsTdy.push(new MedicationToday(med, intk, pos, auxDate));
                    }
                }
                if(!taken) medsTdy.push(new MedicationToday(med, -1, pos, auxDate));
            }
        } 
    }

    medsTdy.sort((a, b) => a.date - b.date);
    return medsTdy;
}



///////////// FUNCIONES AUXILIARES /////////////

function buildMedication(medication,medicationl) {
    const medicationName = document.createElement("h3");
    medicationName.style.margin = "0";

    const medicationNameContent = document.createTextNode(medication.name);
    medicationName.appendChild(medicationNameContent);
  
    const medicationInfo = document.createElement("p");
    const medicationInfoContent = document.createTextNode(`Duración: ${medication.duration} días`);
    const dosageContent = document.createTextNode(`Dosis: ${medication.dosage} g`);
    const lineBreak = document.createElement("br");
    medicationInfo.appendChild(medicationInfoContent);
    medicationInfo.appendChild(lineBreak);
    medicationInfo.appendChild(dosageContent);

    medicationl.appendChild(medicationName);
    medicationl.appendChild(medicationInfo);
    
    return medicationl;
}

function buildIntake(intake,intakel) {
    const medicationName = document.createElement("h3");
    medicationName.style.margin = "0";

    const medicationNameContent = document.createTextNode(intake.med.name);
    medicationName.appendChild(medicationNameContent);
  
    const medicationInfo = document.createElement("p");

    
    const day = intake.date.getDate().toString().padStart(2, "0");
    const month = (intake.date.getMonth() + 1 ).toString().padStart(2, "0");
    const year = intake.date.getFullYear().toString();
    const intakeDateMonth = document.createTextNode(`Fecha: ${day}/${month}/${year}`);
    const intakeNotTakenTxt = document.createTextNode(`TOMA NO REALIZADA`);
    
    const posHours = intake.desv.hour.toString().padStart(2, "0");
    const posMins = intake.desv.minute.toString().padStart(2, "0");
    const theoreticalIntakeContent = document.createTextNode(`Hora teórica de toma: ${posHours}:${posMins}`);
    const lineBreak = document.createElement("br");
    const lineBreak2 = document.createElement("br");
    
    medicationInfo.appendChild(intakeDateMonth);
    medicationInfo.appendChild(lineBreak);
    
    if(intake.intake != -1) {
        const intkDate = new Date(intake.intake.date);
        const hours = intkDate.getHours().toString().padStart(2, "0");
        const minutes = intkDate.getMinutes().toString().padStart(2, "0");
        const actualIntakeContent = document.createTextNode(`Hora de toma: ${hours}:${minutes}`);
        medicationInfo.appendChild(actualIntakeContent);
    } else {
        medicationInfo.appendChild(intakeNotTakenTxt);
        medicationInfo.style.color = "red";
    }

    medicationInfo.appendChild(lineBreak2);
    medicationInfo.appendChild(theoreticalIntakeContent);

    intakel.appendChild(medicationName);
    intakel.appendChild(medicationInfo);
    
    return intakel;
}

function buildEmpty(obj, iteml) {
    const emptyStr = document.createElement("h3");
    emptyStr.style.margin = "0";
    const descStr = document.createElement("p");
    descStr.style.margin = "0";
    
    const emptyStrContent = document.createTextNode("Esta lista está vacía.");
    const descStrContent = document.createTextNode("Ningún elemento a mostrar.");
    emptyStr.appendChild(emptyStrContent);
    descStr.appendChild(descStrContent);
    
    iteml.appendChild(emptyStr);
    iteml.appendChild(descStr);
    
    return iteml;
}

function addElementToList(obj, lst, buildFoo) {
    const list = document.getElementById(lst);
    const iteml = document.createElement("li");
    iteml.setAttribute("tabindex","0");
    list.appendChild(buildFoo(obj, iteml));
}

function loadDate() {
    const startDate = document.getElementById("fechaInicio");
    const endDate = document.getElementById("fechaFin");
    const today = new Date().toISOString().split("T")[0];
    fechaInicio.value = today;
    fechaFin.value = today
}

function loadLists() {
    addElementToList(null, "medicacionesActivas", buildEmpty);
    addElementToList(null, "tomasActivas", buildEmpty);
}

function clearList(listId) {
    const list = document.getElementById(listId);
    const items = list.getElementsByTagName("li");
    Array.from(items).forEach((item) => item.remove());
}

function calcDate(n) {
    const today = new Date();
    return new Date(today.setDate(today.getDate() - n));
}

function setDate(date, id) {
    const settedDate = document.getElementById(id);
    settedDate.value = date.toISOString().split("T")[0];
}

async function addList(list, addFoo, getFoo, startDate, endDate, patient) {
    const items = await getFoo(patient.id, startDate, endDate);
    clearList(list);
    if(items.length == 0) {
        addElementToList(null, list, buildEmpty);
        return;
    }
    for (const item of items) addElementToList(item, list, addFoo);
}



///////////// FUNCIONES DE CARGA DE LA PAGINA Y FUNCIONALIDAD /////////////

if(document.addEventListener)
    window.addEventListener("load", loaded);
else if(document.attachEvent)
    window.attachEvent("onload", loaded);

function loaded() {
    loadDate();
    loadLists();
    
    const listLoaderButton = document.getElementById("confirmar"); 
    const dateSetter1 = document.getElementById("NBut");
    const dateSetter2 = document.getElementById("30dBut");
    const dateSetter3 = document.getElementById("today");
    const dateSetter4 = document.getElementById("7dBut");
    const dateSetter5 = document.getElementById("365dBut");

    if(document.addEventListener) {
      listLoaderButton.addEventListener("click", loadActiveMeds);
      dateSetter2.addEventListener("click", setDateIntervalFor30d);
      dateSetter1.addEventListener("click", setDateIntervalForN);
      dateSetter3.addEventListener("click", setDateIntervalForToday);
      dateSetter4.addEventListener("click", setDateIntervalFor7D);
      dateSetter5.addEventListener("click", setDateIntervalFor1Y);
    }
    else if(document.attachEvent) {
      listLoaderButton.attachEvent("onclick", loadActiveMeds);
      dateSetter2.attachEvent("click", setDateIntervalFor30d);
      dateSetter1.attachEvent("onclick", setDateIntervalForN);
      dateSetter3.attachEvent("onclick", setDateIntervalForToday);
      dateSetter4.attachEvent("onclick", setDateIntervalFor7D);
      dateSetter5.attachEvent("onclick", setDateIntervalFor1Y);
    }
}



///////////// FUNCIONES DE LA PAGINA /////////////

function displayError(message) {
  const errorContainer = document.getElementById('errorMessages');
  errorContainer.setAttribute("aria-label",message);
  if (errorContainer) {
    errorContainer.textContent = message;
   
    errorContainer.style.display = 'block';
  } else {
    console.error('Error container not found:', message);
  }
}

async function loadActiveMeds() {
  const patientId = document.getElementById("bLogin");
  const startDate = document.getElementById("fechaInicio");
  const endDate = document.getElementById("fechaFin");

  

  if (!patientId.value) {
    displayError("Por favor, ingrese un código de paciente válido.");
    document.getElementById('bLogin').focus();
    return;
  }

  if (new Date(startDate.value) > new Date(endDate.value)) {
    displayError("La fecha de inicio no puede ser posterior a la fecha de fin.");
    document.getElementById('fechaInicio').focus();
    return;
  }

  try {
    const patient = await getPatient(patientId.value);
    await addList("medicacionesActivas", buildMedication, getActiveMedications, startDate.value, endDate.value, patient);
    await addList("tomasActivas", buildIntake, getIntakesToday, startDate.value, endDate.value, patient);
    document.getElementById('errorMessages').style.display = 'none';
    document.getElementById('notificacionFechas').style.display = 'none';
    document.getElementById('idLista1').focus();
    
  } catch (error) {
    displayError("Error al cargar los datos del paciente: " + error.message);
  }
}

function setDateIntervalFor30d() {
    const botonEstablecer = document.getElementById("30dBut");
    setDate(new Date(), "fechaFin");
    setDate(calcDate(30), "fechaInicio");
    displayNotificacion("Notificación: Se han establecido las fechas correctamente" );
    botonEstablecer.setAttribute("aria-flowto","fechaInicio");
   
}

function setDateIntervalForToday() {
    
    const botonEstablecer = document.getElementById("today");
    setDate(new Date(), "fechaFin");
    setDate(new Date(), "fechaInicio");
    //una vez pulsado que salte al formulario de fecha
    botonEstablecer.setAttribute("aria-flowto","fechaInicio");
    displayNotificacion("Notificacion: Se han establecido las fechas correctamente" );
   
    //una vez pulsado que salte al formulario de fecha
}

function setDateIntervalForN() {
  const n = document.getElementById("ndias").value;
  const botonEstablecer = document.getElementById("NBut");

  if (isNaN(n) || n <= 0) {
    displayError("Por favor, ingrese un número válido de días.");
    document.getElementById('ndias').focus();
    document.getElementById('notificacionFechas').style.display = 'none';
    return;
  }
  setDate(calcDate(n), "fechaInicio");
  setDate(new Date(), "fechaFin");
  document.getElementById('errorMessages').style.display = 'none';
  //una vez pulsado que salte al formulario de fecha
  displayNotificacion("Notificacion: Se han establecido las fechas correctamente" );
   
  
}

function setDateIntervalFor7D() {
    const botonEstablecer = document.getElementById("7dBut");
    

    setDate(new Date(), "fechaFin");
    setDate(calcDate(7), "fechaInicio");
    //una vez pulsado que salte al formulario de fecha
    displayNotificacion("Notificacion: Se han establecido las fechas correctamente" );
    
}

function setDateIntervalFor1Y() {
    const botonEstablecer = document.getElementById("365dBut");

    setDate(new Date(), "fechaFin");
    setDate(calcDate(365), "fechaInicio");
    //una vez pulsado que salte al formulario de fecha
    displayNotificacion("Notificacion: Se han establecido las fechas correctamente" );
   
    botonEstablecer.setAttribute("aria-flowto","fechaInicio");
}


function displayNotificacion(message) {
    const notifContainer = document.getElementById("notificacionFechas");
    notifContainer.setAttribute("aria-label",message);
    if (notifContainer) {
        notifContainer.textContent = message;
     
        notifContainer.style.display = 'block';
    } else {
      console.error('Notificacion container not found:', message);
    }
  }