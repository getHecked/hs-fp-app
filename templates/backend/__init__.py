def process_user_query(query_string):
    return [f"Hi {name}!\n" for name in query_string.split(' ') if name[0].isupper()==True]
