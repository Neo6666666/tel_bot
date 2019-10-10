import logging


class UserManager:
    @staticmethod
    def get_users_list():
        with open('users.list', 'r') as f:
            user_list = f.readlines()
            logging.getLogger().debug(f'Requested user list: {user_list}')
            return user_list

    @staticmethod
    def is_user_in_list(user_id):
        logging.getLogger().debug(f'Is user {user_id} in {UserManager.get_users_list()}')
        return str(user_id) in UserManager.get_users_list()

    @staticmethod
    def add_user_in_list(user_id):
        with open('users.list', 'a') as f:
            logging.getLogger().debug(f'Add new user {user_id}')
            f.write(str(user_id))
            f.flush()

    @staticmethod
    def write_users_list(users_list, mode_destructive=False):
        mode = 'w' if mode_destructive else 'a'
        with open('users.list', mode=mode) as f:
            f.writelines(users_list)
            f.flush()

    @staticmethod
    def remove_user_from_list(user_id):
        users = UserManager.get_users_list()
        logging.getLogger().debug(f'Remove user {user_id} from {users}')
        users.remove(str(user_id))
        UserManager.write_users_list(users)
        logging.getLogger().debug(f'Result of removing is {UserManager.get_users_list()}')
