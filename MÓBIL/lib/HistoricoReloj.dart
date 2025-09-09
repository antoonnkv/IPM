import 'package:flutter/material.dart';
import 'package:p2_ipm/PantallaMarcarMedReloj.dart';
import 'package:provider/provider.dart';
import 'modelo.dart';

class ListaCompletaMedicamentosActivosReloj extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final model = Provider.of<Model>(context);
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.blue[100],
        title: Text('\nMedicación activa:',
                    style: TextStyle(color: Colors.indigo[800],
                                     fontSize: 15,
                                     fontWeight: FontWeight.bold),
                    textAlign: TextAlign.center,),
                     centerTitle: true,
                     toolbarHeight: 60,
      ),
      body: Flexible(
        flex: 3,
        child: Container(
          alignment: Alignment.center,
          decoration: BoxDecoration(
            image: DecorationImage(
              image: NetworkImage(
                "https://img.freepik.com/vector-gratis/fondo-decorativo-textura-diseno-trazo-pincel-acuarela-azul-suave_1055-17681.jpg"),
                fit: BoxFit.cover,
            ),
          ),
          child: model.activeMedList.isEmpty
          ? Center(
            child: Text(
              "No hay medicamentos disponibles",
              style: TextStyle(color: Colors.white, fontSize: 8),
            ),
          )
          : ListView.builder(
            itemCount: model.activeMedList.length,
            itemBuilder: (context, index) {
              final medication = model.activeMedList[index];
              return ListTile(
                title: Column(
                  crossAxisAlignment: CrossAxisAlignment.center,

                  children: [
                    SizedBox(height: 15),
                    Text(
                      medication.name,

                      style: TextStyle(
                        fontWeight: FontWeight.bold,
                        fontSize: 15,
                        color: Colors.indigo,
                      ),
                      textAlign: TextAlign.right,),
                      SizedBox(height: 1
                      ),
                      Text('Dosis:${medication.dosage}',
                           style: TextStyle(
                             fontWeight: FontWeight.bold,
                             fontSize: 15,
                             color: Colors.black),
                           textAlign: TextAlign.right,
                      ),
                      SizedBox(height: 1),
                      Text('Duración:${medication.duration} días',
                           style: TextStyle(
                             fontWeight: FontWeight.bold,
                             fontSize: 15,
                             color: Colors.black),
                           textAlign: TextAlign.right,),
                  ],
                ),
              );
            },
          ),
        ),
      ),
    );
  }
}
