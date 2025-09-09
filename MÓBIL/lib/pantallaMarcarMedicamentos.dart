import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'package:p2_ipm/modelo.dart';
import 'package:provider/provider.dart';

class MarcarMed extends StatefulWidget {
  const MarcarMed({Key? key}) : super(key: key);

  @override
  _marcarMedState createState() => _marcarMedState();
}

class _marcarMedState extends State<MarcarMed> {

  @override
  void initState() {
    super.initState();
  }


  @override
  Widget build(BuildContext context) {
    final model = Provider.of<Model>(context);
    return Scaffold(
      body: Container(
        decoration: BoxDecoration(
          image: DecorationImage(
            image: NetworkImage(
                "https://img.freepik.com/vector-gratis/fondo-decorativo-textura-diseno-trazo-pincel-acuarela-azul-suave_1055-17681.jpg"),
            fit: BoxFit.cover,
          ),
        ),
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            children: [
              calendario(),
              SizedBox(height: 30),
              Expanded(
              child: ListView(
                children: model.medListToday
                    .map((medication) => Check(
                          med: medication,
                          today: model.dataSeleccionada
                        ))
                    .toList(),
              ),
            ),
            ],
          ),
        ),
      ),
    );
  }

  Widget calendario() {
    final model = Provider.of<Model>(context, listen: true);
    return Container(
      height: 100,
      child: Column(
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              IconButton(
                icon: Icon(Icons.chevron_left),
                onPressed: () async {
                  await model.retrocederSemanas();
                },
              ),
              Text(
                model.formatDate(model.dataSeleccionada),
                style: TextStyle(fontSize: 30, fontWeight: FontWeight.bold),
              ),
              IconButton(
                icon: Icon(Icons.chevron_right),
                onPressed: () async {
                  await model.avanzarSemanas();
                },
              ),
            ],
          ),
          SizedBox(height: 10),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: model.semanas.map((date) {
              return GestureDetector(
                onTap: () async {
                  await model.seleccionarData(date);
                },
                child: Container(
                  width: 40,
                  height: 40,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    color: date.day == model.dataSeleccionada.day
                        ? Colors.indigo
                        : Colors.transparent,
                  ),
                  child: Center(
                    child: Text(
                      '${date.day}',
                      style: TextStyle(
                        color: date.day == model.dataSeleccionada.day
                            ? Colors.white
                            : Colors.black, fontSize: 20,
                      ),
                    ),
                  ),
                ),
              );
            }).toList(),
          ),
        ],
      ),
    );
  }


}

class Check extends StatefulWidget {
  final MedicationToday med;
  final DateTime today;

  const Check({Key? key, required this.med, required this.today}) : super(key: key);

  @override
  _CheckState createState() => _CheckState();
}

class _CheckState extends State<Check> {
  
  @override
  void initState() {
    super.initState();
  }

  void _mostrarDetallesMed(BuildContext context, MedicationToday medt) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text(medt.med.name),
          content: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            mainAxisSize: MainAxisSize.min,
            children: [
              Text("Dosis: ${medt.med.dosage} g"),
              Text("Fecha de inicio: ${medt.med.start_date}"),
              Text("Duración del tratamiento: ${medt.med.duration} días"),
              Text("Fecha de la toma ${DateFormat('dd/MM/yyyy HH:mm').format(medt.time)}")
            ],
          ),
          actions: [
            TextButton(
              child: const Text('Cerrar'),
              onPressed: () {
                Navigator.of(context).pop();
              },
            ),
          ],
        );
      }
    );
  }

  void _confirmarToma(BuildContext context) {
    final model = Provider.of<Model>(context, listen: false);
    if (!widget.med.taken) {
      showDialog(
        context: context,
        builder: (BuildContext context) {
          return AlertDialog(
            title: const Text('Confirmar toma'),
            content: const Text('¿Estás seguro de que quieres confirmar esta toma?'),
            actions: [
              TextButton(
                child: const Text('Cancelar'),
                onPressed: () {
                  Navigator.of(context).pop();
                },
              ),
              TextButton(
                child: const Text('Confirmar'),
                onPressed: () async {
                  setState(() {
                    widget.med.taken = true;
                  });
                  await model.addIntake(widget.med.med.id, widget.med.time);
                  Navigator.of(context).pop();
                },
              ),
            ],
          );
        }
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    MedicationToday medToday = widget.med;
    String hora = DateFormat('HH:mm').format(medToday.time);
    
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: GestureDetector(
        onTap: () {
          _mostrarDetallesMed(context, medToday);
        },
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              hora,
              style: const TextStyle(fontSize: 35, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 8),
            Row(
              children: [
                Expanded(
                  child: Text(
                    medToday.med.name,
                    style: const TextStyle(fontSize: 25),
                  ),
                ),
                Transform.scale(
                  scale: 1.75,
                  child: Checkbox(
                    value: widget.med.taken,
                    onChanged: widget.med.taken ? null : (bool? value) {
                      _confirmarToma(context);
                    },
                  ),
                )
              ],
            ),
          ],
        ),
      ),
    );
  }
}
