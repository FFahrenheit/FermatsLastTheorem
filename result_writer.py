from datetime import datetime
import csv

class ResultWriter:
    def __init__(self, header):
        self.filename = "results/result-" + str(datetime.now()).replace(':','-') + ".csv"
        # self.filename = "results/result.csv"
        self.header = header

        with open(self.filename, 'w', newline='') as results_file:
            writer = csv.writer(results_file, delimiter=',')
            writer.writerow(self.header)
        
        self.records = []

    def write_record(self, record):
        self.records.append(record)

        with open(self.filename, 'a', newline='') as results_file:
            writer = csv.writer(results_file, delimiter=',')
            writer.writerow(record)