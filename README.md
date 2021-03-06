# JudgeLight

## 依赖

- Linux
- Python3.6+
- gcc5+

## 平台可用性

开发环境为 Ubuntu 18.04，为保证最佳体验，请使用 Ubuntu 16.04 及以上版本。

Python 代码中使用了 `f-string`，因此**仅**支持 Python 3.6 及以上版本。

仅支持 16.04 及更高版本的 Ubuntu 系统。

## 安装

### 从 pypi:

```bash
$ pip install -U JudgeLight
```

### 从 GitHub:

```bash
$ pip install -U git+https://github.com/MeiK2333/JudgeLight.git
```

### 源码安装:

```bash
$ git clone https://github.com/MeiK2333/JudgeLight.git
$ cd JudgeLight && python3 setup.py install
```

## 测试

### 核心功能

```bash
$ cd tests && python test_core.py
```

### 资源限制

```bash
$ cd tests && python test_limit.py
```

### 系统调用限制

```bash
$ cd tests && python test_syscall.py
```

## 使用方法

`JudgeLight` 只有一个类，类中只有一个方法 `run()`：

```python
from JudgeLight import JudgeLight

jl = JudgeLight('/bin/echo', ['Hello', 'World'])
stats = jl.run()

print(stats)
```

运行输出：

```bash
Hello World
{'time_used': 3, 'real_time_used': 32, 'memory_used': 740, 'signum': 0, 're_flag': 0, 're_syscall': -1}
```

## 可用参数

`JudgeLight` 在类初始化的时候可以传入参数，分别为：

- `exec_file_path`: 要执行的程序
- `exec_args`: 执行时的命令行参数，类型为字符串列表
- `envs`: 执行时的 env，类型为字符串列表，如 `envs=['path=/usr/sbin']`
- `time_limit`: CPU 时间限制，单位毫秒
- `real_time_limit`: 真实时间限制，单位毫秒
- `memory_limit`: 内存限制，单位 KB
- `output_size_limit`: 最大输出限制，单位字节
- `stack_limit`: 栈限制，单位 KB
- `input_file_path`: 输入数据文件
- `output_file_path`: 输出数据文件，如果不存在则会创建
- `error_file_path`: error 流的输出文件，如果不存在则会创建
- `uid`: 执行目标程序的用户 id
- `gid`: 执行目标程序的用户组 id
- `trace=True`: 是否使用 `ptrace` 进行系统调用限制，如果不使用的话，同时将无法获得准确的内存使用量（偏大）
- `allow_system_calls_rule=None`: 允许执行的系统调用规则，在 C 代码中定义，目前只能取值为 `None` 或者 `'default'`

## 返回参数

- `time_used`: CPU 时间使用量
- `real_time_used`: 真实时间使用量
- `memory_used`: 内存占用
- `signum`: 程序退出的 `code`（C/C++ `main` 函数的返回值）
- `re_flag`: `runtime error` 的标志，标示程序是否是因为运行异常而退出的
- `re_syscall`: 如果程序是因为使用了不允许的系统调用而退出，则这个值将是系统调用的值。注意，在不同的系统上（或者同一个系统的不同版本上），系统调用与其数值的对应关系是不同的，可以去 `<sys/syscall.h>` 文件中自行寻找对应。
