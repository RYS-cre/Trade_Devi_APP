App : TradeDevi

*** Steps to run TradeDevi application in development server ***

step 1 :    activate VIRTUAL ENVIORNMENT to save/run dependencies within development server

            to start development server...
                type >>>source trade_devi_virtual_env/bin/activate

            once finished coding/development ( making changes to the source code ), within the CLI...
                type >>>deactivate

step 1.5 :  Adding a database to the App...
                type >>>python manage.py migrate
            To view the newly added database...  
                type >>>ls -l

step 2 :    To view/run the development server to start coding..
                type >>>python manage.py runserver
                
            to quit the development server...
                type >>>control + c 

*** FOR EXTRA HELP READ THE PDF INSIDE THIS DIRECTORY *** PYTHON CRASH COURSE ***
*** EXTRA DOCS FOR THIS PROJECT... https://www.djangoproject.com/ ***
