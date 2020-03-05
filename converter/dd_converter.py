def dd_to_ddmm(dd_str):
    mins_per_deg = 60
    dd = int(dd_str)
    mm = (float(dd_str) - float(dd)) * mins_per_deg


    ddmm = str(dd) + '° ' + str(mm) + '\''
    return ddmm


def dd_to_ddmmss(dd_str):
    mins_per_deg = 60
    secs_per_min = 60
    dd = int(dd_str)
    mm = int((float(dd_str) - float(dd)) * mins_per_deg)
    ss = (((float(dd_str) - dd) * mins_per_deg) - mm) * secs_per_min

    ddmmss = str(dd) + '° ' + str(mm) + '\' ' + str(ss) + '\"'
    return ddmmss
