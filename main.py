# this is where all files will be compiled. Should do the following in order:
# first - using image input, get number from barcode image
# next - match number to corresponding dictionary values; display (product_database.ipynb)
# next - use values to get info about product sustainability and potential allergens (product_info.py, allergen_info.py)
# next - use values to get info about brand sustainability (brand_info.py)
import product_database
import allergen_info
import brand_info
import product_info

def main():
   product_entry = product_database.get_database_entry(577606577902)
   product_brand = product_entry[0]
   product_type = product_entry[1]
   product_materials = product_entry[2]