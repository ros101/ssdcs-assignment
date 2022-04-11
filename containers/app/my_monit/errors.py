'''Exceptions raised in the application'''

class AuthorizationException(Exception):
    '''The user is not authorized'''

class DbIntegrityError(Exception):
    '''Integrity violation on db'''