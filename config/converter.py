from PyQt4 import uic 
fin = open('../ui/qtPrincipal.ui','r')
fout = open('../views/FormPrincipal.py','w')
uic.compileUi(fin,fout,execute=False)
fin.close()
fout.close()

fin = open('../ui/qtSobre.ui','r')
fout = open('../views/FormSobre.py','w')
uic.compileUi(fin,fout,execute=False)
fin.close()
fout.close()

fin = open('../ui/qtSincronizar.ui','r')
fout = open('../views/FormSincronizar.py','w')
uic.compileUi(fin,fout,execute=False)
fin.close()
fout.close()