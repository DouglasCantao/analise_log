# -*- coding: utf-8 -*-
import psycopg2


def consulta(sql):
    # Criando a conexão com o banco
    con = psycopg2.connect(database='news', user='vagrant')
    cursor = con.cursor()
    cursor.execute(sql)

    result = cursor.fetchall()
    for item in result:
        print(str(item).replace("(", "").replace(")",""))
    con.close()


# consulta para recuperar os 3 artigos mais visitados
sql_1 = " SELECT    a.title,"\
        "           count(l.path):: INTEGER as views"\
        " FROM  log l"\
        " JOIN articles a"\
        "       ON substring(l.path, 10) = a.slug"\
        " WHERE (method ilike 'get')"\
        "       AND (status ilike '%200 ok%')"\
        " GROUP BY a.title"\
        " ORDER BY a.title DESC LIMIT 3;"


# consulta para recuperar os autores mais populares
sql_2 = " SELECT au.name,"\
        "      count(slug):: INTEGER as views"\
        " FROM articles as a"\
        " JOIN authors as au"\
        " ON a.author = au.id"\
        " INNER JOIN log as l"\
        " ON a.slug = substring(l.path, 10)"\
        " WHERE (l.status ilike '%200 ok%')"\
        "       AND(l.method ilike 'get')"\
        " GROUP BY au.name"\
        " ORDER BY Views DESC LIMIT 5;"


# consulta para recuperar os dias com maior porcentagem de erro
sql_3 = " SELECT  to_char(time, 'Mon dd, YYYY') as day,"\
        " ((count(time)) / 100):: numeric(12,1)::text || '%' errors"\
        " FROM log"\
        " WHERE (status not ilike '%200 ok%')"\
        " GROUP BY day"\
        " ORDER BY errors;"

consulta(sql_1)
consulta(sql_2)
consulta(sql_3)