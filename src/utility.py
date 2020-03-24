def is_Integer(args):
    if isinstance(args,int):
        return 1
    return 0

def get_keys_list(mapp):
    return list(mapp.keys())

def get_keys_string(mapp,header):
    string = header + "\n"
    keys = list(mapp.keys())
    for i in range(len(keys)):
        string = string + str(i+1) + ". " + keys[i] + "\n"
    return string