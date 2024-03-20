import pandas as pd

class Csv:
    def Open_csv(self, csv_file: str) -> list:
        '''
        This function accept the csv file name as input.

        csv_file >>> csv file name

        The output will be a list of a dictionary
        '''

        df = pd.read_csv(csv_file)
        
        try:
            df = df.drop(columns=df.columns[df.columns.str.contains('Unnamed', case=False)])
        except AttributeError:
            pass

        df = df.to_dict()
        csv_listed = df

        return csv_listed

    def analysing_datas(self, csv_listed : list) -> list:

        """
        This function, will transform the list of values in a dict with all datas organized. After this, will save in a list and return as output

        csv_listed >>> list

        output >>> list
    
        """

        quantity_line = list(csv_listed['Time'].keys())

        new_dict = {}
        list_dict = []


        for line in quantity_line:

            new_dict['Time'] = csv_listed['Time'][line]
            new_dict['IP Source'] = csv_listed['IP Source'][line]
            new_dict['Port Source'] = csv_listed['Port Source'][line]
            new_dict['IP Destination'] = csv_listed['IP Destination'][line]
            new_dict['Destination Port'] = csv_listed['Destination Port'][line]
            new_dict['Event Type'] = csv_listed['Event Type'][line]
            new_dict['Severity'] = csv_listed['Severity'][line]
            new_dict['Alert Signature'] = csv_listed['Alert Signature'][line]

            list_dict.append(new_dict)

        return list_dict
