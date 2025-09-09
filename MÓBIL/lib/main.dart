import 'package:flutter/material.dart';
import 'package:p2_ipm/pantallaDeLogin.dart';
import 'package:provider/provider.dart';
import 'LoginReloj.dart';
import 'modelo.dart';

void main() {
  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => Model()),
      ],
      child: MyApp(),
    ),
  );
}
class MyApp extends StatelessWidget {
  const MyApp({super.key});
  final double maxDimension = 400.0;
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'MEDICtime',
      theme: ThemeData(
        visualDensity: VisualDensity.compact,
        useMaterial3: true,
      ),
      home: Builder(
        builder: (context) {
          if (MediaQuery.of(context).size.width <= maxDimension &&
            MediaQuery.of(context).size.height <= maxDimension) {
            return LoginReloj();
          } else {
            return Inicio();
          }
        },
      ),
    );
  }
}
