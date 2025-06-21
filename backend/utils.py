def get_user(id, connection):
    """Retrieve information for a precise user about their use of the canipark.
    
    Args:
        id: int - The id of the user to fetch information about.
        connection: SQL connection - The sql connection where to retrieve the information from.
        
    Returns:
        tuple - All the information that are available about the use of the canipark by the user.
    """
    with connection:
        with connection.cursor() as cursor:
            sql = """
                SELECT id, nb_attemps, nb_obtained 
                FROM Users
                WHERE id=%s
                """
            user_info = cursor.execute(sql, id)
    return user_info
    