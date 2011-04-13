

def truthiness(value):
    if hasattr(value, 'lower'):
        if value.lower() == 'true':
            return True
        elif value.lower() == 'false':
            return False
        else:
            raise StandardError('Bad Input: -->%s<--' % value)
    else:
        return bool(value)

