import os

import pandas as pd
from connection import close_conn, create_conn
from to_landing import load_table_to_landing
from utils.db import WarehouseConnection, get_warehouse_creds


def main():

    engine = create_conn(
        WarehouseConnection(get_warehouse_creds()).connection_string()
    )
    """ Landing area """
    file_path = "data/restaurant_data.xlsx"
    table_name = os.getenv('TABLE_NAME')

    menu_items = pd.read_excel(file_path, sheet_name='Restaurant Menu Items')
    restaurants = pd.read_excel(file_path, sheet_name='Reference categories')
    # load_table_to_landing(df, engine, table_name, 'landing')

    close_conn(engine)


if __name__ == "__main__":
    main()