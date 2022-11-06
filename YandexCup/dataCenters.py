class DataCenter:
    def __init__(self, servers):
        self.number_of_servers = servers
        self.number_of_working_servers = servers
        self.number_of_reset = 0
        self.server_status = {i + 1: True for i in range(servers)}
    
    def disable(self, number):
        if self.server_status[number] is True:
            self.server_status[number] = False
            self.number_of_working_servers -= 1

    def reset(self):
        self.number_of_reset += 1
        self.number_of_working_servers = self.number_of_servers
        self.server_status = {i + 1: True for i in range(self.number_of_servers)}
    
    def parameter(self):
        return self.number_of_reset * self.number_of_working_servers


def main():
    n, m, q = map(int, input().split())
    data_center = {i + 1: DataCenter(m) for i in range(n)}
    for i in range(q):
        read_data = input().split()
        if read_data[0] == "RESET":
            data_center[int(read_data[1])].reset()
        elif read_data[0] == "DISABLE":
            data_center[int(read_data[1])].disable(int(read_data[2]))
        elif read_data[0] == "GETMAX":
            counts = {key: value.parameter() for key, value in data_center.items()}
            print(max(counts, key=counts.get.parameter()))
        else:
            counts = {key: value.parameter() for key, value in data_center.items()}
            print(min(counts, key=counts.get))



if __name__ == "__main__":
    main()
