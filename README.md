# Requirements
1. Python 3.7.3+
2. MacOS
3. ChromeDriver 84.0.4147.30 with chrome version 84+
4. Selenium
5. Pytest-bdd 3.3.0+

# Setup_guide
Python
1. Install homebrew "
>https://brew.sh/

2. Install npm and Node.js by homebrew
>brew install npm

3. Install python by npm 
>npm install python

Chromedriver
1. Access caskroom from Homebrew 
>brew tap homebrew/cask

2. Install Chromedriver from Homebrew caskroom 
>brew cask install chromedriver

Selenium
1. Install by python package installer pip 
>pip install selenium

Pytest-bdd
1. Install by python package installer pip 
>pip install pytest-bdd

# Description
Aim: Automate the trade page of CRO/USDC with google chrome

Test case:

	A - Reach CRO/USDC trade page:
		A01: Start chrome and go to homepage (https://crypto.com/exchange)
		A02: Click CRO Markets -> CRO/USDC to access CRO/USDC trade page

	B - Check CRO/USDC trade page:
		B01: Check trade page layout (trading view, order list box, trading history, trading box)
		B02: Reach login page from trade page by clicking <Login> button on trading box
		B03: Check order history
		B04: Check trading box input 


# Steps
execute by
>pytest steps
