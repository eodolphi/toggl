import time

import arrow
import click

from toggl import api
from toggl import schedule


@click.group()
def toggl_app():
    """ Command line access to toggl.com

    Report time using the command line!
    """


@toggl_app.command()
def info():
    """
    Get info about your toggle environment
    """
    clients = dict((client['id'], client) for client in api.clients.get())
    projects = [project for project in api.projects.get() if project['active']]

    workspaces = set(str(project['wid']) for project in projects)
    click.echo(
        'You have access to the following workspaces: {}\n'.format(
            ', '.join(workspaces)
        )
    )

    click.echo('And the following project....\n')

    for project in projects:
        client = clients.get(project.get('cid'))
        click.echo(
            '    {name}: {id} ({client})'.format(
                name=project['name'],
                id=project['id'],
                client=client['name'] if client else 'No client'
            )
        )


@toggl_app.command()
@click.option('--start', type=click.STRING)
def fix(start):
    """
    Update toggle according to your schedule.

    Starting from the last day you filled in
    """
    if start:
        start = arrow.get(start)
    else:
        start = arrow.get(api.time_entries.get(start_date=arrow.get(1970, 01, 01).isoformat())[-1]['start'])
        start = start.replace(days=+1)

    entries = schedule.time_entries(start)
    click.echo('Toggling from {}. Hang on, this might take while'.format(
        start.humanize()
    ))
    for entry in entries:
        time.sleep(1)

        api.time_entries.post({
            'time_entry': {
                'description': '',
                'pid': entry['project'],
                'duration': (entry['end'] - entry['start']).seconds,
                'start': entry['start'].isoformat(),
                'created_with': 'toggle/eodolphi'
            }
        })


if __name__ == '__main__':
    toggl_app()
