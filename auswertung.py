import pandas as pd


def show_data():
    """
    Returns the DataFrame form the csv file without manipulation
    :returns data: DataFrame form csv file
    """

    data = pd.read_csv("Funds_sheet_Data.csv")
    return data


def search_countries(country):
    """
    Returns a list of all companies located in the given country
    :param country: String with given country
    :return: list of all companies located in the given country
    """
    results = []
    data = show_data()
    for index in range(0, len(data['HQ'])):
        if country in data['HQ'][index]:
            titles = ["Name", "website", "Est. Date", "HQ", "Funds(total)", "Last Funding Type", "CB Rank",
                      "#employees"]
            row = ''
            for title in titles:
                if title == '#employees':
                    row = str(row) + str(data[title][index])
                else:
                    row = str(row) + str(data[title][index]) + "   -   "
            results.append(row)
    return results


def sort_by_funds():
    """
    Returns a list of all companies sorted descending by funds
    :return: list of all companies sorted descending by funds
    """
    data = show_data()
    data = data.sort_values(by='Funds(total)', ascending=False)
    data = data.reset_index(drop=True)
    results = []
    for index in range(0, len(data['Funds(total)'])):
        titles = ["Name", "website", "Est. Date", "HQ", "Funds(total)", "Last Funding Type", "CB Rank",
                  "#employees"]
        row = ''
        for title in titles:
            if title == '#employees':
                row = str(row) + str(data[title][index])
            else:
                row = str(row) + str(data[title][index]) + "   -   "
        results.append(row)
    return results


def sort_by_name():
    """
    Returns a list of all companies sorted by name
    :return: list of all companies sorted by name
    """
    data = show_data()
    data_sorted = data.sort_values(by='Name')
    data_sorted = data_sorted.reset_index(drop=True)
    ergebnis = []
    for index in range(0, len(data_sorted['Name'])):
        titles = ["Name", "website", "Est. Date", "HQ", "Funds(total)", "Last Funding Type", "CB Rank",
                  "#employees"]
        row = ''
        for title in titles:
            if title == '#employees':
                row = str(row) + str(data_sorted[title][index])
            else:
                row = str(row) + str(data_sorted[title][index]) + "   -   "
        ergebnis.append(row)
    return ergebnis





