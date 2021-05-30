from PyQt5 import QtCore,QtGui,QtWidgets
import sys
import qtawesome
 
class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
 
    def init_ui(self):
        self.setFixedSize(1024,600)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件 Crea el widget principal
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局 Crea un diseño de cuadrícula de la parte principal
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局 Establecer el diseño del widget principal de la ventana en diseño de cuadrícula
 
        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout) # 设置左侧部件布局为网格
 
        self.right_widget = QtWidgets.QWidget() # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout) # 设置右侧部件布局为网格
 
        self.main_layout.addWidget(self.left_widget,0,0,12,2) # 左侧部件在第0行第0列，占12行2列
        self.main_layout.addWidget(self.right_widget,0,2,12,10) # 右侧部件在第0行第3列，占12行10列
        self.setCentralWidget(self.main_widget) # 设置窗口主部件

        # self.left_close = QtWidgets.QPushButton("") # 关闭按钮
        self.left_close =QtWidgets.QPushButton(qtawesome.icon('fa.times',color='white'),"")
        # self.left_visit = QtWidgets.QPushButton("") # 空白按钮
        self.left_visit = QtWidgets.QPushButton(qtawesome.icon('fa.gamepad',color='white'),"")
        # self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮
        self.left_mini =QtWidgets.QPushButton(qtawesome.icon('fa.film',color='white'),"")
        self.left_close.clicked.connect(self.close_window) #关联
 
        self.left_label_1 = QtWidgets.QPushButton("Recomendación")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("Mi música")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("Contacto y ayuda")
        self.left_label_3.setObjectName('left_label')
 
        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.music',color='white'),"Canciones populares")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.sellsy',color='white'),"En línea FM")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.film',color='white'),"Popular MV")
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.home',color='white'),"Música local")
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.download',color='white'),"Gestión de descargas")
        self.left_button_5.setObjectName('left_button')
        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.heart',color='white'),"Mi colección")
        self.left_button_6.setObjectName('left_button')
        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.comment',color='white'),"Realimentación")
        self.left_button_7.setObjectName('left_button')
        self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.star',color='white'),"Síganos")
        self.left_button_8.setObjectName('left_button')
        self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa.question',color='white'),"Reportar problema")
        self.left_button_9.setObjectName('left_button')
        self.left_xxx = QtWidgets.QPushButton(" ")

        self.left_layout.addWidget(self.left_mini, 0, 0,1,1)
        self.left_layout.addWidget(self.left_close, 0, 2,1,1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)

        self.left_layout.addWidget(self.left_label_1,1,0,1,3)
        self.left_layout.addWidget(self.left_button_1, 2, 0,1,3)
        self.left_layout.addWidget(self.left_button_2, 3, 0,1,3)
        self.left_layout.addWidget(self.left_button_3, 4, 0,1,3)
        self.left_layout.addWidget(self.left_label_2, 5, 0,1,3)
        self.left_layout.addWidget(self.left_button_4, 6, 0,1,3)
        self.left_layout.addWidget(self.left_button_5, 7, 0,1,3)
        self.left_layout.addWidget(self.left_button_6, 8, 0,1,3)
        self.left_layout.addWidget(self.left_label_3, 9, 0,1,3)
        self.left_layout.addWidget(self.left_button_7, 10, 0,1,3)
        self.left_layout.addWidget(self.left_button_8, 11, 0,1,3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)

        self.right_bar_widget = QtWidgets.QWidget() # 右侧顶部搜索框部件
        self.right_bar_layout = QtWidgets.QGridLayout() # 右侧顶部搜索框网格布局
        self.right_bar_widget.setLayout(self.right_bar_layout)
        self.search_icon = QtWidgets.QLabel(chr(0xf002) + ' '+'Buscar ')
        self.search_icon.setFont(qtawesome.font('fa', 16))
        self.right_bar_widget_search_input = QtWidgets.QLineEdit()
        self.right_bar_widget_search_input.setPlaceholderText("Ingrese cantante, canción o usuario, presione Enter para buscar")
 
        self.right_bar_layout.addWidget(self.search_icon,0,0,1,1)
        self.right_bar_layout.addWidget(self.right_bar_widget_search_input,0,1,1,8)
 
        self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)

        self.right_recommend_label = QtWidgets.QLabel("Recomendación de hoy")
        self.right_recommend_label.setObjectName('right_lable')
 
        self.right_recommend_widget = QtWidgets.QWidget() # 推荐封面部件
        self.right_recommend_layout = QtWidgets.QGridLayout() # 推荐封面网格布局
        self.right_recommend_widget.setLayout(self.right_recommend_layout)
 
        self.recommend_button_1 = QtWidgets.QToolButton()
        self.recommend_button_1.setText("Playlist personalizada") # 设置按钮文本
        self.recommend_button_1.setIcon(QtGui.QIcon('C:/Users/brend/Pictures/r1.jpg')) # 设置按钮图标
        self.recommend_button_1.setIconSize(QtCore.QSize(100,100)) # 设置图标大小
        self.recommend_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon) # 设置按钮形式为上图下文
 
        self.recommend_button_2 = QtWidgets.QToolButton()
        self.recommend_button_2.setText("Playlist triste")
        self.recommend_button_2.setIcon(QtGui.QIcon('C:/Users/brend/Pictures/r2.jpg'))
        self.recommend_button_2.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
 
        self.recommend_button_3 = QtWidgets.QToolButton()
        self.recommend_button_3.setText("Antes de ir a la cama")
        self.recommend_button_3.setIcon(QtGui.QIcon('C:/Users/brend/Pictures/r3.jpg'))
        self.recommend_button_3.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
 
        self.recommend_button_4 = QtWidgets.QToolButton()
        self.recommend_button_4.setText("Sólo escucha")
        self.recommend_button_4.setIcon(QtGui.QIcon('C:/Users/brend/Pictures/r4.jpg'))
        self.recommend_button_4.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
 
        self.recommend_button_5 = QtWidgets.QToolButton()
        self.recommend_button_5.setText("Música de anime")
        self.recommend_button_5.setIcon(QtGui.QIcon('C:/Users/brend/Pictures/01.jpg'))
        self.recommend_button_5.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
 
        self.right_recommend_layout.addWidget(self.recommend_button_1,0,0)
        self.right_recommend_layout.addWidget(self.recommend_button_2,0,1)
        self.right_recommend_layout.addWidget(self.recommend_button_3, 0, 2)
        self.right_recommend_layout.addWidget(self.recommend_button_4, 0, 3)
        self.right_recommend_layout.addWidget(self.recommend_button_5, 0, 4)
 
        self.right_layout.addWidget(self.right_recommend_label, 1, 0, 1, 9)
        self.right_layout.addWidget(self.right_recommend_widget, 2, 0, 2, 9)


        self.right_newsong_lable = QtWidgets.QLabel("Última canción")
        self.right_newsong_lable.setObjectName('right_lable')
 
        self.right_playlist_lable = QtWidgets.QLabel("Lista de reproducción popular")
        self.right_playlist_lable.setObjectName('right_lable')
 
        self.right_newsong_widget = QtWidgets.QWidget()  # 最新歌曲部件
        self.right_newsong_layout = QtWidgets.QGridLayout() # 最新歌曲部件网格布局
        self.right_newsong_widget.setLayout(self.right_newsong_layout)
 
        self.newsong_button_1 = QtWidgets.QPushButton("Bohemian Rhapsody    Queen           Bohemian Rhapsody         05::54")
        self.newsong_button_2 = QtWidgets.QPushButton("Dance Monkey         Tones and I     The Kids Are Coming       03::29")
        self.newsong_button_3 = QtWidgets.QPushButton("Girls Like You       Maroon 5        Red Pill Blues            03::55")
        self.newsong_button_4 = QtWidgets.QPushButton("Cheap Thrills        Sia             Cheap Thrills             03::31")
        self.newsong_button_5 = QtWidgets.QPushButton("Государственный гимн СССР                                  03::29")
        self.newsong_button_6 = QtWidgets.QPushButton("リブート                ミワ              reboot               04::02")

        self.right_newsong_layout.addWidget(self.newsong_button_1,0,1,)
        self.right_newsong_layout.addWidget(self.newsong_button_2, 1, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_3, 2, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_4, 3, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_5, 4, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_6, 5, 1, )
        self.right_playlist_widget = QtWidgets.QWidget() # 播放歌单部件
        self.right_playlist_layout = QtWidgets.QGridLayout() # 播放歌单网格布局
        self.right_playlist_widget.setLayout(self.right_playlist_layout)
 
        self.playlist_button_1 = QtWidgets.QToolButton()
        self.playlist_button_1.setText("Ayuda para dormir")
        self.playlist_button_1.setIcon(QtGui.QIcon('C:/Users/brend/Pictures/p1.jpg'))
        self.playlist_button_1.setIconSize(QtCore.QSize(80, 80))
        self.playlist_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
 
        self.playlist_button_2 = QtWidgets.QToolButton()
        self.playlist_button_2.setText("Música clásica")
        self.playlist_button_2.setIcon(QtGui.QIcon('C:/Users/brend/Pictures/p2.jpg'))
        self.playlist_button_2.setIconSize(QtCore.QSize(80, 80))
        self.playlist_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
 
        self.playlist_button_3 = QtWidgets.QToolButton()
        self.playlist_button_3.setText("Retro")
        self.playlist_button_3.setIcon(QtGui.QIcon('C:/Users/brend/Pictures/p3.jpg'))
        self.playlist_button_3.setIconSize(QtCore.QSize(80, 80))
        self.playlist_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
 
        self.playlist_button_4 = QtWidgets.QToolButton()
        self.playlist_button_4.setText("Para bailar")
        self.playlist_button_4.setIcon(QtGui.QIcon('C:/Users/brend/Pictures/p4.jpg'))
        self.playlist_button_4.setIconSize(QtCore.QSize(80, 80))
        self.playlist_button_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
 
        self.right_playlist_layout.addWidget(self.playlist_button_1,0,0)
        self.right_playlist_layout.addWidget(self.playlist_button_2, 0, 1)
        self.right_playlist_layout.addWidget(self.playlist_button_3, 1, 0)
        self.right_playlist_layout.addWidget(self.playlist_button_4, 1, 1)

        self.right_layout.addWidget(self.right_newsong_lable, 4, 0, 1, 5)
        self.right_layout.addWidget(self.right_playlist_lable, 4, 5, 1, 4)
        self.right_layout.addWidget(self.right_newsong_widget, 5, 0, 1, 5)
        self.right_layout.addWidget(self.right_playlist_widget, 5, 5, 1, 4)

        self.right_process_bar = QtWidgets.QProgressBar()  # 播放进度部件
        self.right_process_bar.setValue(49)
        self.right_process_bar.setFixedHeight(3)  # 设置进度条高度
        self.right_process_bar.setTextVisible(False)  # 不显示进度条文字
 
        self.right_playconsole_widget = QtWidgets.QWidget()  # 播放控制部件
        self.right_playconsole_layout = QtWidgets.QGridLayout()  # 播放控制部件网格布局层
        self.right_playconsole_widget.setLayout(self.right_playconsole_layout)
 
        self.console_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.backward', color='#F76677'), "")
        self.console_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.forward', color='#F76677'), "")
        self.console_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.pause', color='#F76677', font=18), "")
        self.console_button_3.setIconSize(QtCore.QSize(30, 30))
 
        self.right_playconsole_layout.addWidget(self.console_button_1, 0, 0)
        self.right_playconsole_layout.addWidget(self.console_button_2, 0, 2)
        self.right_playconsole_layout.addWidget(self.console_button_3, 0, 1)
        self.right_playconsole_layout.setAlignment(QtCore.Qt.AlignCenter)  # 设置布局内部件居中显示
 
        self.right_layout.addWidget(self.right_process_bar, 9, 0, 1, 9)
        self.right_layout.addWidget(self.right_playconsole_widget, 10, 0, 1, 9)

        self.left_close.setFixedSize(16,16) # 设置关闭按钮的大小
        self.left_visit.setFixedSize(16, 16)  # 设置按钮大小
        self.left_mini.setFixedSize(16, 16) # 设置最小化按钮大小


        self.left_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
            QWidget#left_widget{
            background:gray;
            border-top:1px solid white;
            border-bottom:1px solid white;
            border-left:1px solid white;
            border-top-left-radius:10px;
            border-bottom-left-radius:10px;
        }
        ''')

        self.right_bar_widget_search_input.setStyleSheet(
        '''QLineEdit{
                border:1px solid gray;
                width:300px;
                border-radius:10px;
                padding:2px 4px;
        }''')

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')
        self.right_recommend_widget.setStyleSheet(
            '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')
        self.right_playlist_widget.setStyleSheet(
            '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')
        self.right_newsong_widget.setStyleSheet('''
            QPushButton{
                border:none;
                color:gray;
                font-size:12px;
                height:40px;
                padding-left:5px;
                padding-right:10px;
                text-align:left;
            }
            QPushButton:hover{
                color:black;
                border:1px solid #F3F3F5;
                border-radius:10px;
                background:LightGray;
            }
        ''')
        self.right_process_bar.setStyleSheet('''
            QProgressBar::chunk {
                background-color: #F76677;
            }
        ''')
 
        self.right_playconsole_widget.setStyleSheet('''
            QPushButton{
                border:none;
            }
        ''')

        self.setWindowOpacity(0.9) # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) # 隐藏边框

        
        self.main_layout.setSpacing(0)

    # 无边框的拖动 ARRASTRE SIN BORDES
    def mouseMoveEvent(self, e: QtGui.QMouseEvent):  # 重写移动事件 REESCRIBE EVENTOS MOVILES 
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)
 
    def mousePressEvent(self, e: QtGui.QMouseEvent):
        if e.button() == QtCore.Qt.LeftButton:
            self._isTracking = True
            self._startPos = QtCore.QPoint(e.x(), e.y())
 
    def mouseReleaseEvent(self, e: QtGui.QMouseEvent):
        if e.button() == QtCore.Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    # 关闭按钮动作函数
    def close_window(self):
        self.close()


 
def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()