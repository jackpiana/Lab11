from database.DB_connect import DBConnect
from model.Product import Product


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get_colori():
        colors = set()
        conn = DBConnect.get_connection()
        if conn is None:
            print("connection failed")
        else:
            cursor = conn.cursor()
            query = """
                    SELECT distinct Product_color
                    FROM go_products gp 
                    """
            cursor.execute(query, ())
            res = cursor.fetchall()
            for color in res:
                colors.add(color[0])
        return colors

    @staticmethod
    def get_products_colored(color):
        conn = DBConnect.get_connection()
        prodotti = []
        if conn is None:
            print("Connection failed")
        else:
            cursor = conn.cursor(dictionary=True)
            query = """SELECT *
                        FROM go_products
                        WHERE Product_color = %s
                            """
            cursor.execute(query, (color,))
            for row in cursor:
                prodotti.append(Product(**row))  # **row è un operatore di unpacking (espansione) di un dizionario. nb: serve che tutti i nomi degli attributi combacino
            cursor.close()
        conn.close()
        return prodotti

if __name__ == "__main__":
    prodotti = DAO.get_products_colored("RED")
    for p in prodotti:
        print(p)
