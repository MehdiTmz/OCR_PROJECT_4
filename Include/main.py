from Include.control.mainController import mainController
from Include.view.view import View


view = View()
controller = mainController(view)


if __name__ == "__main__":

    controller.run()
