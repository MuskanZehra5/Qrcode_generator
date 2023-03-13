import db
import qrcode
import random
import string


def alphanum():
    x = ''.join(random.choices(string.digits + string.ascii_letters + string.digits, k=16))
    return x


def get_unique_id_data_from_db():
    unique_ids = db.get_unique_id()
    return unique_ids


def generate_qrcode(unique_id, user, amount):
    # unique id generated
    # unique_id = alphanum()

    qr = qrcode.QRCode(
        version=4,
        box_size=9,
        border=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
    )

    # data to be stored in qrcode
    code_data = unique_id + "\n" + str(user) + "\nYou received amount Rs." + str(amount)

    qr.add_data(code_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="white", back_color="black")
    img.save(str(user) + ".png")


if __name__ == '__main__':

    num = 0
    db.delete_all()
    print('Enter the number of times you want to generate code')
    num = int(input())

    print('Enter the amount')
    amount_ = input()
    count = db.count_data()
    for i in range(num):
        db.insert_data("You received amount Rs." + str(amount_))

    unique_id = get_unique_id_data_from_db()

    if len(unique_id) == 0:
        print("db is empty")

    else:
        for i in range(count, num + count):
            generate_qrcode(unique_id[i], count + 1, amount_)
            count += 1

    db.show_all_data()
