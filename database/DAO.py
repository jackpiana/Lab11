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
        colori_ordinati = sorted(colors)
        return colori_ordinati

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

    @staticmethod
    def get_peso_edge(anno, Product_number1, Product_number2):
        conn = DBConnect.get_connection()
        if conn is None:
            print("Connection failed")
        else:
            cursor = conn.cursor()
            query = """
            select count(distinct giorno)
            from (select t1.giorno as giorno, t1.Product_number as prodotto1, t2.Product_number as prodotto2, t1.Retailer_code
            from (select Retailer_code, Product_number, Date as giorno from go_daily_sales gds where year(gds.Date)=%s) t1
            inner join (select Retailer_code, Product_number, Date as giorno from go_daily_sales gds where year(gds.Date)=%s) t2
            on t1.giorno = t2.giorno
            and t1.Product_number = %s 
            and t2.Product_number = %s
            and t1.Retailer_code = t2.Retailer_code) as v;
            """
            # questa query seleziona il numero di giorni distinti in cui due prodotti sono stati venduti nello stesso giorno dallo stesso venditore
            # se è zero significa che non è mai stato venduto dallo stesso rivenditore nello stesso giorno

            cursor.execute(query, (anno, anno, Product_number1, Product_number2,))
            res = cursor.fetchall()
            cursor.close()
            conn.close()
            return res[0][0]


if __name__ == "__main__":
    prodotti = DAO.get_products_colored("RED")
    for p1 in prodotti:
        for p2 in prodotti:
            if p1 == p2:
                continue
            print(p1)
            print(p2)
            print(DAO.get_peso_edge(2015, p1.Product_number, p2.Product_number))
            print("\n")

