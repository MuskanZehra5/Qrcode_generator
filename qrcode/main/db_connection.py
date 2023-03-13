import pymongo


def db_create():
    my_client = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = my_client["QR_CODE_Information"]
    my_data_table = mydb["information"]
    return my_data_table, mydb
