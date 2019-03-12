# !/usr/bin/python
# -*- coding: utf-8 -*-
import psycopg2


def consulta(sql):
    # Criando a conexão com o banco
    con = psycopg2.connect(database='news', user='vagrant')
    cursor = con.cursor()
    cursor.execute(sql)

    result = cursor.fetchall()
    for item in result:
        print('%s %s' % (item[0], item[1]))
    con.close()


# consulta para recuperar os 3 artigos mais visitados
sql_1 = """ SELECT  articles.title,
                    count(log.path):: INTEGER as views
            FROM  log
            JOIN articles
               ON log.path = CONCAT('/article/', articles.slug)
            WHERE (method ILIKE 'get')
               AND (status ILIKE '%200 ok%')
            GROUP BY articles.title
            ORDER BY views DESC
            LIMIT 3;"""


# consulta para recuperar os autores mais populares
sql_2 = """ SELECT authors.name,
              count(slug):: INTEGER as views
            FROM articles
            JOIN authors
                ON articles.author = authors.id
            INNER JOIN log
                ON articles.slug = substring(log.path, 10)
            WHERE (log.status ILIKE '%200 ok%')
               AND(log.method ILIKE 'get')
            GROUP BY authors.name
            ORDER BY views DESC
            LIMIT 5;"""


# consulta para recuperar os dias com maior porcentagem de erro
sql_3 = """ SELECT  TO_CHAR(time, 'Mon dd, YYYY') AS day,
                    ROUND( 100.0 * (
                     CAST(
                      SUM(
                      CASE WHEN status not ilike '%200 ok%'
                        THEN 1
                        ELSE 0 END) AS decimal)/count(*)),
                    2) AS contagem
                    FROM log
                    GROUP BY day
                    HAVING
                     ROUND(
                      100.0 * (
                       CAST(
                        SUM(
                         CASE WHEN status not ilike '%200 ok%'
                          THEN 1
                          ELSE 0 END) AS decimal) / count(*)),2) >1
                    ORDER BY contagem DESC
                    LIMIT 1;"""


# Execução das consultas
consulta(sql_1)
consulta(sql_2)
consulta(sql_3)
