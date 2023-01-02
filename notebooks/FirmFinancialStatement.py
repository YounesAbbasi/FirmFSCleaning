import pandas as pd
import os
from glob import glob

class FirmFS:
    def __init__(self, Path, name):
        self.path = Path
        self.name = name
    
    def OsWalk(self):
        Pllist = []
        for root, dirs, files in os.walk(self.path):
            for file in files:
                Pllist.append(os.path.join(root, file))
        return Pllist

    def ImportingData(self):
        Bslist = self.OsWalk()
        if Bslist[0].split('\\')[-1][:2] == '~$':
            raise FileExistsError('Excel Shadow file is exist')
        else:
            Bsdf = pd.read_excel(Bslist[0])
        for Bs in Bslist[1:]:
            try:
                Bsdf = pd.concat([Bsdf,pd.read_excel(Bs)])
            except:
                os.remove(Bs)
        return Bsdf

    def UniqueTitle(self):
        df = self.ImportingData()
        return df.description.unique()

