# sudo pip install visdom
# sudo pip install dominate

# start visdom server to monitor the training process: 
# sudo python -m visdom.server

# training
python train.py --dataroot russ2qi770 --display_id 1 --name russ2qi770 --model cycle_gan --checkpoints_dir checkpoints/
