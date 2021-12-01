import csv
import json
from typing import Tuple


def get_data_from_json(
    setup_templates: str, setup_setores: str, headers: str, user_data_filepath: str
) -> Tuple:
    # get headers, templates-pc and setores from setup
    with open(headers, encoding="utf-8") as json_file:
        headers_data = json.load(json_file)["headers"]
    with open(setup_setores, encoding="utf-8") as json_file:
        setores_data = json.load(json_file)["setores"]
    with open(setup_templates, encoding="utf-8") as json_file:
        templates_pc = json.load(json_file)["template-pc"]
    with open(user_data_filepath, encoding="utf-8") as json_file:
        user_data = json.load(json_file)
        items = user_data["items"]
        data = []
        for index, item in enumerate(items):
            tmp_data = []
            tmp_data.append(index + 1)
            item_keys = item.keys()
            for key in item_keys:
                value = item[key]
                if key == "modelo":
                    tmp_data.extend(templates_pc[value])
                elif key == "setor":
                    tmp_data.append(setores_data[value])
                else:
                    tmp_data.append(value)
            data.append(tmp_data)
    return (headers_data, data)


def write_to_file(header: list, data: list, results: str) -> Tuple:
    with open(results, "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)
        # write multiple rows
        writer.writerows(data)


def configs_validation(
    setup_templates: str, setup_setores: str, user_data_filepath: str
):
    with open(setup_setores, encoding="utf-8") as json_file:
        setores_data = json.load(json_file)["setores"]
    with open(setup_templates, encoding="utf-8") as json_file:
        templates_pc = json.load(json_file)["template-pc"]
    with open(user_data_filepath, encoding="utf-8") as json_file:
        user_data = json.load(json_file)
        items = user_data["items"]
    missing_modelos, missing_setores, user_modelos, user_setores = (
        [] for i in range(4)
    )

    fail_state = False
    for item in items:
        user_modelos.append(item["modelo"])
        user_setores.append(item["setor"])
    for modelo in user_modelos:
        if modelo not in templates_pc:
            missing_modelos.append(modelo)
            fail_state = True
    for setor in user_setores:
        if setor not in setores_data:
            missing_setores.append(setor)
            fail_state = True
    return (fail_state, missing_setores, missing_modelos)
