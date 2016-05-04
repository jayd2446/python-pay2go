python-pay2go
=============

Python API client for Pay2go (智付寶)

Installation
============

.. code-block:: bash

    $ pip install pay2go

Usage
=====

MPG API
=======

.. code-block:: py

    import time

    from pay2go import Pay2GoMPGAPI

    mpg_api = Pay2GoMPGAPI(
        hash_key='YOUR_PAY2GO_HASH_KEY',
        hash_iv='YOUR_PAY2GO_HASH_IV',
        environment='sandbox',  # or 'production'
    )

    data = {
        'RespondType': 'JSON',
        'TimeStamp': time.time(),
        'Version': '1.2',
        'LangType': 'zh-tw',
        'MerchantID': 'SOME VALUE',
        'MerchantOrderNo': 'SOME VALUE',
        'Amt': 'SOME VALUE',
        'ItemDesc': 'SOME VALUE',
        'ReturnURL': 'SOME VALUE',
        'Email': 'SOME VALUE',
        'EmailModify': 1,
        'LoginType': 0,
        'CREDIT': 1,
    }

    payment = mpg_api.create_payment(data)

.. code-block:: html

    <form method="post" action="{{ payment.form_action }}">
        {% for key, value in payment.form_data.items %}
        <input type="hidden" name="{{ key }}" value="{{ value }}" />
        {% endfor %}
        <button type="submit">Submit</button>
    </form>

金流合作推廣商 API
==============

.. code-block:: py

    from pay2go import Pay2GoPartnerAPI

    post_data = {
        'Version': '1.2',
        'TimeStamp': time.time(),
        'MemberUnified': 'SOME VALUE',
        'MemberName': 'SOME VALUE',
        'MemberPhone': 'SOME VALUE',
        'ManagerName': 'SOME VALUE',
        'ManagerNameE': 'SOME VALUE',
        'LoginAccount': 'SOME VALUE',
        'ManagerMobile': 'SOME VALUE',
        'ManagerEmail': 'SOME VALUE',
        'MerchantID': 'SOME VALUE',
        'MerchantName': 'SOME VALUE',
        'MerchantNameE': 'SOME VALUE',
        'MerchantWebURL': 'SOME VALUE',
        'MerchantAddrCity': 'SOME VALUE',
        'MerchantAddrArea': 'SOME VALUE',
        'MerchantAddrCode': 'SOME VALUE',
        'MerchantAddr': 'SOME VALUE',
        'NationalE': 'SOME VALUE',
        'CityE': 'SOME VALUE',
        'MerchantType': 'SOME VALUE',
        'BusinessType': 'SOME VALUE',
        'MerchantDesc': 'SOME VALUE',
        'BankCode': 'SOME VALUE',
        'SubBankCode': 'SOME VALUE',
        'BankAccount': 'SOME VALUE',
        'PaymentType': 'SOME VALUE',
        'AgreedFee': 'SOME VALUE',
    }

    partner_api = Pay2GoPartnerAPI(
        hash_key='YOUR_PAY2GO_HASH_KEY',
        hash_iv='YOUR_PAY2GO_HASH_IV',
        environment='sandbox',  # or 'production'
    )

    response_data = partner_api.add_merchant('YOUR_PAY2GO_PARTNER_ID', post_data)

    if response_data['status'] == 'SUCCESS':
        result = response_data['result']
        print(result['MerchantHashKey'])
        print(result['MerchantIvKey'])
    else:
        print('ERROR')
