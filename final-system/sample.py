import numpy as np
import matplotlib.pyplot as plt

def find_sync_symbol(data, start, lenght_of_pulse):
    #sync is one HIGH and 31 ZERO
    #one is already detected
    position = start + int(1.5 * lenght_of_pulse);
    isItSync = True
    for i in range(24):
        if position >= len(data):
            return False
        if data[position] != 0:
            return False
        
        position += lenght_of_pulse

    if isItSync:
        end = position
        while data[end] == 0:
            end +=1

        lenght_of_pulse = (end-start)/(31+1)
    
    return isItSync, lenght_of_pulse

def find_first_impulse(data, start = 0):
    ones = np.where(data == 1)[0]
    if (start >= len(ones)):
        return False
    lenght_of_conseq = start + 1
    last = ones[start]
    while ones[lenght_of_conseq] == last+lenght_of_conseq-start:
        lenght_of_conseq += 1
        if lenght_of_conseq >= len(ones):
            break
    
    return lenght_of_conseq - start, ones[start]


def main(signal):
    ones = []
    sampled_data_list = []
    n = 0
    while n < len(signal):
        if not type(find_first_impulse(signal, n)) == tuple:
            break
        length_of_pulse, position = find_first_impulse(signal, n)
        
        if type(find_sync_symbol(signal, position, length_of_pulse)) == tuple:
            print("sync found")
            plt.axvline(x = position, color="r", label="sync found")
            length_of_pulse_synced = find_sync_symbol(signal, position, length_of_pulse)[1]
            print(length_of_pulse, length_of_pulse_synced)
            #length_of_pulse = (length_of_pulse_synced*31 + length_of_pulse)//32
            length_of_pulse = length_of_pulse_synced
            start = position+(32*length_of_pulse_synced)
            plt.axvline(x = start, color="g", label="sync found")
            
            start += 0.5*length_of_pulse
            sampled_data = ""
            for i in range(96):
                index = int(start + (i*length_of_pulse_synced))
                sampled_data += str(int(signal[index]))
                plt.axvline(x = index, color="m", label="sync found")
            
            sampled_data_list.append(sampled_data)
            break

        ones.append(position)
        n += int(length_of_pulse)

    plt.plot(signal, color='b', label='signal')
    for xc in ones:
        #plt.axvline(x=xc, label="one detected")
        pass
    plt.show()
    return sampled_data_list;

if __name__ == "__main__":
    sample_data = np.genfromtxt('../demodulated_signal.csv', delimiter=',')
    sampled_signal = main(sample_data)

    print(sampled_signal)