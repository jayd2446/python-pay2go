# coding: utf-8

from collections import OrderedDict
import hashlib

from .compat import urlencode


class Pay2GoMPGAPI(object):

    def __init__(self, hash_key, hash_iv, environment, *args, **kwargs):
        self.hash_key = hash_key
        self.hash_iv = hash_iv
        self.environment = environment

        self.base_urls = {
            'sandbox': 'https://capi.pay2go.com',
            'production': 'https://api.pay2go.com',
        }
        self.endpoints = {
            'mpg_gateway': '/MPG/mpg_gateway',
        }
        self.required_fields = (
            'Amt',
            'MerchantID',
            'MerchantOrderNo',
            'TimeStamp',
            'Version',
        )

    @property
    def base_url(self):
        return self.base_urls[self.environment]

    def build_url(self, endpoint):
        return '{0}{1}'.format(self.base_url, endpoint)

    def build_form_data(self, data):
        def generate_check_value(data):
            ordered_dict = OrderedDict()

            ordered_dict['HashKey'] = self.hash_key
            for field_name in self.required_fields:
                ordered_dict[field_name] = data[field_name]
            ordered_dict['HashIV'] = self.hash_iv

            check_value = hashlib.sha256(urlencode(ordered_dict).encode('utf-8')).hexdigest().upper()

            return check_value

        form_data = dict(data)
        form_data['CheckValue'] = generate_check_value(data)

        return form_data

    def create_payment(self, data):
        payment = Payment(
            form_action=self.build_url(self.endpoints['mpg_gateway']),
            form_data=self.build_form_data(data)
        )

        return payment


class Payment(object):

    def __init__(self, form_action, form_data, *args, **kwargs):
        self.form_action = form_action
        self.form_data = form_data
