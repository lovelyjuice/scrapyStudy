import pymysql
from scrapyStudy import settings

connection = pymysql.connect(host=settings.MYSQL_HOST,
                         port=settings.MYSQL_PORT,
                         user=settings.MYSQL_USER,
                         passwd=settings.MYSQL_PASSWORD,
                         db=settings.MYSQL_DB)
cursor=connection.cursor()


class Sql:
    @classmethod
    def inset_novel(cls, name, author, novelUrl, description, lastUpdate, nameId):
        sql = 'insert into novel(name,author,novelUrl,description,lastUpdate,nameId) values(%s,$s,%s,%s,%s,%s) '
        cursor.execute(sql,(name,author,novelUrl,description,lastUpdate,nameId))
        connection.commit()

    @classmethod
    def exist_name_id(cls,name_id):
        sql='select nameId from novel where nameId="%s"'
        cursor.execute(sql,(name_id,))
        return cursor.rowcount>0
