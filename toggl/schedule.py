import arrow

from toggl.config import TIMEZONE, SCHEDULE, PROJECT


def time_entries(start):
    for day in arrow.Arrow.range('day', start, arrow.now(TIMEZONE)):
        for block in SCHEDULE.get(day.format('dddd').lower(), []):
            yield {
                'start': day.replace(hour=block['start'].hour, minute=block['start'].minute),
                'end': day.replace(hour=block['end'].hour, minute=block['end'].minute),
                'project': PROJECT
            }
