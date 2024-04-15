# Quotes To Scrape Sandbox

A collection of websites that lists quotes from famous people. It has many endpoints showing the quotes in many different ways, each of them including new scraping challenges as described below.

| Endpoints            |                                                    |
| -------------------- | -------------------------------------------------- |
| Default              | Microdata and pagination                           |
| Scroll               | Infinite scrolling pagination                      |
| JavaScript           | JavaScript generated content                       |
| JavaScript (Delayed) | Same as JavaScript but with a delay (?delay=10000) |
| Tableful             | A table based messed-up layout                     |
| Login                | Login with CSRF token (Any user/password works)    |
| ViewStates           | An AJAX based filter form with ViewStates          |
| Random               | A single random quote                              |

There are following information that can be scraped...

- Quote Text
- Quote Author
- Quote tags

# How to Run?

1.  Clone this repository.

	```
	git clone https://github.com/VIIVIIIIX/quotes-to-scrape-sandbox.git
	```

2. Create a virtual environment.

	```
	cd quotes-to-scrape-sandbox
	python3 -m venv .venv
	```

3. Activate the virtual environment and install necessary libraries.

	```
	cd .venv
	source ./bin/activate
	cd ..
	pip install -r requirements.txt
	```

4. Change the directory and run the code to generate the csv containing data.

	- Quotes - Default

		```
		cd quotes-default
		python3 quotes-default.py
		```

	- Quotes - Scroll

		```
		cd quotes-scroll
		python3 quotes-scroll.py
		```

	- Quotes - JavaScript

		```
		cd quotes-js
		python3 quotes-js.py
		```

	- Quotes - JavaScript Delayed 

		```
		cd quotes-js-delayed
		python3 quotes-js-delayed.py
		```

	- Quotes - Login

		```
		cd quotes-login
		python3 quotes-login.py
		```

	- Quotes - Tableful

		```
		cd quotes-tableful
		python3 quotes-tableful.py
		```

	- Quotes - ViewStates

		```
		cd quotes-viewstates
		python3 quotes-viewstates.py
		```

	- Quotes - Random

		```
		cd quotes-random
		python3 quotes-random.py
		```
