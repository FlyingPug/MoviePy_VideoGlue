from moviepy.editor import VideoFileClip, concatenate_videoclips, clips_array

import os

MH = 1081 #Max Height of a clip

def ChangeSizeOfClip(Clips,Height):
    for i in range(len(Clips)):
        if Clips[i].h != Height:
            Clips[i] = Clips[i].resize(height=Height)
    return Clips
    
def MinHeight(Clips):
    min = 999999999
    for clip in Clips:
        if clip.h < min:
            min = clip.h
    print(min)
    return min

def MaxHeight(Clips):
    max = 0
    for clip in Clips:
        if clip.h > max and MH > 0 and clip.h < MH:
            max = clip.h
    print(max)
    return max

def PrintClipsFrameCount(Clips):
    for clip in Clips:
        print(clip.filename,' - ',int(clip.fps * clip.duration))

# Press the green button in the gutter to run the script.
videos = []
if __name__ == '__main__':
    for file in os.listdir():
        if file.endswith("mp4") or file.endswith("mov") or file.endswith("webm"):
            videos.append(VideoFileClip(file))
    minH = MaxHeight(videos) #You can use MinHeight to accelerate process but it'll make video in bad quality
    ChangeSizeOfClip(videos,minH)
    PrintClipsFrameCount(videos)
    final_clip = concatenate_videoclips(videos,method="compose")
    final_clip.write_videofile("result/video.mp4")

