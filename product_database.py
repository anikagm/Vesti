products = {
    '374440989658': {
        "Brand": "Prada",
        "Product type": "Sunglasses",
        "Materials": {
            "Acetate": 100
        }
    },
    '240335076189': {
        "Brand": "Zara",
        "Product type": "Sweatshirt",
        "Materials": {
            "Cotton": 85,
            "Web cotton": 15
        }
    },
    '588879154298': {
        "Brand": "Levi's",
        "Product type": "Jeans",
        "Materials": {
            "Cotton": 85,
            "Lyocell": 7,
            "Elastomultiester": 6,
            "Elastane": 2
        }
    },
    '111120732189': {
        "Brand": "Forever 21",
        "Product type": "Dress",
        "Materials": {
            "Polyester": 73,
            "Rayon": 26,
            "Nylon": 1
        }
    },
    '577606577902': {
        "Brand": "H&M",
        "Product type": "Scarf",
        "Materials": {
            "Recycled polyester": 100
        }
    }
}
# print(products['374440989658'])
def get_database_entry(barcode_num):
  product_info = products['374440989658'] # hardcoded
  brand = product_info["Brand"]
  type = product_info["Product type"]
  materials = product_info["Materials"]

  return brand, type, materials
