
import pandas as pd
import numpy as np

def generate_csv():
    # from https://www.isover.fr/produits/catalogue?f[0]=field_product_er_product_type%3A1241&sorting_product=Popularity
    unique_product_name = ["Isoconfort 35", "Comblissimo", "Isoconfort 35 Revetu Kraft"]

    unique_date = pd.date_range("06-01-2019", "06-10-2019")
    date_count = len(unique_date)

    product_ids = []
    product_names = []
    dates = []
    inventory_levels = []
    for product_id, product_name in enumerate(unique_product_name):
        start_inventory_level = np.random.randint(5,80)
        end_inventory_level = np.random.randint(5,80)
        product_inventory_levels = np.linspace(start_inventory_level, end_inventory_level, date_count, dtype=int)
        noise = np.random.randint(-3,3, date_count)
        product_inventory_levels += noise
        product_ids.append([product_id] * date_count)
        product_names.append([product_name] * date_count)
        dates.append(unique_date)
        inventory_levels.append(product_inventory_levels)

    df = pd.DataFrame({
        "product_id":np.concatenate(product_ids),
        "product_name":np.concatenate(product_names),
        "dates":np.concatenate(dates),
        "inventory_level":np.concatenate(inventory_levels)
    })

    df.to_csv("products.csv")

if __name__ == '__main__':
    generate_csv()

