bang_diem = { 
            1112233: {'Tin ky thuat': 9.2, 'An toan dien': 8.9, 'The duc': 4.1},
            1112244: {'Tin ky thuat': 3.7, 'An toan dien': 7.9, 'The duc': 9.0}
            }

def mon_hoc_khong_dau(mssv):
    if mssv in bang_diem:    
        mon_hocs = []
        for mon_hoc in bang_diem[mssv]:
            if bang_diem[mssv][mon_hoc] < 5:
                mon_hocs.append(mon_hoc)
        return mon_hocs
    return None

def main():
    mssv = int(input("Nhap MSSV: "))
    mon_hocs = mon_hoc_khong_dau(mssv)
    if mon_hocs is None:
        print("Khong tim thay sinh vien co MSSV " + str(mssv))
    elif len(mon_hocs) == 0:
        print("Sinh vien co MSSV " + str(mssv) + " khong bi mon nao")
    else:
        print("Sinh vien co MSSV " + str(mssv) + " rot cac mon: " + ', '.join(mon_hocs))

if __name__ == "__main__":
    main()