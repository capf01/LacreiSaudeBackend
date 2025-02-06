Lacrei Saúde Backend

Introdução

O Lacrei Saúde Backend é o servidor responsável por gerenciar os serviços da plataforma Lacrei Saúde, uma iniciativa voltada para fornecer atendimento médico inclusivo e acessível. Este repositório contém todas as configurações necessárias para o desenvolvimento, manutenção e contribuição ao projeto.

Abaixo, você encontrará um guia detalhado para configurar o ambiente de desenvolvimento e executar o projeto localmente.

1. Configuração do Ambiente

1.1 Instale o Poetry

O Poetry é uma ferramenta de gerenciamento de dependências e empacotamento para Python. Ele facilita a criação de ambientes virtuais e a instalação de pacotes necessários para o projeto.

Instalação no Linux/macOS

Execute o seguinte comando no terminal:

curl -sSL https://install.python-poetry.org | python3 -

Instalação no Windows

Abra o PowerShell e execute:

(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

Após a instalação, verifique se o Poetry foi instalado corretamente:

poetry --version

1.2 Clone o Repositório

Para obter uma cópia do código-fonte do projeto, execute:

git clone https://github.com/capf01/LacreiSaudeBackend.git
cd LacreiSaudeBackend

1.3 Configure o Ambiente Virtual e Instale as Dependências

O Poetry cria automaticamente um ambiente virtual e instala as dependências do projeto:

poetry install

Este comando irá:

Criar um ambiente virtual para o projeto (caso ainda não exista);

Instalar todas as dependências listadas no arquivo pyproject.toml.

1.4 Ative o Ambiente Virtual

Após a instalação das dependências, ative o ambiente virtual:

poetry shell

Agora você poderá executar comandos Python e scripts do projeto dentro do ambiente virtual.

1.5 Configure as Variáveis de Ambiente

O projeto pode exigir variáveis de ambiente para funcionamento correto. Crie um arquivo .env na raiz do projeto e adicione os valores necessários. Exemplo:

DATABASE_URL=postgresql://usuario:senha@localhost:5432/lacrei_saude
SECRET_KEY=sua_chave_secreta_aqui
DEBUG=True

2. Banco de Dados

Se o projeto utilizar um banco de dados, aplique as migrações para criar as tabelas necessárias:

poetry run python manage.py migrate

3. Executando o Servidor

Para iniciar o servidor de desenvolvimento, execute:

poetry run python manage.py runserver

O servidor estará disponível no navegador em:
👉 http://127.0.0.1:8000/

4. Executando Testes

Para garantir que tudo está funcionando corretamente, execute os testes do projeto:

poetry run python manage.py test

5. Contribuindo para o Projeto

Se você deseja contribuir para o desenvolvimento do Lacrei Saúde Backend, siga as etapas abaixo:

5.1 Faça um Fork do Repositório

No GitHub, clique em Fork para criar uma cópia do repositório no seu perfil.

5.2 Crie uma Nova Branch

Dentro do repositório clonado, crie uma branch para suas alterações:

git checkout -b minha-feature

5.3 Faça as Alterações e Commit

Após realizar as alterações no código, faça o commit:

git commit -m "Adicionando nova feature"

5.4 Envie as Alterações para o Repositório Remoto

git push origin minha-feature

5.5 Abra um Pull Request

Acesse o repositório no GitHub e abra um Pull Request para revisão.

6. Documentação Adicional

Para mais informações sobre o projeto e sua arquitetura, consulte a documentação disponível no diretório docs/ ou no repositório do GitHub.

Caso tenha dúvidas ou precise de suporte, sinta-se à vontade para abrir uma issue no repositório oficial.