from db.db_config import mydict as md

def get_cnd_comparators():
    md.execute("SELECT comparator FROM cnd_comparators")
    db_comparators = md.fetchall()
    list_comparators = [i[0] for i in db_comparators]
    md.execute("SELECT comparator_index FROM cnd_comparators")
    db_index = md.fetchall()
    list_index = [i[0] for i in db_index]
    list = dict(zip(list_comparators,list_index))
    # md.close()
    return list

def get_ctb_comparators():
    md.execute("SELECT comparator FROM ctb_comparators")
    db_comparators = md.fetchall()
    list_comparators = [i[0] for i in db_comparators]
    md.execute("SELECT comparator_index FROM ctb_comparators")
    db_index = md.fetchall()
    list_index = [i[0] for i in db_index]
    list = dict(zip(list_comparators,list_index))
    # md.close()
    return list

def get_dpp_comparators():
    md.execute("SELECT comparator FROM dpp_comparators")
    db_comparators = md.fetchall()
    list_comparators = [i[0] for i in db_comparators]
    md.execute("SELECT comparator_index FROM dpp_comparators")
    db_index = md.fetchall()
    list_index = [i[0] for i in db_index]
    list = dict(zip(list_comparators,list_index))
    # md.close()
    return list

def get_fsc_comparators():
    md.execute("SELECT comparator FROM fsc_comparators")
    db_comparators = md.fetchall()
    list_comparators = [i[0] for i in db_comparators]
    md.execute("SELECT comparator_index FROM fsc_comparators")
    db_index = md.fetchall()
    list_index = [i[0] for i in db_index]
    list = dict(zip(list_comparators,list_index))
    # md.close()
    return list

def get_leg_comparators():
    md.execute("SELECT comparator FROM leg_comparators")
    db_comparators = md.fetchall()
    list_comparators = [i[0] for i in db_comparators]
    md.execute("SELECT comparator_index FROM leg_comparators")
    db_index = md.fetchall()
    list_index = [i[0] for i in db_index]
    list = dict(zip(list_comparators,list_index))
    # md.close()
    return list

def get_ots_comparators():
    md.execute("SELECT comparator FROM ots_comparators")
    db_comparators = md.fetchall()
    list_comparators = [i[0] for i in db_comparators]
    md.execute("SELECT comparator_index FROM ots_comparators")
    db_index = md.fetchall()
    list_index = [i[0] for i in db_index]
    list = dict(zip(list_comparators,list_index))
    # md.close()
    return list