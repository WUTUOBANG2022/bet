#!/bin/bash
set -e

# 安装Node依赖并构建
npm install
npm run build

echo "前端构建完成"
