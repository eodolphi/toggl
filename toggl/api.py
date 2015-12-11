import slumber
from toggl.config import API_KEY, WORKSPACE

api = slumber.API('https://www.toggl.com/api/v8/', auth=(API_KEY, 'api_token'), append_slash=False)

projects = api.workspaces(WORKSPACE).projects
clients = api.workspaces(WORKSPACE).clients
time_entries = api.time_entries

