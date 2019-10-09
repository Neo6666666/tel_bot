def is_user_in_list(user_id):
    return user_id in get_users_list()


def get_users_list():
    with open('users.list', 'r') as f:
        return [i.rstrip('\r\n') for i in f.readlines()]


def add_user_in_list(user_id):
    with open('users.list', 'a') as f:
        f.write(user_id)


def write_users_list(users_list, mode_destructive=False):
    mode = 'w' if mode_destructive else 'a'
    with open('users.list', mode=mode) as f:
        f.writelines(users_list)


def remove_user_from_list(user_id):
    users = get_users_list().remove(user_id)
    write_users_list(users)
