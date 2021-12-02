import pathlib

import click
import colorama
from colorama import Fore, Style

import levantamento_op

colorama.init()


def main():

    cwd = pathlib.Path.cwd()
    setup_headers_filepath = cwd / "config/setup-headers.json"
    setup_setores_filepath = cwd / "config/setup-setores.json"
    setup_templates_filepath = cwd / "config/setup-templates.json"
    user_data_filepath = cwd / "config/user-data.json"
    results_csv = cwd / "results/levantamento-results.csv"
    click.echo(click.style("\n Failsafe Activated halting bot.", fg="red"))
    fail_state, missing_setores, missing_modelos = levantamento_op.configs_validation(
        setup_templates_filepath, setup_setores_filepath, user_data_filepath
    )
    if fail_state is True:
        click.echo("Resolva os erros dos arquivos de configuração para continuar.")
        for modelo in missing_modelos:
            click.echo(
                "O sertor "
                + Fore.RED
                + modelo
                + Style.RESET_ALL
                + " não consta no arquivo de configuração {}".format(
                    setup_setores_filepath
                )
            )
        for setor in missing_setores:
            click.echo(
                "O sertor "
                + Fore.RED
                + setor
                + Style.RESET_ALL
                + " não consta no arquivo de configuração {}".format(
                    setup_setores_filepath
                )
            )
        return
    header, data = levantamento_op.get_data_from_json(
        setup_templates_filepath,
        setup_setores_filepath,
        setup_headers_filepath,
        user_data_filepath,
    )
    levantamento_op.write_to_file(header, data, results_csv)


if __name__ == "__main__":
    main()
