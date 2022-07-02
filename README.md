# Scraper

## Constraints

I decided to give myself 4 hours max on this project. </br>

The submission would be submitted at the end of 4 hours regardless of the project state. I didn't want to spend the
majority of my freetime outside of work, school, and family making this as flexibile, effecient, and pythonic as
possible.

<ul>
<li>1 hour was spent planning</li>
<li>1 hour spent creating front-end</li>
<li>1 hour spent creating back-end</li>
<li>1 hour writing tests and documentation</li>
</ul>

## Challenges and Solutions

<table>
<tr><td>Challenge</td><td>Solution</td></tr>
<tr><td>Pagination</td><td>Specifying "start=" parameter to a product of x*15, x = page</td></tr>
<tr><td>Slow speeds due to multiple requests</td><td>Creating worker pull and unrolling request loop 5 times. Not sure exact % of performance increase with this, but increasing concurrent requests from 3 to 5 was a ~ 40%-50% decrease in execution time.</td></tr>
<tr><td>Some HTML elements didn't have id's or class names</td><td>scrape parent elements and validate data from there</td></tr>
<tr><td>Verbose code due to unforeseen challenges</td><td>List comprehensions, zip() functions, reduce repeated code by making functions</td></tr>
<tr><td>Testing due to self-inflicted time constraints</td><td>Only wrote tests to test basic functionality, didn't create mocked requests and static test documents</td></tr>
</table>

## Running the Scraper

unzip the scraper.zip file

open terminal and cd to root of project

### For Linux + macOS, run these commands in order:
create and activate virtual environment:</br>
```
python3 -m ensurepip --upgrade
```

```
python3 -m venv venv
```

```
source venv/bin/activate
```
Install requirements

if running NOT unit tests run this command:

```
python3 -m pip install -r requirements.txt
```

if running unit tests run this command:

```
python3 -m pip install -r requirements-dev.txt
```

### For Windows:
create and activate virtual environment:</br>

```
python -m ensurepip --upgrade
```

```
python -m venv venv
```

```
venv\Scripts\activate.bat
```
Install requirements

if running NOT unit tests run this command:

```
python3 -m pip install -r requirements.txt
```

if running unit tests run this command:

```
python3 -m pip install -r requirements-dev.txt
```

# Running the Scraper

Once requirements have been installed, run:

```
python3 main.py
```

It should now launch the service on: [http://localhost:9081]("http://localhost:9081")

Once the page is loaded, you can select either the JSON or CSV button.

Clicking each on will download a posts file with the respective file type selected.

The scraper is ran each time the button is pressed to ensure up-to-date results

# Running Tests

If you installed requirements-dev.txt and would like to run the unit tests, run the following command in the root of the
project:

``` 
pytest tests/ -vv 
```




