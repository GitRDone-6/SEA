from model.whitelisted_ip import WhitelistedIP
from model.blacklisted_ip import BlacklistedIP
from model.ip_range import IPRange


class Target:
    """
    Stores the IPs in context of a Run Configuration
    """

    __whitelist: WhitelistedIP
    __blacklist: BlacklistedIP

    def __init__(self, dictionary: dict = None):
        if dictionary:
            self.__whitelist = WhitelistedIP(dictionary['whitelist']['ip_range_list'])
            self.__blacklist = BlacklistedIP(dictionary['blacklist']['ip_range_list'])

    def whitelist(self) -> WhitelistedIP:
        return self.__whitelist

    def blacklist(self) -> BlacklistedIP:
        return self.__blacklist

    def to_dict(self) -> dict:
        target_object_dictionary: dict = {'whitelist': self.whitelist().to_dict(),
                                          'blacklist': self.blacklist().to_dict()}
        return target_object_dictionary

    def set_whitelist(self, iprange: IPRange) -> 'Target':
        self.__whitelist = WhitelistedIP(iprange.get_list())
        return self

    def set_blacklist(self, iprange: IPRange) -> 'Target':
        self.__blacklist = BlacklistedIP(iprange.get_list())
        return self
