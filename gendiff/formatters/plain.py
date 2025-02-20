def to_str(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return f"'{value}'"

def build_plain_iter(diff, path=""):
    lines = []
    for dictionary in diff:
        property = f"{path}{dictionary['key']}"

        if dictionary['status'] == 'added':
            lines.append(f"Property '{property}' "\
                         f"was added with value: "\
                         f"{to_str(dictionary['value'])}")

        if dictionary['status'] == 'removed':
            lines.append(f"Property '{property}' was removed")

        if dictionary['status'] == 'nested':
            new_value = build_plain_iter(dictionary['value'], f"{property}.")
            lines.append(f"{new_value}")

        if dictionary['status'] == 'changed':
            lines.append(f"Property '{property}' was updated. "\
                         f"From {to_str(dictionary['old_value'])} to "\
                         f"{to_str(dictionary['new_value'])}")
    return '\n'.join(lines)

def plain(diff):
    return build_plain_iter(diff)