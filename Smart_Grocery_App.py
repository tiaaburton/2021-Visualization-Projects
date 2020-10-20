try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# V1 Takes local receipt image
# V2 coming soon. Will be able to take picture of receipt
def grocery_list():
    receipt = Image.open('/Users/tiareina/PycharmProjects/pythonProject/REC_1.jpg')
    groceries_from_receipt = pytesseract.image_to_string(receipt, lang='eng').split("\n")
    # groceries_from_receipt = ["", "", ""]
    items = groceries_from_receipt.copy()[8:12]
    items = [x.split(' ')[:-1] for x in items]
    items = [' '.join(x) for x in items]
    if groceries_from_receipt is None:
        print('There is nothing in your grocery list. Get started now!')
    return print(items)


def add_item():
    new_item = input("Add the name of your new grocery item here.")
    return new_item


grocery_list()
