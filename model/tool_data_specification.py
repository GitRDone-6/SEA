class ToolDataSpecification:
    """
    Responsible for tracking the different tags wanted to be tracked from the xml output of the tool

    ***There are several problems. If the tag gives everything inside of its element; what happens if we are given
    a tag that belongs to another tag below it?
    TODO we need to find this implementation. Get the answers from the stakeholders.
    """
    __list_of_tags: list[str]

    def __init__(self):
        self.__list_of_tags = []
        pass

    def insert_specifications(self, specifications:str):
        """
        Insert into our list the tags we want to track from the output of the tool.
        :param specifications:
        :return:
        """

        self.__list_of_tags.append(specifications)

