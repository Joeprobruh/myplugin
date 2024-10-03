2024-10-01T16:46:07Z
###### Almost time to wrap up the day, let's finish strong!
###### Okay, it's asking for a flag, let's give it that.

```bash
myplugin -p
```

<details> 
  <summary>POST-RUN NOTES: </summary>
  
###### What?? an error?
###### But it built just fine!
###### Ugh, I'll get to this tomorrow.
###### Gonna be on my mind all night now...

   <details> 
   <summary>HINT: </summary>
If your terminal shows the below error, congrats! You're done with Entry 4, BUT!

To test your debugging chops, see if you can fix the below error without reading the next entry!

```bash
Traceback (most recent call last):
  File "C:\Program Files\Python310\lib\runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "C:\Program Files\Python310\lib\runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "C:\Program Files\Python310\Scripts\myplugin.exe\__main__.py", line 4, in <module>
  File "C:\Program Files\Python310\lib\site-packages\myplugin\plugin_runner.py", line 51, in <module>
    main()
  File "C:\Program Files\Python310\lib\site-packages\myplugin\plugin_runner.py", line 36, in main
    PLUGIN_DIR = os.path.dirname(os.path.abspath(__file__))
NameError: name 'os' is not defined
```


</details>
</details>