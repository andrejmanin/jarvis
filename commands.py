import webbrowser
import random
import subprocess
import sys

def chrome():
    webbrowser.open('https://www.google.com/')

def youtube():
    webbrowser.open('https://www.youtube.com/')

def music():
    music_list = ['https://music.youtube.com/watch?v=QN1odfjtMoo&list=RDAMVMQN1odfjtMoo', 'https://music.youtube.com/watch?v=hTWKbfoikeg', 'https://music.youtube.com/watch?v=QUvVdTlA23w&list=RDAMVMhTWKbfoikeg', 'https://music.youtube.com/watch?v=VcsMFlxWGfA&list=RDAMVMVcsMFlxWGfA', 'https://music.youtube.com/watch?v=ktF_D0-ndCE', 'https://music.youtube.com/watch?v=q7xpwbdHAKM', 'https://music.youtube.com/watch?v=POyZQaexBOM&list=RDAMVMPOyZQaexBOM', 'https://music.youtube.com/watch?v=8zX35YQzvVQ&list=RDAMVMPOyZQaexBOM', 'https://music.youtube.com/watch?v=Gk3nlsDG7Ng&list=RDAMVMhjF0cEJVlsw', 'https://music.youtube.com/watch?v=HZnNt9nnEhw&list=OLAK5uy_mUTYCeC-X91GXyD5lgyPP9lPaT3SzVhbg', 'https://music.youtube.com/watch?v=QTIkudYT3mg&list=RDAMPLOLAK5uy_mUTYCeC-X91GXyD5lgyPP9lPaT3SzVhbg', 'https://music.youtube.com/watch?v=SRcnnId15BA', 'https://music.youtube.com/watch?v=fPO76Jlnz6c', 'https://music.youtube.com/watch?v=TO-_3tck2tg&list=RDAMVMfPO76Jlnz6c', 'https://music.youtube.com/watch?v=XrsbfrFPATs&list=OLAK5uy_nChLJ6OwuxwMF0UXADCu9pNx32f_6GuZA']
    webbrowser.open(music_list[random.randint(0, len(music_list)) - 1])

def restart_program():
    python = sys.executable
    subprocess.Popen([python] + sys.argv)