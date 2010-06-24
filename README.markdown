tg2\_webservices: A super small example showing how to do webservices / different formatted output with Turbogears 2.
===========================================================


This example uses Turbogears 2.1b2. 

This is a simple blog application, which will show off the web services applications by providing an API for reading posts etc.


To install, I recommend using pip and virtualenv.

  1. Install Turbogears 2.1b2
  
    pip install -E tg2env\
    
    -e 'hg+http://bitbucket.org/turbogears/tg-dev/@2.1b2#egg=TurboGears2'\
    
    -e 'hg+http://bitbucket.org/turbogears/tgdevtools-dev/@2.1b2#egg=tg.devtools'
    
  2. `source tg2env/bin/activate` - activate the virtualenv
  3. `paster quickstart my_wonderful_app`, which will setup the database structure etc
  4. Visit http://127.0.0.1:8080/edit_posts/ to add posts
  5. Visit http://127.0.0.1:8080/api/get/1 (or any id you created) to see post info
