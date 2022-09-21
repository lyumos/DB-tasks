import psycopg2


def create_tables(conn):
    with conn.cursor() as cur:
        cur.execute("""
                CREATE TABLE IF NOT EXISTS clients(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(20) NOT NULL,
                    surname VARCHAR(40) NOT NULL,
                    email VARCHAR(40) UNIQUE NOT NULL
                );
                """)

        cur.execute("""
                CREATE TABLE IF NOT EXISTS phones(
                    id SERIAL PRIMARY KEY,
                    phone VARCHAR(15),
                    client_id INTEGER,
                    FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
                );
                """)
        conn.commit()


def add_client(conn):
    c_name = input('Введите имя клиента: ')
    c_surname = input('Введите фамилию клиента: ')
    c_email = input('Введите email клиента: ')
    c_phones = input('Введите через запятую номера телефонов клиента (можно пропустить): ')
    with conn.cursor() as cur:
        # добавляем данные в clients
        cur.execute(f"""
                        INSERT INTO clients(name,surname,email) 
                        VALUES('{c_name}','{c_surname}','{c_email}');
                        """)
        if c_phones:
            #  добавляем данные о phone (если есть) в phones
            for c_phone in c_phones.split(','):
                # вычленяем id клиента из clients по его email
                cur.execute("""
                               SELECT id FROM clients WHERE email=%s;
                               """, (c_email,))
                c_id = cur.fetchone()[0]
                # добавляем информацию о телефоне
                cur.execute(f"""
                               INSERT INTO phones(phone,client_id) 
                               VALUES('{c_phone}',{c_id});
                               """)
        print('--> Данные успешно добавлены!')
        conn.commit()


def add_phone(conn):
    phone = input('Введите новый номер телефона клиента: ')
    email = input('Введите email клиента: ')
    with conn.cursor() as cur:
        # вычленяем id клиента из clients по его email
        cur.execute("""
                       SELECT id FROM clients WHERE email=%s;
                       """, (email,))
        c_id = cur.fetchone()[0]
        # добавляем информацию о телефоне
        cur.execute(f"""
                       INSERT INTO phones(phone,client_id) 
                       VALUES('{phone}',{c_id});
                       """)
        print('--> Данные о номере телефона успешно добавлены!')
        conn.commit()


def change_info(conn):
    email = input('Введите email клиента: ')
    new_name = input('Введите новое имя клиента: ')
    new_surname = input('Введите новую фамилию клиента: ')
    new_email = input('Введите новый адрес электронной почты клиента: ')
    new_phone = input('Введите новый номер телефона клиента: ')
    with conn.cursor() as cur:
        # вычленяем id клиента из clients по его email
        cur.execute("""
                   SELECT id FROM clients WHERE email=%s;
                   """, (email,))
        c_id = cur.fetchone()[0]
        # изменяем информацию в зависимости от выбранной пользователем опции
        if new_name:
            cur.execute("""
                    UPDATE clients SET name=%s WHERE id=%s;
                    """, (new_name, c_id))
        if new_surname:
            cur.execute("""
                    UPDATE clients SET surname=%s WHERE id=%s;
                    """, (new_surname, c_id))
        if new_email:
            cur.execute("""
                    UPDATE clients SET email=%s WHERE id=%s;
                    """, (new_email, c_id))
        if new_phone:
            cur.execute("""
                    SELECT phone FROM phones WHERE client_id=%s;
                    """, ([c_id]))
            fetch_res = cur.fetchall()
            if len(fetch_res) == 1:
                cur.execute("""
                        UPDATE phones SET phone=%s WHERE client_id=%s;
                        """, (new_phone, c_id))
            # если у клиента имеется несколько телефонов
            if len(fetch_res) > 1:
                print(f'У клиента имеется {len(fetch_res)} телефонов. Выберите, какой именно нужно изменить ->')
                for phone in fetch_res:
                    print(f'{phone[0]}')
                old_phone = input('Введите, какой из номеров клиента нужно изменить: ')
                for phone_ in fetch_res:
                    if phone_[0] == old_phone:
                        # ищем id номера телефона, который нужно изменить
                        cur.execute("""
                               SELECT id FROM phones WHERE phone=%s;
                               """, (old_phone,))
                        phone_id = cur.fetchone()[0]
                        # заменяем старый номер на новый
                        cur.execute("""
                                UPDATE phones SET phone=%s WHERE id=%s;
                                """, (new_phone, phone_id))
        print('--> Данные изменены успешно!')
        conn.commit()


def delete_phone(conn):
    email = input('Введите email клиента: ')
    del_phone = input('Введите номер телефона клиента, который нужно удалить: ')
    with conn.cursor() as cur:
        # вычленяем id клиента из clients по его email
        cur.execute("""
                       SELECT id FROM clients WHERE email=%s;
                       """, (email,))
        c_id = cur.fetchone()[0]
        # вычленяем id номера телефона
        cur.execute("""
                      SELECT id FROM phones WHERE client_id=%s and phone=%s;
                      """, (c_id,del_phone))
        phone_id = cur.fetchone()[0]
        # удаляем номер
        cur.execute("""
                       DELETE FROM phones WHERE id=%s;
                       """, (phone_id,))
        print('--> Номер успешно удален!')
        conn.commit()


def delete_client(conn):
    email = input('Введите email клиента (обязательно): ')
    with conn.cursor() as cur:
        # вычленяем id клиента из clients по его email
        cur.execute("""
                           SELECT id FROM clients WHERE email=%s;
                           """, (email,))
        c_id = cur.fetchone()[0]
        # вычленяем id номеров телефонов
        cur.execute("""
                          SELECT id FROM phones WHERE client_id=%s;
                          """, (c_id,))
        fetch_res = cur.fetchall()
        # удаляем клиента и номера телефонов
        for phone_id in fetch_res:
            cur.execute("""
                           DELETE FROM phones WHERE id=%s;
                           """, (phone_id,))
        cur.execute("""
                           DELETE FROM clients WHERE id=%s;
                           """, (c_id,))
        print('--> Данные успешно удалены!')
        conn.commit()


def find_client(conn):
    # поиск по имени, фамилии или по email, или по телефону
    with conn.cursor() as cur:
        c_name = input('Введите имя клиента (можно пропустить): ')
        c_surname = input('Введите фамилию клиента (можно пропустить): ')
        # из учета того, что клиентов с такими ФИ может быть несколько
        if c_name and c_surname:
                cur.execute("""
                               SELECT * FROM clients WHERE name=%s and surname=%s;
                               """, (c_name,c_surname))

                c_info = cur.fetchall()
                for info in c_info:
                    c_id = info[0]
                    cur.execute("""
                                   SELECT phone FROM phones WHERE client_id=%s;
                                   """, (c_id,))
                    ph_info = cur.fetchall()
                    print(f'\n-- id клиента: {info[0]}\nИмя клиента: {info[1]}\nФамилия клиента: {info[2]}\nEmail клиента: {info[3]}\nТелефон клиента: {ph_info}\n')
        else:
            c_email = input('Введите email клиента (можно пропустить): ')
            if c_email:
                # у каждого клиента уникальный email, но может быть несколько телефонов
                cur.execute("""
                                               SELECT * FROM clients WHERE email=%s;
                                               """, (c_email,))
                c_info = cur.fetchall()
                c_id = c_info[0][0]
                cur.execute("""
                                               SELECT phone FROM phones WHERE client_id=%s;
                                               """, (c_id,))
                ph_info = cur.fetchall()
                print(
                    f'\n-- id клиента: {c_info[0][0]}\nИмя клиента: {c_info[0][1]}\nФамилия клиента: {c_info[0][2]}\nEmail клиента: {c_info[0][3]}\nТелефон клиента: {ph_info}\n')
            else:
                c_phone = input('Введите номер телефона клиента: ')
                #  пусть телефон не уникален и по одному тлф может быть несколько клиентов
                if c_phone:
                    cur.execute("""
                                  SELECT client_id FROM phones WHERE phone=%s;
                                  """, (c_phone,))
                    c_info = cur.fetchall()
                    for info in c_info:
                        c_id = info[0]
                        cur.execute("""
                                       SELECT * FROM clients WHERE id=%s;
                                       """, (c_id,))
                        client_info = cur.fetchall()
                        for client in client_info:
                            cur.execute("""
                                           SELECT phone FROM phones WHERE client_id=%s;
                                           """, (c_id,))
                            ph_info = cur.fetchall()
                            print(f'\n-- id клиента: {client[0]}\nИмя клиента: {client[1]}\nФамилия клиента: {client[2]}\nEmail клиента: {client[3]}\nТелефон клиента: {ph_info}\n')

def actions():
    with psycopg2.connect(database="clients_db", user="postgres", password="66Onipoh") as conn:
        create_tables(conn)
        print('Какое действие хотите выполнить?\n1 Добавить нового клиента\n2 Добавить телефон для клиента\n3 Изменить данные клиента\n4 Удалить телефон клиента\n5 Удалить клиента\n6 Найти клиента по его данным')
        actions = {1:add_client,2:add_phone,3:change_info,4:delete_phone,5:delete_client,6:find_client}
        while True:
            action = int(input('\nВведите номер действия: '))
            if action == 1: actions[1](conn)
            if action == 2: actions[2](conn)
            if action == 3: actions[3](conn)
            if action == 4: actions[4](conn)
            if action == 5: actions[5](conn)
            if action == 6: actions[6](conn)
        conn.close()

if __name__ == '__main__':
    actions()
