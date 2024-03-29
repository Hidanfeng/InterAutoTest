from utils.LogUtil import my_log
import pymysql
#1、创建封装类
class Mysql:
#2、初始化数据，连接数据库，光标对象
    def __init__(self,host,user,password,database,charset="utf8",port=3306):
        self.log = my_log()
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset,
            port=port
            )
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
#3、创建查询、执行方法
    def fetchone(self,sql):
        """
        单个查询
        :param sql:
        :return:
        """
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def fetchall(self,sql):
        """
        多个查询
        :param sql:
        :return:
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def exec(self,sql):
        """
        执行
        :return:
        """
        try:
            if self.conn and self.cursor:
                res = self.cursor.execute(sql)
                self.conn.commit()
        except Exception as ex:
            self.conn.rollback()
            self.log.error("Mysql 执行失败")
            self.log.error(ex)
            return False
        return res

#4、关闭对象
    def __del__(self):
        #关闭光标对象
        if self.cursor is not None:
            self.cursor.close()
        #关闭连接对象
        if self.conn is not None:
            self.cursor.close()

if __name__ == "__main__":
    mysql = Mysql("127.0.0.1",
                  "root",
                  "xdf602525","xustudy",
                  charset="utf8"
                  )

    res = mysql.fetchone("select *from students where sno = 110")
    # res = mysql.exec("INSERT INTO students (`sno`, `sname`, `ssex`, `sbirthday`, `class`, `age`) VALUES ('120', '曾华', '男', '1977-09-01 00:00:00', '95033', 18);")
    print(res)
    sbirthday = res['sbirthday']
    print(type(sbirthday))
    # uu = list(res.keys())
    # print(uu)
    #1、创建db_conf.yml, db1,db2
    #2、编写数据库基本信息
    #3、重构Conf.py
    #4、执行


"""
#1、导入pymysql包
import pymysql
#2、连接database
conn = pymysql.connect(
    host = "211.103.136.242",
    user = "test",
    password = "test123456",
    database = "meiduo",
    charset = "utf8",
    port =7090

)
#3、获取执行sql的光标对象
cursor = conn.cursor()
#4、执行sql
sql = "select username,password from tb_users"
cursor.execute(sql)
res = cursor.fetchone()
print(res)
#5、关闭对象
cursor.close()
conn.close()"""
