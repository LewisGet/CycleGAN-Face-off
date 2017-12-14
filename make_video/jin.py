import cv2, pdb, os
import numpy as np

name = 'jin'
expriments = ['original']

def main():
    l = len(expriments)
    # Create a VideoCapture object and read from input file
    # If the input is the camera, pass 0 instead of the video file name
    caps = []
    for experiment in expriments:
        caps.append(cv2.VideoCapture(name + '/' + name + '_' + experiment + '.mkv'))
    
    # Check if camera opened successfully
    for cap in caps:
        if (cap.isOpened()== False): 
            print("Error opening video stream or file")
    
    frame_width = 512
    frame_height = 256 * l
    out = cv2.VideoWriter(name + '/' + 'output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (frame_width,frame_height))

    # Read until video is completed
    while(caps[0].isOpened()):
        # Capture frame-by-frame
        rets = []
        frames = []
        for cap in caps:
            ret, frame = cap.read()
            rets.append(ret)
            frames.append(frame)

        if rets[0] == True:
            frame_all = np.concatenate(frames, axis=0)
            font = cv2.FONT_HERSHEY_SIMPLEX
            for i in range(l):
                experiment = expriments[i]
                cv2.putText(frame_all, experiment,(10 ,i * 256 + 50), font, 1,(255,0,0),3,cv2.LINE_AA)
            # Display the resulting frame
            #cv2.imshow('Frame',frame_all)
            out.write(frame_all)
        
            # Press Q on keyboard to  exit
            #if cv2.waitKey(25) & 0xFF == ord('q'):
            #    break
        
        # Break the loop
        else: 
            break
    
    # When everything done, release the video capture object
    for i in range(l):
        caps[i].release()
    
    out.release()

    # Closes all the frames
    cv2.destroyAllWindows()

    # extract audio
    first_video_path = name + '/' + name + '_' + expriments[0] + '.mkv'
    audio_path = name + '/sound.mp3'
    extract_audio_command = "ffmpeg -i " + first_video_path + " -q:a 0 -map a " + audio_path
    os.system(extract_audio_command)

    # compose video with audio
    input_video_path = name + '/output.avi'
    output_video_path = name + '/output_with_sound.mkv'
    add_audio_command = "ffmpeg -i " + input_video_path + " -i " + audio_path + " -map 0 -map 1 -codec copy " + output_video_path
    os.system(add_audio_command)

if __name__ == "__main__":
    main()

    