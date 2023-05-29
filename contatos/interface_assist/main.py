import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from cadastro_cliente import CadastroClienteWindow
from OrdemServico import OrdemServicoDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Carregar o arquivo .ui
        script = os.path.dirname(os.path.abspath(__file__))
        arquivo_ui = os.path.join(script, 'teste.ui')
        loadUi(arquivo_ui, self)

        self.setWindowTitle('ASSIST-3.0')
        self.setGeometry(100, 100, 840, 740)

        self.pushButton.clicked.connect(self.on_button_clientes_clicked)    
        self.pushButton_3.clicked.connect(self.on_ordem_servico_clicked)
        self.pushButton_5.clicked.connect(self.close)  # Conectar o botão "Sair" ao método close

    def on_button_clientes_clicked(self):
        self.cadastro_cliente_window = CadastroClienteWindow()
        self.cadastro_cliente_window.show()

    def on_ordem_servico_clicked(self):
        self.ordem_servico_window = OrdemServicoDialog()  
        self.ordem_servico_window.show()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

