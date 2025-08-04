#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FabLab数据分析器 - 本地服务器启动脚本
解决CORS跨域问题
"""

import http.server
import socketserver
import webbrowser
import os
import sys

def start_server():
    """启动本地HTTP服务器"""
    
    # 设置端口
    PORT = 8000
    
    # 切换到脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # 检查HTML文件是否存在
    html_file = 'fablab_analyzer.html'
    if not os.path.exists(html_file):
        print(f"错误：找不到文件 {html_file}")
        return
    
    # 创建HTTP服务器
    Handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("=" * 50)
            print("🚀 FabLab数据分析器 - 本地服务器")
            print("=" * 50)
            print(f"📁 服务器目录: {script_dir}")
            print(f"🌐 服务器地址: http://localhost:{PORT}")
            print(f"📄 HTML文件: http://localhost:{PORT}/{html_file}")
            print("=" * 50)
            print("💡 提示：")
            print("1. 服务器启动后，浏览器会自动打开页面")
            print("2. 如果浏览器没有自动打开，请手动访问上述地址")
            print("3. 按 Ctrl+C 停止服务器")
            print("=" * 50)
            
            # 自动打开浏览器
            webbrowser.open(f'http://localhost:{PORT}/{html_file}')
            
            # 启动服务器
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n\n🛑 服务器已停止")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ 端口 {PORT} 已被占用，请尝试其他端口或关闭占用该端口的程序")
        else:
            print(f"❌ 启动服务器失败: {e}")
    except Exception as e:
        print(f"❌ 未知错误: {e}")

if __name__ == "__main__":
    start_server() 