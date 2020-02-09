from random import choices

class DatabaseAPI:
    def __init__(self):
        self._chars = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_")

    def generate_key(self, k=8):
        return "".join(choices(self._chars, k=k))

    def create_url(self, long_url, key_string=None):
        raise NotImplementedError

    def read_url_or_404(self, my_key):
        raise NotImplementedError

    def read_all_urls(self):
        raise NotImplementedError

    def update_url(self, my_key, long_url):
        raise NotImplementedError
        
    def delete_url(self, my_key):
        raise NotImplementedError

    def bulk_generate_keys(self, n=10):
        raise NotImplementedError

    def insert_key(self, new_key):
        raise NotImplementedError

    def consume_key(self):
        raise NotImplementedError