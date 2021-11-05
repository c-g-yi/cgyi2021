# encoding:utf-8
'''
rate of search to click
'''
import re

def TDW_PL(tdw, argv):
    today = argv[0]

    sql = '''
    delete from csig_th_medicalbaike_interface::t_uqa_search_stat
    where tdbank_imp_date = '%s' ''' % today
    tdw.execute(sql)

    sql1 = '''
        select value
            ,case when product='health.deluxe' then '健康'
            when product='yidian' and platform='miniprogram' then '小程序'
            when product='yidian' and platform in ('txyd','Android','iOS') then 'app'
            else 'H5' end f_platform
        from csig_th_medicalbaike_interface :: t_medicalbaike_web_report_logs_fdt0 
        WHERE tdbank_imp_date='{0}' and event='yidian.exposure'
            and value like '%searchId%'
            and value like '%cardId%'
            and value like '%answerv2_5647456%'
        GROUP BY value
            ,case when product='health.deluxe' then '健康'
            when product='yidian' and platform='miniprogram' then '小程序'
            when product='yidian' and platform in ('txyd','Android','iOS') then 'app'
            else 'H5' end 
    '''.format(today)
    res1 = tdw.execute(sql1)
    if res1:
        list_data = []
        searchId_all_exp = []
        for data in res1:
            try:
                search_cardId = re.compile(r'''cardId":"(.*?)"''')
                cardId_list = search_cardId.findall(data)

                search_searchId = re.compile(r'''searchId":"(.*?)"''')
                searchId_findall = search_searchId.findall(data)
                f_platform = data.split('\t')[-1].strip()

                list1 = []
                if 'answerv2_5647456' in cardId_list and f_platform:
                    searchId_str = ''''''
                    count = 0
                    for s in searchId_findall:
                        if s not in searchId_str:
                            if s not in searchId_all_exp:
                                searchId_all_exp.append(s)
                            count += 1
                            searchId_str += s + ','
                    if searchId_str != '''''':
                        list1.append(searchId_str)
                        list1.append(f_platform)
                        list1.append(count)
                        list_data.append(list1)
            except:
                tdw.WriteLog('searchId or query not exist')

        jian_num1, xiao_num1, app_num1, H5_num1 = 0, 0, 0, 0
        for data in list_data:
            f_platform = data[1]
            c = data[-1]
            if f_platform == '健康':
                jian_num1 += c
            if f_platform == '小程序':
                xiao_num1 += c
            if f_platform == 'app':
                app_num1 += c
            if f_platform == 'H5':
                H5_num1 += c
        list_count1 = []
        list_count1.append(jian_num1)
        list_count1.append(xiao_num1)
        list_count1.append(app_num1)
        list_count1.append(H5_num1)
    else:
        list_count1 = [0, 0, 0, 0]

    sql2 = '''
        select value 
            ,case when product='health.deluxe' then '健康'
            when product='yidian' and platform='miniprogram' then '小程序'
            when product='yidian' and platform in ('txyd','Android','iOS') then 'app'
            else 'H5' end platform
            ,count(distinct get_json_object(value,'$.searchId'))  clk_cnt
        from csig_th_medicalbaike_interface :: t_medicalbaike_web_report_logs_fdt0
        WHERE tdbank_imp_date = '{0}' 
            and event in ('searchlist.itemclk')
            and uin != 0        
            and product in ('health.deluxe','yidian')
            and get_json_object(value,'$.query') is not null
            and get_json_object(value,'$.searchId') is not null
            and get_json_object(value, '$.cardId') == 'answerv2_5647456'
        GROUP BY value
            ,case when product='health.deluxe' then '健康'
            when product='yidian' and platform='miniprogram' then '小程序'
            when product='yidian' and platform in ('txyd','Android','iOS') then 'app'
            else 'H5' end
    '''.format(today)
    res2 = tdw.execute(sql2)

    if res2:
        jian_num2, xiao_num2, app_num2, H5_num2 = 0, 0, 0, 0
        list_data2 = []
        list_count2 = []
        for data in res2:
            try:
                search_cardId = re.compile(r'''cardId":"(.*?)"''')
                cardId_list = search_cardId.findall(data)

                search_searchId = re.compile(r'''searchId":"(.*?)"''')
                searchId = search_searchId.findall(data)[0]

                f_platform = data.split('\t')[1].strip()
                count = data.split('\t')[-1].strip()
                if count == False:
                    count = 0
                else:
                    count = int(count)
                if 'answerv2_5647456' in cardId_list and f_platform and searchId:
                    list_data2.append(searchId)
                    list_data2.append(f_platform)
                    list_data2.append(count)
                    if searchId in searchId_all_exp:
                        if f_platform == '健康':
                            jian_num2 += count
                        if f_platform == '小程序':
                            xiao_num2 += count
                        if f_platform == 'app':
                            app_num2 += count
                        if f_platform == 'H5':
                            H5_num2 += count

            except:
                tdw.WriteLog('searchId or query not exist')
        list_count2.append(jian_num2)
        list_count2.append(xiao_num2)
        list_count2.append(app_num2)
        list_count2.append(H5_num2)
    else:
        list_count2 = [0, 0, 0, 0]

    sql = '''
    use csig_th_medicalbaike_interface;
    '''
    tdw.execute(sql)

    for i in range(4):
        if i == 0:
            f_platform = '健康'
        if i == 1:
            f_platform = '小程序'
        if i == 2:
            f_platform = 'app'
        if i == 3:
            f_platform = 'H5'
        search_cnt = list_count1[i]
        clk_cnt = list_count2[i]

        sql4 = '''
        insert into t_uqa_search_stat
        (tdbank_imp_date, f_search_result_type, f_platform, f_search_cnt, f_search_clk_cnt)
        values ('{0}', '{1}', '{2}', '{3}', '{4}')
        '''.format(today, 'all', f_platform, search_cnt, clk_cnt)
        tdw.execute(sql4)



    # article
    sql1 = '''
        select value
            ,case when product='health.deluxe' then '健康'
            when product='yidian' and platform='miniprogram' then '小程序'
            when product='yidian' and platform in ('txyd','Android','iOS') then 'app'
            else 'H5' end f_platform
        from csig_th_medicalbaike_interface :: t_medicalbaike_web_report_logs_fdt0 
        WHERE tdbank_imp_date='{0}' and event='yidian.exposure'
            and value like '%searchId%'
            and value like '%cardId%'
            and value like '%answerv2_5647456%'
            and value like '%article%'
        GROUP BY value
            ,case when product='health.deluxe' then '健康'
            when product='yidian' and platform='miniprogram' then '小程序'
            when product='yidian' and platform in ('txyd','Android','iOS') then 'app'
            else 'H5' end 
    '''.format(today)
    res1 = tdw.execute(sql1)
    if res1:
        list_data = []
        searchId_all_exp = []
        for data in res1:
            try:
                search_cardId = re.compile(r'''cardId":"(.*?)"''')
                cardId_list = search_cardId.findall(data)

                search_searchId = re.compile(r'''searchId":"(.*?)"''')
                searchId_findall = search_searchId.findall(data)

                search_type = re.compile(r'''type":"(.*?)"''')
                type1 = search_type.findall(data)
                f_platform = data.split('\t')[-1].strip()

                list1 = []
                if 'answerv2_5647456' in cardId_list and f_platform and 'article' in type1:
                    searchId_str = ''''''
                    count = 0
                    for s in searchId_findall:
                        if s not in searchId_str:
                            if s not in searchId_all_exp:
                                searchId_all_exp.append(s)
                            count += 1
                            searchId_str += s + ','
                    if searchId_str != '''''':
                        list1.append(searchId_str)
                        list1.append(f_platform)
                        list1.append(count)
                        list_data.append(list1)
            except:
                tdw.WriteLog('searchId or query not exist')

        jian_num1, xiao_num1, app_num1, H5_num1 = 0, 0, 0, 0
        for data in list_data:
            f_platform = data[1]
            c = data[-1]
            if f_platform == '健康':
                jian_num1 += c
            if f_platform == '小程序':
                xiao_num1 += c
            if f_platform == 'app':
                app_num1 += c
            if f_platform == 'H5':
                H5_num1 += c
        list_count1 = []
        list_count1.append(jian_num1)
        list_count1.append(xiao_num1)
        list_count1.append(app_num1)
        list_count1.append(H5_num1)
    else:
        list_count1 = [0, 0, 0, 0]

    sql2 = '''
        select value 
            ,case when product='health.deluxe' then '健康'
            when product='yidian' and platform='miniprogram' then '小程序'
            when product='yidian' and platform in ('txyd','Android','iOS') then 'app'
            else 'H5' end platform
            ,count(distinct get_json_object(value,'$.searchId'))  clk_cnt
        from csig_th_medicalbaike_interface :: t_medicalbaike_web_report_logs_fdt0
        WHERE tdbank_imp_date = '{0}' 
            and event in ('searchlist.itemclk')
            and uin != 0        
            and product in ('health.deluxe','yidian')
            and get_json_object(value,'$.query') is not null
            and get_json_object(value,'$.searchId') is not null
            and get_json_object(value, '$.cardId') == 'answerv2_5647456'
        GROUP BY value
            ,case when product='health.deluxe' then '健康'
            when product='yidian' and platform='miniprogram' then '小程序'
            when product='yidian' and platform in ('txyd','Android','iOS') then 'app'
            else 'H5' end
    '''.format(today)
    res2 = tdw.execute(sql2)

    if res2:
        jian_num2, xiao_num2, app_num2, H5_num2 = 0, 0, 0, 0
        list_data2 = []
        list_count2 = []
        for data in res2:
            try:
                search_cardId = re.compile(r'''cardId":"(.*?)"''')
                cardId_list = search_cardId.findall(data)

                search_searchId = re.compile(r'''searchId":"(.*?)"''')
                searchId = search_searchId.findall(data)[0]

                f_platform = data.split('\t')[1].strip()
                count = data.split('\t')[-1].strip()
                if count == False:
                    count = 0
                else:
                    count = int(count)
                if 'answerv2_5647456' in cardId_list and f_platform and searchId:
                    list_data2.append(searchId)
                    list_data2.append(f_platform)
                    list_data2.append(count)
                    if searchId in searchId_all_exp:
                        if f_platform == '健康':
                            jian_num2 += count
                        if f_platform == '小程序':
                            xiao_num2 += count
                        if f_platform == 'app':
                            app_num2 += count
                        if f_platform == 'H5':
                            H5_num2 += count

            except:
                tdw.WriteLog('searchId or query not exist')
        list_count2.append(jian_num2)
        list_count2.append(xiao_num2)
        list_count2.append(app_num2)
        list_count2.append(H5_num2)
    else:
        list_count2 = [0, 0, 0, 0]

    sql = '''
    use csig_th_medicalbaike_interface;
    '''
    tdw.execute(sql)

    for i in range(4):
        if i == 0:
            f_platform = '健康'
        if i == 1:
            f_platform = '小程序'
        if i == 2:
            f_platform = 'app'
        if i == 3:
            f_platform = 'H5'
        search_cnt = list_count1[i]
        clk_cnt = list_count2[i]

        sql4 = '''
        insert into t_uqa_search_stat
        (tdbank_imp_date, f_search_result_type, f_platform, f_search_cnt, f_search_clk_cnt)
        values ('{0}', '{1}', '{2}', '{3}', '{4}')
        '''.format(today, 'article', f_platform, search_cnt, clk_cnt)
        tdw.execute(sql4)



    # video
    sql1 = '''
        select value
            ,case when product='health.deluxe' then '健康'
            when product='yidian' and platform='miniprogram' then '小程序'
            when product='yidian' and platform in ('txyd','Android','iOS') then 'app'
            else 'H5' end f_platform
        from csig_th_medicalbaike_interface :: t_medicalbaike_web_report_logs_fdt0 
        WHERE tdbank_imp_date='{0}' and event='yidian.exposure'
            and value like '%searchId%'
            and value like '%cardId%'
            and value like '%answerv2_5647456%'
            and value like '%video%'
        GROUP BY value
            ,case when product='health.deluxe' then '健康'
            when product='yidian' and platform='miniprogram' then '小程序'
            when product='yidian' and platform in ('txyd','Android','iOS') then 'app'
            else 'H5' end 
    '''.format(today)
    res1 = tdw.execute(sql1)

    if res1:
        list_data = []
        searchId_all_exp = []
        for data in res1:
            try:
                search_cardId = re.compile(r'''cardId":"(.*?)"''')
                cardId_list = search_cardId.findall(data)

                search_searchId = re.compile(r'''searchId":"(.*?)"''')
                searchId_findall = search_searchId.findall(data)
                search_type = re.compile(r'''type":"(.*?)"''')
                type1 = search_type.findall(data)
                f_platform = data.split('\t')[-1].strip()

                list1 = []
                if 'answerv2_5647456' in cardId_list and f_platform and 'video' in type1:
                    searchId_str = ''''''
                    count = 0
                    for s in searchId_findall:
                        if s not in searchId_str:
                            if s not in searchId_all_exp:
                                searchId_all_exp.append(s)
                            count += 1
                            searchId_str += s + ','
                    if searchId_str != '''''':
                        list1.append(searchId_str)
                        list1.append(f_platform)
                        list1.append(count)
                        list_data.append(list1)
            except:
                tdw.WriteLog('searchId or query not exist')

        jian_num1, xiao_num1, app_num1, H5_num1 = 0, 0, 0, 0
        for data in list_data:
            f_platform = data[1]
            c = data[-1]
            if f_platform == '健康':
                jian_num1 += c
            if f_platform == '小程序':
                xiao_num1 += c
            if f_platform == 'app':
                app_num1 += c
            if f_platform == 'H5':
                H5_num1 += c
        list_count1 = []
        list_count1.append(jian_num1)
        list_count1.append(xiao_num1)
        list_count1.append(app_num1)
        list_count1.append(H5_num1)
    else:
        list_count1 = [0, 0, 0, 0]

    sql2 = '''
        select value 
            ,case when product='health.deluxe' then '健康'
            when product='yidian' and platform='miniprogram' then '小程序'
            when product='yidian' and platform in ('txyd','Android','iOS') then 'app'
            else 'H5' end platform
            ,count(distinct get_json_object(value,'$.searchId'))  clk_cnt
        from csig_th_medicalbaike_interface :: t_medicalbaike_web_report_logs_fdt0
        WHERE tdbank_imp_date = '{0}' 
            and event in ('searchlist.itemclk')
            and uin != 0        
            and product in ('health.deluxe','yidian')
            and get_json_object(value,'$.query') is not null
            and get_json_object(value,'$.searchId') is not null
            and get_json_object(value, '$.cardId') == 'answerv2_5647456'
        GROUP BY value
            ,case when product='health.deluxe' then '健康'
            when product='yidian' and platform='miniprogram' then '小程序'
            when product='yidian' and platform in ('txyd','Android','iOS') then 'app'
            else 'H5' end
    '''.format(today)
    res2 = tdw.execute(sql2)

    if res2:
        jian_num2, xiao_num2, app_num2, H5_num2 = 0, 0, 0, 0
        list_data2 = []
        list_count2 = []
        for data in res2:
            try:
                search_cardId = re.compile(r'''cardId":"(.*?)"''')
                cardId_list = search_cardId.findall(data)

                search_searchId = re.compile(r'''searchId":"(.*?)"''')
                searchId = search_searchId.findall(data)[0]

                f_platform = data.split('\t')[1].strip()
                count = data.split('\t')[-1].strip()
                if count == False:
                    count = 0
                else:
                    count = int(count)
                if 'answerv2_5647456' in cardId_list and f_platform and searchId:
                    list_data2.append(searchId)
                    list_data2.append(f_platform)
                    list_data2.append(count)
                    if searchId in searchId_all_exp:
                        if f_platform == '健康':
                            jian_num2 += count
                        if f_platform == '小程序':
                            xiao_num2 += count
                        if f_platform == 'app':
                            app_num2 += count
                        if f_platform == 'H5':
                            H5_num2 += count

            except:
                tdw.WriteLog('searchId or query not exist')
        list_count2.append(jian_num2)
        list_count2.append(xiao_num2)
        list_count2.append(app_num2)
        list_count2.append(H5_num2)
    else:
        list_count2 = [0, 0, 0, 0]

    sql = '''
    use csig_th_medicalbaike_interface;
    '''
    tdw.execute(sql)

    for i in range(4):
        if i == 0:
            f_platform = '健康'
        if i == 1:
            f_platform = '小程序'
        if i == 2:
            f_platform = 'app'
        if i == 3:
            f_platform = 'H5'
        search_cnt = list_count1[i]
        clk_cnt = list_count2[i]

        sql4 = '''
        insert into t_uqa_search_stat
        (tdbank_imp_date, f_search_result_type, f_platform, f_search_cnt, f_search_clk_cnt)
        values ('{0}', '{1}', '{2}', '{3}', '{4}')
        '''.format(today, 'video', f_platform, search_cnt, clk_cnt)
        tdw.execute(sql4)

    # audio
    sql1 = '''
        select value
            ,case when product='health.deluxe' then '健康'
            when product='yidian' and platform='miniprogram' then '小程序'
            when product='yidian' and platform in ('txyd','Android','iOS') then 'app'
            else 'H5' end f_platform
        from csig_th_medicalbaike_interface :: t_medicalbaike_web_report_logs_fdt0 
        WHERE tdbank_imp_date='{0}' and event='yidian.exposure'
            and value like '%searchId%'
            and value like '%cardId%'
            and value like '%answerv2_5647456%'
            and value like '%audio%'
        GROUP BY value
            ,case when product='health.deluxe' then '健康'
            when product='yidian' and platform='miniprogram' then '小程序'
            when product='yidian' and platform in ('txyd','Android','iOS') then 'app'
            else 'H5' end 
    '''.format(today)
    res1 = tdw.execute(sql1)

    if res1:
        list_data = []
        searchId_all_exp = []
        for data in res1:
            try:
                search_cardId = re.compile(r'''cardId":"(.*?)"''')
                cardId_list = search_cardId.findall(data)

                search_searchId = re.compile(r'''searchId":"(.*?)"''')
                searchId_findall = search_searchId.findall(data)
                search_type = re.compile(r'''type":"(.*?)"''')
                type1 = search_type.findall(data)
                f_platform = data.split('\t')[-1].strip()

                list1 = []
                if 'answerv2_5647456' in cardId_list and f_platform and 'audio' in type1:
                    searchId_str = ''''''
                    count = 0
                    for s in searchId_findall:
                        if s not in searchId_str:
                            if s not in searchId_all_exp:
                                searchId_all_exp.append(s)
                            count += 1
                            searchId_str += s + ','
                    if searchId_str != '''''':
                        list1.append(searchId_str)
                        list1.append(f_platform)
                        list1.append(count)
                        list_data.append(list1)
            except:
                tdw.WriteLog('searchId or query not exist')

        jian_num1, xiao_num1, app_num1, H5_num1 = 0, 0, 0, 0
        for data in list_data:
            f_platform = data[1]
            c = data[-1]
            if f_platform == '健康':
                jian_num1 += c
            if f_platform == '小程序':
                xiao_num1 += c
            if f_platform == 'app':
                app_num1 += c
            if f_platform == 'H5':
                H5_num1 += c
        list_count1 = []
        list_count1.append(jian_num1)
        list_count1.append(xiao_num1)
        list_count1.append(app_num1)
        list_count1.append(H5_num1)
    else:
        list_count1 = [0, 0, 0, 0]


    sql2 = '''
        select value 
            ,case when product='health.deluxe' then '健康'
            when product='yidian' and platform='miniprogram' then '小程序'
            when product='yidian' and platform in ('txyd','Android','iOS') then 'app'
            else 'H5' end platform
            ,count(distinct get_json_object(value,'$.searchId'))  clk_cnt
        from csig_th_medicalbaike_interface :: t_medicalbaike_web_report_logs_fdt0
        WHERE tdbank_imp_date = '{0}' 
            and event in ('searchlist.itemclk')
            and uin != 0        
            and product in ('health.deluxe','yidian')
            and get_json_object(value,'$.query') is not null
            and get_json_object(value,'$.searchId') is not null
            and get_json_object(value, '$.cardId') == 'answerv2_5647456'
        GROUP BY value
            ,case when product='health.deluxe' then '健康'
            when product='yidian' and platform='miniprogram' then '小程序'
            when product='yidian' and platform in ('txyd','Android','iOS') then 'app'
            else 'H5' end
    '''.format(today)
    res2 = tdw.execute(sql2)

    if res2:
        jian_num2, xiao_num2, app_num2, H5_num2 = 0, 0, 0, 0
        list_data2 = []
        list_count2 = []
        for data in res2:
            try:
                search_cardId = re.compile(r'''cardId":"(.*?)"''')
                cardId_list = search_cardId.findall(data)

                search_searchId = re.compile(r'''searchId":"(.*?)"''')
                searchId = search_searchId.findall(data)[0]

                f_platform = data.split('\t')[1].strip()
                count = data.split('\t')[-1].strip()
                if count == False:
                    count = 0
                else:
                    count = int(count)
                if 'answerv2_5647456' in cardId_list and f_platform and searchId:
                    list_data2.append(searchId)
                    list_data2.append(f_platform)
                    list_data2.append(count)
                    if searchId in searchId_all_exp:
                        if f_platform == '健康':
                            jian_num2 += count
                        if f_platform == '小程序':
                            xiao_num2 += count
                        if f_platform == 'app':
                            app_num2 += count
                        if f_platform == 'H5':
                            H5_num2 += count

            except:
                tdw.WriteLog('searchId or query not exist')
        list_count2.append(jian_num2)
        list_count2.append(xiao_num2)
        list_count2.append(app_num2)
        list_count2.append(H5_num2)
    else:
        list_count2 = [0, 0, 0, 0]

    sql = '''
    use csig_th_medicalbaike_interface;
    '''
    tdw.execute(sql)

    for i in range(4):
        if i == 0:
            f_platform = '健康'
        if i == 1:
            f_platform = '小程序'
        if i == 2:
            f_platform = 'app'
        if i == 3:
            f_platform = 'H5'
        search_cnt = list_count1[i]
        clk_cnt = list_count2[i]

        sql4 = '''
        insert into t_uqa_search_stat
        (tdbank_imp_date, f_search_result_type, f_platform, f_search_cnt, f_search_clk_cnt)
        values ('{0}', '{1}', '{2}', '{3}', '{4}')
        '''.format(today, 'audio', f_platform, search_cnt, clk_cnt)
        tdw.execute(sql4)




    # yesorno
    sql1 = '''
        select value
            ,case when product='health.deluxe' then '健康'
            when product='yidian' and platform='miniprogram' then '小程序'
            when product='yidian' and platform in ('txyd','Android','iOS') then 'app'
            else 'H5' end f_platform
        from csig_th_medicalbaike_interface :: t_medicalbaike_web_report_logs_fdt0 
        WHERE tdbank_imp_date='{0}' 
        		and event='yidian.exposure'
            and value like '%searchId%'
            and value like '%cardId%'
            and value like '%answerv2_5647456%'
            and value like '%yesorno%'
        GROUP BY value
            ,case when product='health.deluxe' then '健康'
            when product='yidian' and platform='miniprogram' then '小程序'
            when product='yidian' and platform in ('txyd','Android','iOS') then 'app'
            else 'H5' end 
    '''.format(today)
    res1 = tdw.execute(sql1)



    if res1:
        list_data = []
        searchId_all_exp = []
        for data in res1:
            try:
                search_cardId = re.compile(r'''cardId":"(.*?)"''')
                cardId_list = search_cardId.findall(data)

                search_searchId = re.compile(r'''searchId":"(.*?)"''')
                searchId_findall = search_searchId.findall(data)

                search_yesorno = re.compile(r'''yesorno":(.*?),''')
                yesorno = search_yesorno.findall(data)[0]
                f_platform = data.split('\t')[-1].strip()

                list1 = []
                if 'answerv2_5647456' in cardId_list and f_platform and yesorno != 'false':
                    searchId_str = ''''''
                    count = 0
                    for s in searchId_findall:
                        if s not in searchId_str:
                            if s not in searchId_all_exp:
                                searchId_all_exp.append(s)
                            count += 1
                            searchId_str += s + ','
                    if searchId_str != '''''':
                        list1.append(searchId_str)
                        list1.append(f_platform)
                        list1.append(count)
                        list_data.append(list1)
            except:
                tdw.WriteLog('searchId or query not exist')


        jian_num1, xiao_num1, app_num1, H5_num1 = 0, 0, 0, 0
        for data in list_data:
            f_platform = data[1]
            c = data[-1]
            if f_platform == '健康':
                jian_num1 += c
            if f_platform == '小程序':
                xiao_num1 += c
            if f_platform == 'app':
                app_num1 += c
            if f_platform == 'H5':
                H5_num1 += c
        list_count1 = []
        list_count1.append(jian_num1)
        list_count1.append(xiao_num1)
        list_count1.append(app_num1)
        list_count1.append(H5_num1)
    else:
        list_count1 = [0, 0, 0, 0]
# f_search_cnt  搜索次数   f_search_clk_cnt   点击次数

    sql2 = '''
        select value 
            ,case when product='health.deluxe' then '健康'
            when product='yidian' and platform='miniprogram' then '小程序'
            when product='yidian' and platform in ('txyd','Android','iOS') then 'app'
            else 'H5' end platform
            ,count(distinct get_json_object(value,'$.searchId'))  clk_cnt
        from csig_th_medicalbaike_interface :: t_medicalbaike_web_report_logs_fdt0
        WHERE tdbank_imp_date = '{0}' 
            and event in ('searchlist.itemclk')
            and uin != 0        
            and product in ('health.deluxe','yidian')
            and get_json_object(value,'$.query') is not null
            and get_json_object(value,'$.searchId') is not null
            and get_json_object(value, '$.cardId') == 'answerv2_5647456'
        GROUP BY value
            ,case when product='health.deluxe' then '健康'
            when product='yidian' and platform='miniprogram' then '小程序'
            when product='yidian' and platform in ('txyd','Android','iOS') then 'app'
            else 'H5' end
    '''.format(today)
    res2 = tdw.execute(sql2)

    if res2:
        jian_num2, xiao_num2, app_num2, H5_num2 = 0, 0, 0, 0
        list_data2 = []
        list_count2 = []
        for data in res2:
            try:
                search_cardId = re.compile(r'''cardId":"(.*?)"''')
                cardId_list = search_cardId.findall(data)

                search_searchId = re.compile(r'''searchId":"(.*?)"''')
                searchId = search_searchId.findall(data)[0]

                f_platform = data.split('\t')[1].strip()
                count = data.split('\t')[-1].strip()
                if count == False:
                    count = 0
                else:
                    count = int(count)
                if 'answerv2_5647456' in cardId_list and f_platform and searchId:
                    list_data2.append(searchId)
                    list_data2.append(f_platform)
                    list_data2.append(count)
                    if searchId in searchId_all_exp:
                        if f_platform == '健康':
                            jian_num2 += count
                        if f_platform == '小程序':
                            xiao_num2 += count
                        if f_platform == 'app':
                            app_num2 += count
                        if f_platform == 'H5':
                            H5_num2 += count
            except:
                tdw.WriteLog('searchId or query not exist')
        list_count2.append(jian_num2)
        list_count2.append(xiao_num2)
        list_count2.append(app_num2)
        list_count2.append(H5_num2)
    else:
        list_count2 = [0, 0, 0, 0]


    sql = '''
    use csig_th_medicalbaike_interface;
    '''
    tdw.execute(sql)

    for i in range(4):
        if i == 0:
            f_platform = '健康'
        if i == 1:
            f_platform = '小程序'
        if i == 2:
            f_platform = 'app'
        if i == 3:
            f_platform = 'H5'
        search_cnt = list_count1[i]
        clk_cnt = list_count2[i]

        sql4 = '''
        insert into t_uqa_search_stat
        (tdbank_imp_date, f_search_result_type, f_platform, f_search_cnt, f_search_clk_cnt)
        values ('{0}', '{1}', '{2}', '{3}', '{4}')
        '''.format(today, 'yesorno', f_platform, search_cnt, clk_cnt)
        tdw.execute(sql4)



    # yesorno_exposure
    sql1 = '''
        select value
            ,case when product='health.deluxe' then '健康'
            when product='yidian' and platform='miniprogram' then '小程序'
            when product='yidian' and platform in ('txyd','Android','iOS') then 'app'
            else 'H5' end f_platform
        from csig_th_medicalbaike_interface :: t_medicalbaike_web_report_logs_fdt0 
        WHERE tdbank_imp_date='{0}' and event='yidian.exposure'
            and value like '%searchId%'
            and value like '%cardId%'
            and value like '%answerv2_5647456%'
        GROUP BY value
            ,case when product='health.deluxe' then '健康'
            when product='yidian' and platform='miniprogram' then '小程序'
            when product='yidian' and platform in ('txyd','Android','iOS') then 'app'
            else 'H5' end 
    '''.format(today)
    res1 = tdw.execute(sql1)

    if res1:
        list_data0 = []
        list_data = []
        searchId_all_exp = []
        searchId_all_exp1 = []
        for data in res1:
            try:
                search_cardId = re.compile(r'''cardId":"(.*?)"''')
                cardId_list = search_cardId.findall(data)

                search_searchId = re.compile(r'''searchId":"(.*?)"''')
                searchId_findall = search_searchId.findall(data)

                f_platform = data.split('\t')[-1].strip()

                list0 = []
                if 'answerv2_5647456' in cardId_list and f_platform:
                    searchId_str = ''''''
                    count = 0
                    for s in searchId_findall:
                        if s not in searchId_str:
                            if s not in searchId_all_exp1:
                                searchId_all_exp1.append(s)
                            count += 1
                            searchId_str += s + ','
                    if searchId_str != '''''':
                        list0.append(searchId_str)
                        list0.append(f_platform)
                        list0.append(count)
                        list_data0.append(list0)
                search_yesorno = re.compile(r'''yesorno":(.*?),''')
                yesorno = search_yesorno.findall(data)[0]
                list1 = []
                if 'answerv2_5647456' in cardId_list and f_platform and yesorno != 'false':
                    searchId_str = ''''''
                    count = 0
                    for s in searchId_findall:
                        if s not in searchId_str:
                            if s not in searchId_all_exp:
                                searchId_all_exp.append(s)
                            count += 1
                            searchId_str += s + ','
                    if searchId_str != '''''':
                        list1.append(searchId_str)
                        list1.append(f_platform)
                        list1.append(count)
                        list_data.append(list1)
            except:
                tdw.WriteLog('searchId or query not exist')

        jian_num1, xiao_num1, app_num1, H5_num1 = 0, 0, 0, 0
        for data in list_data0:
            f_platform = data[1]
            c = data[-1]
            if f_platform == '健康':
                jian_num1 += c
            if f_platform == '小程序':
                xiao_num1 += c
            if f_platform == 'app':
                app_num1 += c
            if f_platform == 'H5':
                H5_num1 += c
        list_count1 = []
        list_count1.append(jian_num1)
        list_count1.append(xiao_num1)
        list_count1.append(app_num1)
        list_count1.append(H5_num1)
        jian_num11, xiao_num11, app_num11, H5_num11 = 0, 0, 0, 0
        for data in list_data:
            f_platform = data[1]
            c = data[-1]
            if f_platform == '健康':
                jian_num11 += c
            if f_platform == '小程序':
                xiao_num11 += c
            if f_platform == 'app':
                app_num11 += c
            if f_platform == 'H5':
                H5_num11 += c
        list_count11 = []
        list_count11.append(jian_num11)
        list_count11.append(xiao_num11)
        list_count11.append(app_num11)
        list_count11.append(H5_num11)
    else:
        list_count1 = [0, 0, 0, 0]
        list_count11 = [0, 0, 0, 0]

    for i in range(4):
        if i == 0:
            f_platform = '健康'
        if i == 1:
            f_platform = '小程序'
        if i == 2:
            f_platform = 'app'
        if i == 3:
            f_platform = 'H5'
        search_cnt = list_count1[i]
        clk_cnt = list_count11[i]

        sql4 = '''
        insert into t_uqa_search_stat
        (tdbank_imp_date, f_search_result_type, f_platform, f_search_cnt, f_search_clk_cnt)
        values ('{0}', '{1}', '{2}', '{3}', '{4}')
        '''.format(today, 'yesorno_exposure', f_platform, search_cnt, clk_cnt)
        tdw.execute(sql4)

    # article_exposure
    sql1 = '''
        select value
            ,case when product='health.deluxe' then '健康'
            when product='yidian' and platform='miniprogram' then '小程序'
            when product='yidian' and platform in ('txyd','Android','iOS') then 'app'
            else 'H5' end f_platform
        from csig_th_medicalbaike_interface :: t_medicalbaike_web_report_logs_fdt0 
        WHERE tdbank_imp_date='{0}' and event='yidian.exposure'
            and value like '%searchId%'
            and value like '%cardId%'
            and value like '%answerv2_5647456%'
        GROUP BY value
            ,case when product='health.deluxe' then '健康'
            when product='yidian' and platform='miniprogram' then '小程序'
            when product='yidian' and platform in ('txyd','Android','iOS') then 'app'
            else 'H5' end 
    '''.format(today)
    res1 = tdw.execute(sql1)

    if res1:
        list_data0 = []
        list_data = []
        searchId_all_exp = []
        searchId_all_exp1 = []
        for data in res1:
            try:
                search_cardId = re.compile(r'''cardId":"(.*?)"''')
                cardId_list = search_cardId.findall(data)

                search_searchId = re.compile(r'''searchId":"(.*?)"''')
                searchId_findall = search_searchId.findall(data)

                search_type = re.compile(r'''type":"(.*?)"''')
                type1 = search_type.findall(data)[0]
                f_platform = data.split('\t')[-1].strip()

                list0 = []
                if 'answerv2_5647456' in cardId_list and f_platform:
                    searchId_str = ''''''
                    count = 0
                    for s in searchId_findall:
                        if s not in searchId_str:
                            if s not in searchId_all_exp1:
                                searchId_all_exp1.append(s)
                            count += 1
                            searchId_str += s + ','
                    if searchId_str != '''''':
                        list0.append(searchId_str)
                        list0.append(f_platform)
                        list0.append(count)
                        list_data0.append(list0)

                list1 = []
                if 'answerv2_5647456' in cardId_list and f_platform and 'article' in type1:
                    searchId_str = ''''''
                    count = 0
                    for s in searchId_findall:
                        if s not in searchId_str:
                            if s not in searchId_all_exp:
                                searchId_all_exp.append(s)
                            count += 1
                            searchId_str += s + ','
                    if searchId_str != '''''':
                        list1.append(searchId_str)
                        list1.append(f_platform)
                        list1.append(count)
                        list_data.append(list1)
            except:
                tdw.WriteLog('searchId or query not exist')

        jian_num1, xiao_num1, app_num1, H5_num1 = 0, 0, 0, 0
        for data in list_data0:
            f_platform = data[1]
            c = data[-1]
            if f_platform == '健康':
                jian_num1 += c
            if f_platform == '小程序':
                xiao_num1 += c
            if f_platform == 'app':
                app_num1 += c
            if f_platform == 'H5':
                H5_num1 += c
        list_count1 = []
        list_count1.append(jian_num1)
        list_count1.append(xiao_num1)
        list_count1.append(app_num1)
        list_count1.append(H5_num1)
        jian_num11, xiao_num11, app_num11, H5_num11 = 0, 0, 0, 0
        for data in list_data:
            f_platform = data[1]
            c = data[-1]
            if f_platform == '健康':
                jian_num11 += c
            if f_platform == '小程序':
                xiao_num11 += c
            if f_platform == 'app':
                app_num11 += c
            if f_platform == 'H5':
                H5_num11 += c
        list_count11 = []
        list_count11.append(jian_num11)
        list_count11.append(xiao_num11)
        list_count11.append(app_num11)
        list_count11.append(H5_num11)
    else:
        list_count1 = [0, 0, 0, 0]
        list_count11 = [0, 0, 0, 0]

    for i in range(4):
        if i == 0:
            f_platform = '健康'
        if i == 1:
            f_platform = '小程序'
        if i == 2:
            f_platform = 'app'
        if i == 3:
            f_platform = 'H5'
        search_cnt = list_count1[i]
        clk_cnt = list_count11[i]

        sql4 = '''
        insert into t_uqa_search_stat
        (tdbank_imp_date, f_search_result_type, f_platform, f_search_cnt, f_search_clk_cnt)
        values ('{0}', '{1}', '{2}', '{3}', '{4}')
        '''.format(today, 'article_exposure', f_platform, search_cnt, clk_cnt)
        tdw.execute(sql4)


    # video_exposure
    sql1 = '''
        select value
            ,case when product='health.deluxe' then '健康'
            when product='yidian' and platform='miniprogram' then '小程序'
            when product='yidian' and platform in ('txyd','Android','iOS') then 'app'
            else 'H5' end f_platform
        from csig_th_medicalbaike_interface :: t_medicalbaike_web_report_logs_fdt0 
        WHERE tdbank_imp_date='{0}' and event='yidian.exposure'
            and value like '%searchId%'
            and value like '%cardId%'
            and value like '%answerv2_5647456%'
        GROUP BY value
            ,case when product='health.deluxe' then '健康'
            when product='yidian' and platform='miniprogram' then '小程序'
            when product='yidian' and platform in ('txyd','Android','iOS') then 'app'
            else 'H5' end 
    '''.format(today)
    res1 = tdw.execute(sql1)

    if res1:
        list_data0 = []
        list_data = []
        searchId_all_exp = []
        searchId_all_exp1 = []
        for data in res1:
            try:
                search_cardId = re.compile(r'''cardId":"(.*?)"''')
                cardId_list = search_cardId.findall(data)

                search_searchId = re.compile(r'''searchId":"(.*?)"''')
                searchId_findall = search_searchId.findall(data)

                search_type = re.compile(r'''type":"(.*?)"''')
                type1 = search_type.findall(data)[0]
                f_platform = data.split('\t')[-1].strip()

                list0 = []
                if 'answerv2_5647456' in cardId_list and f_platform:
                    searchId_str = ''''''
                    count = 0
                    for s in searchId_findall:
                        if s not in searchId_str:
                            if s not in searchId_all_exp1:
                                searchId_all_exp1.append(s)
                            count += 1
                            searchId_str += s + ','
                    if searchId_str != '''''':
                        list0.append(searchId_str)
                        list0.append(f_platform)
                        list0.append(count)
                        list_data0.append(list0)

                list1 = []
                if 'answerv2_5647456' in cardId_list and f_platform and 'video' in type1:
                    searchId_str = ''''''
                    count = 0
                    for s in searchId_findall:
                        if s not in searchId_str:
                            if s not in searchId_all_exp:
                                searchId_all_exp.append(s)
                            count += 1
                            searchId_str += s + ','
                    if searchId_str != '''''':
                        list1.append(searchId_str)
                        list1.append(f_platform)
                        list1.append(count)
                        list_data.append(list1)
            except:
                tdw.WriteLog('searchId or query not exist')

        jian_num1, xiao_num1, app_num1, H5_num1 = 0, 0, 0, 0
        for data in list_data0:
            f_platform = data[1]
            c = data[-1]
            if f_platform == '健康':
                jian_num1 += c
            if f_platform == '小程序':
                xiao_num1 += c
            if f_platform == 'app':
                app_num1 += c
            if f_platform == 'H5':
                H5_num1 += c
        list_count1 = []
        list_count1.append(jian_num1)
        list_count1.append(xiao_num1)
        list_count1.append(app_num1)
        list_count1.append(H5_num1)
        jian_num11, xiao_num11, app_num11, H5_num11 = 0, 0, 0, 0
        for data in list_data:
            f_platform = data[1]
            c = data[-1]
            if f_platform == '健康':
                jian_num11 += c
            if f_platform == '小程序':
                xiao_num11 += c
            if f_platform == 'app':
                app_num11 += c
            if f_platform == 'H5':
                H5_num11 += c
        list_count11 = []
        list_count11.append(jian_num11)
        list_count11.append(xiao_num11)
        list_count11.append(app_num11)
        list_count11.append(H5_num11)
    else:
        list_count1 = [0, 0, 0, 0]
        list_count11 = [0, 0, 0, 0]

    for i in range(4):
        if i == 0:
            f_platform = '健康'
        if i == 1:
            f_platform = '小程序'
        if i == 2:
            f_platform = 'app'
        if i == 3:
            f_platform = 'H5'
        search_cnt = list_count1[i]
        clk_cnt = list_count11[i]

        sql4 = '''
        insert into t_uqa_search_stat
        (tdbank_imp_date, f_search_result_type, f_platform, f_search_cnt, f_search_clk_cnt)
        values ('{0}', '{1}', '{2}', '{3}', '{4}')
        '''.format(today, 'video_exposure', f_platform, search_cnt, clk_cnt)
        tdw.execute(sql4)

    # audio_exposure
    sql1 = '''
        select value
            ,case when product='health.deluxe' then '健康'
            when product='yidian' and platform='miniprogram' then '小程序'
            when product='yidian' and platform in ('txyd','Android','iOS') then 'app'
            else 'H5' end f_platform
        from csig_th_medicalbaike_interface :: t_medicalbaike_web_report_logs_fdt0 
        WHERE tdbank_imp_date='{0}' and event='yidian.exposure'
            and value like '%searchId%'
            and value like '%cardId%'
            and value like '%answerv2_5647456%'
        GROUP BY value
            ,case when product='health.deluxe' then '健康'
            when product='yidian' and platform='miniprogram' then '小程序'
            when product='yidian' and platform in ('txyd','Android','iOS') then 'app'
            else 'H5' end 
    '''.format(today)
    res1 = tdw.execute(sql1)

    if res1:
        list_data0 = []
        list_data = []
        searchId_all_exp = []
        searchId_all_exp1 = []
        for data in res1:
            try:
                search_cardId = re.compile(r'''cardId":"(.*?)"''')
                cardId_list = search_cardId.findall(data)

                search_searchId = re.compile(r'''searchId":"(.*?)"''')
                searchId_findall = search_searchId.findall(data)

                search_type = re.compile(r'''type":"(.*?)"''')
                type1 = search_type.findall(data)[0]
                f_platform = data.split('\t')[-1].strip()

                list0 = []
                if 'answerv2_5647456' in cardId_list and f_platform:
                    searchId_str = ''''''
                    count = 0
                    for s in searchId_findall:
                        if s not in searchId_str:
                            if s not in searchId_all_exp1:
                                searchId_all_exp1.append(s)
                            count += 1
                            searchId_str += s + ','
                    if searchId_str != '''''':
                        list0.append(searchId_str)
                        list0.append(f_platform)
                        list0.append(count)
                        list_data0.append(list0)

                list1 = []
                if 'answerv2_5647456' in cardId_list and f_platform and 'audio' in type1:
                    searchId_str = ''''''
                    count = 0
                    for s in searchId_findall:
                        if s not in searchId_str:
                            if s not in searchId_all_exp:
                                searchId_all_exp.append(s)
                            count += 1
                            searchId_str += s + ','
                    if searchId_str != '''''':
                        list1.append(searchId_str)
                        list1.append(f_platform)
                        list1.append(count)
                        list_data.append(list1)
            except:
                tdw.WriteLog('searchId or query not exist')

        jian_num1, xiao_num1, app_num1, H5_num1 = 0, 0, 0, 0
        for data in list_data0:
            f_platform = data[1]
            c = data[-1]
            if f_platform == '健康':
                jian_num1 += c
            if f_platform == '小程序':
                xiao_num1 += c
            if f_platform == 'app':
                app_num1 += c
            if f_platform == 'H5':
                H5_num1 += c
        list_count1 = []
        list_count1.append(jian_num1)
        list_count1.append(xiao_num1)
        list_count1.append(app_num1)
        list_count1.append(H5_num1)
        jian_num11, xiao_num11, app_num11, H5_num11 = 0, 0, 0, 0
        for data in list_data:
            f_platform = data[1]
            c = data[-1]
            if f_platform == '健康':
                jian_num11 += c
            if f_platform == '小程序':
                xiao_num11 += c
            if f_platform == 'app':
                app_num11 += c
            if f_platform == 'H5':
                H5_num11 += c
        list_count11 = []
        list_count11.append(jian_num11)
        list_count11.append(xiao_num11)
        list_count11.append(app_num11)
        list_count11.append(H5_num11)
    else:
        list_count1 = [0, 0, 0, 0]
        list_count11 = [0, 0, 0, 0]

    for i in range(4):
        if i == 0:
            f_platform = '健康'
        if i == 1:
            f_platform = '小程序'
        if i == 2:
            f_platform = 'app'
        if i == 3:
            f_platform = 'H5'
        search_cnt = list_count1[i]
        clk_cnt = list_count11[i]

        sql4 = '''
        insert into t_uqa_search_stat
        (tdbank_imp_date, f_search_result_type, f_platform, f_search_cnt, f_search_clk_cnt)
        values ('{0}', '{1}', '{2}', '{3}', '{4}')
        '''.format(today, 'audio_exposure', f_platform, search_cnt, clk_cnt)
        tdw.execute(sql4)








