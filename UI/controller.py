import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = ["2015", "2016", "2017", "2018"]
        self._listColor = DAO.get_colori()
        self.selected_color = None
        self.selected_year = None



    def fillDD(self):
        for anno in self._listYear:
            self._view._ddyear.options.append(ft.dropdown.Option(key=anno,
                                                                 text=anno,
                                                                 data=anno,
                                                                 on_click=self.read_year))
        for colore in self._listColor:
            self._view._ddcolor.options.append(ft.dropdown.Option(key=colore,
                                                                 text=colore,
                                                                 data=colore,
                                                                 on_click=self.read_color))

            # on_click=self.read_stato))


    def handle_graph(self, e):
        pass

    def fillDDProduct(self):
        pass

    def handle_search(self, e):
        pass

    def read_year(self, e):
        self.selected_year = e.control.data

    def read_color(self, e):
        self.selected_color = e.control.data
        print(self.selected_color)



