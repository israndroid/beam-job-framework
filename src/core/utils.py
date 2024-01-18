import src.core.boolean_logic as LG


def print_info(obj, message:str=''):
    if LG.is_not_none(obj) and LG.is_not_empty(obj):
        print(f'####### {message}  #######')
    print(f'type(obj): {type(obj)}')
    print(f'obj: {obj}')
    return obj