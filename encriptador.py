from wx import*
from encrip import*
from ventanita import*
from acerca import *
from aiuda import*

class MiAyuda (Ayuda):
    def __init__(self):
        Ayuda.__init__(self, None)

class MiAcerca(Edita):
    def __init__(self):
        Edita.__init__(self, None)

class Enc (Mold):
    def __init__(self,parent):
        Mold.__init__(self,None)
        self.b_encrip.Disable()
        self.b_desen.Disable()
        self.Bind(EVT_MENU,self.cerrar,self.m_salir)
        self.Bind(EVT_MENU,self.abrir,self.m_abrir)
        self.Bind(EVT_MENU,self.guardar,self.m_guardar)
        self.Bind(EVT_MENU,self.guardarComo,self.m_guardarC)
        self.Bind(EVT_MENU,self.nuevo,self.m_nuevo)
        self.Bind(EVT_MENU, self.acercade, self.b_acerca)
        self.Bind(EVT_MENU, self.ayuda, self.m_ayuda)
        self.b_encrip.Bind(EVT_BUTTON,self.encriptar)
        self.b_desen.Bind(EVT_BUTTON,self.desencriptar)
        self.c_con.Bind(EVT_CHAR, self.teclazo)
        self.c_1.Bind(EVT_CHAR, self.tab)

    def tab (self, event):
        print event.GetKeyCode()
        if event.GetKeyCode()==9:
            self.c_con.SetFocus()

        else:
            event.Skip()

    def teclazo(self, event):
        if (48 <= event.GetKeyCode() <= 57)or event.GetKeyCode()==8 or event.GetKeyCode()==127:
            event.Skip()

        if len(self.c_con.GetValue()) >= 3:
            self.b_encrip.Enable()
            self.b_desen.Enable()
        else:
            self.b_encrip.Disable()
            self.b_desen.Disable()

    def abrir (self, e):
        men = self.c_2.GetValue()
        if men!= ' ':
            self.dlg = FileDialog(None, "Abrir ...", "", "Documentos de texto (*.txt)|*.txt", style=FD_OPEN)
            self.dlg.ShowModal()
            self.archivo= self.dlg.GetPath()
            self.c_2.SetLabelText('')
            f = open(self.archivo, 'r')
            txt = f.read().decode('utf-8')
            f.close()
            self.SetTitle(self.dlg.GetFilename())
            self.c_1.SetValue(txt)
            self.dlg.Destroy()

    def nuevo(self,e):
        men = self.c_2.GetValue()
        if men != ' ':
            self.ventanita()
        else:
            self.c_1.SetLabelText(' ')
            self.c_2.SetLabelText(' ')
            self.c_con.SetLabelText(' ')

    def guardar(self,e):
        if self.GetTitle() == 'Encriptador':
            self.guardarComo(e)
        else:
            txt = self.c_2.GetValue()
            f = open(self.archivo, "w")
            f.write(txt.encode('utf8'))
            f.close()

    def guardarComo(self,e):
        self.dlg = FileDialog(self, "Guardar Como...", "", "","Documentos de texto (*.txt)|*.txt",FD_SAVE )
        self.dlg.ShowModal()
        self.archivo=self.dlg.GetPath()
        txt = self.c_2.GetValue()
        f = open(self.archivo, "w")
        f.write(txt.encode('utf8'))
        f.close()
        self.dlg.Destroy()

    def cerrar (self, e):
        self.Close()

    def desencriptar (self,e):
        memcrip = []
        men = self.c_1.GetValue()
        con = self.c_con.GetValue()
        j = 0
        for x in range(len(men)):
            if 90 >= (ord(men[x])) >= 65 or 122 >= (ord(men[x])) >= 97:
                c = ord(men[x]) - int(con[j])
                if (c > 90 and c < 97) or c < 65:
                    memcrip.append(chr(c + 26))
                else:
                    memcrip.append(chr(c))
                j += 1
            else:
                memcrip.append(men[x])
            if j == 4:
                j = 0
        t = ''
        for x in range(len(memcrip)):
            t = t + memcrip[x]
        self.c_con.SetLabelText('')
        self.c_1.SetLabelText('')
        self.c_2.SetLabelText(t)

    def encriptar (self,e):
        memcrip=[]
        men=self.c_1.GetValue()
        con=self.c_con.GetValue()
        j=0
        for x in range (len(men)):
            if 90>=(ord(men[x]))>=65 or 122>=(ord(men[x]))>=97:
                c=ord(men[x])+int(con[j])
                if (c>90 and c<97) or c>122:
                    memcrip.append(chr(c-26))
                else:
                    memcrip.append(chr(c))
                j+=1
            else:
                memcrip.append(men[x])
            if j==4:
                j=0
        t=''
        for x in range(len(memcrip)):
            t=t+memcrip[x]
        self.c_con.SetLabelText('')
        self.c_1.SetLabelText('')
        self.c_2.SetLabelText(t)

    def acercade(self, e):
        a = MiAcerca()
        a.Show()

    def ventanita(self):
        a=MiVentana()
        a.Show()

    def ayuda(self,e):
        a=MiAyuda()
        a.Show()

class MiVentana(Ven,Enc):
    def __init__(self):
        Ven.__init__(self,None)
        self.Bind(EVT_BUTTON,self.guar,self.b_gd)

    def guar (self,e):
        self.guardar(e)

class MiAplicacion (App):
    def OnInit(self):
        self.frame=Enc(None)
        self.frame.Show()
        return True
app=MiAplicacion()
app.MainLoop()
