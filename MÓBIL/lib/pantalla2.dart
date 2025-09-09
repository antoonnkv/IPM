import 'package:flutter/material.dart';
import 'package:p2_ipm/modelo.dart';
import 'package:p2_ipm/pantallaDeLogin.dart';
import 'package:p2_ipm/pantallaHistoricoMedicamentos.dart';
import 'package:p2_ipm/pantallaMarcarMedicamentos.dart';
import 'package:provider/provider.dart';

class Pagina2 extends StatefulWidget {
  const Pagina2({Key? key}) : super(key: key);

  @override
  _Pagina2State createState() => _Pagina2State();
}

class _Pagina2State extends State<Pagina2> {
  int _pagAct = 0;

  @override
  Widget build(BuildContext context) {
    final modelo = Provider.of<Model>(context);
    String? nombrePaciente = modelo.pat?.name;

    return Scaffold(
      appBar: AppBar(
        title: _pagAct == 0
        ? Text(
          "Hola $nombrePaciente!",
          style: TextStyle(
            fontSize: 21,
            fontWeight: FontWeight.bold,
            color: Colors.white,
            fontFamily: 'Roboto',
          ),
        )
        : Text(
          "Mis medicaciones",
          style: TextStyle(
            fontSize: 21,
            fontWeight: FontWeight.bold,
            color: Colors.white,
            fontFamily: 'Roboto',
          ),
        ),
        backgroundColor: Colors.indigo,
        leading: _pagAct == 0
        ? IconButton(
          icon: Icon(Icons.arrow_back),
          onPressed: () {
            Navigator.pushReplacement(
              context,
              MaterialPageRoute(builder: (context) => Inicio()),
            );
          },
        )
        : null,
      ),
      body: _pagAct == 0 ? MarcarMed() : ListaCompletaMedicamentos(),
      bottomNavigationBar: BottomNavigationBar(
        onTap: (index) {
          setState(() {
            _pagAct = index;
          });
        },
        currentIndex: _pagAct,
        selectedItemColor: Colors.white,
        unselectedItemColor: Colors.grey,
        items: [
          BottomNavigationBarItem(icon: Icon(Icons.account_circle), label: ""),
          BottomNavigationBarItem(icon: Icon(Icons.add_box_outlined), label: ""),
        ],
        backgroundColor: Colors.indigo,
      ),
    );
  }
}
