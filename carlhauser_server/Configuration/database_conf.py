# ==================== ------ STD LIBRARIES ------- ====================
import os
import pathlib
import sys
from collections import namedtuple

# ==================== ------ PERSONAL LIBRARIES ------- ====================
sys.path.append(os.path.abspath(os.path.pardir))
from carlhauser_server.Configuration.template_conf import JSON_parsable_Dict


class Default_database_conf(JSON_parsable_Dict):
    def __init__(self):
        # Please note that CERT and KEY files must be in carl-hauser/carlhauser_server (where the flask server is)

        # ============================== SCRIPTS ==============================
        self.DB_SCRIPTS_PATH = pathlib.Path('carlhauser_server', 'Data', 'database_scripts')
        # Cache, storage and test scripts directories
        self.DB_SCRIPTS_PATH_CACHE = pathlib.Path('carlhauser_server', 'Data', 'database_scripts', 'cache')
        self.DB_SCRIPTS_PATH_STORAGE = pathlib.Path('carlhauser_server', 'Data', 'database_scripts', 'storage')
        self.DB_SCRIPTS_PATH_TEST = pathlib.Path('carlhauser_server', 'Data', 'database_scripts', 'test')

        # ============================== SOCKETS ==============================
        self.DB_SOCKETS_PATH = pathlib.Path('carlhauser_server', 'Data', 'database_sockets')
        # Cache, storage and test scripts directories
        self.DB_SOCKETS_PATH_CACHE = pathlib.Path('carlhauser_server', 'Data', 'database_sockets', 'cache.sock')
        self.DB_SOCKETS_PATH_STORAGE = pathlib.Path('carlhauser_server', 'Data', 'database_sockets', 'storage.sock')
        self.DB_SOCKETS_PATH_TEST = pathlib.Path('carlhauser_server', 'Data', 'database_sockets', 'test.sock')

        # ============================== DB ==============================
        self.DB_DATA_PATH = pathlib.Path('carlhauser_server', 'Data', 'database_data')

        # ============================== DB PARAMETERS ==============================
        # Expiration time after which a add_request, computation_request, ... is removed (satisfied or not)
        self.REQUEST_EXPIRATION = 86400
        self.ANSWER_EXPIRATION = 86400

        # ============================== WORKERS PARAMETERS ==============================
        # NB of worker on launch
        self.ADDER_WORKER_NB = 2
        self.ADDER_WAIT_SEC = 1

        # NB of worker on launch
        self.REQUESTER_WORKER_NB = 2
        self.REQUESTER_WAIT_SEC = 1


def parse_from_dict(conf):
    return namedtuple("Default_database_conf", conf.keys())(*conf.values())
