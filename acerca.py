# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Edita
###########################################################################

class Edita ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Acerca De", pos = wx.DefaultPosition, size = wx.Size( 613,302 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU, name = u"Acerca De" )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.i_Logo = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"candado.ico", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.i_Logo, 0, wx.ALL, 5 )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.t_edita = wx.StaticText( self, wx.ID_ANY, u"EDITA 1.1.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.t_edita.Wrap( -1 )
		self.t_edita.SetFont( wx.Font( 22, 74, 90, 92, False, "Calibri" ) )
		
		bSizer2.Add( self.t_edita, 0, wx.ALL, 5 )
		
		self.t_Descri = wx.StaticText( self, wx.ID_ANY, u"Encriptador/Desencriptador Informatico de Texto Ascii 1.1.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.t_Descri.Wrap( -1 )
		bSizer2.Add( self.t_Descri, 0, wx.ALL, 5 )
		
		self.t_copyright = wx.StaticText( self, wx.ID_ANY, u"Copyright © 2016", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.t_copyright.Wrap( -1 )
		bSizer2.Add( self.t_copyright, 0, wx.ALL, 5 )
		
		self.m_staticline21 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline21, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.t_programa = wx.StaticText( self, wx.ID_ANY, u"EDITA es una herramienta de texto que permite \nencriptar o desencriptar mensajes que esten en\nel formate ASCII.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.t_programa.Wrap( -1 )
		self.t_programa.SetFont( wx.Font( 11, 74, 93, 90, False, "Arial" ) )
		
		bSizer2.Add( self.t_programa, 0, wx.ALL, 5 )
		
		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Desarrolladores:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer2.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.t_nombres = wx.StaticText( self, wx.ID_ANY, u"Manassero Franco,Marques Aldana y Pasquini Matias", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.t_nombres.Wrap( -1 )
		bSizer2.Add( self.t_nombres, 0, wx.ALL, 5 )
		
		self.m_hyperlink = wx.HyperlinkCtrl( self, wx.ID_ANY, u"Visita el sitio de ITEC Rio Cuarto", u"http://www.itec.org.ar", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
		bSizer2.Add( self.m_hyperlink, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

