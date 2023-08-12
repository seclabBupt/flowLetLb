import matplotlib.pyplot as plt
import os
import re

class plot_flowInfo:

    def __init__(self, path):
        self.dataPath = path
        self.datas = {}
        self.fileNames = {}
        
        self.getFileName()
        self.getTotalData()

        self.plot()

    def getFileName(self):
        self.fileNames = os.listdir(self.dataPath)
    
    def getTotalData(self):
        for fileName in self.fileNames:
            self.datas[fileName] = self.getData(fileName)


    def getData(self, fileName):
        filePath = self.dataPath + '/' + fileName
        logData = {}

        with open(filePath, 'r') as file:
            data = file.read()

            bandwidth_data = re.findall(r'(\d+\.\d+|\d+) MBytes/sec', data)

            bandwidth = [float(re.findall(r'(\d+\.\d+|\d+)', item)[0]) for item in bandwidth_data]
            logData["bandwidth"] = bandwidth
            
            time_interval = re.findall(r'\d+\.\d+-\d+\.\d+\s*sec', data)
            logData["time_values"] = [(float(re.findall(r'\d+\.\d+', item)[0]), float(re.findall(r'\d+\.\d+', item)[1])) for item in time_interval]
        
        # file.close()
        # print(logData)

        return logData

    def plot(self):
        plt.xlabel('Time (sec)')
        plt.ylabel('Bandwidth (MBytes/sec)')
        plt.title('Bandwidth Variation')
        plt.grid(True)

        for fileName in self.fileNames:
            time_values = self.datas[fileName]['time_values']
            time_average = [(interval[0] + interval[1]) / 2 for interval in time_values]
            bandwidth_data = self.datas[fileName]['bandwidth']

            time_average = time_average[:len(bandwidth_data) - 2]
            bandwidth_data = bandwidth_data[:len(bandwidth_data) - 2]
            plt.plot(time_average, bandwidth_data, marker='.')

        # plt.show()
        plt.savefig(self.dataPath + "/flowInfo.png")
        plt.close()
        
def main():
    print("init...")

    paths = os.listdir("flowInfo")
    for path in paths:
        # 跳过无用文件
        if path == ".DS_Store":
            continue
        
        path = "flowInfo/" + path
        
        # 删除存在的png文件
        if os.path.exists(path + "/flowInfo.png"):
            os.remove(path + "/flowInfo.png")
        
        plot_flowInfo(path)

if __name__ == "__main__":
    main()
