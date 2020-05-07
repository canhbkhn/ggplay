import psycopg2
try:
    connection = psycopg2.connect(user = "postgres", # thang nay khi cai postgres se co ten mac dinh ntn
                                  password = "Canh1234", # dat luc cai postgres
                                  host = "127.0.0.1", # local host
                                  port = "5432", # config khi cai postgres
                                  database = "gplay")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    #print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    #cursor.execute("SELECT version();")
    #record = cursor.fetchone()
    #print("You are connected to - ", record,"\n")
    
    # add to db
    cursor.execute("INSERT INTO apps(app_id, item_name, updated, author, filesize, downloads, version, compatibility, content_rating, author_link, genre, price, rating_value, review_number, description, iap, developer_badge, physical_address, video_url, developer_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", ("1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"))
    connection.commit()
    cursor.close()
    
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")