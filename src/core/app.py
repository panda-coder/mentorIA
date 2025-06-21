"""Main application entry point for Kivy version"""

from core.containers import Container


def run():
    """Run the Kivy application"""
    try:
        container = Container()
        container.wire(modules=[__name__])
        
        app = container.main_app()
        app.run()
        
    except Exception as ex:
        print(f"ERROR in app.run(): {ex}")
        import traceback
        traceback.print_exc()