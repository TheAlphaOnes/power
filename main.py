import typer,sys
from rich.console import Console
from typing_extensions import Annotated
from typing import Optional

from plugs.app_manager import *

console =  Console()
app = typer.Typer(invoke_without_command=True)


@app.command()
def home(name: Annotated[Optional[str], typer.Argument(sys.argv)] = None):
    if name:
        print(name)
    else:
        print("home")

@app.command()
def create(name:str):
    print("create"+name)

@app.command()
def init():
    print("init")

@app.command()
def clear():
    print("clear")

@app.command()
def show():
    print("show")

@app.command()
def clip():
    print("clip")

@app.command()
def remove():
    print("remove")

@app.command()
def backup():
    print("backup")

@app.command()
def edit():
    print("edit")

@app.command()
def search():
    print("search")

def default(name: Annotated[Optional[str], typer.Argument(sys.argv)] = None):
    print(name)
    if name:print("This is my function!"+name)
    else:print("This is my function!")


def main():
    args = sys.argv
    if len(args) == 1:
        power('Norm',"12/7/23")





if __name__ == "__main__":

    app(main())
