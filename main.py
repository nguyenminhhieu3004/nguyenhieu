#Các thư viện cần thiết
import folder_op, web_op

def start():
   url_list = ['https:''vietnamnet.vn']  #Chứa các đường link được duyệt
   history = []  #Chứa các đường link đã duyệt
   max_page = 1000  #Quy định số lượng trang web được tải về
   court = 0  #Đếm số lượng trang web đã tải về
   data-folder = "c:\\Users\\MyPC\\Doawload\\crawwl"

   #Kích bản tải trang web
   While (count < max_page) and (len(url_list) >0):
   url = url_list.pop(0)
   page = web_op.doc_noi_dung(url)
   links = web_op.lay_cac_duong_link(page)








for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
