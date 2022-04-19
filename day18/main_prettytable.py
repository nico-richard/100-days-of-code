from prettytable import PrettyTable

table = PrettyTable()

table.add_column('Name', ['Nico', 'Lucie', 'Sylvain'])
table.add_column('Height', ['180', '170', '192'])
table.align = 'l'

print(table)