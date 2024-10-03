2024-10-02T10:47:02Z
###### No such file or directory?
###### How is that even possible?
###### Let's look in the `src/myplugin/data/` folder for that success file.

<details> 
  <summary>POST-INVESTIGATION NOTES: </summary>
  
###### Oh, I see the file type has changed from `.txt` to `.csv`.
###### I will change it in `plugin_runner.py` and rebuild again.
###### Thankfully, it only needs to be fixed in `one place`.

```bash
pip uninstall myplugin
python -m build
pip install .\dist\myplugin-0.0.1-py3-none-any.whl
myplugin -p
```

   <details> 
   <summary>HINT: </summary>
See Entry 5's hint. Line 37.
I'm done holding your hand. :P

</details>
</details>