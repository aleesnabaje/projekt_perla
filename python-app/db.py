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

    def put_wydarzenie(self, id, wydarzenie_edytuj):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE wydarzenia SET data_od = %s WHERE id = %s", (wydarzenie_edytuj["data_od"], id))
        cursor.execute("UPDATE wydarzenia SET data_do = %s WHERE id = %s", (wydarzenie_edytuj["data_do"], id))
        cursor.execute("UPDATE wydarzenia SET nazwa = %s WHERE id = %s", (wydarzenie_edytuj["nazwa"], id))
        cursor.execute("UPDATE wydarzenia SET tytul = %s WHERE id = %s", (wydarzenie_edytuj["tytul"], id))
        cursor.execute("UPDATE wydarzenia SET opis = %s WHERE id = %s", (wydarzenie_edytuj["opis"], id))
        cursor.execute("UPDATE wydarzenia SET id_org = %s WHERE id = %s", (wydarzenie_edytuj["id_org"], id))
        cursor.execute("UPDATE wydarzenia SET id_rodz = %s WHERE id = %s", (wydarzenie_edytuj["id_rodz"], id))
        cursor.execute("UPDATE wydarzenia SET id_adr = %s WHERE id = %s", (wydarzenie_edytuj["id_adr"], id))
        conn.commit()
        cursor.close()
        conn.close()
        return { "status":"ok","updated_id": id } 
    
    def soft_delete_wydarzenie(self, id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE wydarzenia SET deleted = 1 WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return { "status":"ok","deleted_id": id } 
    
#-----------------------------------------------------------------------------------------------------------------
    
    def get_organizator(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM organizatorzy")
        organizator = cursor.fetchall()
        cursor.close()
        conn.close()
        return organizator
    
    def save_organizator(self, organizator_data):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("INSERT INTO organizatorzy (nazwa) VALUES (%s)", (organizator_data['nazwa'],))
        conn.commit()
        cursor.close()
        conn.close()
        return { "status":"ok","added_id": cursor.lastrowid } 
    
    def put_organizator(self, id, organizator_edytuj):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE organizatorzy SET nazwa = %s WHERE id = %s", (organizator_edytuj["nazwa"], id))
        conn.commit()
        cursor.close()
        conn.close()
        return { "status":"ok","updated_id": id } 
    
    def soft_delete_organizator(self, id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE organizatorzy SET deleted = 1 WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return { "status":"ok","deleted_id": id } 
    
#---------------------------------------------------------------------------------------------------------
    
    def get_adres(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM adresy")
        adres = cursor.fetchall()
        cursor.close()
        conn.close()
        return adres
    
    def save_adres(self, adres_data):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("INSERT INTO adresy (adres, wspolrzedne) VALUES (%s, %s)", (adres_data['adres'], adres_data['wspolrzedne']))
        conn.commit()
        cursor.close()
        conn.close()
        return { "status":"ok","added_id": cursor.lastrowid } 
    
    def put_adres(self, id, adres_edytuj):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE adresy SET adres = %s, wspolrzedne = %s WHERE id = %s", (adres_edytuj["adres"],adres_edytuj['wspolrzedne'], id))
        conn.commit()
        cursor.close()
        conn.close()
        return { "status":"ok","updated_id": id } 
    
    def soft_delete_adres(self, id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE adresy SET deleted = 1 WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return { "status":"ok","deleted_id": id } 