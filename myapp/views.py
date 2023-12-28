from django.shortcuts import render
import subprocess
from django.http import HttpResponse

# Create your views here.

from django.shortcuts import render

# command_btn1 = "Get-VM | where {$_.State -eq 'Off'}"
command_btn2 = "ls"
script_path = "D:\\YUANYE\\project\\YJY\\p1.ps1"
command = f"PowerShell -ExecutionPolicy Unrestricted -File {script_path}"


def index(request):
    return render(request, 'index.html')


def button1(request):
    # 执行batch文件
    # 运行PowerShell命令
    # 'powershell' 是调用PowerShell的命令
    # '-Command' 后面跟要执行的PowerShell命令
    result = subprocess.run(command, capture_output=True, text=True)

    # 打印命令输出
    response = result.stdout

    # 检查是否有错误
    if result.stderr:
        response = "Error:" + str(result.stderr)
    return HttpResponse(response)


def button2(request):
    # 执行batch文件
    # 运行PowerShell命令
    # 'powershell' 是调用PowerShell的命令
    # '-Command' 后面跟要执行的PowerShell命令
    result = subprocess.run(["powershell", "-Command", command_btn2], capture_output=True, text=True)

    # 打印命令输出
    response = result.stdout

    # 检查是否有错误
    if result.stderr:
        response = "Error:" + str(result.stderr)
    return HttpResponse(response)
