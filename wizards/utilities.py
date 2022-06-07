# addition

def parse_db_url(url):

    chunks = url.split("//")[1].split(":")

    return {
        "username": chunks[0],
        "password": chunks[1].split("@")[0],
        "host": chunks[1].split("@")[1],
        "port": chunks[2].split("/")[0],
        "name": chunks[2].split("/")[1]
    }