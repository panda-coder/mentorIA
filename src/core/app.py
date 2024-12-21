
from flet import app

from core.containers import Container
from dependency_injector.wiring import inject



@inject
def main(page):
    container = Container()
    container.wire(modules=[__name__])

    main_page = container.main_page()
    main_page.build(page)
    return None

def run():
    app(target=main)