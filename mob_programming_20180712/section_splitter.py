def split_sections(ini_string):
    if not "[" in ini_string:
        return [(None, ini_string)]

    if ini_string == "[]":
        return [('', '')]

    sections = []
    for section in ini_string.split('\n['):
        name_content = section.split(']\n', maxsplit=1)
        if len(name_content) == 1:
            name_content.insert(0, None)

        sections.append((name_content[0], name_content[1]))

    if sections and sections[0][0] and sections[0][0].startswith('['):
        sections[0] = (sections[0][0][1:], sections[0][1])
        
    return sections