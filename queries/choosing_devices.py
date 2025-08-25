import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_histogram(data, title, n_bins):
    sns.histplot(data, bins=n_bins, kde=True)
    plt.title(title)
    plt.show()

data = input("Enter the CSV file name (with .csv extension): ")

df = pd.read_csv(data)

print(df['protocol'].value_counts())

siemens = df[df['protocol'] == 'siemens']
telnet = df[df['protocol'] == 'telnet']
modbus = df[df['protocol'] == 'modbus']
ftp = df[df['protocol'] == 'ftp']
dnp3 = df[df['protocol'] == 'dnp3']

siemens.sort_values(by='distance')
telnet.sort_values(by='distance')
modbus.sort_values(by='distance')
ftp.sort_values(by='distance')
dnp3.sort_values(by='distance')

n_bins = int(len(df) / 10)
plot_histogram(df['distance'], 'Windfarm Distance Distribution', n_bins)

n_bins = int(len(siemens) / 10)
plot_histogram(siemens['distance'], 'Siemens S7 Devices Windfarm Distance Distribution', n_bins)

n_bins = int(len(telnet) / 10)
plot_histogram(telnet['distance'], 'Telnet Devices Windfarm Distance Distribution', n_bins)

n_bins = int(len(modbus) / 3)
plot_histogram(modbus['distance'], 'Modbus Devices Windfarm Distance Distribution', n_bins)

n_bins = int(len(ftp) / 10)
plot_histogram(ftp['distance'], 'FTP Devices Windfarm Distance Distribution', n_bins)

n_bins = int(len(dnp3) / 3)
plot_histogram(dnp3['distance'], 'DNP3 Devices Windfarm Distance Distribution', n_bins)
