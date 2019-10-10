class UserManager:
    @staticmethod
    def get_users_list():
        with open('users.list', 'w+') as f:
            return [i.rstrip('\r\n') for i in f.readlines()]

    @staticmethod
    def is_user_in_list(user_id):
        return user_id in UserManager.get_users_list()

    @staticmethod
    def add_user_in_list(user_id):
        with open('users.list', 'a') as f:
            f.write(user_id)

    @staticmethod
    def write_users_list(users_list, mode_destructive=False):
        mode = 'w' if mode_destructive else 'a'
        with open('users.list', mode=mode) as f:
            f.writelines(users_list)

    @staticmethod
    def remove_user_from_list(user_id):
        users = UserManager.get_users_list()
        users.remove(user_id)
        UserManager.write_users_list(users)
