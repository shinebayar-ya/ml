import pandas as pd
import glob

def txt2csv(directory_path, diagnostic):
    txt_files = glob.glob(directory_path + '/*.txt')
    column_names = ['Wavelength', 'Intensity']
    samples = []
    for file in txt_files:
        df = pd.read_csv(file, skiprows=4, names=column_names)[:-1]
        df['Wavelength'] = df['Wavelength'].astype(int)
        df = df.pivot_table(values='Intensity', columns='Wavelength')
        df['Diagnostic'] = diagnostic
        samples.append(df)
    return pd.concat(samples, ignore_index=True)