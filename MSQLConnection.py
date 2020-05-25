import MySQLdb



def connection():
    conn = MySQLdb.connect(host='127.0.0.1', user = 'root', passwd='yourpassword',db='YourDB')
    c = conn.cursor()
    return c, conn

if __name__ = '__main__':
    c, conn = connection()
    print('woohoo')
