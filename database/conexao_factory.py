import psycopg2

class ConexaoFactory:
    def get_conexao(self):
        psycopg2.connect(host='silly.db.elephantsql.com', database='kftvhvxo', 
                     user='kftvhvxo', password='UrqNmPPcgkLTPmXezzWyAN2zezG71PCG')
