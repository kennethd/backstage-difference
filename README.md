
# differencesvc

Example code implementation of a web service that accepts a number *n* and
returns the difference between sum(1..n)^2 and sum(1^2, ..., n^2)

## Introduction

Let me begin by stating what you will soon discover: I varied from the spec in
implementation details in terms of packages used.

I should have mentioned in our conversation that I was not a Django developer,
and I felt it would take an unreasonable amount of time for me to complete the
task in an unfamiliar framework.  I also hope altering the question somewhat
from "How would you implement this using X" to "How would you implement this
quickly using the tools of your choice" will provide interesting talking
points about our different choices.

In addition to switching from Django to Flask, I have also switched to a
sqlite3 data store.  For such a lightweight service, with such simple data
requirements, it seemed to me the benefits of no additional setup outweighs
any particular db's featureset.  It also allowed me to re-use some code I had
lying around from a personal project.

## Setup

For rapid prototyping and deployment I generally re-use a few simple Makefile
recipies, and I have done so here.  At the very least it provides a reference
implementation of the preferred command for running unit tests, and managing
extra-python package dependencies, etc...  The included version assumes a
Debian-based system for package dependencies.

To ensure all system dependencies and virtualenv Python dependencies are
installed, simply type (while in the project's root directory):

```
    make package-deps install
```

**WARNING `make package-deps` calls `sudo apt-get upgrade` and may alter your
system!** If you don't want to risk your system being updated, just make sure
you have the requirements listed below & only issue `make install`

`make install` also re-initializes your database (after creating a backup for
you), if you want to re-install the package & maintain your db without having
to copy the backup back into place, use `make upgrade` instead.

To run the app on the default port, do

```
    make run
```

If your port 8000 is occupied, you can specify a non-default port:

```
    make APP_PORT=8080 run
```

Developers can run the app in debug mode via `make debug`.

## Requirements

Debian packages

  * git
  * GNU make 
  * python2.7 
  * python-dev 
  * python-pip 
  * python-virtualenv

Python packages (installed into virtualenv by `make install` command, above)

  * flask
  * nose
  * coverage
  * pylint

## Service request endpoints

  * `GET /difference/{number}`

Also supported is the spec mandated `GET /difference?number=n`

Returns JSON:
```json
    {
        "datetime": request_datetime,
        "value": difference,
        "number": n,
        "occurrences": number_of_times_n_has_been_requested
    }
```

  * `GET /difference/history/{number}`

Again, `GET /difference/history?number=n` should also be supported.

Returns JSON dict with single key named "items", which contains a list of the
above structures.

## Web frontend endpoints

  * `GET /`



