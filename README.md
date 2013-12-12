### This project has [moved](https://github.com/GraphAlchemist/GraphJSON.io) and is being ported to Angular.

### Inspired (and with original code) by APC Jones [Arrows project](https://github.com/apcj/arrows) and deployed at [GraphJSON.io](www.GraphJSON.io)


###Get setup###

*Make sure you have [virtualenv](http://www.virtualenv.org/en/latest/) and [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/) installed.*

This application is powered by [Flask](http://flask.pocoo.org/)
Dependencies installed seperately, [Flask-Bootstrap](http://pythonhosted.org/Flask-Bootstrap/)

###Get things running###

`mkvirtualenv -r requirements.txt your_venv_name`

`workon your_venv_name`

`git clone git@github.com:graphalchemist/ga_arrows.git`

`python app.py`

Now flask should be running at http://localhost:5000/

**Right now the arrows tool is set up at http://localhost:5000/ga_arrows/tool.**

####Some thoughts####
1. All of the orignal arrows code was first commited by itelf
1. The second commit is getting flask installed
1. The third commit is getting arrows shoved into flask

* There are some differences between the version of arrows at http://www.apcjones.com/arrows/#, and the github code https://github.com/apcj/arrows.

1. All of the orignal arrows code was originally commited by itelf  
2. The second commit is getting flask installed 
3. The third commit is getting arrows shoved into flask 

* There are some differences between the version of arrows at http://www.apcjones.com/arrows/#, and the github code https://github.com/apcj/arrows
* There are also some slight differences with the version we are currently running.  This is likely because Apcj used Bootstrap 2 and we've installed Bootstrap 3 with Flask-Bootsrap
* Finally, we've started the project with an oustanding bug!  Yay!  Check it out in the issues
