import pdb
import scipy
import matplotlib.pyplot as plt

log_fn_d2 = 'loss_log_D2.txt'
log_fn_mask = 'loss_log_mask.txt'
log_fn_original = 'loss_log_original.txt'
log_fn_unet = 'loss_log_unet.txt'

which_loss = ['D_A', 'G_A', 'Cyc_A']

gap = 20

def read_log(fn):
    with open(fn, "r") as ins:
        loss_dict = {'total_iter': [],
                                'D_A': [], 
                                'G_A': [],
                                'Cyc_A': [], 
                                'D_B': [],
                                'G_B': [],
                                'Cyc_B': []}
        count = 0
        for line in ins:
            count = count + 1
            if count % gap == 0 and not line.startswith('=') :
                line = line.split(' ')
                # line[1] epoch num
                epoch_num = int(line[1][:-1])
                # line[3] iter num
                iter_num = int(line[3][:-1])
                # line[7] D_A
                D_A = float(line[7])
                # line[9] G_A
                G_A = float(line[9])
                # line[11] Cyc_A
                Cyc_A = float(line[11])
                # line[13] D_B
                D_B = float(line[13])
                # line[15] G_B
                G_B = float(line[15])
                # line[17] Cyc_B
                Cyc_B = float(line[17])

                loss_dict['total_iter'].append((epoch_num-1)* + iter_num)
                loss_dict['D_A'].append(D_A)
                loss_dict['G_A'].append(G_A)
                loss_dict['Cyc_A'].append(Cyc_A)
                loss_dict['D_B'].append(D_B)
                loss_dict['G_B'].append(G_B)
                loss_dict['Cyc_B'].append(Cyc_B)

    return loss_dict

def read_log_d2(fn):
    with open(fn, "r") as ins:
        loss_dict = {'total_iter': [],
                                'D_A': [], 
                                'G_A': [],
                                'Cyc_A': [], 
                                'D_B': [],
                                'G_B': [],
                                'Cyc_B': []}
        count = 0
        for line in ins:
            count = count + 1
            if count % gap == 0 and not line.startswith('='):
                line = line.split(' ')
                # line[1] epoch num
                epoch_num = int(line[1][:-1])
                # line[3] iter num
                iter_num = int(line[3][:-1])
                # line[7] D_A
                D_A1 = float(line[7])
                D_A2 = float(line[9])
                D_A = (D_A1 + D_A2)/2
                # line[9] G_A
                G_A = float(line[11])
                # line[11] Cyc_A
                Cyc_A = float(line[13])
                # line[13] D_B
                D_B1 = float(line[15])
                D_B2 = float(line[17])
                D_B = (D_B1 + D_B2)/2
                # line[15] G_B
                G_B = float(line[19])
                # line[17] Cyc_B
                Cyc_B = float(line[21])

                loss_dict['total_iter'].append((epoch_num-1)* + iter_num)
                loss_dict['D_A'].append(D_A)
                loss_dict['G_A'].append(G_A)
                loss_dict['Cyc_A'].append(Cyc_A)
                loss_dict['D_B'].append(D_B)
                loss_dict['G_B'].append(G_B)
                loss_dict['Cyc_B'].append(Cyc_B)

    return loss_dict


if __name__ == "__main__":
    loss_dict_original = read_log(log_fn_original)
    loss_dict_mask = read_log(log_fn_mask)
    loss_dict_d2 = read_log_d2(log_fn_d2)
    loss_dict_unet = read_log(log_fn_unet)
    for this_loss in which_loss:
        vanilla = plt.plot(loss_dict_original[this_loss],'r', label="Vanilla CycleGAN")
        # mask = plt.plot(loss_dict_mask[this_loss],'b', label="Mask CycleGAN (weighted loss)")
        unet = plt.plot(loss_dict_unet[this_loss],'g', label="CycleGAN with U-Net generator")
        d2 = plt.plot(loss_dict_d2[this_loss],'b', label="CycleGAN with 2 discriminators")
        plt.legend()
        plt.xlabel('epoch')
        plt.ylabel(this_loss + ' loss')
        plt.axis([0, 4000/gap, 0, 2])
        plt.savefig(this_loss + '.png')        
        plt.show()
        