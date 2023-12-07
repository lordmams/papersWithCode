import sqlite3
from dao import ModelDAO
from model.ReferencesM import References

class ReferencesDAO(ModelDAO.modeleDAO):
    def __init__(self):
        '''
        Initialise l'objet ReferencesDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.modeleDAO.connect_objet
        self.cur = params.cursor()

    def create_table(self):
        '''
        Méthode pour créer la table "references" dans la base de données.
        '''
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS references (
                    reference_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    author TEXT,
                    publication_year INTEGER
                )
            ''')
            conn.commit()

    def insert_reference(self, objIns: References) -> int:
        '''
        Insère un objet dans la table References.

        :param objIns: L'objet à insérer dans la table.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = '''INSERT INTO references (title, author, publication_year) 
                       VALUES (?, ?, ?);'''
            self.cur.execute(query, (objIns.getTitle(), objIns.getAuthor(), objIns.getPublicationYear()))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_ReferencesDAO.insert_reference() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def insert_multiple_references(self, objInsList: list[References]) -> int:
        '''
        Insère une liste d'objets dans la table References.

        :param objInsList: La liste d'objets à insérer.
        :return: Le nombre de lignes affectées.
        '''
        pass

    def find_one(self, reference_id) -> References:
        '''
        Trouve un objet dans la table References par clé.

        :param reference_id: La clé de recherche.
        :return: L'objet trouvé.
        '''
        try:
            query = '''SELECT * FROM references WHERE reference_id = ?;'''
            self.cur.execute(query, (reference_id,))
            res = self.cur.fetchone()

            if res:
                ref = References()
                ref.setReferenceId(res[0])
                ref.setTitle(res[1])
                ref.setAuthor(res[2])
                ref.setPublicationYear(res[3])

                return ref
            else:
                return None
        except Exception as e:
            print(f"Erreur_ReferencesDAO.find_one() ::: {e}")
        finally:
            self.cur.close()

    # ... (continuer avec les autres méthodes)
