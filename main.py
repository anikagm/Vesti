# this is where all files will be compiled. Should do the following in order:
# first - using image input, get number from barcode image
# next - match number to corresponding dictionary values; display (product_database.ipynb)
# next - use values to get info about product sustainability and potential allergens (product_info.py, allergen_info.py)
# next - use values to get info about brand sustainability (brand_info.py)
import image_analysis
import product_database
import allergen_info
import brand_info
import product_info

def get_id_number():
    id_number = image_analysis.analyze_image("barcode.jpg")
    product_detail_list = product_database.get_database_entry(id_number)
    brand = product_detail_list[0]
    product_type = product_detail_list[1]
    material_content = product_detail_list[2]
    print(brand, product_type, material_content)

    return brand, product_type, material_content

def main():
    brand, product_type, material_content = get_id_number()
    product_info.get_product_info(brand, product_type, material_content)
    allergen_info.allergen_details(product_type, material_content)
    brand_info.get_brand_info(brand)

if __name__ == "__main__":
    main()