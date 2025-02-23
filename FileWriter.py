def send_data(data):
    with open('tracked_data.txt','a') as data_file:
        data_file.write(data)


