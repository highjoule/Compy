# submysrs
It is pandemia times and my girlfriend and I found a cool new TV-series in a language she understands but me. On top of that, not english subtitles avaliable. 
Problem would be solved if I could learn German in 2 hours, instead of doing that, I made a little subtitle projector in my computer that let us enjoy our new TV show.

Since the streaming is made from a TV, I could not syncronize the video created and the TV show perfectly. therefore this is far from being perfect. Some manual work is still required. A future issue could integrate an computing way to solve sync.

Also, once both are sychronized stopping for a loo pause migth be a bit trick.

In order to make this video possible, you will have to download the subtitle file in a .srt file.

You will also need moviepy and ImageMagick and make a little trick with the latter.

## Before coding

1. Moviepy Installation with pip

`pip install moviepy`

2. ImageMagick

Download the ImageMagick from [here](https://imagemagick.org/script/download.php)

3. Fix the IMAGEMAGICK_BINARY issue from in the file config_default.py. (Consult the file in the repository)

For Windows users, find where ImageMagick is installed, the path of magick.exe should be add in the last row of config_default.py.
For Linux users, making sure that convert.py is installed should be enough.

4. Run the code in susmysrs.md in this repository.

