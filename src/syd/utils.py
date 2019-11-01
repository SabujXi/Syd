def get_source_snippet_from_text(text, line_no, limit=10):
    """Line no starts at 1 not at 0"""
    source = text
    lines = source.splitlines()

    half_limit = limit//2
    half_limit_l = half_limit
    if line_no > half_limit:
        half_limit_l = line_no - half_limit
    else:
        half_limit_l = 1
    res = []
    res.extend(
        ['.... ' + line for line in lines[half_limit_l - 1:line_no - 1]]
    )

    error_line = lines[line_no - 1]
    res.append('->.. ' + error_line)

    res.extend(
        ['.... ' + line for line in lines[line_no:line_no + half_limit]]
    )
    return '\n'.join(res)
