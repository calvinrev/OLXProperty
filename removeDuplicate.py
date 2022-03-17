import pymysql
import time
from OLX import settings

conn = pymysql.connect(
    host = settings.MYSQL_HOST,
    db = settings.MYSQL_DBNAME,
    user = settings.MYSQL_USER,
    passwd = settings.MYSQL_PASSWD,
    use_unicode = True
)
cursor = conn.cursor()

# count duplicate
def countDuplicate(date):
    cursor.execute( f'''WITH Tab AS (SELECT property_id, COUNT(*) AS JML FROM olxproperty \
                        WHERE crawl_time = '{date}' \
                        GROUP BY property_id \
                        HAVING JML > 1 \
                        ORDER BY JML DESC) \
                        SELECT SUM(JML) FROM Tab;''' 
                  )
    n_dup = cursor.fetchone()[0]
    print(f'{date}: {n_dup} duplicate rows found!')

def main():
    # set last date
    cursor.execute( f'SELECT max(crawl_time) FROM olxproperty' )
    last_date = cursor.fetchone()[0]
    countDuplicate(last_date)

    # remove duplicate
    cursor.execute( f'''DELETE t1 FROM olxproperty t1 \
                        INNER JOIN olxproperty t2 \
                        WHERE \
                            t1.id < t2.id AND \
                            t1.property_id = t2.property_id AND \
                            t1.crawl_time='{last_date}' AND t2.crawl_time='{last_date}';''' 
                )
    conn.commit()
    countDuplicate(last_date)

# Execute main function
if __name__=="__main__":
    start_time = time.time()
    main()
    conn.close()
    print("%s minutes elapsed time" % round((time.time() - start_time)/60, 3))
