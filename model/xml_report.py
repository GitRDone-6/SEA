import os
from xml.etree import ElementTree
from model import run_result



class XMLReport:
    """
    Class that generates XML report
    """

    __report_name: str
    __report_description: str
    __run_results: list[run_result.RunResult]


    def __init__(self):
        pass

    def report_name(self) -> str:
        return self.__report_name

    def report_description(self) -> str:
        return self.__report_description

    def run_results(self) -> list[run_result.RunResult]:
        """
        Knows at least 1 run result from RunResult
        """
        return self.__run_results

    def constuct_format(self, run_results, parent_node=None, parent_name='', run_description):
        """
        Construct in the xml format
        :return:
        """

        def node_for_value(report_name, run_results, parent_node, parent_name):
            """
            Create the sub elements and returns the ordered elements.
            :param report_name:
            :param run_results:
            :param parent_node:
            :param parent_name:
            :return:
            """
            value = os.path.join(parent_name, run_results)
            node = ElementTree.SubElement(parent_node, 'scan')
            child = ElementTree.SubElement(node, 'input')
            child.set('results', run_results)
            child = ElementTree.SubElement(child, 'from')
            child.set('run description', run_description)
            child.text = report_name
            return node

        #Create an element to hold all child elements
        if parent_node is None:
            node = ElementTree.Element('main')
            node.set('tool', 'results')
        else:
            node = ElementTree.SubElement(parent_node, 'main')

        #Add the sub-elements
        for key, value in dict_.iteritems():
            if isinstance(run_results, dict):
                child = node_for_value(key, key, node, parent_name)
                construct_format(run_results, child, key, run_description)
            else:
                node_for_value(key, run_results, node, parent_name)
        return node

    def write_to_file(self):
        """
        write to an xml file
        :return:
        """
        #construct_format(results).tostring()
        pass