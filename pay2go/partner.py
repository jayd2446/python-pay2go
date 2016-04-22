# coding: utf-8

import binascii

from Crypto.Cipher import AES
import requests

from .compat import urlencode


class Pay2GoPartnerAPI(object):

    def __init__(self, hash_key, hash_iv, environment, *args, **kwargs):
        self.hash_key = hash_key
        self.hash_iv = hash_iv
        self.environment = environment

        self.base_urls = {
            'sandbox': 'https://cweb.pay2go.com',
            'production': 'https://web.pay2go.com',
        }
        self.endpoints = {
            'add_merchant': '/API/AddMerchant',
        }

    @property
    def base_url(self):
        return self.base_urls[self.environment]

    def build_url(self, endpoint):
        return '{0}{1}'.format(self.base_url, endpoint)

    def make_request(self, method, endpoint, *args, **kwargs):
        url = self.build_url(endpoint)

        session = requests.sessions.Session()
        r = session.request(method=method, url=url, **kwargs)

        if not r.ok:
            # TODO: custom Exception class
            raise RuntimeError('Shit happens')

        response_data = r.json()

        return response_data

    def encrypt(self, post_data):
        def add_padding(string, block_size=32):
            length = len(string)
            pad = block_size - (length % block_size)
            string += chr(pad) * pad

            return string

        cipher = AES.new(key=self.hash_key, mode=AES.MODE_CBC, IV=self.hash_iv)

        post_data = urlencode(post_data)
        post_data = cipher.encrypt(add_padding(post_data))
        post_data = binascii.hexlify(post_data)
        post_data = post_data.strip()

        return post_data

    def add_merchant(self, partner_id, post_data):
        """
        https://cweb.pay2go.com/API/AddMerchant
        """

        real_data = {
            'PartnerID_': partner_id,
            'PostData_': self.encrypt(post_data),
        }
        endpoint = self.endpoints['add_merchant']
        response_data = self.make_request('POST', endpoint, data=real_data)

        return response_data
