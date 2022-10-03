import webbrowser
import csv

# Todo: think of how to clean code
# Todo: think of how to simplify application (one click)

def main():
    # Load universal parameters
    prefix = "https://www.ebay-kleinanzeigen.de"
    postal_code = "s-21337"
    price_min = "0"
    # price_max = "50"
    # object = "schreibtischstuhl"
    region_key = "k0l3262r" #This weird key depends on the region.
    # radius = "5"

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
            price_max = item[2]

            # Set up and open parametrized object link
            link = (prefix + "/" + postal_code + "/" + "preis:" + price_min + ":" +
                    price_max + "/" + object + "/" + region_key + radius)

            webbrowser.open(link)

if __name__ == "__main__":
    main()