import os, sys, inspect, csv


from pyspark import SparkConf, SparkContext

### myfunc is to add all numbers in the first column.
def myfunc(s):
  total = 0
  if s.endswith(".csv"):
    #s_new = os.path.realpath(os.path.abspath(os.path.join(data_path, s)))
    #cr = csv.reader(open(s_new,"rb"))
    cr = csv.reader(open(s,"rb"))
    for row in cr:
      total += int(row[0])
  print "The total number of ", s, " is: ", total
  return total

def main():
  ### Initialize the SparkConf and SparkContext
  conf = SparkConf().setAppName("log_analysis").setMaster("local")
  sc = SparkContext(conf = conf)

  ### Load data from HDFS
  datafile = sc.wholeTextFiles("hdfs://l/project/monitoring/archive/openstack/logs/generic/")    

  ### Sent the application in each of the slave node
  temp = datafile.foreach(lambda (path, content): myfunc(str(path).strip('file:')))


if __name__ == "__main__":
  main()
