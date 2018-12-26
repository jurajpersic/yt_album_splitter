# yt_album_splitter
Python script for downloading and splitting an album from youtube.

## Prerequisits
```
sudo pip install pydub
sudo pip install youtube_dl
```

## Usage
Call python script yt_downloader.py with 2 arguments.
- First argument is a link to youtube video to be downloaded.
- Second argument is a file (or path to file) which determines how the mp3 file will be sliced. 

The  text file should contain song titles and starting times of each song in one of the following formats: 
- hh:mm:ss
- mm:ss

It works with both leading zeros and without them.
It is irrelevant whether the title is after of before the start time. 
The script will create full audio mp3 from the video, as well as individual titled tracks.

## Example

As an example, you can download an album with:
```
cd example
python ../yt_album_splitter.py 'https://www.youtube.com/watch?v=N0LZ20ppkNo' track_list.txt
```
Enjoy in good music!
