import sys
from PyQt4 import QtGui , QtCore

app = QtGui.QApplication( sys.argv )

widget = QtGui.QWidget()
widget.resize( 250 , 150 )
widget.setWindowTitle( 'title' )


# widget.setWindowIcon( QtGui.QIcon( '16-111129230521' ) )

widget.setToolTip( '<b>tishi</b>' )
QtGui.QToolTip.setFont( QtGui.QFont( 'OldEnglish' , 12 ) )

quit = QtGui.QPushButton( 'tuichu' , widget )
quit.setGeometry( 10 ,20 , 50 ,30 )

widget.connect( quit , QtCore.SIGNAL( 'clicked()' ) , QtGui.qApp , QtCore.SLOT( 'quit()' )  )

reply = QtGui.QMessageBox.question( widget , 'message' , 'wenti' , QtGui.QMessageBox.Yes , QtGui.QMessageBox.No )

widget.show()

sys.exit( app.exec_() )