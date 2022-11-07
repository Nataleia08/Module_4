def is_valid_pin_codes(pin_codes):
    l_pins = len(pin_codes)
    if l_pins == 0:
        return False
    else:
        list_codes = set(pin_codes)
        l_s = len(list_codes)
        if l_s != l_pins:
            return False
        else:
            for i in pin_codes:
                l_item = len(i)
                if l_item != 4:
                    return False
                else:
                    try:
                        k = int(i)
                    except ValueError:
                        return False
            return True


is_valid_pin_codes(['1101', '9034', '0011'])
