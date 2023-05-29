from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MainWindow")
        self.setGeometry(100, 100, 800, 600)

        # Criação do menu em cascata
        menu_bar = self.menuBar()

        # Definir estilo para as letras do menu e índice
        menu_style = "QMenuBar { color: red; font-size: 14px; font-weight: bold; background-color: transparent; } QMenuBar::item { padding: 10px 20px; } QMenu::item { font-weight: bold; }"
        menu_bar.setStyleSheet(menu_style)

        file_menu = menu_bar.addMenu("Cadastro")       
        edit_menu = menu_bar.addMenu("Busca")
       
        

        # Ação do menu "File"
        new_action = QAction("Clientes", self)
        file_menu.addAction(new_action)

        open_action = QAction("Ordem de Serviço", self)
        file_menu.addAction(open_action)

        save_action = QAction("Peças", self)
        file_menu.addAction(save_action)

        # Ação do menu "Edit"
        copy_action = QAction("Clientes", self)
        edit_menu.addAction(copy_action)

        cut_action = QAction("Ordem de Serviço", self)
        edit_menu.addAction(cut_action)

        paste_action = QAction("Tipo de Serviços", self)
        edit_menu.addAction(paste_action)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()







