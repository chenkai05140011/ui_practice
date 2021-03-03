import pymysql
def Delete_Org(response_add):
    # 打开数据库链接
    db = pymysql.connect("192.168.1.254", "member_ts", "kyLMBoJ06XXC7k3T", "member_ts")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL语句更新数据
    orgname=response_add[2]
    sql = """delete from member_org where org_name = '%s'""" % (orgname)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        Log.LogOutput(level=LogLevel.INFO, message='删除机构数据成功')
    except Exception as e:
        Log.LogOutput(level=LogLevel.ERROR, message='删除机构数据失败：case%s'%e)
        # 发生错误时回滚
        db.rollback()
    finally:
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()
        return orgname