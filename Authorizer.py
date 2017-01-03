
import argparse


from oauth2client.file import Storage
from oauth2client.client import flow_from_clientsecrets
from oauth2client import tools


class Authorizer:
    def __init__(self, storage_filename):
        self.storage = Storage(storage_filename)

    SCOPE = 'https://www.googleapis.com/auth/contacts.readonly' # https://www.google.com/m8/feeds/

    # Partly as per https://cloud.google.com/appengine/docs/python/endpoints/access_from_python
    def autherise_via_constructed_wsflow(self, flags):

        # Acquire and store oauth token.
        credentials = self.storage.get() # RC modded - use member storage.

        if credentials is None or credentials.invalid:
            flow = flow_from_clientsecrets("client_secret.json",
                                           scope=self.SCOPE)

            credentials = tools.run_flow(flow, self.storage, flags)
