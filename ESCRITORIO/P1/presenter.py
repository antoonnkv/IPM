import gi, re, threading
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GLib
from view import view
from model import *

import datetime
#INTERNALIZACIÓN 
import gettext
#siguiendo la convención para poner normbre a estas funciones:
_ = gettext.gettext
N_ = gettext.ngettext


class Presenter:
    def __init__(self, window):
        self.view = view(self)
        self.window = window
        self.currentwdw = 1
        self.screen_switcher(self.currentwdw)

    def is_valid_patient(self, id):
        self.model = PatientModel()
        patient = self.model.get_patient(id)
        return patient if patient is not None else None

    def obtenerDatosMedicamentos(self):
        nombremedicamentos = []
        idmedicamentos = []
        dosagemedicamentos = []
        datemedicamentos = []
        durationmedicamentos = []

        self.model = MedicationsModel()

        medications, numMeds = self.model.get_Medications(None, None, self.patient.id)
        for medication in medications:
            nombremedicamentos.append(_(medication.name))
            idmedicamentos.append(_(medication.id))
            dosagemedicamentos.append(_(medication.dosage))
            
            date = datetime.datetime.strptime(medication.start_date, "%Y-%m-%d") 
            datemedicamentos.append(_(date.strftime("%x")))
            
            durationmedicamentos.append(_(medication.treatment_duration))
        return nombremedicamentos, idmedicamentos, dosagemedicamentos, datemedicamentos, durationmedicamentos

    def obtenerDatosPosologia(self):
        idmedicamentos = []
        hourposology = []
        minuteposology = []
        idPosology = []

        self.model = PosologyModel()
        posologies = self.model.get_Posology(None, None, self.patient.id, self.medication.id)

        for pos in posologies:
            idPosology.append(_(pos.id))
            hourposology.append(_(pos.hour))
            minuteposology.append(_(pos.minute))
            idmedicamentos.append(_(pos.medication_id))

        return idmedicamentos, hourposology, minuteposology, idPosology

    def run_in_thread(self, target, args=(), callback=None):
        loading_dialog = self.view.show_loading_window()
        loading_dialog.present()

        def thread_target(*args):
            result = target(*args)
            GLib.idle_add(self.thread_finished, result, loading_dialog, callback)

        thread = threading.Thread(target=thread_target, args=args)
        thread.start()

    def thread_finished(self, result, loading_dialog, callback):
        self.close_loading_window(loading_dialog)
        if callback:
            callback(result)

    def screen_switcher(self,*args):
        self.window.set_default_size(1, 1)
        if args[0] == 1: self.mostrarBuscarPaciente()
        elif args[0] == 2: self.datosPaciente()
        elif args[0] == 3: self.anadirMedicamento()
        elif args[0] == 4: self.listaPosologias()
        elif args[0] == 5: self.anadirPosologia()

    def mostrarBuscarPaciente(self):
        self.window.set_default_size(1, 1)
        self.currentwdw = 1
        self.window.set_child(self.view.widget)

    def datosPaciente(self):
        if self.currentwdw == 1:
            cajaPrincipal = self.window.get_child()
            code_format = r"^\d{3}-\d{2}-\d{4}$"
            entry = cajaPrincipal.get_first_child().get_next_sibling()
            entry2 = entry.get_first_child()
            entryID = entry2.get_text()

            if not entryID:
                self.view.show_error(_("No se ha introducido un código.\nIntroduzca el código de paciente con el siguiente formato:\nXXX-XX-XXXX"))
            else:
                if not re.match(code_format, entryID):
                    self.view.show_error(_("No se ha introducido un código válido.\nInténtelo de nuevo asegurándose que sigue el formato correcto:\nXXX-XX-XXXX"))
                    return
                
                def fetch_patient_data():
                    try:
                        self.patient = self.is_valid_patient(entryID)
                        return self.obtenerDatosMedicamentos()
                    except ModelException: return "error_patient_not_found"
                    except requests.exceptions.ConnectionError: return "error_connection"

                def update_ui(result):
                    if result == "error_patient_not_found":
                        self.view.show_error(_("No se ha encontrado un paciente con ese código.\nAsegúrese de estar introduciendo correctamente el código."))
                    elif result == "error_connection":
                        self.view.conexionError(_("Error de conexión: No se pudo establecer comunicación con el servidor.",self.screen_switcher,2))
                    else:
                        nameLst, idLst, dosageLst, dateLst, durationLst = result
                        self.currentwdw = 2
                        self.window.set_child(self.view.datosPaciente(self.patient.name, self.patient.surname, self.patient.code, nameLst, idLst, dateLst, durationLst, dosageLst, None))

                self.run_in_thread(fetch_patient_data, callback=update_ui)
        else:
            def fetch_medications_data(): 
                try:
                    return self.obtenerDatosMedicamentos()
                except requests.exceptions.ConnectionError: return "error_connection"

            def update_ui(result):

                if result == "error_connection":
                    self.view.conexionError(_("Error de conexión: No se pudo establecer comunicación con el servidor."),self.screen_switcher,2)
                else:
                    nameLst, idLst, dosageLst, dateLst, durationLst = result
                    self.window.set_child(self.view.datosPaciente(self.patient.name, self.patient.surname, self.patient.code, nameLst, idLst, dateLst, durationLst, dosageLst, None))
            self.run_in_thread(fetch_medications_data, callback=update_ui)

    def anadirMedicamento(self):
        self.currentwdw = 3
        self.window.set_child(self.view.anadirMedicamento())

    def confirmarAnadirMedicamento(self, *arg):
        errorStr = _("Uno o más parámetros están vacios:\n")
        frmatErrorStr = _("Uno o más parámetros no son válidos, asegúrese de estar usando el formato correcto:\n")
        show = True
        date_format = r"^\d{4}-\d{2}-\d{2}$"

        cajaPrincipal = self.window.get_child()
        grid = cajaPrincipal.get_first_child()

        nameData = grid.get_child_at(0, 0).get_text()
        dateData = grid.get_child_at(1, 1).get_text()
        
        dosageData = grid.get_child_at(1, 2).get_text()
        durationData = grid.get_child_at(1, 3).get_text()

        if not nameData:
            errorStr += _("Nombre del medicamento.\n")
            show = False
        if not dateData:
            errorStr += _("Fecha de inicio (DD/MM/AA).\n")
            show = False
        if not dosageData:
            errorStr += _("Dosis\n (Ej: 2.3).")
            show = False
        if not durationData:
            errorStr += _("Duracion (Ej: 15).\n")
            show = False

        if show:
            
            try:
                date = datetime.datetime.strptime(dateData, "%x")
                dateData= date.strftime("%Y-%m-%d")
            except ValueError:
                frmatErrorStr += _("Fecha de inicio (DD/MM/AA)\n")
                show = False
            try:
                dosageData = float(dosageData)
                if dosageData <= 0:
                    frmatErrorStr += _("Dosis (Ej: 2.3).\n")
                    show = False
            except ValueError:
                frmatErrorStr += _("Dosis (Ej: 2.3).\n")
                show = False
            if durationData.isdigit() == False:
                frmatErrorStr += _("Duración (Ej: 15).\n")
                show = False
            elif int(durationData) <= 0:
                frmatErrorStr += _("Duración (Ej: 15).\n")
                show = False

            if show == False:
                self.view.show_error(frmatErrorStr)
                return

            self.model = MedicationsModel()
            medicamentoValido = self.model.search_medication(nameData)

            if medicamentoValido is None:
                self.view.show_error(_("Error inesperado al leer el fichero con los medicamentos.\nAsegúrese de tener el fichero medications.json en el directorio Source para poder añadir un medicamento válido."))
                return

            if medicamentoValido:
                def add_medication():
                    try:
                        self.model.add_Medication(self.patient.id, nameData.upper(), float(dosageData), dateData, int(durationData))
                        return "success"
                    except ModelException: return "error_unexpected"
                    except requests.exceptions.ConnectionError: return "error_connection"

                def update_ui(result):
                    if result == "success":
                        self.currentwdw = 2
                        self.screen_switcher(self.currentwdw)
                    elif result == "error_unexpected":
                        self.view.show_error(_("Error inesperado al añadir.\nEs posible que el medicamento haya sido eliminado."))
                        self.currentwdw = 2
                        self.screen_switcher(self.currentwdw)
                    elif result == "error_connection":
                        self.view.conexionError(_("Error de conexión: No se pudo establecer comunicación con el servidor."),self.confirmarAnadirMedicamento,self,None)

                self.run_in_thread(add_medication, callback=update_ui)
            else:
                self.view.show_error(_("Medicamento no encontrado.\nAsegúrese que el medicamento es un medicamento existente."))
        else:
            self.view.show_error(errorStr)

    def updateMed(self, *args):
        if args[1] is not None:
            errorStr = _("Uno o más parámetros están vacios:\n")
            show = True
            frmatErrorStr = _("Uno o más parámetros no son válidos, asegúrese de estar usando el formato correcto:\n")
            date_format = r"^\d{4}-\d{2}-\d{2}$"

            cajaPrincipal = self.window.get_child()
            CajaVertical2 = cajaPrincipal.get_last_child()

            child = CajaVertical2.get_first_child()
            gridSeg = None

            while child:
                if isinstance(child, Gtk.Grid):
                    gridSeg = child
                    break
                child = child.get_next_sibling()

            medStartDate = gridSeg.get_child_at(1, 3).get_text()

            medDosage = gridSeg.get_child_at(1, 4).get_text()
            medDuration = gridSeg.get_child_at(1, 5).get_text()

            if not medStartDate:
                errorStr += _("Fecha de inicio (DD/MM/AA)\n")
                show = False
            if not medDosage:
                errorStr += _("Dosis (Ej: 2.3).")
                show = False
            if not medDuration:
                errorStr += _("Duracion (Ej: 15)")
                show = False

            if show:
                try:
                    date = datetime.datetime.strptime(medStartDate, "%x")
                    medStartDate= date.strftime("%Y-%m-%d")
                except ValueError:
                    frmatErrorStr += _("Fecha de inicio (DD/MM/AA)\n")
                    show = False
                try:
                    dosageData = float(medDosage)
                    if dosageData <= 0:
                        frmatErrorStr += _("Dosis (Ej: 2.3).\n")
                        show = False
                except ValueError:
                    frmatErrorStr += _("Dosis (Ej: 2.3).\n")
                    show = False
                if medDuration.isdigit() == False:
                    frmatErrorStr += _("Duración (Ej: 15).")
                    show = False
                elif int(medDuration) <= 0:
                    frmatErrorStr += _("Duración (Ej: 15).")
                    show = False

                if show == False:
                    self.view.show_error(frmatErrorStr)
                    return

                def update_medication():
                    try:
                        self.model = MedicationsModel()
                        self.model.update_Medications(self.patient.id, int(args[1]), args[2], float(medDosage), medStartDate, int(medDuration))
                        return "success"
                    except ModelException:
                        return "error_unexpected"
                    except requests.exceptions.ConnectionError:
                        return "error_connection"

                def update_ui(result):
                    if result == "success":
                        self.currentwdw = 2
                        self.screen_switcher(self.currentwdw)
                        self.view.show_ok()
                    elif result == "error_unexpected":
                        self.view.show_error(_("Error inesperado al actualizar.\nEs posible que el medicamento haya sido eliminado."))
                        self.currentwdw = 2
                        self.screen_switcher(self.currentwdw)
                    elif result == "error_connection":
                        self.view.conexionError(_("Error de conexión: No se pudo establecer comunicación con el servidor.",self.updateMed,*args))

                self.run_in_thread(update_medication, callback=update_ui)
            else:
                self.view.show_error(errorStr)
        else:
            self.view.show_error(_("Seleccione antes un medicamento para poder modificar sus datos."))

    def delMed(self, *args):
        def delete_medication():
            try:
                self.model = MedicationsModel()
                self.model.delete_Medications(self.patient.id, args[0])
                return "success"
            except ModelException:
                return "error_unexpected"
            except requests.exceptions.ConnectionError:
                return "error_connection"

        def update_ui(result):
            if result == "success":
                self.currentwdw = 2
                self.screen_switcher(self.currentwdw)
            elif result == "error_unexpected":
                self.view.show_error(_("Error inesperado al  eliminar.\nEs posible que el medicamento haya sido eliminado."))
                self.screen_switcher(self.currentwdw)
            elif result == "error_connection":
                self.view.conexionError(_("Error de conexión: No se pudo establecer comunicación con el servidor.",self.delMed,*args))

        self.run_in_thread(delete_medication, callback=update_ui)

    def showRowData(self, *args):

        def fetch_medication_data():
            try:
                nameLst, idLst, dosageLst, dateLst, durationLst = self.obtenerDatosMedicamentos()
                if nameLst is None: return "error_connection"
                self.model = MedicationsModel()
                self.medication = self.model.get_Medication(self.patient.id, args[0])
                return nameLst, idLst, dosageLst, dateLst, durationLst
            except ModelException: return "error_unexpected"
            except requests.exceptions.ConnectionError: return "error_connection"

        def update_ui(result):
            if result == "error_unexpected":
                self.view.show_error(_("Error inesperado al mostrar los datos.\nEs posible que el medicamento haya sido eliminado."))
                self.screen_switcher(self.currentwdw)
            elif result == "error_connection":
                self.view.conexionError(_("Error de conexión: No se pudo establecer comunicación con el servidor.",self.showRowData,*args))
            else:
                nameLst, idLst, dosageLst, dateLst, durationLst = result
                self.window.set_child(self.view.datosPaciente(self.patient.name, self.patient.surname, self.patient.code, nameLst, idLst, dateLst, durationLst, dosageLst, args[1]))

        self.run_in_thread(fetch_medication_data, callback=update_ui)

    def listaPosologias(self, *args):
        self.currentwdw = 4

        def fetch_posology_data():
            try:
                return self.obtenerDatosPosologia()
            except ModelException: return "error_obtaining_posologies"
            except requests.exceptions.ConnectionError: return "error_connection"
            

        def update_ui(result):
            if result == "error_obtaining_posologies":
                self.view.show_error(_("Error inesperado al acceder a las posologías.\nEs posible que el medicamento haya sido eliminado."))
                self.currentwdw = 2
                self.screen_switcher(self.currentwdw)
            elif result == "error_connection":
                self.view.conexionError(_("Error de conexión: No se pudo establecer comunicación con el servidor.",self.listaPosologias,None))
            else:
                idmedicamentos, hourposology, minuteposology, idPosology = result
                self.window.set_child(self.view.datosPosologia(self.medication.name, idPosology, hourposology, minuteposology, None))

        self.run_in_thread(fetch_posology_data, callback=update_ui)

    def delPos(self, *args):
        def delete_posology():
            try:
                self.model = PosologyModel()
                self.model.delete_posology(self.patient.id, self.medication.id, args[0])
                return "success"
            except ModelException:
                return "error_unexpected"
            except requests.exceptions.ConnectionError:
                return "error_connection"

        def update_ui(result):
            if result == "success":
                self.currentwdw = 4
                self.screen_switcher(self.currentwdw)
            elif result == "error_unexpected":
                self.view.show_error(_("Error inesperado al eliminar.\nEs posible que la posología haya sido eliminada."))
                self.currentwdw = 4
                self.screen_switcher(self.currentwdw)
            elif result == "error_connection":
                self.view.conexionError(_("Error de conexión: No se pudo establecer comunicación con el servidor.",self.delPos,*args))

        self.run_in_thread(delete_posology, callback=update_ui)

    def showRowDataPos(self, *args):
        def fetch_posology_data():
            try: 
                idmedicamentos, hourposology, minuteposology, idPosology = self.obtenerDatosPosologia()
                if idmedicamentos is None: return "error_connection"
                return idmedicamentos, hourposology, minuteposology, idPosology
            except ModelException: return "error_unexpected"
            except requests.exceptions.ConnectionError: return "error_connection"

        def update_ui(result):
            if result == "error_unexpected":
                self.view.show_error(_("Error inesperado al mostrar los datos.\nEs posible que la posología haya sido eliminada."))
                self.screen_switcher(self.currentwdw)
            elif result == "error_connection":
                self.view.conexionError(_("Error de conexión: No se pudo establecer comunicación con el servidor.",self.showRowDataPos,*args))
            else:
                idmedicamentos, hourposology, minuteposology, idPosology = result
                self.window.set_child(self.view.datosPosologia(self.medication.name, idPosology, hourposology, minuteposology, args[1]))

        self.run_in_thread(fetch_posology_data, callback=update_ui)

    def anadirPosologia(self):
        self.currentwdw = 5
        self.window.set_child(self.view.anadirPosologia())

    def confirmarAnadirPosologia(self, *args):
        frmatErrorStr = _("Uno o más parámetros no son válidos, asegúrese de estar usando el formato correcto:\n")
        errorStr = _("Uno o más parámetros están vacios:\n")
        show = True

        cajaPrincipal = self.window.get_child()
        grid = cajaPrincipal.get_first_child()

        minuteData = grid.get_child_at(1, 2).get_text()
        hourData = grid.get_child_at(1, 1).get_text()

        if not hourData:
            errorStr += _("Horas (Ej:8).\n")
            show = False
        if not minuteData:
            errorStr += _("Minutos (Ej: 30).")
            show = False

        if show:
            if hourData.isdigit() == False:
                frmatErrorStr += _("Horas (Ej: 8).\n")
                show = False
            elif int(hourData) < 1:
                frmatErrorStr += _("Horas (Ej: 8).\n")
                show = False

            if minuteData.isdigit() == False:
                frmatErrorStr += _("Minutos (Ej: 30).")
                show = False
            elif int(minuteData) < 0 or int(minuteData) > 59:
                frmatErrorStr += _("Minutos (Ej: 30).")
                show = False

            if show == False:
                self.view.show_error(frmatErrorStr)
                return

            def add_posology():
                try:
                    self.model = PosologyModel()
                    self.model.add_posology(self.patient.id, self.medication.id, int(hourData), int(minuteData))
                    return "success"
                except ModelException:
                    return "error_unexpected"
                except requests.exceptions.ConnectionError:
                    return "error_connection"

            def update_ui(result):
                if result == "success":
                    self.currentwdw = 4
                    self.screen_switcher(self.currentwdw)
                elif result == "error_unexpected":
                    self.view.show_error(_("Error inesperado al añadir.\nEs posible que la posología haya sido eliminada."))
                    self.currentwdw = 4
                    self.screen_switcher(self.currentwdw)
                elif result == "error_connection":
                    self.view.conexionError(_("Error de conexión: No se pudo establecer comunicación con el servidor.",self.confirmarAnadirPosologia,*args))

            self.run_in_thread(add_posology, callback=update_ui)
        else:
            self.view.show_error(errorStr)

    def updatePos(self, *args):
        if args[0] is not None:
            errorStr = _("Uno o más parámetros están vacios:\n")
            frmatErrorStr = _("Uno o más parámetros no son válidos, asegúrese de estar usando el formato correcto:\n")
            show = True

            cajaPrincipal = self.window.get_child()
            CajaVertical2 = cajaPrincipal.get_last_child()

            child = CajaVertical2.get_first_child()
            gridSeg = None

            while child:
                if isinstance(child, Gtk.Grid):
                    gridSeg = child
                    break
                child = child.get_next_sibling()

            hourData = gridSeg.get_child_at(1, 1).get_text()
            minuteData = gridSeg.get_child_at(1, 2).get_text()

            if not hourData:
                errorStr += _("Horas (Ej:8).\n")
                show = False
            if not minuteData:
                errorStr += _("Minutos (Ej:30).")
                show = False

            if show:
                if hourData.isdigit() == False:
                    frmatErrorStr += _("Horas (Ej: 8).\n")
                    show = False
                elif int(hourData) < 1:
                    frmatErrorStr += _("Horas (Ej: 8).\n")
                    show = False

                if minuteData.isdigit() == False:
                    frmatErrorStr += _("Minutos (Ej: 30).")
                    show = False
                elif int(minuteData) < 0 or int(minuteData) > 59:
                    frmatErrorStr += _("Minutos (Ej: 30).")
                    show = False

                if show == False:
                    self.view.show_error(frmatErrorStr)
                    return

                def update_posology():
                    try:
                        self.model = PosologyModel()
                        self.model.update_posology(self.patient.id, self.medication.id, args[0], int(hourData), int(minuteData))
                        return "success"
                    except ModelException: return "error_unexpected"
                    except requests.exceptions.ConnectionError: return "error_connection"

                def update_ui(result):
                    if result == "success":
                        self.currentwdw = 4
                        self.screen_switcher(self.currentwdw)
                        self.view.show_ok()
                    elif result == "error_unexpected":
                        self.view.show_error(_("Error inesperado al actualizar.\nEs posible que la posología haya sido eliminada."))
                        self.screen_switcher(self.currentwdw)
                    elif result == "error_connection":
                        self.view.conexionError(_("Error de conexión: No se pudo establecer comunicación con el servidor."),self.updatePos,*args)

                self.run_in_thread(update_posology, callback=update_ui)
            else: self.view.show_error(errorStr)
        else: self.view.show_error(_("Seleccione antes una posología para poder modificar sus datos"))

    def go_to_error(self, arg, strn):
        self.view.show_error(strn)

    def on_close_dialog(self, button, dialog):
        dialog.close()

    def cerrar_conexion_error(self,dialog,funcion,args):
        funcion(*args)
        dialog.close()

    def delete_confirm_pressed(self, arg, id, dialog, typeList):
        if typeList == 0: self.delMed(id)
        if typeList == 1: self.delPos(id)
        dialog.close()

    def close_loading_window(self, dialog):
        GLib.idle_add(dialog.close)

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_title("MediTrack")
        self.set_default_size(1, 1)
        presenter = Presenter(self)
        self.set_child(presenter.view.widget)

class MyApp(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def do_activate(self):
        win = MainWindow(application=self)
        win.present()
