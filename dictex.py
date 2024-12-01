
m_keys = []  # str
m_values = []  # str

def keys() -> list[str]:
    return m_keys



def values() -> list[str]:
    return m_values

def items() -> list[tuple[str, str]]:
    return list(zip(m_keys, m_values))

# difficult
def update(dict1: dict[str, str]) -> None:
    pass

def pop(key: str) -> str:
    pass

def get(key: str, msg: str = None) -> str:
    pass

def clear() -> None:
    pass

# add if not exist, if exist do nothing
def setdefault(key: str, value: str) -> None:
    pass

#update({'name': 'sharon'})
setdefault('name', 'sharon')
setdefault('city', 'Tel aviv')
setdefault('city', 'Tel aviv')
print(items())  # [('name', 'sharon'), ('city', 'Tel aviv')]
print(get('name', 'not exist'))  # sharon
print(get('age', 'not exist'))  # not exist
print(keys())  # ['name', 'city']
print(values())  # ['sharon', 'tel Aviv']
print(pop('name'))  # sharon
print(items()) # [('city', 'Tel aviv')]
clear()
print(items())  # []

