def is_none(value) -> bool:
    if value is None:
        return True
    else:
        return False


def is_not_none(value) -> bool:
    return not is_none(value)


def is_empty(value) -> bool:
    if is_none(value):
        return False
    elif type(value) is str:
        return True if value.strip() == '' else False
    elif type(value) is list:
        return True if len(value) == 0 else False
    else:
        return False


def is_not_empty(value) -> bool:
    return not is_empty(value)

