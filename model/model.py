from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()
        self._businesses_artefatto=[]  #CONTROLLARE
        self._businesses_museo=[]    #CONTROLLARE

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        if len(self._businesses_artefatto) == 0:
            self._businesses_artefatto = self._businesses_artefatto= ArtefattoDAO.read_all_businesses()
        else:
            print("No need to read again from database using SQL query")
        return self._businesses_artefatto
        # TODO   (CONTROLLARE)

    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        epoche=[]
        for i in range(len(self._businesses_artefatto)):
            epoca=self._businesses_artefatto[2]
            epoca.apppend(epoche)
        return epoche
        #TODO   (CONTROLLARE)

    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""
        if len(self._businesses_museo)==0:
            self._businesses_museo=self._businesses_museo=MuseoDAO.read_all_businesses()
        else:
            print("No need to read again from database using SQL query")
        return self._businesses_museo
        # TODO   (CONTROLLARE)

