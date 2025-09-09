import gi, os
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GLib

#INTERNALIZACIÓN 
import gettext
#siguiendo la convención para poner normbre a estas funciones:
_ = gettext.gettext
N_ = gettext.ngettext

class view:

    def __init__(self, presenter, *args):
        self.presenter = presenter
        self.widget = self.mostrarBuscarPaciente("") 

    def show_loading_window(self):
        dialog = Gtk.Dialog(title=_("Cargando"), transient_for=self.presenter.window)
        dialog.set_modal(True)
        dialog.set_default_size(200, 100)

        dialog.set_decorated(False)
        dialog.set_resizable(False)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.set_margin_top(20)
        vbox.set_margin_bottom(20)
        vbox.set_margin_start(20)
        vbox.set_margin_end(20)

        spinner = Gtk.Spinner()
        spinner.start()
        vbox.append(spinner)

        label = Gtk.Label(label=_("Cargando, por favor espere..."))
        vbox.append(label)

        dialog.set_child(vbox)
        return dialog

    def confirmDel(self,arg,id,listType):

        dialog = Gtk.Dialog(title=_("AVISO"), transient_for=self.presenter.window)
        dialog.set_modal(True)
        dialog.set_default_size(100, 75)
        dialog.set_resizable(False)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.set_margin_top(15)
        vbox.set_margin_bottom(15)
        vbox.set_margin_start(15)
        vbox.set_margin_end(15)

        image = Gtk.Image.new_from_file(os.path.join(os.path.dirname(__file__), "Sources/iconerror.png"))
        image.set_pixel_size(30)
        vbox.append(image)

        message_label = Gtk.Label(label=_("Estas a punto de eliminar un elemento.\nESTA ACCION NO SE PUEDE DESHACER\n¿Estas seguro que desea realizar la accion?"))
        message_label.set_justify(Gtk.Justification.CENTER)
        message_label.set_halign(Gtk.Align.CENTER) 
        vbox.append(message_label)

        close_button = Gtk.Button(label=_("Cerrar"))
        close_button.connect("clicked", self.presenter.on_close_dialog, dialog)

        confirm_button = Gtk.Button(label=_("Confirmar"))
        confirm_button.connect("clicked", self.presenter.delete_confirm_pressed, id, dialog, listType)

        bbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        bbox.set_halign(Gtk.Align.CENTER)
        bbox.append(close_button)
        bbox.append(confirm_button)

        vbox.append(bbox)

        dialog.set_child(vbox)
        dialog.present()

    def conexionError(self,message,funcion,*args):
        dialog = Gtk.Dialog(title=_("ERROR CONEXIÓN"), transient_for=self.presenter.window)
        dialog.set_modal(True)
        dialog.set_default_size(100, 75)
        dialog.set_resizable(False)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.set_margin_top(15)
        vbox.set_margin_bottom(15)
        vbox.set_margin_start(15)
        vbox.set_margin_end(15)

        image = Gtk.Image.new_from_file(os.path.join(os.path.dirname(__file__), "Sources/iconerror.png"))
        image.set_pixel_size(30)
        vbox.append(image)

        message_label = Gtk.Label(label=message)
        message_label.set_justify(Gtk.Justification.CENTER)
        message_label.set_halign(Gtk.Align.CENTER) 
        vbox.append(message_label)

        close_button = Gtk.Button(label=_("Recargar"))
        close_button.connect("clicked", lambda button: self.presenter.cerrar_conexion_error(dialog,funcion,args))

        bbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        bbox.set_halign(Gtk.Align.CENTER)
        bbox.append(close_button)

        vbox.append(bbox)

        dialog.set_child(vbox)
        dialog.present()     

    def show_ok(self):
        dialog = Gtk.Dialog(title="OK", transient_for=self.presenter.window)
        dialog.set_modal(True)
        dialog.set_default_size(100, 75)
        dialog.set_resizable(False)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.set_margin_top(15)
        vbox.set_margin_bottom(15)
        vbox.set_margin_start(15)
        vbox.set_margin_end(15)

        image = Gtk.Image.new_from_file(os.path.join(os.path.dirname(__file__), "Sources/ICONOOK.png"))
        image.set_pixel_size(30)
        vbox.append(image)

        message_label = Gtk.Label(label=_("Elemento actualizado correctamente."))
        message_label.set_justify(Gtk.Justification.CENTER)
        message_label.set_halign(Gtk.Align.CENTER) 
        vbox.append(message_label)

        close_button = Gtk.Button(label=_("Cerrar"))
        close_button.connect("clicked", self.presenter.on_close_dialog, dialog)

        bbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        bbox.set_halign(Gtk.Align.CENTER)
        bbox.append(close_button)
        vbox.append(bbox)

        dialog.set_child(vbox)
        dialog.present()

    def show_error(self, message):
        dialog = Gtk.Dialog(title="ERROR", transient_for=self.presenter.window)
        dialog.set_modal(True)
        dialog.set_default_size(100, 75)
        dialog.set_resizable(False)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.set_margin_top(15)
        vbox.set_margin_bottom(15)
        vbox.set_margin_start(15)
        vbox.set_margin_end(15)

        image = Gtk.Image.new_from_file(os.path.join(os.path.dirname(__file__), "Sources/iconerror.png"))
        image.set_pixel_size(30)
        vbox.append(image)

        message_label = Gtk.Label(label=message)
        message_label.set_justify(Gtk.Justification.CENTER)
        message_label.set_halign(Gtk.Align.CENTER) 
        vbox.append(message_label)

        close_button = Gtk.Button(label=_("Cerrar"))
        close_button.connect("clicked", self.presenter.on_close_dialog, dialog)

        bbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        bbox.set_halign(Gtk.Align.CENTER)
        bbox.append(close_button)
        vbox.append(bbox)

        dialog.set_child(vbox)
        dialog.present()

    def mostrarBuscarPaciente(self,srt):
        cajaPrincipal = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        cajaPrincipal.set_valign(Gtk.Align.CENTER)
        cajaPrincipal.set_halign(Gtk.Align.CENTER)
        cajaPrincipal.set_size_request(300, 150)
        cajaPrincipal.set_margin_bottom(10)
        cajaPrincipal.set_margin_start(10)
        cajaPrincipal.set_margin_end(10)

        image_placeholder = Gtk.Image.new_from_file(os.path.join(os.path.dirname(__file__), "Sources/ICONOAPP.png"))
        image_placeholder.set_pixel_size(120)
        image_placeholder.set_margin_top(10)
        image_placeholder.set_margin_bottom(10)

        entradaPaciente = Gtk.Entry()
        entradaPaciente.set_placeholder_text(_("Codigo del paciente (XXX-XX-XXXX)"))
        entradaPaciente.set_text(srt)
        entradaPaciente.set_hexpand(True)
        entradaPaciente.set_size_request(10, 50)

        botonBuscar = Gtk.Button(label="🔎")
        botonBuscar.connect("clicked",lambda button: self.presenter.screen_switcher(2))
        botonBuscar.set_size_request(entradaPaciente.get_allocated_height(), entradaPaciente.get_allocated_height())

        input_button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        input_button_box.append(entradaPaciente)
        input_button_box.append(botonBuscar)

        cajaPrincipal.append(image_placeholder)
        cajaPrincipal.append(input_button_box)

        return cajaPrincipal


    def datosPaciente(self,name,surname,code,medications,medicationsID,medicationsDate,medicationsDuration,medicationsDose,idMED): 
        cajaPrincipal = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing = 30)  
        cajaPrincipal.set_size_request(960,560)
        cajaPrincipal.set_vexpand(True)
        cajaPrincipal.set_valign(Gtk.Align.CENTER)
        cajaPrincipal.set_margin_top(20)
        cajaPrincipal.set_margin_start(20)
        cajaPrincipal.set_margin_bottom(20)
        cajaPrincipal.set_margin_end(20)

        CajaVertical1=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=40)
        CajaVertical2=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing = 45)

        grid2 = Gtk.Grid()

        etiquetaNombre2 = Gtk.Label(label = name)
        etiquetaNombre2.add_css_class("title-1")

        etiquetaApellido2 = Gtk.Label(label = surname)
        etiquetaApellido2.add_css_class("title-1")

        etiquetaCodigo2 = Gtk.Label(label = code)
        etiquetaCodigo2.add_css_class("title-1")

        AnadirMedicamento2 = Gtk.Button(label = _( "AÑADIR MEDICAMENTO"))
        AnadirMedicamento2.connect("clicked",lambda button: self.presenter.screen_switcher(3))

        IrAtras2 = Gtk.Button(label = _("VOLVER"))
        IrAtras2.connect("clicked",lambda button: self.presenter.screen_switcher(1)) 

        Confirmar = Gtk.Button(label = _("CONFIRMAR"))

        if idMED is None: 
            strn_aux = ""
            medID_aux = None

        else:
            strn_aux = medications[idMED]
            medID_aux = medicationsID[idMED]

        Confirmar.connect("clicked",self.presenter.updateMed,medID_aux,strn_aux)

        VerPosologias = Gtk.Button(label =_( "VER POSOLOGÍAS"))

        if idMED is not None: 
           VerPosologias.connect("clicked",lambda button: self.presenter.screen_switcher(4))
        else:
           VerPosologias.connect("clicked",self.presenter.go_to_error,_("Seleccione antes un medicamento para poder ver sus posologias"))
        

        grid2.set_hexpand(True)
        grid2.attach(etiquetaNombre2,0,0,1,1)   
        grid2.attach(etiquetaApellido2,1, 0,1,1)
        grid2.attach(etiquetaCodigo2,2,0,1,1)
        grid2.set_column_spacing(40)  
        grid2.set_halign(Gtk.Align.CENTER)
        
        gridSeg = Gtk.Grid()
        gridSeg.set_row_spacing(15)
        gridSeg.set_column_spacing(10)
        gridSeg.set_halign(Gtk.Align.CENTER)

        medDosage = Gtk.Entry()
        medDosage.set_placeholder_text(_("Ej: 8.3"))

        medStartDate = Gtk.Entry()
        medStartDate.set_placeholder_text(_("DD/MM/AA"))

        medDuration = Gtk.Entry()
        medDuration.set_placeholder_text(_("Ej: 15"))

        medName = Gtk.Label(label = _("Nombre Medicamento"))

        if idMED is not None:

            medDosage.set_text(str(medicationsDose[idMED]))
            medStartDate.set_text(str(medicationsDate[idMED]))
            medDuration.set_text(str(medicationsDuration[idMED]))
            medName.set_text(str(medications[idMED]))


        labelStartDate = Gtk.Label(label=_("Fecha de Inicio"))
        gridSeg.attach(labelStartDate, 0, 3, 1, 1)
        gridSeg.attach(medStartDate, 1, 3, 1, 1)

        labelDosage = Gtk.Label(label=_("Dosis"))
        gridSeg.attach(labelDosage, 0, 4, 1, 1)
        gridSeg.attach(medDosage, 1, 4, 1, 1)

        labelDuration = Gtk.Label(label=_("Duración"))
        gridSeg.attach(labelDuration, 0, 5, 1, 1)
        gridSeg.attach(medDuration, 1, 5, 1, 1)
        
        CajaVertical1.append(grid2)
        
        listbox = Gtk.ListBox()

        for index,nombreMedicamento in enumerate(medications):

            row = Gtk.ListBoxRow()
            
            box_aux = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL,spacing = 50)
            row.set_child(box_aux)

            
            med = Gtk.Label(label = nombreMedicamento)

            eliminar = Gtk.Button(label = _("ELIMINAR"))
            eliminar.connect("clicked", lambda button, idx=index: self.confirmDel(button, medicationsID[idx], 0))
            
            med.set_hexpand(True)
            med.set_halign(Gtk.Align.START)

            box_aux.append(med)
            box_aux.append(eliminar)

            listbox.append(row)
            
            box_aux.set_margin_top(10)
            box_aux.set_margin_bottom(10)

        listbox.connect("row-activated", lambda _,row: self.presenter.showRowData(medicationsID[row.get_index()],row.get_index()))


        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
           
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_child(listbox)  
        scrolled_window.set_min_content_height(500)  
    
        CajaVertical1.append(scrolled_window) 
        
        Confirmar.set_size_request(230, 50) 
        IrAtras2.set_size_request(230, 50) 
        VerPosologias.set_size_request(230, 50)
        AnadirMedicamento2.set_size_request(230, 50)  

        CajaVertical2.append(IrAtras2) 
        CajaVertical2.append(medName)
        CajaVertical2.append(gridSeg)
        CajaVertical2.append(Confirmar)
        CajaVertical2.append(VerPosologias)
        cajaPrincipal.append(CajaVertical1)
        cajaPrincipal.append(CajaVertical2)
        CajaVertical2.append(AnadirMedicamento2)

        return cajaPrincipal


    def anadirMedicamento(self):
        cajaPrincipal = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=30)
        cajaPrincipal.set_margin_top(10)
        cajaPrincipal.set_margin_end(10)
        cajaPrincipal.set_margin_start(10)
        cajaPrincipal.set_margin_bottom(10)

        grid1 = Gtk.Grid()

        cajaPrincipal.set_halign(Gtk.Align.CENTER)
        cajaPrincipal.set_valign(Gtk.Align.CENTER)
        cajaPrincipal.set_margin_top(20)

        buscarMedicamento = Gtk.Entry()
        buscarMedicamento.set_placeholder_text(_("Nombre del medicamento..."))
        buscarMedicamento.set_size_request(300, 50)

        botonVolver = Gtk.Button(label=_("Volver"))
        botonVolver.set_size_request(100, 50)
        botonVolver.connect("clicked",lambda button: self.presenter.screen_switcher(2))

        botonConfirmar1 = Gtk.Button(label= _("Confirmar"))
        botonConfirmar1.set_size_request(100, 50)
        botonConfirmar1.connect("clicked",self.presenter.confirmarAnadirMedicamento)

        grid1.attach(botonConfirmar1, 0, 6, 2, 1)
        grid1.attach(botonVolver, 0, 7, 2, 1)
        grid1.attach(buscarMedicamento, 0, 0, 2, 1)

        grid1.set_row_spacing(15)
        grid1.set_column_spacing(10)

        medDosage = Gtk.Entry()
        medDosage.set_placeholder_text(_("Ej: 8.3"))
        labelDosage = Gtk.Label(label=_("Dosis"))

        medStartDate = Gtk.Entry()
        medStartDate.set_placeholder_text(_("DD/MM/AA"))
        labelStartDate = Gtk.Label(label=_("Fecha de Inicio"))

        medDuration = Gtk.Entry()
        medDuration.set_placeholder_text(_("Ej: 15"))
        labelDuration = Gtk.Label(label= _("Duración"))      
        
        
        grid1.attach(labelStartDate, 0, 1, 1, 1)
        grid1.attach(medStartDate, 1, 1, 1, 1)
        grid1.attach(labelDosage, 0, 2, 1, 1)
        grid1.attach(medDosage, 1, 2, 1, 1)
        grid1.attach(labelDuration, 0, 3, 1, 1)
        grid1.attach(medDuration, 1, 3, 1, 1)

        cajaPrincipal.append(grid1)
        
        return cajaPrincipal
    
    
    def datosPosologia(self,name,posologiesID,posologiesHour,posologiesMinutes,idPos):
       cajaPrincipal = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing = 30)  
       cajaPrincipal.set_vexpand(True)
       cajaPrincipal.set_size_request(960,560)
       cajaPrincipal.set_valign(Gtk.Align.CENTER)
       cajaPrincipal.set_margin_top(20)
       cajaPrincipal.set_margin_start(20)
       cajaPrincipal.set_margin_bottom(20)
       cajaPrincipal.set_margin_end(20)

       CajaVertical1=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=40)
       CajaVertical2=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=40)

       etiquetaNombreMed2 = Gtk.Label(label = name)
       etiquetaNombreMed2.add_css_class("title-1")

       etiquetaGrid = Gtk.Label(label = _("POSOLOGIA"))
       etiquetaGrid.add_css_class("title-3")
       
       AnadirMedicamento2 = Gtk.Button(label = _("AÑADIR POSOLOGÍA"))
       AnadirMedicamento2.connect("clicked",lambda button: self.presenter.screen_switcher(5))

       IrAtras2 = Gtk.Button(label = _("VOLVER"))
       IrAtras2.connect("clicked",lambda button: self.presenter.screen_switcher(2))

       Confirmar = Gtk.Button(label = _("CONFIRMAR"))

       if idPos is None: 
        posID_aux = None

       else:
        posID_aux = posologiesID[idPos]

       Confirmar.connect("clicked",lambda button: self.presenter.updatePos(posID_aux))

       grid2 = Gtk.Grid()
       grid2.set_hexpand(True)
       
       grid2.attach(etiquetaNombreMed2,0,0,1,1)   
      
       grid2.set_column_spacing(40)  
       grid2.set_halign(Gtk.Align.CENTER)

       gridSeg = Gtk.Grid()
       gridSeg.set_row_spacing(15)
       gridSeg.set_column_spacing(10)
       gridSeg.set_halign(Gtk.Align.CENTER)

       posHour = Gtk.Entry()
       posHour.set_placeholder_text(_("Ej: 8"))

       posMinute = Gtk.Entry()
       posMinute.set_placeholder_text(_("Ej: 30"))
       
       if idPos is not None:

        posHour.set_text(str(posologiesHour[idPos]))
        posMinute.set_text(str(posologiesMinutes[idPos]))
       
       labelHour = Gtk.Label(label=_("Hora"))
       labelMinute = Gtk.Label(label=_("Minuto"))
       
       gridSeg.attach(posHour,1,1,1,1)
       gridSeg.attach(posMinute,1,2,1,1)
       gridSeg.attach(labelHour, 0, 1, 1, 1)
       gridSeg.attach(labelMinute, 0, 2, 1, 1)
       gridSeg.attach(etiquetaGrid,0,0,2,1)
   
       CajaVertical1.append(grid2)

       listbox = Gtk.ListBox()

       for index,pos in enumerate(posologiesID):
           
           row = Gtk.ListBoxRow()
           box_aux = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL,spacing = 50)
           row.set_child(box_aux)
           
           eliminar = Gtk.Button(label =_( "ELIMINAR"))
           eliminar.connect("clicked", lambda button, idx=index: self.confirmDel(button, posologiesID[idx], 1))


           med = Gtk.Label(label = _("Posología Nº: ")+ str(pos) + _("Horas: ") + str(posologiesHour[index]) + _("Minutos:") + str(posologiesMinutes[index]))
           med.set_hexpand(True)
           med.set_halign(Gtk.Align.START)

           box_aux.append(med)
           box_aux.append(eliminar)

           listbox.append(row)

           box_aux.set_margin_top(10)
           box_aux.set_margin_bottom(10)
          
       listbox.connect("row-activated", lambda _,row: self.presenter.showRowDataPos(posologiesID[row.get_index()],row.get_index()))
       listbox.set_selection_mode(Gtk.SelectionMode.NONE)

       scrolled_window = Gtk.ScrolledWindow()
       scrolled_window.set_child(listbox)  
       scrolled_window.set_min_content_height(500)  
   
       CajaVertical1.append(scrolled_window) 
       
       Confirmar.set_size_request(230, 50) 

       IrAtras2.set_size_request(230, 50) 

       AnadirMedicamento2.set_size_request(230, 50)  

       CajaVertical2.append(IrAtras2) 
       CajaVertical2.append(gridSeg)
       CajaVertical2.append(Confirmar)
       cajaPrincipal.append(CajaVertical1)
       cajaPrincipal.append(CajaVertical2)
       CajaVertical2.append(AnadirMedicamento2)

       return cajaPrincipal
    

    def anadirPosologia(self):
       cajaPrincipal = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=30)
       cajaPrincipal.set_margin_top(10)
       cajaPrincipal.set_margin_end(10)
       cajaPrincipal.set_margin_start(10)
       cajaPrincipal.set_margin_bottom(10)
       cajaPrincipal.set_halign(Gtk.Align.CENTER)
       cajaPrincipal.set_valign(Gtk.Align.CENTER)
       cajaPrincipal.set_margin_top(20)

       texto1 = Gtk.Label(label= _("AÑADIR POSOLOGIA"))
       texto1.add_css_class("title-3")
       texto1.set_size_request(300, 50)

       botonVolver = Gtk.Button(label= _("Volver"))
       botonVolver.set_size_request(100, 50)
       botonVolver.connect("clicked",lambda button: self.presenter.screen_switcher(4))

       botonConfirmar1 = Gtk.Button(label= _("Confirmar"))
       botonConfirmar1.set_size_request(100, 50)
       botonConfirmar1.connect("clicked",self.presenter.confirmarAnadirPosologia)

       grid1 = Gtk.Grid()
       grid1.attach(botonConfirmar1, 0, 6, 2, 1)
       grid1.attach(botonVolver, 0, 7, 2, 1)
       grid1.attach(texto1, 0, 0, 2, 1)

       grid1.set_row_spacing(15)
       grid1.set_column_spacing(10)

       medHour = Gtk.Entry()
       medHour.set_placeholder_text(_("Ej: 8"))
       labelHour = Gtk.Label(label=_("Hora"))

       medMinute = Gtk.Entry()
       medMinute.set_placeholder_text(_("Ej: 30"))
       labelMinute = Gtk.Label(label=_("Minuto"))

       grid1.attach(labelHour, 0, 1, 1, 1)
       grid1.attach(medHour, 1, 1, 1, 1)
       grid1.attach(labelMinute, 0, 2, 1, 1)
       grid1.attach(medMinute, 1, 2, 1, 1)
    
       cajaPrincipal.append(grid1)
       
       return cajaPrincipal
