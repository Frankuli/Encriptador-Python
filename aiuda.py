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
## Class Ayuda
###########################################################################

class Ayuda ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Ayuda", pos = wx.DefaultPosition, size = wx.Size( 597,479 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.Titulo = wx.StaticText( self, wx.ID_ANY, u"¿Necesitas ayuda? ", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.Titulo.Wrap( -1 )
		self.Titulo.SetFont( wx.Font( 11, 74, 90, 92, False, "Arial" ) )
		
		bSizer6.Add( self.Titulo, 0, wx.ALL, 5 )
		
		self.edita = wx.StaticText( self, wx.ID_ANY, u"EDITA 1.1.0 Copyright © 2016", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.edita.Wrap( -1 )
		bSizer6.Add( self.edita, 0, wx.ALL, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer6.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.ayudajpg = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"ayudapng.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer6.Add( self.ayudajpg, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer6, 0, wx.EXPAND, 5 )
		
		PreguntasFrecuentes = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Preguntas Frecuentes" ), wx.VERTICAL )
		
		self.m_staticText17 = wx.StaticText( PreguntasFrecuentes.GetStaticBox(), wx.ID_ANY, u"¿Qué es el código ASCII?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		self.m_staticText17.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		PreguntasFrecuentes.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		self.m_staticText18 = wx.StaticText( PreguntasFrecuentes.GetStaticBox(), wx.ID_ANY, u"ASCII (acrónimo inglés de American Standard Code for Information \nInterchange) es un código de caracteres basado en el alfabeto latino ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		PreguntasFrecuentes.Add( self.m_staticText18, 0, wx.ALL, 5 )
		
		self.m_staticline2 = wx.StaticLine( PreguntasFrecuentes.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		PreguntasFrecuentes.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText21 = wx.StaticText( PreguntasFrecuentes.GetStaticBox(), wx.ID_ANY, u"¿Cómo se realiza la conversión a ASCII?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		self.m_staticText21.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		PreguntasFrecuentes.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.m_staticText22 = wx.StaticText( PreguntasFrecuentes.GetStaticBox(), wx.ID_ANY, u"Se realiza una conversión mediante algoritmos llamados ToASCII y \nToUnicode, por el cual se aplican los algoritmos a las etiquetas del \nnombre de dominio que contengan caracteres no-ASCII.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		PreguntasFrecuentes.Add( self.m_staticText22, 0, wx.ALL, 5 )
		
		self.m_staticline6 = wx.StaticLine( PreguntasFrecuentes.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		PreguntasFrecuentes.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText19 = wx.StaticText( PreguntasFrecuentes.GetStaticBox(), wx.ID_ANY, u"¿?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		self.m_staticText19.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		PreguntasFrecuentes.Add( self.m_staticText19, 0, wx.ALL, 5 )
		
		self.m_staticText20 = wx.StaticText( PreguntasFrecuentes.GetStaticBox(), wx.ID_ANY, u". . .", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		PreguntasFrecuentes.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.m_staticline7 = wx.StaticLine( PreguntasFrecuentes.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		PreguntasFrecuentes.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( PreguntasFrecuentes.GetStaticBox(), wx.ID_ANY, u"¿Como es posible que este programa sea tan buenaso?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		self.m_staticText9.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		PreguntasFrecuentes.Add( self.m_staticText9, 0, wx.ALL, 2 )
		
		self.m_staticText10 = wx.StaticText( PreguntasFrecuentes.GetStaticBox(), wx.ID_ANY, u"Sabé ;)", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.m_staticText10.Wrap( -1 )
		PreguntasFrecuentes.Add( self.m_staticText10, 0, wx.ALL, 2 )
		
		self.m_staticline8 = wx.StaticLine( PreguntasFrecuentes.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		PreguntasFrecuentes.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText91 = wx.StaticText( PreguntasFrecuentes.GetStaticBox(), wx.ID_ANY, u"¿Para que necesito la contraseña?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )
		self.m_staticText91.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		PreguntasFrecuentes.Add( self.m_staticText91, 0, wx.ALL, 5 )
		
		self.m_staticText101 = wx.StaticText( PreguntasFrecuentes.GetStaticBox(), wx.ID_ANY, u"Por Que la contraseña es fundamental en el proceso interno de \nencriptacion y desencriptado.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )
		PreguntasFrecuentes.Add( self.m_staticText101, 0, wx.ALL, 5 )
		
		self.m_staticline9 = wx.StaticLine( PreguntasFrecuentes.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		PreguntasFrecuentes.Add( self.m_staticline9, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText24 = wx.StaticText( PreguntasFrecuentes.GetStaticBox(), wx.ID_ANY, u"¿No estas satisfecho?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		self.m_staticText24.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		PreguntasFrecuentes.Add( self.m_staticText24, 0, wx.ALL, 5 )
		
		self.m_hyperlink1 = wx.HyperlinkCtrl( PreguntasFrecuentes.GetStaticBox(), wx.ID_ANY, u"Visita este sitio web para mas info :)", u"https://es.wikipedia.org/wiki/ASCII", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
		PreguntasFrecuentes.Add( self.m_hyperlink1, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( PreguntasFrecuentes, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

