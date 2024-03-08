"""CLI for mysetup"""
import json
import subprocess

import typer

CONTEXT_SETTINGS = {'help_option_names': ['-h', '--help']}

app = typer.Typer(
    add_completion=False,
    no_args_is_help=True,
    context_settings=CONTEXT_SETTINGS,
    help='My setup 🚀',
)


def install_with_winget_from_json(json_filename, ls: bool = False):
    with open(json_filename, encoding='utf-8') as jsonfile:
        winget_apps = json.load(jsonfile)
    for app in winget_apps['packages']:
        if ls:
            print(app['id'])
        else:
            subprocess.run(['winget', 'install', app['id']])


@app.command(name='wgb')
def wingetbasic(ls: bool = False):
    """Install or upgrade all basic winget apps."""
    install_with_winget_from_json('winget_basic.json', ls)


@app.command(name='wga')
def wingetall(ls: bool = False):
    """Install or upgrade all winget apps."""
    install_with_winget_from_json('winget_all.json', ls)


@app.command(name='py')
def install_python(ls: bool = False, force: bool = False):
    """Install or upgrade all Python versions."""
    with open('python_versions.txt', encoding='utf-8') as infile:
        py_versions = [version.strip('\n') for version in infile.readlines()]

    basic_args = ['winget', 'install']
    add_args = ['--override', '\"/passive include_launcher=0\"']

    if force:
        add_args.insert(0, '--force')

    # Install all Python versions
    for version in py_versions:
        if ls:
            print(f'Python {version}')
        else:
            subprocess.run(
                [*basic_args, f'python.python.{version}', *add_args]
            )

    # Last, make sure Python Launchers gets installed
    args = ['winget', 'install', 'python.launcher']
    if not ls:
        subprocess.run(args)


@app.command(name='ch')
def choco(ls: bool = False):
    """Install or upgrade all chocolatey apps."""
    with open('choco_all.json', encoding='utf-8') as jsonfile:
        choco_apps = json.load(jsonfile)
    for app in choco_apps['packages']:
        if ls:
            print(app['id'])
        else:
            subprocess.run(['choco', 'upgrade', app['id']])
