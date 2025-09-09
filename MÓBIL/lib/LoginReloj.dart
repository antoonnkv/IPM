import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'PantallaMarcarMedReloj.dart';
import 'modelo.dart';

class LoginReloj extends StatefulWidget {
  LoginReloj({Key? key}) : super(key: key);

  @override
  _InicioState createState() => _InicioState();
}

class _InicioState extends State<LoginReloj> {
  final TextEditingController _controller = TextEditingController();
  String _patientCode = '';

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: cuerpo(context),
    );
  }

  Widget cuerpo(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        image: DecorationImage(
          image: NetworkImage(
              "https://img.freepik.com/premium-photo/blue-minimalist-wallpaper_889056-12824.jpg"),
          fit: BoxFit.cover,
        ),
      ),
      child: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            //NombreApk1(),
           // NombreApk2(),
           // SizedBox(height: 50),
            CodigoPaciente(_controller, (code) {
              setState(() {
                _patientCode = code;
              });
            }),
            //SizedBox(height: 30),
            botonLogin(context),
          ],
        ),
      ),
    );
  }

  Widget NombreApk1() {
    return Text(
      "MEDICtime",
      style: TextStyle(
        color: Colors.indigo,
        fontSize: 70.0,
        fontFamily: 'Roboto',
        fontWeight: FontWeight.w900,
      ),
    );
  }

  Widget NombreApk2() {
    return Text(
      "tu salud, a tiempo",
      style: TextStyle(
        color: Colors.white,
        fontSize: 40.0,
        fontWeight: FontWeight.bold,
      ),
    );
  }

  Widget CodigoPaciente(
      TextEditingController controller, Function(String) onCodeChanged) {
    return Container(
      padding: EdgeInsets.symmetric(horizontal: 40, vertical: 5),
      child: TextField(
        controller: controller,
        onChanged: onCodeChanged,
        keyboardType: TextInputType.number,
        style: TextStyle(
          fontSize: 20,
          color: Colors.white,
          fontStyle: FontStyle.italic,
        ),
        decoration: InputDecoration(
          hintText: "Código de Paciente",
          hintStyle: TextStyle(
            fontSize: 14,
            color: Colors.white,
            fontStyle: FontStyle.italic,
          ),
          enabledBorder: OutlineInputBorder(
            borderRadius: BorderRadius.circular(25),
            borderSide: BorderSide(
              color: Colors.grey,
              width: 1.0,
            ),
          ),
          focusedBorder: OutlineInputBorder(
            borderRadius: BorderRadius.circular(25),
            borderSide: BorderSide(
              color: Colors.blue,
              width: 2.5,
            ),
          ),
          fillColor: Colors.indigo,
          filled: true,
        ),
      ),
    );
  }

  Widget botonLogin(BuildContext context) {
    return Container(
      width: 150,
      child: TextButton(
        style: TextButton.styleFrom(
          backgroundColor: Colors.indigo,
          padding: EdgeInsets.symmetric(horizontal: 30, vertical: 10),
        ),
        onPressed: () async {
          final model = Provider.of<Model>(context, listen: false);

          if (_patientCode.isEmpty) {
            ScaffoldMessenger.of(context).showSnackBar(SnackBar(
              content: Text('Por favor ingresa el código de paciente'),
            ));
            return;
          }

          try {
            await model.getPatientId(_patientCode);
            await model.getMedList();
            await model.initHomepage();
            await model.getActiveMedications();
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => MarcarMedReloj()),
            );
          } catch (e) {
            ScaffoldMessenger.of(context).showSnackBar(SnackBar(
              content: Text('Error: ${e.toString()}'),
            ));
          }
        },
        child: Text(
          "Login",
          style: TextStyle(
            fontSize: 17,
            color: Colors.white,
            fontWeight: FontWeight.bold,
          ),
        ),
      ),
    );
  }
}
