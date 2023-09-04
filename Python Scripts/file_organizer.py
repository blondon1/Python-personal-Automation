import shutil
import os

#code files
Python_files = (".py")
Java_files = (".java")
HTML_files = (".html")
Cpp_files = (".cpp")
#files
video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")
audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")
Text_files = (".txt")
Word_files = (".docx")
Excel_files = (".xlsx")
PowerPoint_files = (".pptx")
PDF_files = (".pdf")
img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")
#check for file type funtions
def is_audio(file):
    return os.path.splitext(file)[1] in audio

def is_video(file):
    return os.path.splitext(file)[1] in video

def is_image(file):
    return os.path.splitext(file)[1] in img

def is_PDF_files(file):
    return os.path.splitext(file)[1] in PDF_files

def is_PowerPoint_files(file):
    return os.path.splitext(file)[1] in PowerPoint_files

def is_Excel_files(file):
    return os.path.splitext(file)[1] in Excel_files

def is_Word_files(file):
    return os.path.splitext(file)[1] in Word_files

def is_Text_files(file):
    return os.path.splitext(file)[1] in Text_files

def is_Cpp_files(file):
    return os.path.splitext(file)[1] in Cpp_files

def is_HTML_files(file):
    return os.path.splitext(file)[1] in HTML_files

def is_Java_files(file):
    return os.path.splitext(file)[1] in Java_files

def is_Python_files(file):
    return os.path.splitext(file)[1] in Python_files

def is_screenshot(file):
    name, ext = os.path.splitext(file)
    return (ext in img) and "screenshot" in name.lower()

#dir to organized
os.chdir(r"C:\Users\bryan\Downloads")
#job

for file in os.listdir():
        if is_audio(file):
            shutil.move(file, r"C:\Users\bryan\Music")
        elif is_video(file):
            shutil.move(file, r"C:\Users\bryan\Videos")
        elif is_PDF_files(file):
            shutil.move(file, r"C:\Users\bryan\PDF_files")
        elif is_PowerPoint_files(file):
            shutil.move(file, r"C:\Users\bryan\PowerPoint_files")
        elif is_Excel_files(file):
            shutil.move(file, r"C:\Users\bryan\Excel_files")
        elif is_Word_files(file):
            shutil.move(file, r"C:\Users\bryan\Word_files")
        elif is_Text_files(file):
            shutil.move(file, r"C:\Users\bryan\Text_files")
        elif is_Cpp_files(file):
            shutil.move(file, r"C:\Users\bryan\Cpp_files")
        elif is_HTML_files(file):
            shutil.move(file, r"C:\Users\bryan\HTML_files")
        elif is_Java_files(file):
            shutil.move(file, r"C:\Users\bryan\Java_files")
        elif is_Python_files(file):
            shutil.move(file, r"C:\Users\bryan\Python_files")
        elif is_image(file):
            if is_screenshot(file):
                shutil.move(file, r"C:\Users\bryan\screenshots")
            else:
                shutil.move(file, r"C:\Users\bryan\images")
        else:
            shutil.move(file, r"C:\Users\bryan\Extra")      