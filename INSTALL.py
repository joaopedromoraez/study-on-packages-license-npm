import os
# Baixa o .CSV
#Cria o repositorio onde serão clonados os repositorios da lista
os.system("mkdir repositories")
#Cria diretorio que salva o resumo de licencas de cada repositorio
os.system("mkdir summary-licenses-csv summary-licenses-json summary-licenses-filter")

os.system("wget -O Domains_of_5,000_GitHub_Repositories_-_Public_-_Domains.csv https://zenodo.org/record/804474/files/Domains%20of%205%2C000%20GitHub%20Repositories%20-%20Public%20-%20Domains.csv?download=1")

os.system("sudo apt-get install python-dev xz-utils zlib1g libxml2-dev libxslt1-dev libbz2-1.0")

os.system("wget https://github.com/nexB/scancode-toolkit/releases/download/v2.2.1/scancode-toolkit-2.2.1.zip")

os.system("unzip scancode-toolkit-2.2.1.zip")

os.system("mv scancode-toolkit-2.2.1 scancode-toolkit")

os.system("rm scancode-toolkit-2.2.1.zip")

os.system("scancode-toolkit/")

os.system("./scancode --help")
