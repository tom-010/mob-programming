def parse_ini_string(ini_string):
    if not is_valid_ini(ini_string):
        return {}
    result = {None: {}}
    lines = filter(is_valid_line, map(str.strip, ini_string.split("\n")))

    for line in lines:
        if is_valid_section_header(line) :
            return {}
        key, value = line.split('=', 1)
        result[None][key.strip()] = value.strip()
    return result if not result == {None: {}} else {} 

def is_valid_line(line):
    return len(line) > 0 and (is_valid_property(line) or is_valid_section_header(line)) 

def is_valid_property(line):
    return line[0] != '=' and '=' in line

def is_valid_ini(ini_string):
    return ini_string

def is_valid_section_header(line):
    return line[0] == "["

# Nächste Schritte:
# Das Problem ist, dass wir noch keine Abstraktion haben, die Sektionen beschreibt.
# Gewollt ist, dass, sobald ein invalid Sektion-Header gegeben ist, die komplette Sektion gedroppt wird.
# Idee als wir aufgehört haben: Einen Regex auf dem ini_string Sektionen erkennen lassen, diesen string mit dem
# Regex splitten, überprüfen, ob er (einzige) Key in der Sektion valid ist. 
# Falls nein: Ein continue in der for-loop
# Falls ja: Wie oben die einzelnen lines verarbeiten
# Achtung: TDD in kleinen Schritten!
# www.regex101.com
