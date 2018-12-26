from __future__ import unicode_literals
import youtube_dl
from pydub import AudioSegment
from pydub.silence import split_on_silence
import io
import re
import sys
import glob
import os

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}

url = str(sys.argv[1])
text_file = str(sys.argv[2])
print url
print text_file

    
ydl = youtube_dl.YoutubeDL(ydl_opts)
info = ydl.extract_info(url, download=False)
ydl.download([url])

full_filename = info['title'] + u'-'+ info['display_id']+'.mp3'
list_of_files = glob.glob('*.mp3') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)

sound = AudioSegment.from_mp3(latest_file)

file = io.open(text_file,'r', encoding='utf-8')
data = file.read()
lines = data.split('\n')
start_times = []
titles = []
for i in range(len(lines)):
    if len(lines[i])>1:
        split_line = lines[i].split(' ')
        title_str = ''
        title_initiated = False
        start_hour = 0
        start_min = 0
        start_sec = 0
        for j in split_line:
            split_semicolon = j.split(":")
            if len(split_semicolon)==2:
                start_min = int(split_semicolon[0])
                m = re.search(r'\d+', split_semicolon[1])
                numeric = m.group()
                start_sec = int(numeric)
            elif len(split_semicolon)==3:
                start_hour= int(split_semicolon[0])
                start_min = int(split_semicolon[1])
                m = re.search(r'\d+', split_semicolon[2])
                numeric = m.group()
                start_sec = int(numeric)
            elif not title_initiated:
                title_str = title_str + split_semicolon[0]
                title_initiated = True
            else:
                title_str = title_str + ' ' 
                title_str = title_str + split_semicolon[0]
        if title_str[-1] == u' ':
            title_str = title_str[0:-1]  
        print start_hour,start_min,start_sec,title_str
        start_times = start_times + [start_sec + start_min*60 + start_hour*3600]
        titles = titles + [title_str]
print start_times
print titles

for i in range(len(start_times)-1):
    start_idx = start_times[i] * 1000
    end_idx = start_times[i+1] * 1000
    temp = sound[start_idx:end_idx]
    temp.export(titles[i]+".mp3", format="mp3")
start_idx=end_idx
temp = sound[start_idx:]
temp.export(titles[-1]+".mp3", format="mp3")

