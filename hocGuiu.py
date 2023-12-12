from PySide6.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout,QMainWindow,QLayout,QWidget,\
    QFrame, QSplitter
from PySide6.QtCore import Qt
import sys

class AppVidu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Làm ví dụ")
        self.resize(800,600)
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        self.setCentralWidget(main_widget)

        #layout cho main_widget
        main_widget.setLayout(main_layout)

        #tạo Qframe lv1
        fra_lv1_1 = QFrame()
        fra_lv1_1.setStyleSheet("background-color:#111")  # sét màu
        fra_lv1_1.setFixedHeight(40)                        #set chiều cao
        vlo_fra_lv1_1 = QHBoxLayout(fra_lv1_1)          #bố trí giao diện nằm ngang

        fra_lv1_2 = QFrame()
        fra_lv1_2.setStyleSheet("background-color:#222")
        vlo_fra_lv1_2 = QVBoxLayout(fra_lv1_2)    #bố trí giao diện nằm ngang

        #tạo lò xo đẩy trong frame Lv1_2
        spl_fra_lv2 = QSplitter(fra_lv1_2)
        spl_fra_lv2.setOrientation(Qt.Vertical)  #Lò xo đẩy có hương lên xuống
        spl_fra_lv2.setStyleSheet("background-color:red")



        #tạo frame lv2 trong lv1_2
        fra_lv2_1 = QFrame(spl_fra_lv2)
        fra_lv2_1.setStyleSheet("background-color:#333")
        
        

        fra_lv2_2 = QFrame(spl_fra_lv2)
        fra_lv2_2.setStyleSheet("background-color:#444")
        vlo_fra_lv2_2 = QVBoxLayout(fra_lv2_2)


        fra_lv3_2_1 = QFrame(fra_lv2_2)
        fra_lv3_2_1.setStyleSheet("background-color:#555")
        fra_lv3_2_1.setFixedHeight(40)  
        vlo_fra_lv3_2_1 = QVBoxLayout(fra_lv3_2_1)

        fra_lv3_2_2 = QFrame(fra_lv2_2)
        fra_lv3_2_2.setStyleSheet("background-color:#555")
        
        vlo_fra_lv3_2_2 = QVBoxLayout(fra_lv3_2_2)

        vlo_fra_lv2_2.addWidget(fra_lv3_2_1)
        vlo_fra_lv2_2.addWidget(fra_lv3_2_2)

        

       #ad các frame lv2 (1,2) vào splitter
        vlo_fra_lv1_2.addWidget(spl_fra_lv2)
        spl_fra_lv2.addWidget(fra_lv2_1)
        spl_fra_lv2.addWidget(fra_lv2_2)




     
        #add vào main chính
        main_layout.addWidget(fra_lv1_1)
        main_layout.addWidget(fra_lv1_2)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppVidu()
    window.show()
    sys.exit(app.exec())

