from cyclopts import App

app = App()

@app.command()
def serve(seedfile: str | None = None):
    """
    Start CHAP as a backend server
    """
    from .rest_api import main_backend
    main_backend()
