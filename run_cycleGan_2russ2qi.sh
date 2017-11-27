# sudo pip install visdom
# sudo pip install dominate

# start visdom server to monitor the training process: 
# sudo python -m visdom.server

# training
python train.py --dataroot datasets/2russ2qi --display_id 1 --name 2russ2qi --model cycle_gan --checkpoints_dir checkpoints/ --gpu_ids 3
