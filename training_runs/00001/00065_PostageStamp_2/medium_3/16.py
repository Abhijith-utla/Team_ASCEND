def sat(stamps: List[int], target=3, max_stamps=3, options=[18, 1, 43, 81]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# Adding stamps to the list
def sol(stamps=[]):
    return stamps

# Adding more stamps to the list
def sol(stamps=[], extra_stamps=[]):
    return stamps + extra_stamps

# Removing stamp from the list
def sol(stamps=[], remove_stamp=None):
    if remove_stamp in stamps:
        stamps.remove(remove_stamp)
    return stamps

# Changing the target
def sol(stamps=[], target=None):
    if target is not None:
        return target
    else:
        return 3

# Changing the maximum number of stamps
def sol(stamps=[], max_stamps=None):
    if max_stamps is not None:
        return max_stamps
    else:
        return 3

# Changing the options
def sol(stamps=[], options=None):
    if options is not None:
        return options
    else:
        return [

if __name__ == "__main__":
    assert sat(sol())
