import json
from PyQt5.QtNetwork import QNetworkRequest, QNetworkReply, QNetworkAccessManager
from PyQt5.QtCore import QUrl, QUrlQuery
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
import os
from OrdemServico import OrdemServicoDialog


class CadastroClienteWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Carregar o arquivo .ui
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file = os.path.join(script_dir, 'ui_files/CadastroClientes2.ui')
        loadUi(ui_file, self)

        self.setWindowTitle("Ordem de Serviço")
        self.setGeometry(50, 50, 840, 640)

        # Criar o gerenciador de acesso à rede
        self.network_manager = QNetworkAccessManager(self)

        # Conectar o sinal do botão Criar Ordem de Serviço
        self.pushButton_salvar.clicked.connect(self.on_create_cliente_clicked)        
        self.pushButton.clicked.connect(self.on_ordem_servico_clicked)
        self.pushButton_sair.clicked.connect(self.close)  # Conectar o botão "Sair" ao método close


    def on_create_cliente_clicked(self):
        url = QUrl("http://localhost:8000/cliente_create/")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/x-www-form-urlencoded")
        query = QUrlQuery()

        query.addQueryItem("nome", self.lineEdit.text())        
        query.addQueryItem("contato", self.lineEdit_2.text())   
        query.addQueryItem("endereco", self.lineEdit_3.text())    
        query.addQueryItem("observacao", self.textEdit.toPlainText())
        
        

        data = query.toString().encode("utf-8")
        reply = self.network_manager.post(request, data)
        reply.finished.connect(self.on_request_finished)

    def on_ordem_servico_clicked(self):
        if hasattr(self, 'cliente_id'):  # Verificar se o atributo cliente_id foi definido
            self.ordem_servico_window = OrdemServicoDialog(cliente_id=self.cliente_id)  
            self.ordem_servico_window.show()
        else:
            print("Cliente não cadastrado.")


    def on_request_finished(self):
        reply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            response = reply.readAll().data().decode("utf-8")
            response_json = json.loads(response)
            if 'cliente_id' in response_json:
                self.cliente_id = response_json['cliente_id']
                self.pushButton.setEnabled(True)  # Habilitar o botão "Nova Ordem de Serviço"
                print("Cliente criado com sucesso!")
        else:
            print("Erro ao criar cliente:", reply.errorString())
        reply.deleteLater()







        

