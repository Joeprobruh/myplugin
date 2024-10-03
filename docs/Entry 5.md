2024-10-02T08:04:38Z
###### Okay, new day, new me.
###### Got a fresh coffee too.
###### Let's take a look at that error...
###### Okay, `os` is not defined in plugin_runner...
###### Sounds like a dependency problem.
###### I should open `plugin_runner.py` and fix it.

<details> 
  <summary>POST-INVESTIGATION NOTES: </summary>
  
###### _Navigates to src/myplugin/plugin_runner.py_ (HINT: You should, too!)
###### Why is there an octothorpe (hashtag (`#`)) in the middle of Line 2?
###### That is causing the dependency problem.
###### Let's remove that, rebuild, and try again.

```bash
pip uninstall myplugin
python -m build
pip install .\dist\myplugin-0.0.1-py3-none-any.whl
myplugin -p
```

###### And now it's a missing file!
###### Who approved these changes?

   <details> 
   <summary>HINT: </summary>
   
- Okay, this Entry tests your expertise a bit.
- The quick fix: In the left Folder pane, navigate to `src/myplugin/plugin_runner.py` and remove the `#` on Line 2. (`#` is a comment marker in Python, that's why it breaks the injection of the `os` dependency.)
- Then, run the commands in the above `Post-Investigation Notes` section.
- When you see the below output on your terminal, you are ready for Entry 6.

```bash
Traceback (most recent call last):
  File "C:\Program Files\Python310\lib\runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "C:\Program Files\Python310\lib\runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "C:\Program Files\Python310\Scripts\myplugin.exe\__main__.py", line 4, in <module>
  File "C:\Program Files\Python310\lib\site-packages\myplugin\plugin_runner.py", line 51, in <module>
    main()
  File "C:\Program Files\Python310\lib\site-packages\myplugin\plugin_runner.py", line 39, in main
    with open(DATA_FILE, 'r') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Program Files\\Python310\\lib\\site-packages\\myplugin\\data\\success.txt'
```
</details>
</details>