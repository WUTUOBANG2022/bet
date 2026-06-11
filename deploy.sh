#!/bin/bash
# 🚀 一键部署脚本（Mac/Linux）

echo "╔════════════════════════════════════════════════╗"
echo "║   🚀 赌博下注应用一键部署                     ║"
echo "║   Betting App Auto Deploy                      ║"
echo "╚════════════════════════════════════════════════╝"
echo ""

# 检查Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 未找到Python3，请先安装Python"
    exit 1
fi

# 运行部署脚本
python3 deploy.py
