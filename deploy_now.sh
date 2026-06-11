#!/bin/bash
# 🚀 为WUTUOBANG2022一键部署脚本 (Mac/Linux)

echo ""
echo "╔════════════════════════════════════════════════╗"
echo "║   🚀 赌博下注应用一键部署                     ║"
echo "║   GitHub: WUTUOBANG2022                        ║"
echo "╚════════════════════════════════════════════════╝"
echo ""

cd "$(dirname "$0")"

# 检查是否已初始化Git
if [ ! -d ".git" ]; then
    echo "📍 初始化Git仓库..."
    git init
    git add .
    git commit -m "Initial commit: Betting app"
    git remote add origin https://github.com/WUTUOBANG2022/bet.git
    git branch -M main
else
    echo "📍 Git仓库已存在，更新代码..."
    git add .
    git commit -m "Update: Betting app" || echo "没有新改动"
fi

echo ""
echo "📍 推送代码到GitHub..."
git push -u origin main

echo ""
echo "✅ 代码推送完成！"
echo ""
echo "📍 后续步骤："
echo "   1. 访问 https://railway.app"
echo "   2. 用GitHub登录"
echo "   3. 选择 WUTUOBANG2022/bet 仓库"
echo "   4. 配置后端（root: backend）"
echo "   5. 配置前端（root: frontend）"
echo "   6. 设置环境变量"
echo "   7. 等待部署完成"
echo ""
echo "📄 详细步骤请查看：DEPLOY_FOR_WUTUOBANG2022.md"
echo ""
echo "🎉 祝部署顺利！"
