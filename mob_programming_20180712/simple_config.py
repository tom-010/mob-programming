def parse_ini_string(ini_string):
    if not ini_string:
        return {}
    if "=" not in ini_string:
        return{}
    result = {None: {}}
    for line in ini_string.split("\n"):
        if '=' not in line:
            continue

        key, value = line.split('=', 1)
        result[None][key.lstrip()] = value
    return result
