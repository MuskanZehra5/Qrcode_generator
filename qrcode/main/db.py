import db_connection


def insert_data(message):
    my_dict = {"message": message}
    x = my_db_table.insert_one(my_dict)


def delete_all():
    my_db_table.delete_many({})


def get_unique_id():
    id_list = []
    for item in my_db_table.find():
        id_list.append(str(item.get('_id')))
    return str(id_list)


def show_all_data():
    for i in my_db_table.find():
        print(i)


def count_data():
    return my_db_table.estimated_document_count()


my_db_table, mydb = db_connection.db_create()
