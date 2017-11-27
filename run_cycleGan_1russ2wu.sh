# sudo pip install visdom
# sudo pip install dominate

# start visdom server to monitor the training process: 
# sudo python -m visdom.server

# training
python train.py --dataroot datasets/1russ2wu --display_id 1 --name 1russ2wu --model cycle_gan --checkpoints_dir checkpoints/ --gpu_ids 0,1
