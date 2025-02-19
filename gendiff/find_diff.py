def find_diff(data1, data2):
    keys = sorted(
        list(set(data1.keys()) | set(data2.keys()))
    )
    diff = []

    for key in keys:
        if key not in data1:
            diff.append(f'+ {key}: {data2[key]}')
        elif key not in data2:
            diff.append(f'- {key}: {data1[key]}')
        elif data1[key] == data2[key]:
            diff.append(f'  {key}: {data1[key]}')
        elif data1[key] != data2[key]:
            diff.append(f'- {key}: {data1[key]}')
            diff.append(f'+ {key}: {data2[key]}')

    return '\n'.join(diff)
