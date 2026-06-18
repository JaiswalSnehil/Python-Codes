from rich.table import Table
from rich.console import Console

t = Table(title='Fruits')
t.add_column('Name')
t.add_column('Price')
t.add_row('Apple','$1')
t.add_row('Banana','$0.5')
t.add_row('Grapes','$1')
t.add_row('Orange','$0.5')
Console().print(t)