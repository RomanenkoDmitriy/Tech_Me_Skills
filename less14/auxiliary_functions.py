
def add_dict(obj):
    dict_room = {}
    for atr, val in obj.__dict__.items():
        dict_room[atr] = val
        if atr == "doors":
            dict_room[atr] = [door.__dict__ for door in val]
        if atr == "previous_room":
            if val is None:
                dict_room[atr] = val
                return
            else:
                dict_room[atr] = add_dict(val)
    return dict_room

