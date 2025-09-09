import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:http/http.dart' as http;
import 'package:intl/intl.dart';


//const String URL_DE_SERVIDOR = "http://localhost:8000";
const String URL_DE_SERVIDOR = "http://10.0.2.2:8000"; //emulador androidStudio


class ModelException implements Exception {
  final String message;
  ModelException(this.message);
}

class dbItem {
  Map<String, dynamic> data;
  dbItem(this.data);
}


class Patient{
  int id;
  String name;
  Patient(dbItem db) :
        id = db.data['id'],
        name = db.data['name'];
}

class Medication{
  int id;
  String name;
  double dosage;
  String start_date;
  int duration;
  Medication(dbItem db) :
        id = db.data['id'],
        name = db.data['name'],
        dosage = db.data['dosage'],
        start_date = db.data['start_date'],
        duration = db.data['treatment_duration'];
}

class Posology{
  int hour;
  int minute;
  Posology(dbItem db) :
        hour = db.data['hour'],
        minute = db.data['minute'];
}

class Intake{
  DateTime date;
  Intake(dbItem db) :
        date = DateFormat("yyyy-MM-dd'T'HH:mm").parse(db.data['date']);
}

class MedicationToday{
  Medication med;
  DateTime time;
  bool taken;
  MedicationToday(Medication med1, bool taken1, DateTime time1):
        med = med1,
        time = time1,
        taken = taken1;
}

class Model extends ChangeNotifier{
  Patient? _pat;
  List<Intake> _intk = [];
  List<Posology> _pos = [];
  List<MedicationToday> _medListToday = [];
  List<Medication> _medList = [];
  List<Medication> _activeMedList = [];
  List<Medication> _notActiveMedList = [];
  DateTime _dataSeleccionada = DateTime.now();
  late List<DateTime> _semanas = [];

  List<Medication> get activeMedList => _activeMedList;
  List<Medication> get notActiveMedList => _notActiveMedList;

  List<MedicationToday> get medListToday => _medListToday;
  List<Medication> get medList => _medList;
  Patient? get pat => _pat;
  DateTime get dataSeleccionada => _dataSeleccionada;
  List<DateTime> get semanas => _semanas;

  getPatient(String patientId) async {
    var url = "$URL_DE_SERVIDOR/patients?code=$patientId";
    final response = await http.get(Uri.parse(url));
    if (response.statusCode == 200) {
      dbItem db = dbItem(json.decode(response.body));
      _pat = Patient(db);
      notifyListeners();
    } else {
      throw ModelException(json.decode(response.body)['detail']);
    }
  }

  getPatientId(String id) async {
    var url = "$URL_DE_SERVIDOR/patients/$id";
    final response = await http.get(Uri.parse(url));
    if (response.statusCode == 200) {
      dbItem db = dbItem(json.decode(response.body));
      _pat = Patient(db);
      notifyListeners();
    } else {
      throw ModelException(json.decode(response.body)['detail']);
    }
  }

  getMedList() async {
    int? index1;
    int? count;
    int? patientId = _pat?.id;
    var url = "$URL_DE_SERVIDOR/patients/$patientId/medications";

    if (index1 != null || count != null) {
      url += "?";
      if (index1 != null) url += "start_index=$index1&";
      if (count != null) url += "count=$count";
    }

    final response = await http.get(Uri.parse(url));
    if (response.statusCode == 200) {
      List<dynamic> data = json.decode(response.body);
      _medList.clear();
      for(var item in data){
        dbItem db = dbItem(item);
        Medication md = Medication(db);
        _medList.add(md);
      }
    } else {
      throw ModelException(json.decode(response.body)['detail']);
    }
  }

  getPosList(int medID) async {
    int? index1;
    int? count;
    int? patientId = _pat?.id;
    var url = "$URL_DE_SERVIDOR/patients/$patientId/medications/$medID/posologies";

    if (index1 != null || count != null) {
      url += "?";
      if (index1 != null) url += "start_index=$index1&";
      if (count != null) url += "count=$count";
    }

    final response = await http.get(Uri.parse(url));
    if (response.statusCode == 200) {
      List<dynamic> data = json.decode(response.body);
      _pos.clear();
      for(var item in data){
        dbItem db = dbItem(item);
        Posology pos = Posology(db);
        _pos.add(pos);
      }
      notifyListeners();
    } else {
      throw ModelException(json.decode(response.body)['detail']);
    }
  }

  getIntakeList(int medID) async {
    int? index1;
    int? count;
    int? patientId = _pat?.id;
    var url = "$URL_DE_SERVIDOR/patients/$patientId/medications/$medID/intakes";

    if (index1 != null || count != null) {
      url += "?";
      if (index1 != null) url += "start_index=$index1&";
      if (count != null) url += "count=$count";
    }

    final response = await http.get(Uri.parse(url));
    if (response.statusCode == 200) {
      List<dynamic> data = json.decode(response.body);
      _intk.clear();
      for(var item in data){
        dbItem db = dbItem(item);
        Intake intk = Intake(db);
        _intk.add(intk);
      }
    } else {
      throw ModelException(json.decode(response.body)['detail']);
    }
  }

  getMedicationsToday(DateTime date) async {
    _medListToday.clear();
    for (var med in _medList) {
      await getPosList(med.id);
      await getIntakeList(med.id);
      DateTime startDate = DateTime.parse(med.start_date);
      DateTime endDate = startDate.add(Duration(days: med.duration * 365));
      if (date.isBefore(startDate) || date.isAfter(endDate)) continue;

      if (_pos.isNotEmpty) {
        for (var pos in _pos) {
          DateTime medicationTime = DateTime(
            date.year,
            date.month,
            date.day,
            pos.hour,
            pos.minute,
          );

          bool isTaken = _intk.any((intake) {
            return intake.date.year == date.year &&
                intake.date.month == date.month &&
                intake.date.day == date.day &&
                intake.date.hour == pos.hour &&
                intake.date.minute == pos.minute;
          });

          _medListToday.add(MedicationToday(med,isTaken,medicationTime));
        }
      }
      _medListToday.sort((a, b) => a.time.compareTo(b.time));
    }
  }

  getActiveMedications() async {
      DateTime hoy = DateTime.now();
      _activeMedList.clear();
      _notActiveMedList.clear();
      for(Medication med in _medList){
        DateTime startDate = DateTime.parse(med.start_date);
        DateTime endDate = startDate.add(Duration(days: med.duration * 365));
        if (hoy.isBefore(startDate) || hoy.isAfter(endDate)) _notActiveMedList.add(med);
        else _activeMedList.add(med);
      }
      notifyListeners();
  }

  addIntake(int medId, DateTime date) async {
    int? patientId = _pat?.id;
    String formattedDate = DateFormat("yyyy-MM-dd'T'HH:mm").format(date);
    var url = "$URL_DE_SERVIDOR/patients/$patientId/medications/$medId/intakes";
    final intakeItem = {
      "id": null,
      "date": formattedDate,
      "medication_id": medId,
    };
    final response = await http.post(Uri.parse(url),headers: {"Content-Type": "application/json"},body: json.encode(intakeItem));
    if (response.statusCode != 201) throw ModelException(json.decode(response.body)['detail']);
  }

  actualizarSemanas() {
    _semanas = List.generate(7, (index) {
      return _dataSeleccionada.subtract(
        Duration(days: _dataSeleccionada.weekday - index - 1));
    });
  }

  seleccionarData(DateTime date) async {
    _dataSeleccionada = date;
    await getMedicationsToday(_dataSeleccionada);
    notifyListeners();
  }

  retrocederSemanas() async {
    _dataSeleccionada = _dataSeleccionada.subtract(Duration(days: 7));
    actualizarSemanas();
    await getMedicationsToday(_dataSeleccionada);
    notifyListeners();
  }

  avanzarSemanas() async {
    _dataSeleccionada = _dataSeleccionada.add(Duration(days: 7));
    actualizarSemanas();
    await getMedicationsToday(_dataSeleccionada);
    notifyListeners();
  }

  initHomepage() async {
    actualizarSemanas();
    await getMedicationsToday(_dataSeleccionada);
    notifyListeners();
  }

  String formatDate(DateTime date) {
    final months = [
      'Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun',
      'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'
    ];
    return '${date.day} ${months[date.month - 1]}';
  }

}
