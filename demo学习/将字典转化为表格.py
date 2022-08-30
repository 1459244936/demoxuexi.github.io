# 将字典导出为excel
import xlwt
import pandas as pd


def export_excel(export):
    # 将字典列表转换为DataFrame
    pf = pd.DataFrame(list(export))
    # 指定字段顺序
    order = ['编号', '姓名', '部门', '绩效', '奖金', '基本工资']
    pf = pf[order]

    # 指定生成的Excel表格名称
    file_path = pd.ExcelWriter('D:/name.xlsx')
    # 输出
    pf.to_excel(file_path, encoding='utf-8', index=False)
    # 保存表格
    file_path.save()


staff_info = [
    {'编号': 'S1001', '姓名': '吕建国', '部门': '销售部', '绩效': 100, '奖金': 2250, '基本工资': 7500},
    {'编号': 'S1002', '姓名': '张想', '部门': '后勤部', '绩效': 100, '奖金': 4250, '基本工资': 7500},
    {'编号': 'S1003', '姓名': '王淑兰', '部门': '后勤部', '绩效': 300, '奖金': 3500, '基本工资': 6500},
    {'编号': 'S1004', '姓名': '赵丽娟', '部门': '开发部', '绩效': 100, '奖金': 2750, '基本工资': 7500},
    {'编号': 'S1005', '姓名': '陈利', '部门': '开发部', '绩效': 100, '奖金': 1750, '基本工资': 6000},
    {'编号': 'S1006', '姓名': '车敏', '部门': '销售部', '绩效': 300, '奖金': 4250, '基本工资': 7000},
    {'编号': 'S1007', '姓名': '孙飞', '部门': '运营部', '绩效': 200, '奖金': 1500, '基本工资': 7000},
    {'编号': 'S1008', '姓名': '陈彬', '部门': '后勤部', '绩效': 300, '奖金': 1500, '基本工资': 9500}
]

export_excel(staff_info)