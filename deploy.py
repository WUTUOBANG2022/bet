#!/usr/bin/env python3
"""
🚀 一键自动部署工具
自动化处理：Git初始化、GitHub推送、Railway部署等步骤
"""

import os
import sys
import subprocess
import json
from pathlib import Path

class BettingAppDeployer:
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.github_token = None
        self.github_username = None
        self.github_repo = None
        self.railway_token = None
        
    def print_banner(self):
        print("""
╔════════════════════════════════════════════════╗
║   🚀 赌博下注应用一键部署工具              ║
║   Betting App Auto Deployer                    ║
╚════════════════════════════════════════════════╝
        """)
    
    def step1_git_setup(self):
        """第一步：Git初始化和GitHub推送"""
        print("\n📍 第1步：Git初始化...")
        
        # 初始化Git
        subprocess.run(["git", "init"], cwd=self.project_root)
        subprocess.run(["git", "add", "."], cwd=self.project_root)
        subprocess.run(["git", "commit", "-m", "Initial commit: Betting app"], cwd=self.project_root)
        
        # 获取GitHub信息
        self.github_username = input("请输入你的GitHub用户名: ").strip()
        self.github_repo = input("请输入仓库名称 (默认: bet): ").strip() or "bet"
        
        # 创建远程连接
        repo_url = f"https://github.com/{self.github_username}/{self.github_repo}.git"
        subprocess.run(["git", "remote", "add", "origin", repo_url], cwd=self.project_root)
        subprocess.run(["git", "branch", "-M", "main"], cwd=self.project_root)
        
        print(f"\n✅ Git初始化完成！")
        print(f"   仓库URL: {repo_url}")
        
        return repo_url
    
    def step2_github_push(self):
        """第二步：推送代码到GitHub"""
        print("\n📍 第2步：推送代码到GitHub...")
        print("⚠️  需要在浏览器中进行GitHub认证")
        
        # 执行push
        result = subprocess.run(
            ["git", "push", "-u", "origin", "main"],
            cwd=self.project_root,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print("✅ 代码已推送到GitHub！")
        else:
            print("⚠️  推送失败，请检查GitHub凭证")
            print(result.stderr)
            return False
        
        return True
    
    def step3_railway_info(self):
        """第三步：收集Railway信息"""
        print("\n📍 第3步：Railway部署信息...")
        print("""
请按照以下步骤在Railway上部署：

1. 访问 https://railway.app
2. 点击「Start Project」→ 用GitHub登录
3. 选择你的项目仓库
4. 系统会自动创建后端服务

后端配置：
- Root Directory: backend
- Build: pip install -r requirements.txt && python init_db.py
- Start: uvicorn app.main:app --host 0.0.0.0 --port $PORT

环境变量：
- SECRET_KEY: (生成的安全密钥)
- DATABASE_URL: sqlite:///./bet.db

        """)
        
        backend_url = input("请输入部署完成后的后端URL: ").strip()
        
        return backend_url
    
    def step4_frontend_deploy(self, backend_url):
        """第四步：前端部署配置"""
        print("\n📍 第4步：前端部署...")
        print(f"""
在Railway中创建前端服务：

1. 点击「+ New」→ GitHub Repo
2. 配置：
   - Root Directory: frontend
   - Build: npm install && npm run build
   - Start: npm run preview

环境变量：
- VITE_API_BASE_URL: {backend_url}

        """)
        
        frontend_url = input("请输入前端URL（完成部署后）: ").strip()
        
        return frontend_url
    
    def step5_test(self, frontend_url):
        """第五步：功能测试"""
        print("\n📍 第5步：功能测试...")
        print(f"""
✅ 自动测试清单：

1. 打开前端: {frontend_url}
2. 注册新账户
3. 登录
4. 查看比赛列表
5. 尝试下注
6. 查看钱包

如果所有功能都正常，就可以分享给朋友了！
        """)
        
        return True
    
    def step6_share(self, frontend_url):
        """第六步：分享给朋友"""
        print("\n📍 第6步：生成分享文案...")
        
        share_text = f"""
🎲 新应用上线了！

我做了个赌博比赛下注模拟系统，
现在可以和你们一起玩了！

每人初始¥1000，看谁能赚最多！

👉 打开这个链接立即体验：
{frontend_url}

还不赶快来试试？ 🚀
        """
        
        print("\n" + "="*50)
        print("📱 分享文案（复制这个给朋友）：")
        print("="*50)
        print(share_text)
        print("="*50)
        
        # 保存分享文案
        share_file = self.project_root / "share_text.txt"
        with open(share_file, "w", encoding="utf-8") as f:
            f.write(share_text)
        
        print(f"\n✅ 分享文案已保存到: {share_file}")
        
        return share_text
    
    def run(self):
        """执行完整的部署流程"""
        try:
            self.print_banner()
            
            # 步骤1：Git设置
            print("准备开始部署...")
            input("按Enter键继续...")
            
            repo_url = self.step1_git_setup()
            input("按Enter键继续推送到GitHub...")
            
            # 步骤2：GitHub推送
            if not self.step2_github_push():
                print("❌ 部署失败")
                return False
            
            input("按Enter键继续Railway部署...")
            
            # 步骤3-4：Railway信息
            backend_url = self.step3_railway_info()
            frontend_url = self.step4_frontend_deploy(backend_url)
            
            # 步骤5：测试
            input("按Enter键验证功能...")
            self.step5_test(frontend_url)
            
            # 步骤6：分享
            input("按Enter键生成分享文案...")
            self.step6_share(frontend_url)
            
            print("\n" + "="*50)
            print("🎉 部署完成！")
            print("="*50)
            print(f"""
✅ 部署成功！

📊 部署信息：
- 前端: {frontend_url}
- 后端: {backend_url}

👥 接下来：
1. 测试应用功能
2. 分享给朋友
3. 收集反馈

💡 管理应用：
- Railway Dashboard: https://railway.app/dashboard
- API文档: {backend_url}/docs
- GitHub仓库: {repo_url}

祝你玩得开心！ 🎲
            """)
            
            return True
            
        except KeyboardInterrupt:
            print("\n❌ 部署已取消")
            return False
        except Exception as e:
            print(f"\n❌ 错误: {e}")
            return False

if __name__ == "__main__":
    deployer = BettingAppDeployer()
    success = deployer.run()
    sys.exit(0 if success else 1)
