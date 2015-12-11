Automate your Toggling
-----------------------

No longer fear the moment when Eva asks you to update toggle. Simply type:

    $ toggl fix

And be done with it.

Installation
------------

    $ pip install toggl


Configuration
-------------

Create a `.toggle` file in your home directory with the following content:

    [API]

    key = <your api key> # Can be obtained at: https://www.toggl.com/app/profile

    workspace = 566021 # Your deault workspace

    [LOCATION]

    timezone = europe/amsterdam

    [PROJECTS]

    default = 10128232 # Your default project 

    [SCHEDULE]

    monday = 8:30-12:30,13:00-17:00

    tuesday = 8:30-12:30,13:00-17:00

    wednesday = 8:30-12:30,13:00-17:00

    thursday = 8:30-12:30,13:00-17:00

    friday = 8:30-12:30,13:00-17:00
