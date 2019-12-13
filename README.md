# Introdução à Engenharia de Software

## Trabalho Prático

Este trabalho prático tem como objetivo aplicar os conceitos e ferramentas da Engenharia de Software em um caso criado para estudo.

![Captura](https://github.com/Durfan/ufsj-tp-autoimports/blob/master/docs/captura.png)

## Instalação para o desenvolvimento dos outros módulos

Para o desenvolvimento dos módulos definidos em outros grupos, siga os passos abaixo:

``` bash
git clone https://github.com/Durfan/ufsj-tp-autoimports.git  # clonando o repositorio
pip install Django==3.0                                      # instalando o Django
cd ufsj-tp-autoimports/autoimports/                          # pasta para desenvolvimento
python manage.py runserver                                   # executando o servidor web do projeto
http://127.0.0.1:8000/                                       # pagina inicial do projeto
http://127.0.0.1:8000/admin                                  # pagina para administração do BD (SQLite)
```

### Criando o superusuário para uso no sistema

``` bash
python manage.py createsuperuser
```
