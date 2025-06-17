import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    try:
        arr = np.array(list).reshape(3, 3)
    except ValueError:
        raise ValueError("List must contain only numbers.")
    
    calculations = {
        "mean": [],
        "variance": [],
        "standard deviation": [],
        "min": [],
        "max": [],
        "sum": [],
    }
    
    calculations['mean'].append(np.mean(arr, axis=0).tolist())
    calculations['variance'].append(np.var(arr, axis=0).tolist())
    calculations['standard deviation'].append(np.std(arr, axis=0).tolist())
    calculations['min'].append(np.min(arr, axis=0).tolist())
    calculations['max'].append(np.max(arr, axis=0).tolist())
    calculations['sum'].append(np.sum(arr, axis=0).tolist())

    calculations['mean'].append(np.mean(arr, axis=1).tolist())
    calculations['variance'].append(np.var(arr, axis=1).tolist())
    calculations['standard deviation'].append(np.std(arr, axis=1).tolist())
    calculations['min'].append(np.min(arr, axis=1).tolist())
    calculations['max'].append(np.max(arr, axis=1).tolist())
    calculations['sum'].append(np.sum(arr, axis=1).tolist())

    calculations['mean'].append(np.mean(arr).item())
    calculations['variance'].append(np.var(arr).item())
    calculations['standard deviation'].append(np.std(arr).item())
    calculations['min'].append(np.min(arr).item())
    calculations['max'].append(np.max(arr).item())
    calculations['sum'].append(np.sum(arr).item())

    return calculations