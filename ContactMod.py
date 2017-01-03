
import gdata.contacts.client
import gdata.contacts.data

from oauth2client import tools

from Authorizer import Authorizer
from Outputter import Outputter

# This approach to argument parsing from some Google oauth2 example.
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

gd_client = gdata.contacts.client.ContactsClient(source='ContactMod')

authorizer = Authorizer("credentials.dat")
authorizer.autherise_via_constructed_wsflow(flags)

# This, as found somewhere else, didn't work.
#authorizer.storage.get().authorize(gd_client)

# Got further using, as per http://stackoverflow.com/questions/33619181/unexpected-keyword-auth-token-using-python-gdata-getcontacts
auth2token = gdata.gauth.OAuth2TokenFromCredentials(authorizer.storage.get())
gd_client = auth2token.authorize(gd_client)


Outputter.print_all_contacts(gd_client)
