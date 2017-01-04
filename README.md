
# Google Contact Manipulation

Beginning of a project intended to make some corrections to systematic problems in google contacts caused
by dodgy import from Palm years ago.

### Context

https://developers.google.com/gdata/

### General How-To

https://developers.google.com/google-apps/contacts/v3/

https://developers.google.com/identity/protocols/OAuth2

https://developers.google.com/identity/protocols/OAuth2InstalledApp

*Note that the " Choosing a Redirect Method" part of above page seems unnecessary with flows (I hope).*

#### Note Flows:

https://developers.google.com/api-client-library/python/guide/aaa_oauth

*Note OAuth2WebServerFlow used also for installed applications.*

### A couple of different methods, maybe out of date:

http://stackoverflow.com/questions/38708796/why-is-oauth2webserverflow-used-in-this-example


### Includes example of establishing credentials - although from appengine. Other stuff I don't really understand

https://cloud.google.com/appengine/docs/python/endpoints/access_from_python


### Method using flow, but not run_flow - step by step. Gets secret etc from json file.

http://www.datadependence.com/2016/03/google-python-library-oauth2/


### For gmail, but seems too be clearer, and dated Nov 16 so presumably more up-to-date...

https://developers.google.com/gmail/api/quickstart/python


### gdata client
But above not using gdata client. Plenty of examples of applying authorization one acquired to http object and so then to service. But how does this mesh with the gdata client object? Ah!, seems from this that can apply directly to client (specifically used for contacts api):

http://stackoverflow.com/questions/14742382/how-do-i-authorize-a-gdata-client-without-using-the-gdata-oauth2-workflow

But get an error:

TypeError: new_request() got an unexpected keyword argument 'auth_token'

Possible solution:

http://stackoverflow.com/questions/33619181/unexpected-keyword-auth-token-using-python-gdata-getcontacts

### What are these command-line options?
Various examples use try to use command line options for oauth2, but none even suggest what these look like...


### Misc
Martin Fowler on (outdated) access from Ruby. Rather low level.

http://martinfowler.com/articles/command-line-google.html


## Set-up

Added oauth2 to specific env in anaconda using:

conda install -c bioconda oauth2client=1.5.2

Added gdata

conda install gdata
