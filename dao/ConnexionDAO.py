import psycopg2  # pip install psycopg2-binary
import yaml # pip install PyYAML
import os
class ConnexionBD:

    def __init__(self):
        self.cnx = None
        self.params = None
        self.__token = None

    def getConnexion(self):
        try:
            print("- class admin connextion is running ... \n\n")
            print("- config/Config.yml is loading ...")
            current_directory = os.path.dirname(os.path.abspath(__file__))

            # Chemin relatif vers le fichier YAML
            yaml_file_path = os.path.join(current_directory, "../config/config.yaml")
            # get file and data
            if os.path.exists(yaml_file_path):
                with open(yaml_file_path, "r") as fic:
                    donnees = yaml.safe_load(fic)
                    config = donnees["postgreSQLAccess"]
                    db = config["database_name"]
                    host = config["host"]
                    port = config["port"]
                    usr = config["user"]["usr1"]
                    pwd = config["pwd"]["pwd1"]
                   
                    self.cnx = psycopg2.connect(dbname=db,
                                  host=host,
                                  port=port,
                                  user=usr,
                                  password=pwd
                                  )
                    return self.cnx
            else:
                ("Le fichier YAML n'existe pas à l'emplacement spécifié.")
        except Exception as e:
            print(f"Erreur-CONNECTION ::: {e}")
        return self.cnx
    
    def getUserConnection(self):
        try:
            print("- class visitor connexion is running ... \n\n")
            print("- config/Config.yml is loading ...")
            current_directory = os.path.dirname(os.path.abspath(__file__))

            # Chemin relatif vers le fichier YAML
            yaml_file_path = os.path.join(current_directory, "../config/config.yaml")
            # get file and data
            if os.path.exists(yaml_file_path):
                with open(yaml_file_path, "r") as fic:
                    donnees = yaml.safe_load(fic)
                    config = donnees["postgreSQLAccess"]
                    db = config["database_name"]
                    host = config["host"]
                    port = config["port"]
                    usr = config["user"]["usr2"]
                    pwd = config["pwd"]["pwd2"]
                    

                    self.cnx = psycopg2.connect(dbname=db,
                                  host=host,
                                  port=port,
                                  user=usr,
                                  password=pwd
                                  )
                    return self.cnx
            else:
                ("Le fichier YAML n'existe pas à l'emplacement spécifié.")
        except Exception as e:
            print(f"Erreur-CONNECTION ::: {e}")
        return self.cnx
    
    def  __grantAcessToVisitor(self):
        cursor = self.getConnexion().cursor()
        try:
            query = '''
                        GRANT SELECT, INSERT ON TABLE public.categorie TO visitor;
                        GRANT SELECT, INSERT ON TABLE public.publication TO visitor;
                        GRANT SELECT, INSERT ON TABLE public.citation TO visitor;
                        GRANT SELECT, INSERT ON TABLE public.city TO visitor;
                        GRANT SELECT, INSERT ON TABLE public.reference TO visitor;
                        '''
            cursor.execute(query, ( ))
            print(self.getConnexion())
            cursor.connection.commit() 
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_CitationDAO.create() ::: {e}")
    
            cursor.connection.rollback()
        finally:
            cursor.close()

    def getToken(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        yaml_file_path = os.path.join(current_directory, "../config/config.yaml")
   
        if os.path.exists(yaml_file_path):
            with open(yaml_file_path, "r") as fic:
                donnees = yaml.safe_load(fic)
                config = donnees["postgreSQLAccess"]
                return config["token"]