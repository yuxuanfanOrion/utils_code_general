#!/bin/bash

# 使用find来计算总文件数，避免参数列表过长的问题
total=$(find images_1 -name "*.png" | wc -l)
echo "总共发现 $total 个文件"

# 创建目标目录（如果不存在）
mkdir -p ./street_view_data/

# 使用rsync，每次处理一个目录
rsync -av --progress --remove-source-files \
    images_1/ \
    ./street_view_data/ \
    --include="*.png" \
    --exclude="*"

echo -e "\n完成！共移动 $total 个文件"
