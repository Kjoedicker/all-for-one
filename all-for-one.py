import argparse
import sys
import os


# TODO: switch this over to a config?
programs = {
    'gri': 'python3 ../gri/main.py',
    'pker': 'perl ../pker/pker.pl',
    'watchkeeper': 'go run ../watchkeeper/main.go',
    'git-delorean': 'python3 ../git-delorean/main.py',
    'git-latest': 'perl ../git-latest/git-latest.pl',
    'readme-init': 'python3 ../readme-init.py',
    'jira': 'node ../private/jira-fetch/jira.js'
}

def parseCliArguments() -> (str, str):
    if (len(sys.argv) < 2):
        sys.exit('A program must be provided.')

    PROGRAM_INDEX = 1
    SUBCOMMAND_INDEX = 2

    programName = sys.argv[PROGRAM_INDEX]
    if programName not in programs:
        sys.exit(f"Program '{programName}' is not configured.")

    program = programs[programName]
    subcommands = " ".join(sys.argv[SUBCOMMAND_INDEX:]) if len(sys.argv) > 2 else ""

    return (program, subcommands)

if __name__ == '__main__':
    (program, subcommands) = parseCliArguments()
    command = f"{program} {subcommands}"
    os.system(command)