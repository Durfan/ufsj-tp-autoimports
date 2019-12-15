# Introdução à Engenharia de Software

## Trabalho Prático

Este trabalho prático tem como objetivo aplicar os conceitos e ferramentas da Engenharia de Software em um caso criado para estudo.

| Desktop             |  Mobile |
:-------------------------:|:-------------------------:
![Captura](https://github.com/Durfan/ufsj-tp-autoimports/blob/master/docs/captura.png)|![Captura](https://github.com/Durfan/ufsj-tp-autoimports/blob/master/docs/captura2.png)

## Tecnologias e Padrões de Projeto Utilizados

### Visão de Implementação

O trabalho prático foi desenvolvido utilizando um framework que facilita o desenvolvimento dos módulos para equipes separadas. O uso de um framework para a implementação é justificado pela facilidade e praticidade em manusear um banco de dados definido nos modelos estabelecidos para cada módulo. Esse estilo arquitetural permite que outras equipes possam ter um desenvolvimento mais pratico em relação ao trabalho em outros módulos.

### Padrão do Prodejo

MVC que utiliza o [Django](https://www.djangoproject.com/) como framework para implementar os módulos, esse segue exatamente o conceito de model, view e controller como padrão arquitetural. O Django é capaz de criar cada módulo como uma aplicação em separado (webapp), sendo que cada webapp pode compartilhar da mesma estrutura dos modelos dentro de um projeto.

O Django oferece diversas configurações para a api de banco de dados. Para fins de demonstração e facilitar o deploy, o SQLite foi escolhido para integração no projet. A migração para um banco de dados mais escalonavel pode ser feita de maneira simples pelo Django.

#### Componentes

* [Google Charts](https://developers.google.com/chart) Implementa a visualização dos gráficos de balanço no módulo Contabilidade.
* [Bootstrap](https://getbootstrap.com/) _Front-end component library_, responsavel pelo design do front-end do projeto.
* [Font Awesome](https://fontawesome.com/) Iconografia de elementos do front-end.

## Módulos Implementados

* **Contabilidade** usuários poderão gerar um extrato contendo todas as informações de compra e venda ocorridas desde o início do mês.

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
