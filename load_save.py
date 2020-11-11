
def save_data(data, path, filename):
    """
    a function to save data to a json file
    """
    with open(f"{path}/{filename}.json", 'w') as f:
        # data = str(data)
        f.write(data)


def load_data(path, filename):
    """
    a function grab data from json file,
    returns data in a json type
    """
    with open(f"{path}/{filename}.json", 'r') as f:
        data = f.read()
        return data
