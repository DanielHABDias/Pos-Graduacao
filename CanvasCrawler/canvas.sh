#!/usr/bin/env bash

set -u

PROJECT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
VENV_DIR="$PROJECT_DIR/.venv"
PYTHON="$VENV_DIR/bin/python"

if [[ -t 1 ]]; then
    BLUE='\033[1;34m'
    CYAN='\033[1;36m'
    GREEN='\033[1;32m'
    YELLOW='\033[1;33m'
    RED='\033[1;31m'
    RESET='\033[0m'
else
    BLUE=''
    CYAN=''
    GREEN=''
    YELLOW=''
    RED=''
    RESET=''
fi

show_header() {
    clear 2>/dev/null || true
    printf "%b\n" "${BLUE}======================================================${RESET}"
    printf "%b\n" "${CYAN}                  CANVAS PUC MINAS${RESET}"
    printf "%b\n" "${BLUE}======================================================${RESET}"
    printf "Organizador pessoal de disciplinas e materiais\n\n"
}

show_help() {
    printf "Uso:\n"
    printf "  ./canvas.sh                    Abre o menu interativo\n"
    printf "  ./canvas.sh verificar          Testa token e conexão\n"
    printf "  ./canvas.sh formacoes          Mostra ADS e IA\n"
    printf "  ./canvas.sh disciplinas        Seleciona uma formação e lista disciplinas\n"
    printf "  ./canvas.sh explorar           Navega até os itens de um módulo\n"
    printf "  ./canvas.sh baixar             Baixa uma disciplina ou uma formação\n"
    printf "  ./canvas.sh concluir           Marca itens manuais como concluídos\n"
    printf "  ./canvas.sh ajuda              Exibe esta ajuda\n"
}

prepare_environment() {
    if [[ ! -x "$PYTHON" ]]; then
        printf "%b\n" "${YELLOW}Preparando o ambiente Python pela primeira vez...${RESET}"
        if ! command -v python3 >/dev/null 2>&1; then
            printf "%b\n" "${RED}Python 3 não foi encontrado.${RESET}"
            return 1
        fi
        if ! python3 -m venv "$VENV_DIR"; then
            printf "%b\n" "${RED}Não foi possível criar o ambiente virtual.${RESET}"
            printf "No Ubuntu/Debian, instale python3-venv e execute novamente:\n"
            printf "  sudo apt install python3-venv\n"
            return 1
        fi
    fi

    if ! "$PYTHON" -c 'import bs4, dotenv, faster_whisper, httpx, markdownify' >/dev/null 2>&1; then
        printf "%b\n" "${YELLOW}Instalando as dependências do Canvas PUC Minas...${RESET}"
        if ! "$PYTHON" -m pip install -e "$PROJECT_DIR"; then
            printf "%b\n" "${RED}Não foi possível instalar as dependências.${RESET}"
            return 1
        fi
    fi
}

run_app() {
    (
        cd "$PROJECT_DIR" || exit 1
        "$PYTHON" -m canvas_crawler "$@"
    )
}

pause_menu() {
    if [[ -t 0 ]]; then
        printf "\n"
        read -r -p "Pressione Enter para voltar ao menu..." _
    fi
}

run_direct_command() {
    case "${1:-}" in
        verificar)
            run_app doctor
            ;;
        formacoes)
            run_app programs
            ;;
        disciplinas)
            run_app courses
            ;;
        explorar)
            run_app inspect
            ;;
        baixar|crawler)
            run_app crawl
            ;;
        concluir)
            run_app complete
            ;;
        ajuda|-h|--help)
            show_help
            ;;
        *)
            printf "%b\n\n" "${RED}Comando desconhecido: ${1:-}${RESET}"
            show_help
            return 2
            ;;
    esac
}

show_menu() {
    while true; do
        show_header
        printf "%b\n" "${GREEN}1.${RESET} Verificar conexão com o Canvas"
        printf "%b\n" "${GREEN}2.${RESET} Ver minhas formações"
        printf "%b\n" "${GREEN}3.${RESET} Ver disciplinas de uma formação"
        printf "%b\n" "${GREEN}4.${RESET} Explorar módulos e itens"
        printf "%b\n" "${GREEN}5.${RESET} Baixar e organizar uma disciplina"
        printf "%b\n" "${GREEN}6.${RESET} Marcar itens como concluídos"
        printf "%b\n" "${GREEN}7.${RESET} Ajuda e comandos rápidos"
        printf "%b\n" "${GREEN}0.${RESET} Sair"
        printf "\n"
        read -r -p "Escolha uma opção: " option

        case "$option" in
            1)
                printf "\n"
                run_app doctor
                pause_menu
                ;;
            2)
                printf "\n"
                run_app programs
                pause_menu
                ;;
            3)
                printf "\n"
                run_app courses
                pause_menu
                ;;
            4)
                printf "\n"
                run_app inspect
                pause_menu
                ;;
            5)
                printf "\n"
                run_app crawl
                pause_menu
                ;;
            6)
                printf "\n"
                run_app complete
                pause_menu
                ;;
            7)
                printf "\n"
                show_help
                pause_menu
                ;;
            0)
                printf "\nAté a próxima!\n"
                return 0
                ;;
            *)
                printf "%b\n" "${RED}Opção inválida.${RESET}"
                pause_menu
                ;;
        esac
    done
}

main() {
    if [[ "${1:-}" == "ajuda" || "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
        show_help
        return 0
    fi

    prepare_environment || return 1

    if [[ $# -gt 0 ]]; then
        run_direct_command "$1"
    elif [[ -t 0 ]]; then
        show_menu
    else
        printf "%b\n" "${RED}O menu precisa ser executado em um terminal.${RESET}"
        printf "Use ./canvas.sh ajuda para ver os comandos diretos.\n"
        return 1
    fi
}

main "$@"
