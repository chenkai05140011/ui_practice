import pymysql

#预发member_ts
dbinfo_member_ts = {"host": "192.168.1.254", "user": "member_ts", "password": "kyLMBoJ06XXC7k3T", "post": "3306"}
#预发supervision
dbinfo_supervision = {"host": "192.168.1.254", "user": "supervision", "password": "9Uy3AF^$mh5MK6*Trdz8", "post": "3306"}
sql = "SELECT * from member_org WHERE org_code='330000000000_11330000MB19032874';"

class DbConnect():
    def __init__(self,db_cof,database="x"):
        self.db_cof = db_cof
        #打开数据连接
        self.db = pymysql.connect(database=database)