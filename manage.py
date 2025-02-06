#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.

Este script serve como o ponto de entrada para comandos administrativos,
permitindo executar tarefas como migrações, execução do servidor de desenvolvimento,
entre outros comandos do Django.
"""

import os  # For manipulação de variáveis de ambiente e caminhos do sistema
import sys  # Para acessar argumentos passados via linha de comando


def main():
    """Executa tarefas administrativas definidas via linha de comando."""
    
    # Define a variável de ambiente DJANGO_SETTINGS_MODULE com o módulo de configurações do Django.
    # Essa configuração é essencial para que o Django saiba onde encontrar as configurações do projeto.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    
    try:
        # Importa a função de gerenciamento do Django para executar comandos.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Caso a importação falhe, uma mensagem de erro detalhada é exibida, sugerindo possíveis causas.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Executa o comando passado via linha de comando (por exemplo, runserver, migrate, etc.)
    execute_from_command_line(sys.argv)


# Garante que o script só seja executado diretamente e não quando importado como módulo.
if __name__ == '__main__':
    main()
