import commands
import sys
import time

from crontab import CronTab

import lib.Control_Archivos2  as Ca
import lib.Control_Automatico  as Cu



#Log_Actualizador('4. Cambiar nombre de firmware en ejecucion')
res = commands.getoutput('[ -d /home/pi/FirmwareBK2 ] && echo "Existe" || echo "NO_existe"')
print res 