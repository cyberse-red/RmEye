import sql
g_white_list = []
g_white_dll_load_list = [
    'c:\\windows\\system32\\advapi32.dll',
    'c:\\windows\\system32\\crypt32.dll',
    'c:\\windows\\system32\\cryptdll.dll',
    'c:\\windows\\system32\\gdi32.dll',
    'c:\\windows\\system32\\imm32.dll',
    'c:\\windows\\system32\\kernel32.dll',
    'c:\\windows\\system32\\kernelbase.dll',
    'c:\\windows\\system32\\msasn1.dll',
    'c:\\windows\\system32\\msvcrt.dll',
    'c:\\windows\\system32\\ntdll.dll',
    'c:\\windows\\system32\\rpcrt4.dll',
    'c:\\windows\\system32\\rsaenh.dll',
    'c:\\windows\\system32\\samlib.dll',
    'c:\\windows\\system32\\sechost.dll',
    'c:\\windows\\system32\\secur32.dll',
    'c:\\windows\\system32\\shell32.dll',
    'c:\\windows\\system32\\shlwapi.dll',
    'c:\\windows\\system32\\sspicli.dll',
    'c:\\windows\\system32\\user32.dll',
    'c:\\windows\\system32\\vaultcli.dll',
]


def add_white_list(path, hash, reason):
    global g_white_list
    if hash in g_white_list:
        return False
    g_white_list.append(hash)
    sql.push_white_list(path, hash, reason)


def synchronization_white_list():
    sql_data = sql.query_all_white_list()
    for data in sql_data:
        g_white_list.append(data[1])
    print("sync white list success, size: {}".format(len(sql_data)))
