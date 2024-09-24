def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    
    inner_function()
    

"""Traceback (most recent call last):
  File "/data/user/0/ru.iiec.pydroid3/files/accomp_files/iiec_run/iiec_run.py", line 31, in <module>
    start(fakepyfile,mainpyfile)
  File "/data/user/0/ru.iiec.pydroid3/files/accomp_files/iiec_run/iiec_run.py", line 30, in start
    exec(open(mainpyfile).read(),  __main__.__dict__)
  File "<string>", line 9, in <module>
NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?

[Program finished]"""    
inner_function()