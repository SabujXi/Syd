class SydError(Exception):
    pass


class SynamicSydParseError(SydError):
    """Syd parse error in curlybrace parser."""


class SynamicInvalidDateTimeFormat(SydError):
    """When date, time or datetime is invalid"""
