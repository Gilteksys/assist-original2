from PyQt5.QtNetwork import QNetworkRequest, QNetworkReply, QNetworkAccessManager
from PyQt5.QtCore import QUrl, QUrlQuery
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
import os


class OrdemServicoDialog(QDialog):
    def __init__(self, cliente_id=None, parent=None):
        super().__init__(parent)
        self.cliente_id = cliente_id

        # Carregar o arquivo .ui
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file = os.path.join(script_dir, 'ui_files/OrdemServico.ui')
        loadUi(ui_file, self)

        self.setWindowTitle("Ordem de Serviço")
        self.setGeometry(50, 50, 840, 640)

        # Criar o gerenciador de acesso à rede
        self.network_manager = QNetworkAccessManager(self)

        # Conectar o sinal do botão Criar Ordem de Serviço
        self.pushButton.clicked.connect(self.on_create_ordem_servico_clicked)
        self.pushButton_sair.clicked.connect(self.close)  # Conectar o botão "Sair" ao método close

        if self.cliente_id is not None:
            self.lineEdit_CodigoCliente.setText(str(self.cliente_id))


    def on_create_ordem_servico_clicked(self):
        url = QUrl("http://localhost:8000/ordem_servico_create/")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/x-www-form-urlencoded")
        query = QUrlQuery()

        query.addQueryItem("cliente_id", self.lineEdit_CodigoCliente.text())
        query.addQueryItem("aparelho", self.lineEdit.text())
        query.addQueryItem("marca", self.lineEdit_2.text())
        query.addQueryItem("modelo", self.lineEdit_3.text())
        query.addQueryItem("serial", self.lineEdit_4.text())
        query.addQueryItem("observacao", self.textEdit.toPlainText())

        data = query.toString().encode("utf-8")
        reply = self.network_manager.post(request, data)
        reply.finished.connect(self.on_request_finished)

    def on_request_finished(self):
        reply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            print("Ordem de Serviço criada com sucesso!")
        else:
            print("Erro ao criar Ordem de Serviço:", reply.errorString())
        reply.deleteLater()

