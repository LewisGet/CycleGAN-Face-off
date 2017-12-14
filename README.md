This is a modified version of CycleGAN for the paper "CycleGAN Face-off" by Xiaohan Jin, Ye Qi and Shangxuan Wu.

This repo contains the code which adds:
1. SSIM loss. Usage: adding `--with_ssim` in your training script.
1. Better testing script for generating a whole video. Usage: `python generate_fake_sequence.py`
1. Training scripts for some of the experiments like Shangxuan <-> Russ etc.
1. Weighted loss of facial mask. Usage: 
1. Adding make_video folder for making a comparison video (such as make_video/jin/output_with_sould.mkv). Usage: `python jin.py`
1.  Adding draw_plot folder for analysing plots for the log files. Usage: `python draw_plot.py`
