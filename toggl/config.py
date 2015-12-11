import ConfigParser
import os

import arrow
import click


config = ConfigParser.ConfigParser()
config.read('.toggl')
config.read(os.path.expanduser('~/.toggl'))

try:
    API_KEY = config.get('API', 'key')
    WORKSPACE = config.get('API', 'workspace')
    TIMEZONE = config.get('LOCATION', 'timezone')
    PROJECT = config.get('PROJECTS', 'default')

    SCHEDULE = {}

    for day, items in config.items('SCHEDULE'):
        SCHEDULE[day] = []
        for item in items.split(','):
            start, end = item.split('-')
            SCHEDULE[day].append({
                'start': arrow.get(start, 'h:mm'),
                'end': arrow.get(end, 'h:mm')
            })
except ConfigParser.NoSectionError, e:
    raise click.UsageError(
        'Invalid configuration. Please fix your configuration in ~/.toggl:\n{}'.format(
            e
        )
    )
