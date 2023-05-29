import sys
from PyQt5.QtCore import QUrl, QUrlQuery
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cadastro de Cliente")
        self.setGeometry(100, 100, 1200, 800)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout(main_widget)

        self.label_nome = QLabel("Nome:")
        self.edit_nome = QLineEdit()
        layout.addWidget(self.label_nome)
        layout.addWidget(self.edit_nome)

        self.label_endereco = QLabel("Endereço:")
        self.edit_endereco = QLineEdit()
        layout.addWidget(self.label_endereco)
        layout.addWidget(self.edit_endereco)

        self.label_contato = QLabel("Contato:")
        self.edit_contato = QLineEdit()
        layout.addWidget(self.label_contato)
        layout.addWidget(self.edit_contato)

        self.label_documento = QLabel("Documento:")
        self.edit_documento = QLineEdit()
        layout.addWidget(self.label_documento)
        layout.addWidget(self.edit_documento)

        button = QPushButton("Criar Cliente")
        button.clicked.connect(self.on_create_cliente_clicked)
        layout.addWidget(button)

        self.network_manager = QNetworkAccessManager(self)

    def on_create_cliente_clicked(self):
        url = QUrl("http://localhost:8000/contatos/cliente_create/")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/x-www-form-urlencoded")
        query = QUrlQuery()


        query.addQueryItem("nome", self.edit_nome.text())
        query.addQueryItem("endereco", self.edit_endereco.text())
        query.addQueryItem("contato", self.edit_contato.text())
        query.addQueryItem("documento", self.edit_documento.text())


        data = query.toString().encode("utf-8")
        reply = self.network_manager.post(request, data)
        reply.finished.connect(self.on_request_finished)
    def on_request_finished(self):
        reply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            print("Cliente criado com sucesso!")
        else:
            print("Erro ao criar cliente:", reply.errorString())
        reply.deleteLater()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


