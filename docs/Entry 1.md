# 2024-10-01T09:14:35Z
###### Gonna keep notes on the build process for posterity.
###### Got the repo cloned, need to build the project.
###### Okay, that command is:

```bash
python -m build

# use python3.10 if you have multiple Python versions installed
```

<details> 
  <summary>POST-RUN NOTES: </summary>
  
###### What happened? Why did the build fail?
###### No module named 'build'?...
###### _furious Googling_
###### Oh, looks like we need to install Pip packages.
###### Gonna grab a coffee first.

   <details> 
   <summary>HINT: </summary>
If your terminal shows this error, your environment is broken the right way! Move to Entry 2.

```bash
C:\Program Files\Python310\python.exe: No module named build
```

On the other hand, if your terminal shows the below error, it looks like your environment variables and path are a little funky, probably due to multiple Python installations. Ask a Mentor for help if you don't know how to do this already!

```bash
Fatal Python error: init_fs_encoding: failed to get the Python codec of the filesystem encoding
Python runtime state: core initialized
ModuleNotFoundError: No module named 'encodings'

Current thread 0x00004450 (most recent call first):
  <no Python frame>
```

</details>
</details>