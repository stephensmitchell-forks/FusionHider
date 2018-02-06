# Importing sample Fusion Command
# Could import multiple Command definitions here
from .HiderCommand import HiderCommand


commands = []
command_definitions = []

# Define parameters for 1st command
cmd = {
    'cmd_name': 'Hider',
    'cmd_description': 'Iterate Bodies',
    'cmd_id': 'cmdID_demo44',
    'cmd_resources': './resources',
    'workspace': 'FusionSolidEnvironment',
    'toolbar_panel_id': 'SolidScriptsAddinsPanel',
    'class': HiderCommand
}
command_definitions.append(cmd)

# Set to True to display various useful messages when debugging your app
debug = False

# Don't change anything below here:
for cmd_def in command_definitions:
    command = cmd_def['class'](cmd_def, debug)
    commands.append(command)


def run(context):
    for run_command in commands:
        run_command.on_run()


def stop(context):
    for stop_command in commands:
        stop_command.on_stop()
