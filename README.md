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

Right now the arrows tool is set up at http://localhost:5000/ga_arrows/tool.
The whole project is named ga_arrows, but the important pieces will be a 'blueprint'.
All of the necessary components of ga_arrows are stored in the ga_arrows directory in "blueprints."
Blueprints are a modular way to reuse programs in Flask.  Is there more pain in working in blueprints, not really,
they are a lot like applications, however they don't actually 'run.'  Rather they are called and rendered
by the application.  The better question is, is this complete overkill in this case - the answer would be yes.  However,
the reason we are developing a "blueprint" rather than a flask "app" is so that we can easily plug the blueprint in
to other flask apps we might have.

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
