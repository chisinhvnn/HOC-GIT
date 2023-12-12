# Import các thư viện hệ thống
import sys
#import các thư viện thứ 3
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, \
    QFrame, QSplitter, QHBoxLayout
from PySide6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


    #1 Đặt tên app title
        self.setWindowTitle("App mô phỏng")
    #2 Đặt kích thước app
        self.resize(QSize(800,600))

    #3 Khai báo main_layuot
        main_layout_LV1_1 = QVBoxLayout()
        main_layout_LV1_2 = QVBoxLayout()
        #main_layout_LV1_2.setOrientation(Qt.Vertical) # sắp xếp nằm ngang
    #4 Khai báo Widget_main
        main_widget = QWidget()

    #5 set layout cho main widget
        main_widget.setLayout(main_layout_LV1_1)
        main_widget.setLayout(main_layout_LV1_2)

    # Sắp sếp ngang-dọc cho layuot


    #6 set central cho mainWindow
        self.setCentralWidget(main_widget)
    
    #tạo section head
        section_header = QFrame()
        section_header.setStyleSheet("background: red")
        section_header.setFixedHeight(60)
    
    #tạo section giữa
        section_body = QFrame()
        section_body.setStyleSheet("background: =blue")

    #tạo lò xo kéo giãn ở giữa (splitter)
       
        splitter_keo_gian = QSplitter(section_body)
        



    #add vào layout
        main_layout_LV1_1.addWidget(section_header)








if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())