from model import whitelisted_ip, blacklisted_ip


class Target:
    """
    Stores the IPs in context of a Run Configuration
    """

    __whitelist: whitelisted_ip.WhitelistedIP
    __blacklist: blacklisted_ip.BlacklistedIP

    def __init__(self):
        pass

    def whitelist(self) -> whitelisted_ip.WhitelistedIP:
        return self.__whitelist

    def blacklist(self) -> blacklisted_ip.BlacklistedIP:
        return self.__blacklist

    def to_dict(self) -> dict:
        target_object_dictionary: dict = {'whitelist': self.whitelist().to_dict(),
                                          'blacklist': self.blacklist().to_dict()}
        return target_object_dictionary
