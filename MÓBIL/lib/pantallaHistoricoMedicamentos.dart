import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'modelo.dart';

class ListaCompletaMedicamentos extends StatelessWidget {
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
        child: Column(
          children: [

            Expanded(
              child: Container(
                padding: EdgeInsets.all(16.0),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [

                    Text(
                      "Medicamentos Activos",
                      style: TextStyle(
                        color: Colors.indigo,
                        fontSize: 24,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    SizedBox(height: 8),
                    Expanded(
                      child: model.activeMedList.isEmpty
                      ? Center(
                        child: Text(
                          "No hay medicamentos activos disponibles",
                          style: TextStyle(
                            color: Colors.indigo,
                            fontSize: 18,
                          ),
                        ),
                      )
                      : ListView.builder(
                        itemCount: model.activeMedList.length,
                        itemBuilder: (context, index) {
                          final medication = model.activeMedList[index];
                          return ListTile(
                            title: Column(
                              crossAxisAlignment:
                              CrossAxisAlignment.start,
                              children: [
                                Text(
                                  medication.name,
                                  style: TextStyle(
                                    fontWeight: FontWeight.bold,
                                    fontSize: 17,
                                    color: Colors.indigo,
                                  ),
                                ),
                                SizedBox(height: 4),
                                Text(
                                  'Dosis: ${medication.dosage}',
                                  style: TextStyle(
                                    fontWeight: FontWeight.bold,
                                    fontSize: 20,
                                    color: Colors.black,
                                  ),
                                ),
                                SizedBox(height: 4),
                                Text(
                                  'Duración: ${medication.duration} días',
                                  style: TextStyle(
                                    fontWeight: FontWeight.bold,
                                    fontSize: 20,
                                    color: Colors.black,
                                  ),
                                ),
                              ],
                            ),
                          );
                        },
                      ),
                    ),
                  ],
                ),
              ),
            ),
            Divider(
              color: Colors.indigo,
              thickness: 2,
            ),

            Expanded(
              child: Container(
                padding: EdgeInsets.all(16.0),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [

                    Text(
                      "Medicamentos No Activos",
                      style: TextStyle(
                        color: Colors.indigo,
                        fontSize: 24,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    SizedBox(height: 8),
                    Expanded(
                      child: model.notActiveMedList.isEmpty
                      ? Center(
                        child: Text(
                          "No hay medicamentos no activos disponibles",
                          style: TextStyle(
                            color: Colors.indigo,
                            fontSize: 18,
                          ),
                        ),
                      )
                      : ListView.builder(
                        itemCount: model.notActiveMedList.length,
                        itemBuilder: (context, index) {
                          final medication = model.notActiveMedList[index];
                          return ListTile(
                            title: Column(
                              crossAxisAlignment:
                              CrossAxisAlignment.start,
                              children: [
                                Text(
                                  medication.name,
                                  style: TextStyle(
                                    fontWeight: FontWeight.bold,
                                    fontSize: 17,
                                    color: Colors.indigo,
                                  ),
                                ),
                                SizedBox(height: 4),
                                Text(
                                  'Dosis: ${medication.dosage}',
                                  style: TextStyle(
                                    fontWeight: FontWeight.bold,
                                    fontSize: 20,
                                    color: Colors.black,
                                  ),
                                ),
                                SizedBox(height: 4),
                                Text(
                                  'Duración: ${medication.duration} días',
                                  style: TextStyle(
                                    fontWeight: FontWeight.bold,
                                    fontSize: 20,
                                    color: Colors.black,
                                  ),
                                ),
                              ],
                            ),
                          );
                        },
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

