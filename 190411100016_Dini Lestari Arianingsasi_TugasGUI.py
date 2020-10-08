import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout
#inisialisasi pyqt
app = QApplication(sys.argv)
window = QWidget()
#mebuat box dan isi
isi1 = QPushButton(window)
isi1.setStyleSheet("background-color:#e3f2fd;color:red;font-size:50px")
isi1.setText("1")
isi2 = QPushButton(window)
isi2.setStyleSheet("background-color:#e3f2fd;color:red;font-size:50px")
isi2.setText("2")
isi3 = QPushButton(window)
isi3.setStyleSheet("background-color:#e3f2fd;color:red;font-size:50px")
isi3.setText("3")
isi4 = QPushButton(window)
isi4.setStyleSheet("background-color:#e3f2fd;color:red;font-size:50px")
isi4.setText("4")
isi5 = QPushButton(window)
isi5.setStyleSheet("background-color:#e3f2fd;color:red;font-size:50px")
isi5.setText("5")
#isi yang di dalam kotak
layout = QHBoxLayout()
layout.addWidget(isi1)
layout.addWidget(isi2)
layout.addWidget(isi3)
layout.addWidget(isi4)
layout.addWidget(isi5)
#menentukan ukuran window, + title dan menampilkan
window.setGeometry(100,100,350,350)
window.setWindowTitle("Box Example")
window.setLayout(layout)
window.show()
app.exec_()
