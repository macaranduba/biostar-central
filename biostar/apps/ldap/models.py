from django.conf import settings
import ldap


class CN_TYPES():
    CONTAINER = 'Container'
    SCHEMA ='Schema'
    CONFIGURATION = 'Configuration'
    USERS = 'Users'


class Ldap():
    
    def __init__(self):
        #initializing connection values
        dc = 'corp.amdocs.com'

    def _get_conn(self, user=None, password=None):
        """
        Returns LDAP connection
        """
        conn = ldap.initialize('ldap://raadc1.corp.amdocs.com:389', LDAP_INITIALIZE)
        conn.protocol_version = ldap.VERSION3
        conn.simple_bind_s(self._get_str_(user, CN_TYPES.USERS))

    def authenticate(self, user, password):
        """
        Authenticate a user in LDAP
        """
        self._get_conn(user, password)


if __name__=='__main__':
    printf('For LDAP testing')
    #do something to test this class alone
