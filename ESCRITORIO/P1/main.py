from presenter import *

##INTERNACIONALIZACIÓN

import locale
import gettext
from pathlib import Path

#Configuración locale
locale.setlocale(locale.LC_ALL,'')

#Directorio donde se encuentra locale
LOCALE_DIR = Path(__file__).parent/"locale"
locale.bindtextdomain('AppI18n', LOCALE_DIR)

gettext.bindtextdomain('AppI18n', LOCALE_DIR)
gettext.textdomain('AppI18n')

##


app = MyApp(application_id="com.appMedicamentos.IPM")
app.run(None)
