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
## Class Mold
###########################################################################

class Mold ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Encriptador", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.CAPTION|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menu3 = wx.Menu()
		self.m_abrir = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Abrir\tCtrl-O", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_abrir.SetBitmap( wx.Bitmap( u"iconos para menu/folder_open.ico", wx.BITMAP_TYPE_ANY ) )
		self.m_menu3.AppendItem( self.m_abrir )
		
		self.m_nuevo = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Nuevo\tCtrl-N", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_nuevo.SetBitmap( wx.Bitmap( u"iconos para menu/window_new.ico", wx.BITMAP_TYPE_ANY ) )
		self.m_menu3.AppendItem( self.m_nuevo )
		
		self.m_guardar = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Guardar\tCtrl-S", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_guardar.SetBitmap( wx.Bitmap( u"iconos para menu/save.ico", wx.BITMAP_TYPE_ANY ) )
		self.m_menu3.AppendItem( self.m_guardar )
		
		self.m_guardarC = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Guardar como\tCtrl-Shift-S", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_guardarC.SetBitmap( wx.Bitmap( u"iconos para menu/save_as.ico", wx.BITMAP_TYPE_ANY ) )
		self.m_menu3.AppendItem( self.m_guardarC )
		
		self.m_imprimir = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Imprimir\tCtrl-P", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_imprimir.SetBitmap( wx.Bitmap( u"iconos para menu/printer.ico", wx.BITMAP_TYPE_ANY ) )
		self.m_menu3.AppendItem( self.m_imprimir )
		
		self.m_menubar2.Append( self.m_menu3, u"Archivo" ) 
		
		self.m_menu41 = wx.Menu()
		self.m_ayuda = wx.MenuItem( self.m_menu41, wx.ID_ANY, u"Ver ayuda\tCtrl-F1", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_ayuda.SetBitmap( wx.Bitmap( u"iconos para menu/help_browser.ico", wx.BITMAP_TYPE_ANY ) )
		self.m_menu41.AppendItem( self.m_ayuda )
		
		self.b_acerca = wx.MenuItem( self.m_menu41, wx.ID_ANY, u"Acerca de", wx.EmptyString, wx.ITEM_NORMAL )
		self.b_acerca.SetBitmap( wx.Bitmap( u"iconos para menu/toolbar_get_info.ico", wx.BITMAP_TYPE_ANY ) )
		self.m_menu41.AppendItem( self.b_acerca )
		
		self.m_menubar2.Append( self.m_menu41, u"Ayuda" ) 
		
		self.m_menu4 = wx.Menu()
		self.m_salir = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"Salir\tCtrl-Q", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_salir.SetBitmap( wx.Bitmap( u"iconos para menu/dialog_close.ico", wx.BITMAP_TYPE_ANY ) )
		self.m_menu4.AppendItem( self.m_salir )
		
		self.m_menubar2.Append( self.m_menu4, u"Cerrar" ) 
		
		self.SetMenuBar( self.m_menubar2 )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.c_1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 4,100 ), 0 )
		self.c_1.SetMaxLength( 150 ) 
		bSizer2.Add( self.c_1, 0, wx.ALL|wx.EXPAND, 2 )
		
		gSizer1 = wx.GridSizer( 1, 3, 0, 0 )
		
		self.c_con = wx.TextCtrl( self, wx.ID_ANY, u"Contraseña...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.c_con.SetMaxLength( 4 ) 
		gSizer1.Add( self.c_con, 2, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.SHAPED, 2 )
		
		self.b_encrip = wx.Button( self, wx.ID_ANY, u"Encriptar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.b_encrip, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.SHAPED, 3 )
		
		self.b_desen = wx.Button( self, wx.ID_ANY, u"Desencriptar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.b_desen, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.SHAPED, 2 )
		
		
		bSizer2.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		self.c_2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,100 ), 0|wx.TAB_TRAVERSAL )
		self.c_2.SetMaxLength( 150 ) 
		bSizer2.Add( self.c_2, 0, wx.ALL|wx.EXPAND, 2 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

