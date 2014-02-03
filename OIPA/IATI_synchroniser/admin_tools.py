from IATI.parser import Parser
from IATI.models import activity

class AdminTools():

    def get_xml_activity_amount(self, url):
        try:
            parser = Parser()
            xml_file = parser.get_the_file(url)
            occurences = 0

            for line in xml_file:

                if "</iati-identifier>" in line:
                    amount = line.count("</iati-identifier>")
                    occurences += amount

            return occurences

        except Exception as e:
            if e.args:
                print(e.args[0])
            print("ERROR IN GET_XML_ACTIVITY_AMOUNT, FILE URL " + url)


    def get_oipa_activity_amount(self, source_ref):
        return activity.objects.filter(xml_source_ref=source_ref).count()