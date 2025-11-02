from rich.console import Console
from rich.markdown import Markdown
from rich import box

data = [2,5,3,7,9,6,4,8,5]
console = Console()
console.print("Sparkline:", style='bold green')
console.print("▂▅▃▇█▆▄▇▅")