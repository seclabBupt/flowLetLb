#!/bin/bash

# usage:
#   $1: 执行次数
#   $2: iperf3 打流持续时间
#   eg：bash getData.sh 5 1

if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage:"
    echo "\$1: Execution times"
    echo "\$2: duration"
    echo "Example: bash getData.sh 5 10"
    echo "Collect traffic information 5 times, each lasting 10s"
    exit 1
fi

# 指定调用脚本的次数
total_calls=$1
duration=$2

# 循环调用脚本
for ((i=1; i<=$total_calls; i++)); do
    python send_traffic.py $duration
    
    sleepTime=$(( $duration + 10 ))
    sleep $sleepTime
done

tar -cf flowInfo.tar.gz flowInfo/*