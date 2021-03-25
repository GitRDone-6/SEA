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
