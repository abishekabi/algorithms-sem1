
All programs run on python 3


To execute a program:
</br>

`python <file-name>`

</br>

Eg: 
`>> python heap_sort.py`


A random data values are generated in the program at the module `"random_data_generator.py"`

By dafault the input range is set to 100 numbers.
To change the input range to for eg. 2000 change the parameter at the `__main__` function,

`input_list = rd.random_data_generator(100)` 
</br>
to
</br>
`input_list = rd.random_data_generator(2000)`
</br>
or
</br>
`input_list = rd.random_data_generator(data_range = 2000)`
</br>

To measure the performance of all the 5 programs execute the program "p1.py"
</br>
`>> python p1.py`

</br>
It measures the time taken w.r.t the input values ranging 1000 , 2000, 5000, 10000, 40000, 50000
