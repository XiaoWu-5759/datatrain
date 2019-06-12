# anaconda和pycharm 环境问题

```shell
import _ssl # if we can't import it, let the error propagate ImportError: DLL load failed: 找不到指定的模块。
```





<https://www.cnblogs.com/qpanda/p/10183973.html>

今天早晨来，又不行了，还是报错。突然想起来是不是环境变量造成的，echo %path%打印出环境变量来，吓人一跳

```
D:\Anaconda3\envs\jobnote>echo %path%
D:\Program Files\VanDyke Software\Clients\;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Windows\System32\OpenSSH\;C:\Program Files\Java\jdk1.8.0_144\bin;C:\Program Files\Java\jdk1.8.0_144\jre\bin;%conda_home%;%conda_home%\Scripts;%conda_home%\Library\bin;d:\Program Files\Git\cmd;C:\Users\qpand\AppData\Local\Microsoft\WindowsApps;
```

之前做的conda_home变量根本没有被解析出来，重新设置了一下，看到变量已经恢复。重新运行程序，恢复正常。

具体环境变量为什么没有解析出来，还有待研究





<https://blog.csdn.net/fwj380891124/article/details/87179433>

### Python输出窗口报错解决方案

使用PyCharm编写Python代码，

Python 3.7 anaconda environment - import _ssl DLL load fail error

his can be fixed by manually adding in the PATH variables in PyCharm to the console.

1. Open your Anaconda cmd(Anaconda Prompt)
2. Activate your CondaActivate your Conda environment
3. Get the full PATH value by typing `echo %PATH%`
4. if you are on Windows 7/can’t copy the output, cd the cmd to your desktop and type `echo %PATH% > path_val.txt`
5. In PyCharm, go to **Settings -> Build, Execution, Deployment -> Console -> Python Console -> click the folder on the right of Environment variables.**
6. Click the plus button to add a new Environment Variable --> The name should be `PATH` ，The value is the entire output from the echo %PATH% command above.
7. Click OK, then apply.