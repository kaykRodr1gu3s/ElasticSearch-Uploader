import pandas as pd

class Csv:
    def parsing_csv(self, csv_file: str) -> list:
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

data = Csv()

data.parsing_csv("2022-03-14-Qakbot-with-Cobalt-Strike-and-VNC-module.csv")