start_with = 'interface gi1/0'
range = list(range(1, 5))
commands = ''

for port in range:
    commands += "{}/{}\n".format(start_with, port)
    commands += "no shutdown\n\n"

with open("commands.txt", "w") as cmd_file:
    cmd_file.write(commands)
