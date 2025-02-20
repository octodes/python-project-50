DEFAULT_INDENT = 4


def to_str(value, depth):
    if isinstance(value, dict):
        lines = ['{']
        for key, nested_value in value.items():
            if isinstance(nested_value, dict):
                new_value = to_str(nested_value, depth + DEFAULT_INDENT)
                lines.append(f"{' ' * depth}    {key}: {new_value}")
            else:
                lines.append(f"{' ' * depth}    {key}: {nested_value}")
        lines.append(f'{" " * depth}}}')
        return '\n'.join(lines)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value


def line_forming(dictionary, key, depth, sign):
    if to_str(dictionary[key], depth + DEFAULT_INDENT) == '':
        return f'{" " * depth}{sign}{dictionary["key"]}:'
    return f'{" " * depth}{sign}{dictionary["key"]}: ' \
           f'{to_str(dictionary[key], depth + DEFAULT_INDENT)}'


def build_stylish_iter(diff, depth=0):
    lines = ['{']
    for dictionary in diff:
        if dictionary['status'] == 'unchanged':
            lines.append(line_forming(
                dictionary, 'value',
                depth, sign='    '
            ))

        if dictionary['status'] == 'added':
            lines.append(line_forming(
                dictionary, 'value',
                depth, sign='  + '
            ))

        if dictionary['status'] == 'removed':
            lines.append(line_forming(
                dictionary, 'value',
                depth, sign='  - '
            ))

        if dictionary['status'] == 'changed':
            lines.append(
                line_forming(
                    dictionary, 'old_value',
                    depth, sign='  - '
                ))
            lines.append(
                line_forming(
                    dictionary, 'new_value',
                    depth, sign='  + '
                ))

        if dictionary['status'] == 'nested':
            new_value = build_stylish_iter(dictionary['value'],
                                           depth + DEFAULT_INDENT)
            lines.append(
                f'{" " * depth}    {dictionary["key"]}: {new_value}')
    lines.append(f'{" " * depth}}}')
    return '\n'.join(lines)


def stylish(diff):
    return build_stylish_iter(diff)