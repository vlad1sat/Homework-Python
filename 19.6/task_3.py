data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

print("1")
for element_data, information in data.items():
    print(f"{element_data}: {information}")

print("\n2")
data['ETH']['total_diff'] = 100
print(f'ETH: {data["ETH"]}')

print("\n3")
data['tokens'][0]['fst_token_info']['name'] = 'doge'
fst_name = data['tokens'][0]['fst_token_info']['name']
print(f'fst_token_info-name: {fst_name}')

print("\n4")
total_out = 0
for i_value in data.get('tokens'):
    total_out += i_value.pop('total_out')
data['ETH']['total_out'] = total_out
print(data['ETH'])

print("\n5")
old_price = data['tokens'][1]['sec_token_info'].pop('price')
data['tokens'][1]['sec_token_info']['total_price'] = old_price
print(data['tokens'][1]['sec_token_info']['total_price'], end='')
