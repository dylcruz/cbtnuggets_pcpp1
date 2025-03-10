import sqlite3

connection = sqlite3.connect('my-first-database.db')
cursor = connection.cursor()

create_table_statement = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);
'''

connection.commit()

# insert_user_statement = '''
# INSERT INTO users (name, email) VALUES ('Bob Smith', 'bsmith@gmail.com')
# '''
# cursor.execute(insert_user_statement)

select_users_statement = '''
SELECT * FROM users
'''
cursor.execute(select_users_statement)
# connection.commit()

for user in cursor:
    print(user)

# id_to_delete = input('Please enter the id of the user you would like to delete: ')
# delete_user_statement = f'''
# DELETE FROM users WHERE id = ?
# '''
# cursor.execute(delete_user_statement, (id_to_delete,))
# connection.commit()

# print('Here are the updated users after the delete statement: ')
# cursor.execute(select_users_statement)

id_to_update = input('Please enter the id of the user you would like to update: ')
new_email = input('Please enter a new email for the user: ')
new_name = input('Please enter a new name for the user: ')
update_user_statement = f'''
UPDATE users SET email = ?, name = ? WHERE id = ?
'''
cursor.execute(update_user_statement, (new_email, new_name, id_to_update))
connection.commit()

print('Here are the updated users after the update statement: ')
cursor.execute(select_users_statement)

for user in cursor:
    print(user)

connection.close()