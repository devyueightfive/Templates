class AbstractAPI:
    """ Base Api class.

    """
    public_strategy = None
    authorize_strategy = None

    def __init__(self, version=1):
        self._version = version

    def get_ticker(self, pair):
        self.public_strategy.ticker(pair)

    def get_trades(self, pair):
        self.public_strategy.trades(pair)


class WexApi(AbstractAPI):
    def __init__(self, version=1):
        from .wex_api import Public, PublicV2
        super().__init__(version)
        self.public_strategy = {
            '1': Public(),
            '2': PublicV2()
        }.get(str(version), Public())


class BitfinexApi(AbstractAPI):
    def __init__(self, version=1):
        from .bitfinex_api import Public, PublicV2
        super().__init__(version)
        self.public_strategy = {
            '1': Public(),
            '2': PublicV2()
        }.get(str(version), Public())


class YobitApi(AbstractAPI):
    from .yobit_api import Public
    public_strategy = Public()


supported_api = ['bitfinex.com', 'wex.nz', 'yobit.io']


def get_api(api_name, version=1):
    switcher = {
        'bitfinex.com': BitfinexApi(version),
        'wex.nz': WexApi(version),
        'yobit.io': YobitApi(version)
    }
    return switcher.get(api_name, None), list(switcher.keys())
