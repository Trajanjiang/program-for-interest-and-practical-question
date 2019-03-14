#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:07:10 2019

@author: hongfengjiang
"""

# %%
# import library
import pandas as pd
import tushare as ts
from datetime import date 
# %%
# 按照行业收集股票数据
stocks_info = ts.get_stock_basics()
def stocks_info_industry(industry_name):
    df = stocks_info[stocks_info['industry'] == industry_name]
    if df.shape[0] > 0:
        return df['name'].tolist()
    else:
        print('没有该行业股票数据')

# %%
# 定义一个函数选择所需要的报表生成的时间。
def report_time_chosen(n):
    """
    n 为自定义变量所需要的报表年数。
    """
    if n >= 15: 
        print("报表所需生成的年数过长，数据从缺。")
    else:
        today = date.today()
        year = today.year
        month = today.month
        season = int(month/4) + 1
        if season >= 2:
            start_year = year - n - 1
            end_year = year - 1
        else:
            start_year = year - n - 2
            end_year = year - 2
        return [start_year, end_year]

recent_year = report_time_chosen(3)
start_time = recent_year[0]
end_time = recent_year[1]

# %%
# 下载指定年份的报表数据
def report_type_chosen(report_type, year, season):
    """
    report_type: 报表种类
    year: 报表年份
    season: 报表季度
    """
    report_type_dict = {
            '主表': ts.get_report_data(year, season),
            '收益表': ts.get_profit_data(year, season),
            '运营表': ts.get_operation_data(year, season),
            '现金流表': ts.get_cashflow_data(year, season),
            '偿债能力表': ts.get_debtpaying_data(year, season),
                }
    report_chosen = report_type_dict.get(report_type)
    return report_chosen

def get_report(start_year, end_year, report_type):
    report_list = []
    for i in range(start_year, end_year + 1):
        report = report_type_chosen(report_type, i, 4)
        report_list.append(report)
    return report_list
