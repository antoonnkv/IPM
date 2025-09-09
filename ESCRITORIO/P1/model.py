import requests
import json, os

URL_DE_SERVIDOR="http://localhost:8000"  

class ModelException(Exception):
    def __init__(self, mensaje: str):
        super().__init__(mensaje)


#Clases paciente, medicacion, posología
#definimos las clases de forma que sean un atributo de un diccionario definidos por una clave y un valor (nos basamos en ejemplo proporcionado)
class Patient:
    def __init__(self, datos=None):
        if datos is not None:
            for clave, valor in datos.items():
                setattr(self, clave, valor)

class Medication:
    def __init__(self, data=None):
        if data is not None:
            for key, value in data.items():
                setattr(self, key, value)


class Posology:
    def __init__(self, data=None):
        if data is not None:
            for key, value in data.items():
                setattr(self, key, value)
                


#Clase donde definimos las funciones de modelo correspondiente a los Medicamentos
class MedicationsModel:
    #constructor
    def __init__(self): 
        pass

    #busca medicamento dentro de la base de datos json donde se encuentran todos los medicamentos
    def search_medication(self, inpt):  

        fichero = os.path.join(os.path.dirname(__file__), "Sources/medications.json")

        try:
            with open(fichero, 'r') as archivo:
                medicamentos = json.load(archivo)
        except FileNotFoundError: return None
        except json.JSONDecodeError: return None

        nombres = [medicamento['nombre'] for medicamento in medicamentos] #obtenermos lista de nombres de medicamentos

        #bucle que comprueba si hay coincidencia de nombre introducido (inpt) con algún nombre de medicamneto de bd
        for medicamento in nombres:   
            if(inpt.lower() == medicamento.lower()):
                return True
        return False
    
    #get_Medications devuelve el par (lista de medicamentos de un paciente con idPaciente, número de medicamentos de la lista) o excepción
    def get_Medications(self, indice1: int, count: int, idPaciente: int): 

        url_get_med = f"{URL_DE_SERVIDOR}/patients/{idPaciente}/medications"  #url necesaria para poder hacer operaciones con la base de datos
        
        num_meds = 0

        if indice1 is not None or count is not None: #completamos la url concatenando lo siguiente (el procedimiento seguido lo sacamos del ejemplo proporcionado por el profesor)
            url_get_med += "?"
            if indice1 is not None:
                url_get_med += f"start_index={indice1}&"
            if count is not None:
                url_get_med += f"count={count}"
            
        resp = requests.get(url_get_med)  #hacemos petición y obtenemos respuesta
        datos = resp.json() 

        if resp.ok:                         #si obtenemos respuesta con éxito
            medication_list = []            
            for item in datos:               #bucle que construye la lista y obtiene el número de elementos de la misma
                num_meds+=1
                medication_list.append(Medication(item))
            return medication_list,num_meds 
        else:
            raise ModelException(datos["detail"]) #caso contrario a éxito en respuesta devuelve excepción
        
        
    def get_Medication(self, idPaciente: int, idMed:int) -> Medication:

        url_get_M = f"{URL_DE_SERVIDOR}/patients/{idPaciente}/medications/{idMed}" #url necesaria para petición
       
        response = requests.get(url_get_M) #hacemos petición y obtenemos respuesta
        datos = response.json()

        if response.ok:
           return Medication(datos)  #devolvemos objeto tipo Medication con los datos obtenidos (si Éxito)
        else:
            raise ModelException(datos["detail"])
        

    def delete_Medications(self, idPaciente: int, idMed:int):

        url_del_med = f"{URL_DE_SERVIDOR}/patients/{idPaciente}/medications/{idMed}"

        resp = requests.delete(url_del_med)
        
        if resp.ok:
           return
        else:
            datos = resp.json()
            raise ModelException(datos["detail"])
        
    
    def add_Medication(self, patient_id: int, name: str, dosage: float, start_date: str, treatment_duration: int):

        url_add_med = f"{URL_DE_SERVIDOR}/patients/{patient_id}/medications"
        
        medication_item = {     #creamos medication_item para introducir los datos pasados por parámetro en los datos del Medicamento en el servidor
            "id": None,         #el id se asigna al hacer post
            "name": name,
            "dosage": dosage,
            "start_date": start_date,
            "treatment_duration": treatment_duration
        }
        
        resp = requests.post(url_add_med, json=medication_item)
        
        if resp.ok:       #No devuelve nada a menos que se produzca una excepción
            return None
        else:
            datos = resp.json()
            raise ModelException(datos["detail"])
        

    def update_Medications(self, patient_id: int, idMed: int, name: str, dosage: float, start_date: str, treatment_duration: int):

        url_update_med = f"{URL_DE_SERVIDOR}/patients/{patient_id}/medications/{idMed}"

        medication_item = {    #creamos medication_item para con patch() modificar los datos pasados por parámetro en los datos del Medicamento en el servidor
            "id": idMed,
            "name": name,
            "dosage": dosage,
            "start_date": start_date,
            "treatment_duration": treatment_duration
        }

        resp = requests.patch(url_update_med,json=medication_item) # petieción para actualizar el medicamento y obtención de respuesta 

        if resp.ok:      #No devuelve nada a menos que se produzca una excepción
           return
        else:
            datos = resp.json()
            raise ModelException(datos["detail"])



#Clase donde definimos las funciones de modelo correspondiente a los Pacientes
class PatientModel:

    #constructor
    def __init__(self):
        pass

    #obtiene paciente a partir de un id
    def get_patient(self, idPaciente: int) -> Patient:

        url_get_patient = f"{URL_DE_SERVIDOR}/patients?code={idPaciente}"

        resp = requests.get(url_get_patient)  #petición obtener paciente y obtención de paciente como respuesta
        datos = resp.json()
        
        if resp.ok:
            return Patient(datos)
        else:
            raise ModelException(datos["detail"])
        


#Clase donde definimos las funciones de modelo correspondiente a las Posologías
class PosologyModel:

    #constructor
    def __init__(self):
        pass

    #obtiene lista de posologías
    def get_Posology(self, indice1: int, count: int, idPaciente: int, idMedicamento: int) -> list:

        url_get_pos = f"{URL_DE_SERVIDOR}/patients/{idPaciente}/medications/{idMedicamento}/posologies"

        if indice1 is not None or count is not None:  #completamos la url concatenando lo siguiente (el procedimiento seguido lo sacamos del ejemplo proporcionado por el profesor)
            url_get_pos += "?"
            if indice1 is not None:
                url_get_pos += f"start_index={indice1}&"
            if count is not None:
                url_get_pos += f"count={count}"
            
        resp = requests.get(url_get_pos) #hacemos petición y obtenemos respuesta
        datos = resp.json()

        if resp.ok:
            posology_list = []
            for item in datos:            #bucle que construye la lista de posología que se devuelve (caso éxito)
                posology_list.append(Posology(item))
            return posology_list
        else:
            raise ModelException(datos["detail"])
        

    #actualiza los datos de la posología cambiandolos por los datos introducidos por parámetro    
    def update_posology(self, idPaciente: int, idMed: int, idPos:int, hour: int, minute: int):

        url_update_med = f"{URL_DE_SERVIDOR}/patients/{idPaciente}/medications/{idMed}/posologies/{idPos}"

        posology_item = { #creamos posology_item para con patch() modificar los datos pasados por parámetro en los datos de la Posología en el servidor
            "id": idPos,
            "hour": hour,
            "minute": minute,
            "medication_id": idMed
        }

        resp = requests.patch(url_update_med,json=posology_item) # petición de actualizar y guardamos repuesta

        if resp.ok:
           return
        else:
            datos = resp.json()
            raise ModelException(datos["detail"])
        
        
    def delete_posology(self, idPaciente: int, idMed: int, idPos:int):

        url_del_pos = f"{URL_DE_SERVIDOR}/patients/{idPaciente}/medications/{idMed}/posologies/{idPos}"
       
        resp = requests.delete(url_del_pos)
        
        if resp.ok:
           return 
        else:
            datos = resp.json()
            raise ModelException(datos["detail"])
        
            
    def add_posology(self, patient_id: int, medication_id: int, hour: int, minute: int):
        url_add_med = f"{URL_DE_SERVIDOR}/patients/{patient_id}/medications/{medication_id}/posologies"
        
        posology_item = { #creamos posology_item para con post() añadir los datos pasados por parámetro en los datos de la Posología en el servidor
            "id": None,
            "hour": hour,
            "minute": minute,
            "medication_id": medication_id,
        }
        
        resp = requests.post(url_add_med, json=posology_item) #añade posología indicada con posology_item a medicamento concreto en un paciente determinado
        
        if resp.ok:
            return None
        else:
            datos = resp.json()
            raise ModelException(datos["detail"])
