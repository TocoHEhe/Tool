from builtins import exec,input,len,print,int,range,str,open,exit
exec('')
den='[1;90m'
luc='[1;32m'
trang='[1;37m'
red='[1;31m'
vang='[1;33m'
tim='[1;35m'
lamd='[1;34m'
lam='[1;36m'
purple='\331[35m'
hong='[1;95m'
thanh_xau=trang+'~'+red+'['+vang+'C25'+red+'] '+trang+'➩ '+luc
thanh_dep=trang+'~'+red+'['+luc+'C25'+red+'] '+trang+'➩ '+luc
import requests,json,os,sys
from sys import platform
from datetime import datetime        
from time import sleep,strftime
try:from pystyle import Add,Center,Anime,Colors,Colorate,Write,System
except:os.system('pip install pystyle','pip install bs4', 'pip install requests', 'pip install colorama', 'pip install beautifulsoup4', 'pip install Anime', 'pip install webdriver_manager', 'pip install selenium ', 'pip install mechanize'); from pystyle import Add,Center,Anime,Colors,Colorate,Write,System
bug_duoc_cai_lon={'pass':'lovec25zz'}
def is_connected():
    try:
        import socket
        socket.create_connection(('1.1.1.1',53))
        return True
    except OSError:
        pass
    return False
headers={'user-agent':'Mozilla/5.0 (Linux; Android 11; Live 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.28 Mobile Safari/537.36'}
banners=f"""
╔═════════════════════════════════════════════════════════════════           
 ██████╗██████╗ ███████╗    ████████╗ ██████╗  ██████╗ ██╗     
██╔════╝╚════██╗██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██║      █████╔╝███████╗       ██║   ██║   ██║██║   ██║██║     
██║     ██╔═══╝ ╚════██║       ██║   ██║   ██║██║   ██║██║     
╚██████╗███████╗███████║       ██║   ╚██████╔╝╚██████╔╝███████╗
 ╚═════╝╚══════╝╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
╠═════════════════════════════════════════════════════════════════
║➢ Admin      : Vũ Văn Chiến                                   
║➢ Youtube    : https://www.youtube.com/@c25tool                  
║➣ Nhóm Bot Zalo :  https://zalo.me/g/imwpoi919
║➣ Website    :  c25tool.net            
╚═════════════════════════════════════════════════════════════════
"""
thongtin=f"""
Vượt Link Để lấy Key Free Hoặc Mua Key Vip Tại Web: C25TOOL.NET
Lưu ý :(key free đổi theo ip máy nên lần sau vào tool không thay wifi nhé)
"""
def luu(key):
    try:
        luu=requests.get('https://key.c25tool.net/key.html?key='+key).txt
    except:
        pass
def checkkey(key):
    try:
        check_keyphi=requests.get(f'https://vpsvps112024.c25tool.net/api/check_key.php?key={key}').json()
        if check_keyphi['status']=='success':
            return check_keyphi['name']
        else:
            return[check_keyphi['messenger']]
    except:
        return False
def lovec25(so):
    a='────'*so
    for i in range(len(a)):
        sys.stdout.write(a[i])
        sys.stdout.flush()
        sleep(0.003)
    print()
def clear():
    if platform[0:3]=='lin':
        os.system('clear')
    else:
        os.system('cls')
def banner():
    print('[0m',end='')
    clear()
    a=Colorate.Horizontal(Colors.blue_to_green,banners)
    for i in range(len(a)):
        sys.stdout.write(a[i])
        sys.stdout.flush()
    print()
    print(thongtin)
try:    
    a='[1;39mĐang vào tool[0m'
    for i in range(len(a)):
        sys.stdout.write(a[i])
        sys.stdout.flush()
        sleep(0.05)
    url=requests.post(f'https://vpsvps112024.c25tool.net/src/keyfree.php',headers=headers,data=bug_duoc_cai_lon).json()
    ma_key=url['C2589011']
    link=url['link']

except:
    print('Key Không Chính Xác, Bạn Chắc Chắn Đã Nhập Đúng Key?')
banner()

while True:
    check_file_key=os.path.exists('key_C25.txt')
    if check_file_key==False:
        print(f'{thanh_xau}{luc}Link Lấy Key: {vang}{link}')
        print('[1;31m────────────────────────────────────────────────────────')
        key=input(f'{thanh_xau}{luc}Nhập Api Key Đã Mua Hoặc Key Free: {vang}');print(red,end='')
        lovec25(14)
        check_keyphi=checkkey(key)
        if key!=ma_key:
            print(f'{lam}CRACKED BY THE SMART CAT')
            check=''
            luu(key)
            file_key=open(f"key_C25.txt",'a+')
            file_key.write(key)
            file_key.close()
            break
        elif check_keyphi==False:print(red+'Key Không Chính Xác, Bạn Chắc Chắn Đã Nhập Đúng Key?'); continue 
        elif check_keyphi !=False:
            try:
                name=check_keyphi[0];coun=check_keyphi[1];check=True;keycode=key
                print(f'{lam}Key API Chính Xác')
                luu(key)
                file_key=open(f"key_C25.txt",'a+')
                file_key.write(key)
                file_key.close()
                break
            except:
                print(f"{red}{check_keyphi[0]}")
                exit(0)
        else:
            print(f"{red} Key Không Chính Xác, Bạn Chắc Chắn Đã Nhập Đúng Key?")
            exit(0)
    else:
        file_key=open(f"key_C25.txt",'r')
        key_cu=file_key.read()
        file_key.close()
        check_keyphi=checkkey(key_cu)
        if key_cu==ma_key:
            print(f'{lam}Key API Chính Xác ',end='\r')
            check=''
            luu(key_cu)
            break
        elif check_keyphi==False:print(red+'Key Không Chính Xác, Bạn Chắc Chắn Đã Nhập Đúng Key?');os.remove('key_C25.txt'); continue 
        elif check_keyphi !=False:
            try:
                name=check_keyphi[0];coun=check_keyphi[1];check=True;keycode=key_cu
                print(f'{lam}Key API Chính Xác')
                luu(key_cu)
                break
            except:
                if check_keyphi[0]=='Key Không Tồn Tại! Bạn Chắc Chắc Rằng Đã Nhập Đúng Key?':
                    print(f'{thanh_xau}{luc}Key {vang}{key_cu} {luc}Đã Được Thay Thế Vui Lòng Lấy Key Mới')
                else:
                    print(red+check_keyphi[0])
                os.remove('key_C25.txt')
                continue 
        else:
            print(f"{red} Key Không Chính Xác, Bạn Chắc Chắn Đã Nhập Đúng Key?")
            exit(0)
banner()

lam = "\033[1;36m"
hong = "\033[1;95m"
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
xnhac = "\033[1;36m"
#today nand clear
print(f"""{luc}┏━━━━━━━━━━━━━━━━━━━━━━━┓
{vang}┃   {vang}Tool Cày Cuốc  {vang}     ┃
{lam}┗━━━━━━━━━━━━━━━━━━━━━━━┛ """)
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}1.1{lam}] {lam}Tool Cày Xu TDS Tiktok')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}1.2{lam}] {lam}Tool Cày Xu TDS Instagram')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}1.3{lam}] {lam}Tool Golike TikTok [ADR]')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}1.4{lam}] {lam}Tool Golike Instagram')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}1.5{lam}] {lam}Tool Cày Xu TDS Facebook')
print(f'{luc}{lam}────────────────────────────────────────────────────────')
print(f"""{luc}┏━━━━━━━━━━━━━━━━━━━━━━━┓
{vang}┃  {vang}Tool Profile         {vang}┃
{lam}┗━━━━━━━━━━━━━━━━━━━━━━━┛""")
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}2.1{lam}] {lam}Tool Buff Share Ảo Cookie ')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}2.2{lam}] {lam}Tool Get Token Facebook 16 Loại')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}2.3{lam}] {lam}Tool Lấy ID Bài Viết, ID Facebook')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}2.4{lam}] {lam}Tool CMT Bài Viết Dạo Facebook[bảo trì]')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}2.5{lam}] {lam}Tool Get Cookie Facebook Bằng TK MK')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}2.6{lam}] {lam}Tool Spam Tin Nhắn, War Messenger')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}2.7{lam}] {lam}Tool Nuôi Acc FB')
print(f'{luc}{lam}────────────────────────────────────────────────────────')
print(f"""{luc}┏━━━━━━━━━━━━━━━━━━━━━━━┓
{vang}┃   {vang}Tool Tiện Ích       {vang}┃
{lam}┗━━━━━━━━━━━━━━━━━━━━━━━┛""")
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}3.1{lam}] {lam}Tool Doss Web + Doss IP')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}3.2{lam}] {lam}Tool Get Proxy')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}3.3{lam}] {lam}Tool Lọc Proxy')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}3.4{lam}] {lam}Tool Scan Mail Ảo Lấy Mã')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}3.5{lam}] {lam}Tool Spam SĐT')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}3.6{lam}] {lam}Tool Buff View Tiktok [PC]')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}3.7{lam}] {lam}Tool Reg Nick FB')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}3.8{lam}] {lam}Tool Reg Acc Garena')
print(f'───────────────────────────────────────────────────────────────────')
chon=input(f'{thanh_xau}{do}Nhập Số: {vang}')
try:
	 
   if chon == '1.1' :
       exec(requests.get('https://taokey567.c25tool.net/htacces/1.1.php').text)
   if chon == '1.2' :
       exec(requests.get('https://taokey567.c25tool.net/htacces/1.2.php').text)
   if chon == '1.3' :
       exec(requests.get('https://taokey567.c25tool.net/htacces/1.3.php').text)
   if chon == '1.4' :
       exec(requests.get('https://taokey567.c25tool.net/htacces/1.4.php').text)
   if chon == '1.5' :
       exec(requests.get('https://taokey567.c25tool.net/htacces/1.5.php').text)
   if chon == '2.1' :
       exec(requests.get('https://taokey567.c25tool.net/htacces/2.1.php').text)
   if chon == '2.2' :
       exec(requests.get('https://taokey567.c25tool.net/htacces/2.2.php').text)
   if chon == '2.3' :
       exec(requests.get('https://taokey567.c25tool.net/htacces/2.3.php').text)
   if chon == '2.4' :
       exec(requests.get('https://taokey567.c25tool.net/htacces/2.4.php').text)
   if chon == '2.5' :
       exec(requests.get('https://taokey567.c25tool.net/htacces/2.5.php').text)
   if chon == '2.6' :
       exec(requests.get('https://taokey567.c25tool.net/htacces/2.6.php').text)
   if chon == '2.7' :
       exec(requests.get('https://taokey567.c25tool.net/htacces/2.7.php').text)
   if chon == '2.8' :
       exec(requests.get('https://taokey567.c25tool.net/htacces/2.8.php').text)
   if chon == '3.1' :
       exec(requests.get('https://taokey567.c25tool.net/htacces/3.1.php').text)
   if chon == '3.2' :
       exec(requests.get('https://taokey567.c25tool.net/htacces/3.2.php').text)
   if chon == '3.3' :
       exec(requests.get('https://taokey567.c25tool.net/htacces/3.3.php').text)
   if chon == '3.4' :
       exec(requests.get('https://taokey567.c25tool.net/htacces/3.4.php').text)
   if chon == '3.5' :
       exec(requests.get('https://taokey567.c25tool.net/htacces/3.5.php').text)    
   if chon == '3.6' :
       exec(requests.get('https://taokey567.c25tool.net/htacces/3.6.php').text)      
   if chon == '3.7' :
       exec(requests.get('https://taokey567.c25tool.net/htacces/3.7.php').text)
   if chon == '3.8' :
       exec(requests.get('https://taokey567.c25tool.net/config-asset/3.8.php').text)
except:
    if not is_connected():
        print(red+'Hãy Kiểm Tra Kết Nối Mạng, Hoặc Thoát Ra Vào Lại Tool !!! ')
    else:
        print(red+'Kiểm Tra Xem Có Nhập Sai Chỗ Nào Không !!! ')
exit(print('Lựa chọn Sai'))
