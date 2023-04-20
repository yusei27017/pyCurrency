import pymongo

# from logWriter import log_write

conn = pymongo.MongoClient("mongodb://192.168.11.140:27017")
db = conn.admin
col = db.pyCurrency


def insert_log(log):
    # for log in log_array:
    res = col.insert_one(log)


def find_log_by_link(link):
    results = col.find({'link': link})
    if any(results):
        # results is list, need use attr
        return False
    else:
        # print(results)
        # 找不到結果網頁已更新，插入新資料並且通知
        return True


if __name__ == "__main__":
    # insert_log([{"test":"test"}])
    bool_res = find_log_by_link('/activity/detail/22_tvl')
    print(bool_res)
