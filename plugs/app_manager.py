from rich.markdown import Markdown
from rich.console import Console

import requests

console = Console()
client  = requests.Session()

def power(name,date):
    MARKDOWN = f"""
# POWER
- Loged in as {name}
- Loged on {date}
"""
    md  = Markdown(MARKDOWN)
    console.print(md,style="red bold")


