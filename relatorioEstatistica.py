#
# To handle CSV report
#

import csv

def openDatabaseConnection():
    global connectionString
    global dbCursor
    connectionString = cx_Oracle.connect('user/senha@ip:1521/schema')
    dbCursor = connectionString.cursor()
    print('Oracle version:' + connectionString.version)

def closeDatabaseConnection():
    print('Close Database Connection')
    connectionString.close()

def createStatisticTable():
    dbCursor.execute('create table tb_est_result_' + str(datetime.date.today().month).zfill(
        2) + ' as select * from tb_est_result_' + str(datetime.date.today().month - 1).zfill(2) + ' where rownum < 1')
    print('MES: ' + str(datetime.date.today().month).zfill(2))
    print('MES: ' + str(datetime.date.today().month-1).zfill(2))

def insertMultiplesContentStatisticTable(size, content):
    print('Size: '+ str(size))
    lista = list(content)
    item = str(lista[0]).encode('utf-8', 'ignore').decode('utf-8').replace('\'','\"')
    print(item)

    # It´s not work yet, that will be investigate
    #dbCursor.bindarraysize = 1
    #dbCursor.setinputsizes(cx_Oracle.STRING, cx_Oracle.STRING, cx_Oracle.STRING, cx_Oracle.STRING, cx_Oracle.STRING, cx_Oracle.STRING
    #                       , cx_Oracle.STRING, cx_Oracle.STRING, cx_Oracle.DATETIME, cx_Oracle.STRING, cx_Oracle.STRING, cx_Oracle.DATETIME)

    for item in content:
        print(item[0])
        print(item[1])
        print(item[2])

        dbCursor.execute('insert into tb_est_result_06(MODULO, DOCUMENTO, NUMERO, POUPATEMPO, ATENDENTE, SERVICO, REUSO, DEDOS, DATA_ENVIO, MOTIVO, OBSERVACAO, DATA_EVENTO) values (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12)')


    dbCursor.commit()
    print('Fim do for')
    # Now query the results back
    #cur2 = con.cursor()
    #cur2.execute('select * from mytab')
    #res = cur2.fetchall()

# def updateContentStatistTable
#     documentoCompleto = str(tuple_content[0][2])
#     print(documentoCompleto)
#     documentoCompleto = documentoCompleto.split('-')
#     documentoPrefixo = documentoCompleto[0]
#     documentoSufixo = documentoCompleto[1]
#     print('documentoPrefixo: ' + documentoPrefixo)
#     print('documentoSufixo: ' + documentoSufixo)

def handlecsvfile(file):
    openDatabaseConnection()
    #first step
    #createStatisticTable()
    #second step



    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';',quotechar=' ')
        tuple_content = tuple(reader)
        print('Size: '+ str(len(tuple_content)))
        insertMultiplesContentStatisticTable(len(tuple_content), tuple_content)

        # print('RG: ' + rg)
        # print('DG RG: ' + dgrg)
        # for row in tuple_content:
        # # RegExp to clear brackets and single quotation marks.
        #     clear_line = re.sub(r'[\'|\[\]]' ,'', str(row))
        #     print(clear_line)
        #     #for field in clear_line.split(','):
        #     #    print('Field: '+ field)


    closeDatabaseConnection()




handlecsvfile("C:\\Estatistica\\2018 - 04\\1_estatistica_EXEC_BPMPPT_20185730_095731.csv")
