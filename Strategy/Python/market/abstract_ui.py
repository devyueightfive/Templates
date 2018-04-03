from market.api import api

if __name__ == "__main__":
    my_pair = 'eth_usd'
    markets = ['bitfinex.com', 'yobit.io', 'wex.nz', 'yobit.com']
    steps = 4
    for i in range(steps):
        try:
            m_number = int(input(f"\n Step {i+1}({steps}) :Please provide number (0-{len(markets)-1}): "))
        except ValueError as e:
            print(f"Error {e.__str__()}")
            continue
        if m_number >= len(markets) or m_number < 0:
            print("Number is outrange.")
            continue
        selected_api, api_keys = api.get_api(markets[m_number])
        if selected_api:
            print(f'{markets[m_number]} :')
            selected_api.get_ticker(my_pair)
            selected_api.get_trades(my_pair)
        else:
            print(f"No Api for {markets[m_number]}")
            print(f"Supported api : {api_keys}")
