
All programs run on python 3


To execute a program:

python <file-name>


Eg: 
>> python heap_sort.py


A random data values are generated in the program at the module "random_data_generator.py"

By dafault the input range is set to 100 numbers.
To change the input range to for eg. 2000 change the parameter at the __main__ function,
	input_list = rd.random_data_generator(100)
  
		to
  input_list = rd.random_data_generator(2000)
  
		or
	input_list = rd.random_data_generator(data_range = 2000)


To measure the performance of all the 5 programs execute the program "p1.py"
>> python p1.py

It measures the time taken w.r.t the input values ranging 1000 , 2000, 5000, 10000, 40000, 50000

