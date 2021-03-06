# Introdução à Engenharia de Software

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c67b46dff2ad4a8ca60e5c05ee199735)](https://www.codacy.com/manual/Durfan/ufsj-tp-autoimports?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Durfan/ufsj-tp-autoimports&amp;utm_campaign=Badge_Grade) [![tag](https://img.shields.io/github/v/tag/durfan/ufsj-tp-autoimports)](https://github.com/Durfan/ufsj-tp-autoimports/tree/v0.1-Contab) ![python](https://img.shields.io/pypi/pyversions/Django)

## Trabalho Prático

Este trabalho prático tem como objetivo aplicar os conceitos e ferramentas da Engenharia de Software em um caso criado para estudo.

| Desktop                    | Mobile                     |
| :------------------------: | :------------------------: |
| ![Captura](https://github.com/Durfan/ufsj-tp-autoimports/blob/master/docs/captura.png) | ![Captura](https://github.com/Durfan/ufsj-tp-autoimports/blob/master/docs/captura2.png) |

## Tecnologias e Padrões de Projeto Utilizados

### Visão de Implementação

O trabalho prático foi desenvolvido utilizando um framework que facilita o desenvolvimento dos módulos para equipes separadas. O uso de um framework para a implementação é justificado pela facilidade e praticidade em manusear um banco de dados definido nos modelos estabelecidos para cada módulo. Esse estilo arquitetural permite que outras equipes possam ter um desenvolvimento mais pratico em relação ao trabalho em outros módulos.

### Gerenciamento de Configuração e Mudança

Este repositório foi utilizado para o controle de versão, mudança e auditoria de configuração do projeto do trabalho prático. Sendo a entrega do módulo de Contabilidade o baseline estabelecido na TAG [v0.1-Contab](https://github.com/Durfan/ufsj-tp-autoimports/tree/v0.1-Contab).

### Padrão do Projeto

MVC que utiliza o [Django](https://www.djangoproject.com/) como framework para implementar os módulos, esse segue exatamente o conceito de model, view e controller como padrão arquitetural. O Django é capaz de criar cada módulo como uma aplicação em separado (webapp), sendo que cada webapp pode compartilhar da mesma estrutura dos modelos dentro de um projeto.

O Django oferece diversas configurações para a API de banco de dados. Para fins de demonstração e facilitar o deploy, o SQLite foi escolhido para integração no projeto. A migração para um banco de dados mais escalonável pode ser feita de maneira simples pelo Django.

#### Componentes

* [Google Charts](https://developers.google.com/chart) - Implementa a visualização dos gráficos de balanço no módulo Contabilidade.
* [Bootstrap](https://getbootstrap.com/) (_Frontend component library_) - Responsável pelo design do frontend do projeto.
* [Font Awesome](https://fontawesome.com/) - Iconografia de elementos do frontend.

#### Qualidade de Software

[sentry](https://sentry.io/) - Utilizado para monitoramento e verificação de qualidade em cada artefato de software. Por motivos de simplificação de desenvolvimento para outras equipes, a API foi removida.

### Deploy

[pythonanywhere](pythonanywhere.com) - O deploy foi realizado utilizando uma máquina virtual para executar o framework. Não é voltado para fins de produção, apenas para demonstração do trabalho prático. O projeto implementado nesse repositório pode ser visto em [http://durfan.pythonanywhere.com/](http://durfan.pythonanywhere.com/).

## Módulos Implementados

* :dollar: **Contabilidade**: usuários poderão gerar um extrato contendo todas as informações de compra e venda ocorridas desde o início do mês.

### Módulos Parcialmente Implementados

* :key: **Controle de acesso**: desenvolvido para permitir o controle de acesso dos usuário aos módulos implementados. Permite controle total de grupos de usuários. (Componente do framework utilizado)
* :arrows_counterclockwise: **Logística**: implementado a partir da geração de modelos para as tabelas do Banco de Dados com o objetivo de manusear os dados para o módulo de Contabilidade. Pode ser acessado através da administração do projeto.

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
