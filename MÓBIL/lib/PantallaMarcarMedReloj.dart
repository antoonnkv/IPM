import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'package:p2_ipm/modelo.dart';
import 'package:provider/provider.dart';
import 'package:p2_ipm/HistoricoReloj.dart';

class MarcarMedReloj extends StatefulWidget {
  const MarcarMedReloj({Key? key}) : super(key: key);

  @override
  _marcarMedState createState() => _marcarMedState();
}

class _marcarMedState extends State<MarcarMedReloj> {

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
              SizedBox(height: 10),
              calendario(),
              SizedBox(height: 3),
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

  Widget calendario(){
    final model = Provider.of<Model>(context, listen: true);

    return Container(

      child: Padding(
        padding: EdgeInsets.only(left: 27),
        child: Row(

          children: [
            Text(
              model.formatDate(model.dataSeleccionada),
              style: TextStyle(fontSize: 25, fontWeight: FontWeight.bold),
            ),
            SizedBox(width: 5),
            IconButton(
              icon: Icon(Icons.medication),
              onPressed: (){
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => ListaCompletaMedicamentosActivosReloj()),
                );
              },
              iconSize: 40,
            )
          ],
        ),
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
            title: Text(
              medt.med.name,
            style: TextStyle(
                fontSize: 6,
            ),),
            content: Column(
              //crossAxisAlignment: CrossAxisAlignment.start,
              //mainAxisSize: MainAxisSize.min,
              children: [
                Text(
                    "Dosis: ${medt.med.dosage} g",
                    style: TextStyle(
                      fontSize: 5,
                    ),
                ),
                Text(
                    "Fecha de inicio: ${medt.med.start_date}",
                     style: TextStyle(
                       fontSize: 5,
                     ),
                ),
                Text(
                    "Duración del tratamiento: ${medt.med.duration} días",
                    style: TextStyle(
                      fontSize: 5,
                    ),
                ),
                Text(
                    "Fecha de la toma ${DateFormat('dd/MM/yyyy HH:mm').format(medt.time)}",
                    style: TextStyle(
                      fontSize: 5,
                    ),
          )
              ],
            ),
            actions: [
              TextButton(
                child: const Text(
                    'Cerrar',
                    style: TextStyle(
                      fontSize: 6,
                    ),
                ),
                style: TextButton.styleFrom(
                  minimumSize: Size(20, 20),
                ),

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
              title: const Text(
                '¿Estás seguro de que quieres confirmar esta toma?',
                style: TextStyle(
                  fontSize: 7,
                ),
              ),
              actions: [
                Center(
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      TextButton(
                        child: const Text(
                          'Cancelar',
                          style: TextStyle(
                            fontSize: 7,
                          ),
                        ),
                        style: TextButton.styleFrom(
                          minimumSize: Size(30, 30),
                        ),
                        onPressed: () {
                          Navigator.of(context).pop();
                        },
                      ),
                      SizedBox(height: 10),
                      TextButton(
                        child: const Text(
                          'Confirmar',
                          style: TextStyle(
                            fontSize: 7,
                          ),
                        ),
                        style: TextButton.styleFrom(
                          minimumSize: Size(30, 30),
                        ),
                        onPressed: () async {
                          setState(() {
                            widget.med.taken = true;
                          });
                          await model.addIntake(widget.med.med.id, widget.med.time);
                          Navigator.of(context).pop();
                        },
                      ),
                    ],
                  ),
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
              style: const TextStyle(fontSize: 15, fontWeight: FontWeight.bold),
            ),
            Row(
              children: [
                Expanded(
                  child: Text(
                    medToday.med.name,
                    style: const TextStyle(fontSize: 10),
                  ),
                ),
                Transform.scale(
                  scale: 1,
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
