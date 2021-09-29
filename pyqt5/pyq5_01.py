from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit

app = QApplication([])

window = QMainWindow()
window.resize(500, 400)
window.move(300, 310)  # 显示在显示器的什么位置 300 从左到右 310 从上到下
window.setWindowTitle('薪资统计')

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("请输入薪资表")
textEdit.move(10, 25)
textEdit.resize(300, 350)

button = QPushButton('统计', window)
button.move(380, 80)

window.show()

app.exec_()
