import 'package:flutter/material.dart';

import 'package:flutter_test/flutter_test.dart';
import 'package:integration_test/integration_test.dart';
import 'package:p2_ipm/main.dart';
import 'package:p2_ipm/modelo.dart';
import 'package:p2_ipm/pantallaDeLogin.dart';
import 'package:p2_ipm/pantallaMarcarMedicamentos.dart';
import 'package:provider/provider.dart';
//import 'package:integration_test/integration_test.dart';


void main() {

 
  String loginCorrecto = '015-47-6999'; //este código de paciente hay que cambiarlo dependiendo de la BD de quien ejecute los test


  IntegrationTestWidgetsFlutterBinding.ensureInitialized();

  DateTime fechaHoy = DateTime.now();

  testWidgets('Login Incorrecto', (WidgetTester tester) async {
    await tester.pumpWidget(

      MaterialApp( home:
      MultiProvider(
        providers: [
          ChangeNotifierProvider(create: (_) => Model()),
        ],
        child: const MyApp(),),
      ),);

    await tester.pumpAndSettle();


    await tester.enterText(find.byType(TextField), '015476999'); //introduce código incorrecto
    await tester.pumpAndSettle();

    expect(find.text('015476999'), findsOneWidget);
    expect(find.widgetWithText(TextButton, 'Login'), findsOneWidget);


    await tester.pumpAndSettle();
    await tester.tap(find.byType(TextButton)); //pulsa el botón
    await tester.pumpAndSettle(const Duration(seconds: 3));

    await tester.pumpAndSettle();
    expect(find.widgetWithText(TextButton, 'Login'), findsOneWidget);



  }
  );

  testWidgets('Login Correcto', (WidgetTester tester) async {

    await tester.pumpWidget(

      MaterialApp( home:
      MultiProvider(
        providers: [
          ChangeNotifierProvider(create: (_) => Model()),
        ],
        child: const MyApp(),),
      ),);

    await tester.pumpAndSettle();


    await tester.enterText(find.byType(TextField), loginCorrecto); //introduce código correcto
    await tester.pumpAndSettle();

    expect(find.text(loginCorrecto), findsOneWidget);
    expect(find.widgetWithText(TextButton, 'Login'), findsOneWidget);


    await tester.pumpAndSettle();
    await tester.tap(find.byType(TextButton)); //pulsa el botón
    await tester.pumpAndSettle(const Duration(seconds: 3));

    await tester.pumpAndSettle();
    expect(find.widgetWithText(TextButton, 'Login'), findsNothing);//espera que la pantalla no cambie


  }
  );


  testWidgets('Ir a marcar Toma y Confirmar', (WidgetTester tester) async{

    await tester.pumpWidget(

      MaterialApp( home:
      MultiProvider(
        providers: [
          ChangeNotifierProvider(create: (_) => Model()),
        ],
        child: const MyApp(),),
      ),);

    await tester.pumpAndSettle();

    await tester.enterText(find.byType(TextField), loginCorrecto); //introduce código correcto
    await tester.pumpAndSettle();

    expect(find.text(loginCorrecto), findsOneWidget);
    expect(find.widgetWithText(TextButton, 'Login'), findsOneWidget);

    await tester.pumpAndSettle();

    await tester.tap(find.byType(TextButton)); //pulsa el botón
    await tester.pumpAndSettle(const Duration(seconds: 3));

    await tester.pumpAndSettle();
    expect(find.widgetWithText(TextButton, 'Login'), findsNothing);

    final encontrados = find.byType(Checkbox);
    final lista =  tester.widgetList(encontrados);
    var encontr = false;

    for(int i = 0; i < lista.length; i++){

      var elemento = lista.elementAt(i);

      if(elemento is Checkbox && elemento.value == false) {

        await tester.tap(find.byWidget(elemento));
        await tester.pumpAndSettle(const Duration(seconds: 1));
        await tester.pumpAndSettle();
        encontr = true;
        break;
      }

    }

    if(encontr == false) {

      while (encontr == false) {

        await tester.pumpAndSettle();

        Model model = Model();
        final DateTime semanaQueViene = DateTime.now().add(
            const Duration(days: 7));
        expect(find.byIcon(Icons.chevron_right), findsOneWidget);

        await tester.tap(find.byIcon(Icons.chevron_right));

        await tester.pumpAndSettle(const Duration(seconds: 3));
        await tester.pumpAndSettle();


        final encontradosD = find.byType(Checkbox);
        final listaD = tester.widgetList(encontradosD);

        for (int i = 0; i < listaD.length; i++) {

          var elemento = listaD.elementAt(i);
          if (elemento is Checkbox && elemento.value == false) {
            await tester.tap(find.byWidget(elemento));
            await tester.pumpAndSettle(const Duration(seconds: 1));
            await tester.pumpAndSettle();
            encontr = true;
            break;
          }
        }
      }
    }
    await tester.pumpAndSettle(const Duration(seconds: 3));
    await tester.pumpAndSettle();
    expect(find.text('Confirmar'),findsOneWidget);//espera que la pantalla no cambie

    await tester.tap(find.text('Confirmar'));
    expect(find.byType(Checkbox).first, findsOneWidget);
    await tester.pumpAndSettle(const Duration(seconds: 3));
    await tester.pumpAndSettle();

  });
  testWidgets('Ir a marcar Toma y Cancelar', (WidgetTester tester) async{
    await tester.pumpWidget(

      MaterialApp( home:
      MultiProvider(
        providers: [
          ChangeNotifierProvider(create: (_) => Model()),
        ],
        child: const MyApp(),),
      ),
    );

    await tester.pumpAndSettle();


    await tester.enterText(find.byType(TextField), loginCorrecto); //introduce código incorrecto
    await tester.pumpAndSettle();

    expect(find.text(loginCorrecto), findsOneWidget);
    expect(find.widgetWithText(TextButton, 'Login'), findsOneWidget);

    await tester.pumpAndSettle();
    await tester.tap(find.byType(TextButton)); //pulsa el botón

    await tester.pumpAndSettle(const Duration(seconds: 3));
    await tester.pumpAndSettle();

    expect(find.widgetWithText(TextButton, 'Login'), findsNothing);

    final encontrados = find.byType(Checkbox);
    final lista =  tester.widgetList(encontrados);

    var encontr = false;
    for(int i = 0; i < lista.length; i++){
      var elemento = lista.elementAt(i);
      if(elemento is Checkbox && elemento.value == false) {

        await tester.tap(find.byWidget(elemento));
        await tester.pumpAndSettle(const Duration(seconds: 1));
        await tester.pumpAndSettle();
        encontr = true;
        break;
      }

    }

    if(encontr == false) {

      while (encontr == false) {
        await tester.pumpAndSettle(const Duration(seconds: 3));

        await tester.pumpAndSettle();

        Model model = Model();
        final DateTime semanaQueViene = DateTime.now().add(
            const Duration(days: 7));
        

        expect(find.byIcon(Icons.chevron_right), findsOneWidget);
        await tester.tap(find.byIcon(Icons.chevron_right));

        await tester.pumpAndSettle(const Duration(seconds: 3));
        await tester.pumpAndSettle();

        final encontradosD = find.byType(Checkbox);
        final listaD = tester.widgetList(encontradosD);
        for (int i = 0; i < listaD.length; i++) {
          var elemento = listaD.elementAt(i);

          if (elemento is Checkbox && elemento.value == false) {

            await tester.tap(find.byWidget(elemento));
            await tester.pumpAndSettle(const Duration(seconds: 1));
            await tester.pumpAndSettle();
            encontr = true;
            break;

          }
        }
      }
    }

    await tester.pumpAndSettle(const Duration(seconds: 3));
    await tester.pumpAndSettle();

    expect(find.text('Cancelar'),findsOneWidget);//espera que la pantalla no cambie
    await tester.tap(find.text('Cancelar'));
    await tester.pumpAndSettle(const Duration(seconds: 3));

    expect(find.byType(Checkbox).first, findsOneWidget);
    await tester.pumpAndSettle(const Duration(seconds: 3));
    await tester.pumpAndSettle();

  });

  
  testWidgets('Scroll y ver detalles de un medicamento', (WidgetTester tester) async{
    await tester.pumpWidget(
      MaterialApp(
        home: MultiProvider(
          providers:  [
            ChangeNotifierProvider(create: (_) => Model()),
          ],
          child: const MyApp(),
        ),
      ),
    );

    await tester.pumpAndSettle();

    await tester.enterText(find.byType(TextField),loginCorrecto);
    await tester.tap(find.widgetWithText(TextButton, 'Login'));
    await tester.pumpAndSettle(const Duration(seconds: 3));
    await tester.pumpAndSettle();

    final listViewFinder = find.byType(ListView);
    expect(listViewFinder, findsOneWidget);

    await tester.fling(listViewFinder, Offset(0, -300), 3000);
    await tester.pumpAndSettle(const Duration(seconds: 3));
    await tester.pumpAndSettle();

    final firstMedicationTimeFinder = find.textContaining(':').first;
    expect(firstMedicationTimeFinder, findsOneWidget);

    await tester.tap(firstMedicationTimeFinder);
    await tester.pumpAndSettle(const Duration(seconds: 3));
    await tester.pumpAndSettle();


    expect(find.byType(AlertDialog), findsOneWidget);


    final closeButtonFinder = find.text('Cerrar');
    expect(closeButtonFinder, findsOneWidget);

    await tester.tap(closeButtonFinder);
    await tester.pumpAndSettle();


    expect(find.byType(AlertDialog), findsNothing);

  });

  testWidgets('Verifica que el día de hoy esté correcto', (WidgetTester tester) async {
    await tester.pumpWidget(
      MaterialApp( home:
      MultiProvider(
        providers: [
          ChangeNotifierProvider(create: (_) => Model()),
        ],
        child: const MyApp(),),
      ),);
    await tester.pumpAndSettle();

    //await tester.pumpWidget(MaterialApp( home:MyApp()));

    await tester.enterText(find.byType(TextField), loginCorrecto); //introduce código incorrecto

    await tester.pumpAndSettle();
    expect(find.text(loginCorrecto), findsOneWidget);
    expect(find.widgetWithText(TextButton, 'Login'), findsOneWidget);


    await tester.pumpAndSettle();
    await tester.tap(find.byType(TextButton)); //pulsa el botón
    //await tester.press(find.byType(TextButton)); //pulsa el botón
    await tester.pump(const Duration(seconds: 1));

    await tester.pumpAndSettle();
    Model model = Model();
    String AwaitedDate = model.formatDate(fechaHoy);
    expect(find.text(AwaitedDate), findsOneWidget);
  });

  testWidgets('Cambiar de dia en el calendario', (WidgetTester tester) async {
    await tester.pumpWidget(
      MaterialApp( home:
      MultiProvider(
        providers: [
          ChangeNotifierProvider(create: (_) => Model()),
        ],
        child: const MyApp(),),
      ),);
    await tester.pumpAndSettle();

    //await tester.pumpWidget(MaterialApp( home:MyApp()));

    await tester.enterText(find.byType(TextField), loginCorrecto); //introduce código incorrecto
    await tester.pumpAndSettle();
    expect(find.text(loginCorrecto), findsOneWidget);
    expect(find.widgetWithText(TextButton, 'Login'), findsOneWidget);


    await tester.pumpAndSettle();
    await tester.tap(find.byType(TextButton)); //pulsa el botón
    //await tester.press(find.byType(TextButton)); //pulsa el botón
    await tester.pump(const Duration(seconds: 1));

    await tester.pumpAndSettle();
    Model model = Model();
    final DateTime manana = fechaHoy.add(const Duration(days: 1));
    final DateTime ayer = fechaHoy.subtract(const Duration(days: 1));

    Finder dateFind = find.text(manana.day.toString());
    String AwaitedDate = model.formatDate(manana);

    if (tester.any(dateFind)) {
      await tester.tap(dateFind);
      await tester.pump(const Duration(seconds: 1));
      await tester.pumpAndSettle();
      expect(find.text(AwaitedDate), findsOneWidget);
    } else {
      AwaitedDate = model.formatDate(ayer);
      dateFind = find.text(ayer.day.toString());
      await tester.tap(dateFind);
      await tester.pump(const Duration(seconds: 1));
      await tester.pumpAndSettle();
      expect(find.text(AwaitedDate), findsOneWidget);
      await tester.pumpAndSettle();
    }//subtractsubtract
  });

  testWidgets('Avanzar de semana en el calendario', (WidgetTester tester) async {
    await tester.pumpWidget(
      MaterialApp( home:
      MultiProvider(
        providers: [
          ChangeNotifierProvider(create: (_) => Model()),
        ],
        child: const MyApp(),),
      ),);
    await tester.pumpAndSettle();

    //await tester.pumpWidget(MaterialApp( home:MyApp()));

    await tester.enterText(find.byType(TextField), loginCorrecto); //introduce código incorrecto
    await tester.pumpAndSettle();
    expect(find.text(loginCorrecto), findsOneWidget);
    expect(find.widgetWithText(TextButton, 'Login'), findsOneWidget);


    await tester.pumpAndSettle();
    await tester.tap(find.byType(TextButton)); //pulsa el botón
    //await tester.press(find.byType(TextButton)); //pulsa el botón
    await tester.pump(const Duration(seconds: 1));

    await tester.pumpAndSettle();
    Model model = Model();
    final DateTime semanaQueViene = fechaHoy.add(const Duration(days: 7));
    String AwaitedDate = model.formatDate(semanaQueViene);
    expect(find.byIcon(Icons.chevron_right), findsOneWidget);
    await tester.tap(find.byIcon(Icons.chevron_right));

    await tester.pump(const Duration(seconds: 1));
    await tester.pumpAndSettle();
    expect(find.text(AwaitedDate), findsOneWidget);
  });

  testWidgets('Retroceder de semana en el calendario', (WidgetTester tester) async {
    await tester.pumpWidget(
      MaterialApp( home:
      MultiProvider(
        providers: [
          ChangeNotifierProvider(create: (_) => Model()),
        ],
        child: const MyApp(),),
      ),);
    await tester.pumpAndSettle();

    //await tester.pumpWidget(MaterialApp( home:MyApp()));

    await tester.enterText(find.byType(TextField), loginCorrecto); //introduce código incorrecto
    await tester.pumpAndSettle();
    expect(find.text(loginCorrecto), findsOneWidget);
    expect(find.widgetWithText(TextButton, 'Login'), findsOneWidget);


    await tester.pumpAndSettle();
    await tester.tap(find.byType(TextButton)); //pulsa el botón
    //await tester.press(find.byType(TextButton)); //pulsa el botón
    await tester.pump(const Duration(seconds: 1));

    await tester.pumpAndSettle();
    Model model = Model();
    final DateTime semanaQueViene = fechaHoy.subtract(const Duration(days: 7));
    String AwaitedDate = model.formatDate(semanaQueViene);
    expect(find.byIcon(Icons.chevron_left), findsOneWidget);
    await tester.tap(find.byIcon(Icons.chevron_left));
    await tester.pump(const Duration(seconds: 1));
    await tester.pumpAndSettle();
    expect(find.text(AwaitedDate), findsOneWidget);
  });




  testWidgets('Cerrar sesión desde la flecha del AppBar', (WidgetTester tester) async {
    await tester.pumpWidget(
      MaterialApp(
        home: MultiProvider(
          providers: [
            ChangeNotifierProvider(create: (_) => Model()),
          ],
          child: const MyApp(),
        ),
      ),
    );
    await tester.pumpAndSettle();


    await tester.enterText(find.byType(TextField),loginCorrecto);
    await tester.tap(find.widgetWithText(TextButton, 'Login'));
    await tester.pumpAndSettle(const Duration(seconds: 1));


    expect(find.textContaining('Hola'), findsOneWidget);


    final backButtonFinder = find.byIcon(Icons.arrow_back);
    expect(backButtonFinder, findsOneWidget);

    await tester.tap(backButtonFinder);
    await tester.pumpAndSettle();

    expect(find.byType(Inicio), findsOneWidget);
    expect(find.text('Login'), findsOneWidget);
  });


}


