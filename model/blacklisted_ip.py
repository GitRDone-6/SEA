from model import ip_range


class BlacklistedIP(ip_range.IPRange):
    """
    A Range of IP's not to be scanned. This IP Range cannot be editted
    """

    def __init__(self, ip_list: list[tuple] or list[str]):
        ip_range.IPRange.__init__(self)
        self._list = ip_list

    '''
    No editing.
    '''
    def insert_range(self, given_lower: str, given_upper: str) -> 'BlacklistedIP':
        return self

    def insert_ip(self, ip: str) -> 'BlacklistedIP':
        return self

    def pop_lowest(self) -> str:
        return ''

    def pop_highest(self) -> str:
        return ''

    def clear_list(self) -> 'BlacklistedIP':
        return self

    def eliminate_ip(self, ip: str) -> bool:
        return False

    def eliminate_range(self, range: 'ip_range.IPRange') -> bool:
        return False