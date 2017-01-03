
# Partly based on example https://developers.google.com/google-apps/contacts/v3/


class Outputter:
    def __init__(self):
        pass # No content for now.

    @staticmethod
    def print_all_contacts(gd_client):
        feed = gd_client.GetContacts()
        for i, entry in enumerate(feed.entry):

            if entry.name and entry.name.full_name and entry.name.full_name.text:
                print '\n%s %s' % (i + 1, entry.name.full_name.text)
            else:
                print '\nNO NAME'

            if entry.content:
                print '    %s' % (entry.content.text)

            # Display the primary email address for the contact.
            for email in entry.email:
                if email.primary and email.primary == 'true':
                    print '    %s' % (email.address)

            # Display extended properties.
            for extended_property in entry.extended_property:
                if extended_property.value:
                    value = extended_property.value
                else:
                    value = extended_property.GetXmlBlob()
                print '    Extended Property - %s: %s' % (extended_property.name, value)
