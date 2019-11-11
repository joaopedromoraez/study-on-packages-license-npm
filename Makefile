all: 
	@mkdir repositories

	@mkdir summary-licenses-csv summary-licenses-json summary-licenses-filter graphs

	@wget -O src/Domains_of_5,000_GitHub_Repositories_-_Public_-_Domains.csv https://zenodo.org/record/804474/files/Domains%20of%205%2C000%20GitHub%20Repositories%20-%20Public%20-%20Domains.csv?download=1

	@sudo apt-get install python-dev xz-utils zlib1g libxml2-dev libxslt1-dev libbz2-1.0 python3-pip

	@pip3 install matplotlib 

	@pip3 install pandas

	@wget https://github.com/nexB/scancode-toolkit/releases/download/v2.2.1/scancode-toolkit-2.2.1.zip

	@unzip scancode-toolkit-2.2.1.zip

	@mv scancode-toolkit-2.2.1 scancode-toolkit

	@rm scancode-toolkit-2.2.1.zip

	@scancode-toolkit/scancode --help

clone:
	@python3 src/clone-repositories.py

scancode:
	@python3 src/license-scan.py

duplicate:
	@python3 src/duplicate-license.py

resumeCSV:
	@python3 src/duplicate-license-csv.py

graphics:
	@python3 src/statistical-graphs.py