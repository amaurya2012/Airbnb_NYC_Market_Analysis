import sqlite3

conn = sqlite3.connect("airbnb.db")
cursor = conn.cursor()

queries = {
    "Listings by Borough": """
        SELECT neighbourhood_group, COUNT(*) AS listings
        FROM airbnb
        GROUP BY neighbourhood_group
        ORDER BY listings DESC;
    """,

    "Average Price by Borough": """
        SELECT neighbourhood_group, ROUND(AVG(price), 2) AS avg_price
        FROM airbnb
        GROUP BY neighbourhood_group
        ORDER BY avg_price DESC;
    """,

    "Listings by Room Type": """
        SELECT room_type, COUNT(*) AS listings
        FROM airbnb
        GROUP BY room_type
        ORDER BY listings DESC;
    """,

    "Average Price by Room Type": """
        SELECT room_type, ROUND(AVG(price), 2) AS avg_price, COUNT(*) AS listings
        FROM airbnb
        GROUP BY room_type
        ORDER BY avg_price DESC;
    """,

    "Top 10 Neighbourhoods": """
        SELECT neighbourhood, COUNT(*) AS listings
        FROM airbnb
        GROUP BY neighbourhood
        ORDER BY listings DESC
        LIMIT 10;
    """
}

for title, query in queries.items():
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

conn.close()