from dao import ModelDAO
from model.CitationM import Citation

class CitationDAO(ModelDAO.modeleDAO):
    def __init__(self,sercurity=1):
        if sercurity == 0:
            params = ModelDAO.modeleDAO.connect_object
        if sercurity == 1:
            params = ModelDAO.modeleDAO.user_connect
        self.cur=params.cursor()

    # INSERT

    def create(self, citation)->int:
        try:
            query = '''INSERT INTO citation ( publication) 
                       VALUES (%s);'''
            self.cur.execute(query, ( citation.getCitationPublication()))
            self.cur.connection.commit() 
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_CitationDAO.create() ::: {e}")
    
            self.cur.connection.rollback()
        finally:
            self.cur.close()
# return 0



    # SELECT
    def findById(self, citationId)->object:
        try:
            query = '''SELECT id,publication, count_ones(value) as nb_citation FROM citation WHERE id = %s;'''
            self.cur.execute(query, (citationId,))
            res = self.cur.fetchone()

            if res:

                c = Citation()

                c.setCitationId(res[0])
                c.setCitationPublication(res[1])
                c.setCitationValue(res[2])



                return c
            else:
                return None
        except Exception as e:
            print(f"Erreur_CitationDAO.FindById() ::: {e}")
        finally:
            self.cur.close()


    def findAll(self)->list:
        try:
            query = '''SELECT * FROM citation;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            liste_c = [] # [Brands(brand_id=row[0], brand_name=row[1]) for row in res] if res else None

            if len(res)>0:

                for r in res:
                    c = Citation()

                    c.setCitationId(r[0])
                    c.setCitationPublication(r[1])
                    c.setCitationValue(r[2])


                    liste_c.append(c)

                return liste_c

            else:

                return None

        except Exception as e:
            print(f"Erreur_CitationDAO.findAll() ::: {e}")
        finally:
            self.cur.close()

    # UPDATE


    def update(self, citation)->int:
        try:
            query = '''UPDATE citation SET publication = %s WHERE id = %s;'''
            self.cur.execute(query, (citation.getCitationPublication(), citation.getCitationId()))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_CitationDAO.update() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    # DELETE


    def deleteById(self, citationId)->int:
        try:
            query = f'''DELETE FROM citation WHERE citation_id = %s;'''
            self.cur.execute(query, (citationId,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_PublicationDAO.deleteById() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()


    def findCitationsNodes(self, citationId)->list:
        try:
            query = f'''with
                            desired_citation as (
                                Select id,value
                                From citation
                                Where id = %s 
                            )
                            Select
                                c.id,
                                c.publication,
                                compare_citations (c.value, dc.value) as nb_references
                            From
                                citation c
                                cross join desired_citation dc
                            where
                                c.id <> dc.id
                                and compare_citations (c.value, dc.value) > 10
                            Limit 20;
                        '''
            self.cur.execute(query, (citationId,))
            res = self.cur.fetchall()
            liste_c = []
            if len(res)>0:
                for r in res:
                    c = Citation()

                    c.setCitationId(r[0])
                    c.setCitationPublication(r[1])
                    c.setCitationValue(r[2])
                    liste_c.append(c)
                return liste_c
            else:
                return None
        except Exception as e:
            print(f"Erreur_CitationDAO.FindById() ::: {e}")
        finally:
            self.cur.close()

    def findCompareCitations(self, citationId,compareCitationId)->object:
        try:
            query = '''
                with
                desired_citation as (
                    SELECT id,value
                    FROM citation
                    WHERE id = %s 
                )
                SELECT c.id, c.publication, compare_citations (c.value, dc.value) as nodes
                FROM citation c
                CROSS JOIN desired_citation dc
                WHERE c.id = %s
                '''
            self.cur.execute(query, (citationId,compareCitationId))
            res = self.cur.fetchone()

            if res:
                c = Citation()
                c.setCitationId(res[0])
                c.setCitationPublication(res[1])
                c.setCitationValue(res[2])
                return c
            else:
                return None
        except Exception as e:
            print(f"Erreur_CitationDAO.FindById() ::: {e}")
        finally:
            self.cur.close()
        

    def createCountsFunction(self, citationId)->int:
        try:
            query = f'''
                CREATE OR REPLACE FUNCTION count_ones(value TEXT) RETURNS INTEGER AS $$
                DECLARE
                    counter INTEGER := 0;
                    i INTEGER := 1;
                BEGIN
                    WHILE i <= LENGTH(value) LOOP
                        IF SUBSTRING(value FROM i FOR 1) = '1' THEN
                            counter := counter + 1;
                        END IF;
                        i := i + 1;
                    END LOOP;
                    
                    RETURN counter;
                END;
                $$ LANGUAGE plpgsql;
                '''
            self.cur.execute(query, ())
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_CitationDAO.createCountsFunction() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()
    
    def createCompareCitationsFunction(self)->int:
        try:
            query = f'''
                CREATE OR REPLACE FUNCTION compare_citations(string1 TEXT, string2 TEXT) RETURNS INTEGER AS $$
                DECLARE
                    citation_number INTEGER := 0;
                    i INTEGER := 1;
                BEGIN
                    WHILE i <= LENGTH(string1) AND i <= LENGTH(string2) LOOP
                        IF SUBSTRING(string1 FROM i FOR 1) = '1' AND SUBSTRING(string2 FROM i FOR 1) = '1' THEN
                            citation_number := citation_number + 1;
                        END IF;
                        i := i + 1;
                    END LOOP;

                    RETURN citation_number;
                END;
                $$ LANGUAGE plpgsql;
                '''
            self.cur.execute(query, ())
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_CitationDAO.createCompareCitationsFunction() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()