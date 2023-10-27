import argparse
import sys
import os
import yaml
import os.path

def parseCliArguments() -> (str, str):
    if (len(sys.argv) < 2):
        sys.exit('A program must be provided.')

    PROGRAM_INDEX = 1
    SUBCOMMAND_INDEX = 2

    programName = sys.argv[PROGRAM_INDEX]
    subcommands = sys.argv[SUBCOMMAND_INDEX:]

    return (programName, subcommands)

def readConfig():
    dirname = os.path.dirname(__file__) or '.'
    with open(dirname + '/programs.yml', 'r') as file:
        config = yaml.safe_load(file)
    return config
    
def buildCommand(programName: str, subCommands: str):
    config = readConfig()

    if programName not in config['programs']:
        sys.exit(f"Program '{programName}' is not configured.")

    rootPath = config['rootPath']
    program = config['programs'][programName]
    subCommands = " ".join(subCommands)

    return f"{program['runtime']} {rootPath}{program['path']} {subcommands}"

if __name__ == '__main__':
    (programName, subcommands) = parseCliArguments()
    command = buildCommand(programName, subcommands)

    os.system(command)