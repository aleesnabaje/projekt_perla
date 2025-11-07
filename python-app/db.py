from dbconnection import get_connection
class db:
    def __init__(self):
        self.connection = get_connection()

    def get_wydarzenie(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM wydarzenia")
        wydarzenie = cursor.fetchall()
        cursor.close()
        conn.close()
        return wydarzenie
    
    def save_wydarzenie(self, wydarzenie_data):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("INSERT INTO wydarzenia (data_od,data_do,nazwa, tytul,id_org,id_rodz,id_adr,opis) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (wydarzenie_data['data_od'],wydarzenie_data['data_do'],wydarzenie_data['nazwa'], wydarzenie_data['tytul'],wydarzenie_data['id_org'],wydarzenie_data['id_rodz'],wydarzenie_data['id_adr'],wydarzenie_data['opis']))
        conn.commit()
        cursor.close()
        conn.close()
        return { "status":"ok","added_id": cursor.lastrowid } 

    def put_wydarzenie(self, wydarzenie_edytuj):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        kolumna = wydarzenie_edytuj["nazwa_kolumny"]
        cursor.execute(f"UPDATE wydarzenia SET {kolumna} = %s WHERE id = %s", (wydarzenie_edytuj["nowa_wartosc"], wydarzenie_edytuj["id_rekordu"]))
        cursor.close()
        conn.close()
        return { "status":"ok","updated_id": wydarzenie_edytuj["id_rekordu"] } 