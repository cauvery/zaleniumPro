# zaleniumPro


## Overview

Zalenium Demo project


## Prerequisites
Python 3 and pip

## Installation

Clone the repo:

```
  $ git clone https://github.com/cauvery/zaleniumPro.git
```

Install `pip` the python package installer, if you don't already have it:

```
  $ sudo easy_install pip
```

Next, install the required dependencies:

```
  $ pip install -r requirements.txt 
```
## Pull Docker images and run docker to start zalenium

```
docker pull elgalu/selenium
```

```
docker pull dosel/zalenium
```

```
docker run --rm -ti --name zalenium -d -p 4444:4444 -e PULL_SELENIUM_IMAGE=true -v /var/run/docker.sock:/var/run/docker.sock --privileged dosel/zalenium start
```

## To view to docker console from browser
http://localhost:4444/grid/console

## For live preview of tests execution from browser
http://localhost:4444/grid/admin/live

## For zalenium dashboard
http://localhsot:4444/dashboard

## Execute the tests 
To execute the tests from command line option
```
  $ pytest -s tests 
```

To execute the tests in parallel use -n command line option
```
  $ pytest -s tests -n 3
```

