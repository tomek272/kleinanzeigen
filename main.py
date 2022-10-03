import webbrowser
import csv

def main():
    # Load universal parameters
    prefix = "https://www.ebay-kleinanzeigen.de"
    postal_code = "s-21337"
    region_key = "k0l3262r" #This weird key depends on the region.

    # Load objects from list
    file_in = "items.csv"
    with open(file_in) as items_file:
        items_reader = csv.reader(items_file, delimiter=",")
        next(items_reader, None) #Skip initial, i.e. header, line

        # Check every object on Kleinanzeigen
        for item in items_reader:

            # Load object parameters
            object = item[0]
            radius = item[1]
            price_min = item[2]
            price_max = item[3]

            # Todo: override item configuration by argparser

            # Set up and open parametrized object link
            link = (prefix + "/" + postal_code + "/" + "preis:" + price_min + ":" +
                    price_max + "/" + object + "/" + region_key + radius)

            # Todo: do not open all items at once
            webbrowser.open(link)

if __name__ == "__main__":
    main()