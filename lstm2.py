import pandas as pandas
from random import random
import pandas as pd

import get_params

data = get_params.processed_data

	
labels = ['request_time','request_path','request_lb_ip','host']
df = pd.DataFrame.from_records(get_params.processed_data, columns=labels)


pdf =  pd.get_dummies(df, prefix=['request_path','request_lb_ip','host'])

feature_list = list(pdf)
#print (pdf.dtypes)
