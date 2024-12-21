from dependency_injector import containers, providers 
from presentation.win.main import MainPage

class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    main_page = providers.Factory(MainPage)