"""
parameters.py

This file is for defining global parameters such as subject list and dataset names
used across signal processing modules.
"""

# ==============================
# 📁 Dataset Lists
# ==============================

# PURE
# TestData (private, single subject)
# VIPL-HR 
# Vital Videos 
# IRB-approved dataset


''' PURE Subject List '''
PURE_subject_list = [
                '01-01', '01-02', '01-03', '01-04', '01-05', '01-06',
                '02-01', '02-02', '02-03', '02-04', '02-05', '02-06',
                '03-01', '03-02', '03-03', '03-04', '03-05', '03-06',
                '04-01', '04-02', '04-03', '04-04', '04-05', '04-06',
                '05-01', '05-02', 
                # 얼굴 인식 안되는 프레임 존재
                # '05-03', '05-04', '05-05', '05-06',
                '06-01', '06-03', '06-04', '06-05', '06-06',
                '07-01', '07-02', '07-03', '07-04', '07-05', '07-06',
                '08-01', '08-02', '08-03', '08-04', '08-05', '08-06',
                '09-01', '09-02', '09-03', '09-04', '09-05', '09-06',
                '10-01', '10-02', '10-03', '10-04', '10-05', '10-06',
                # 'ForPublication/01-01', 'ForPublication/01-02', 'ForPublication/01-03', 'ForPublication/01-04', 'ForPublication/01-05', 'ForPublication/01-06'
]

## PURE 중에서 산소포화도 변동성 있는 데이터
# 02-02, 02-04
# 03-02
# 06-01, 06-05
# 07-02, 07-03, 07-04, 07-05
# 09-03 (Raw가 나은 거..)
# 10-05


''' TestData Subject List'''
TestData_subject_list = [
                'SpO2-2', 'SpO2-3', 'SpO2-low-1', 'SpO2-low-2', 'SpO2-low-3',
                'SpO2-4', 'SpO2-5', 'SpO2-6', 'SpO2-low-4', 'SpO2-low-5', 'SpO2-low-6',
                'SpO2-7', 'SpO2-8', 'SpO2-9', 'SpO2-low-7', 'SpO2-low-8',
]


''' VIPL_HR Subject List'''



''' Vital Videos Subject List'''



''' IRB Subject List'''