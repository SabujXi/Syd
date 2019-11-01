class SydError(Exception):
    pass


class SynamicSydParseError(SydError):
    """Syd parse error in curlybrace parser."""
