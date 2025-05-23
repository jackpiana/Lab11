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
        self.selected_product = None



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


    def handle_graph(self, e):
        self._model.reset()
        self._view.txtOut.controls.clear()
        self._view._page.update()

        self._model.buildGraph(self.selected_color, self.selected_year)
        self._view.txtOut.controls.append(ft.Text(f"{self._model.grafo}"))
        top_edges = self._model.get_top3_edges()
        for e in top_edges:
            self._view.txtOut.controls.append(ft.Text(f"edge: {e[0].Product} - "
                                                      f"{e[1].Product} "
                                                      f"--- peso: {e[2]}"))
        top_nodes = self._model.top_nodes()
        self._view.txtOut.controls.append(ft.Text(f"nodi ripetuti: "))
        for n in top_nodes:
            self._view.txtOut.controls.append(ft.Text(f"{n}"))

        self._view._page.update()


    def fillDDProduct(self):
        self._view._ddnode.options.clear()
        for p in DAO.get_products_colored(self.selected_color):
            self._view._ddnode.options.append(ft.dropdown.Option(key=p,
                                                                 text=p,
                                                                 data=p,
                                                                 on_click=self.read_product))
        self._view._page.update()


    def handle_search(self, e):
        pass

    def read_year(self, e):
        self.selected_year = e.control.data
        print(self.selected_year)


    def read_color(self, e):
        self.selected_color = e.control.data
        print(self.selected_color)
        self.fillDDProduct()


    def read_product(self, e):
        self.selected_product = e.control.data
        print(self.selected_product)


