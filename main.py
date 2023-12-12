from PySide6.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout,QMainWindow,QLayout,QWidget,\
    QFrame, QSplitter
from PySide6.QtCore import Qt
import sys

from src.views import HButton,PButton,SSlider,TSlider, AYButton

class AppGui(QMainWindow):
    def __init__(self):
        super().__init__()

        #Set tiêu đề    
        self.setWindowTitle("Làm app")
        #thiết lập kích thước
        self.resize(800,600)

        main_widget = QWidget()
        main_layout =QVBoxLayout()
        #set centealWedget
        self.setCentralWidget(main_widget)
        main_widget.setLayout(main_layout)


        #tạo layoutLv1
        frm_lv1_header = QFrame()
        frm_lv1_header.setStyleSheet("background-color:#111")
        frm_lv1_header.setFixedHeight(100)
        hlo_frm_lv1_header = QHBoxLayout(frm_lv1_header)

        #tọ buuton
        btn_hbutton = HButton()
        btn_hbutton.setText("Hải Button")
        btn_hbuttonP = PButton(
                                text= "Phương Defaut Button",
                                outline="0px",
                                border="0px currentcolor",
                                margin="0px",
                                font_weight="700",
                                line_height="1.71429",
                                font_size="0.875rem",
                                text_transform="unset",
                                font_family='"Public Sans", sans-serif',
                                min_width="64px",
                                padding_x="6px",
                                padding_y="12px",
                                border_radius="8px",
                                color="rgb(255, 255, 255)",
                                background_color= "rgb(33, 43, 54)",
                                hover_bg_color="rgb(116, 37, 37)"
                                )
        
        
        btn_hbuttonAY = AYButton()
        btn_hbuttonAY.setText("AY Button")

        hlo_frm_lv1_header.addWidget(btn_hbutton)
        hlo_frm_lv1_header.addWidget(btn_hbuttonP)
        hlo_frm_lv1_header.addWidget(btn_hbuttonAY)

        frm_lv1_body = QFrame()
        frm_lv1_body.setStyleSheet("background-color:#111")
        vlo_frm_lv1_body = QVBoxLayout(frm_lv1_body)

        #tạo splitter
        spl_lv1_body = QSplitter(frm_lv1_body)
        spl_lv1_body.setOrientation(Qt.Vertical)
        spl_lv1_body.setStyleSheet("background-color:red")

        vlo_frm_lv1_body.addWidget(spl_lv1_body)

        #Tạo frame trong splitter:
        frm_lv2_body_1=QFrame(spl_lv1_body)
        frm_lv2_body_1.setStyleSheet("background-color:#222")

        hlo_frm_lv2_body_1=QHBoxLayout(frm_lv2_body_1)

        frm_lv2_body_2=QFrame(spl_lv1_body)
        frm_lv2_body_2.setStyleSheet("background-color:#222")
        vlo_frm_lv2_body_header=QVBoxLayout(frm_lv2_body_2)

        #tạo thêm frem trog frm_lv2_body_2 
        frm_lv3_1_body_2 = QFrame(frm_lv2_body_2) 
        frm_lv3_1_body_2.setStyleSheet("background-color:#333")
        frm_lv3_1_body_2.setFixedHeight(40)
        hlo_frm_lv3_1_body_2=QHBoxLayout(frm_lv3_1_body_2)

        frm_lv3_2_body_2 = QFrame(frm_lv2_body_2) 
        frm_lv3_2_body_2.setStyleSheet("background-color:#333")
        vlo_frm_lv3_2_body_2 = QVBoxLayout(frm_lv3_2_body_2)

        vlo_frm_lv2_body_header.addWidget(frm_lv3_1_body_2)
        vlo_frm_lv2_body_header.addWidget(frm_lv3_2_body_2)

        spl_lv1_body.addWidget(frm_lv2_body_1)
        spl_lv1_body.addWidget(frm_lv2_body_2)


        #Thêm các frame vào main chính
        main_layout.addWidget(frm_lv1_header)
        main_layout.addWidget(frm_lv1_body)



if __name__=="__main__":
    app = QApplication(sys.argv)
    windown = AppGui()
    windown.show()
    sys.exit(app.exec())