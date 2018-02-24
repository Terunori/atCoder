#!/bin/bash
problemname=$1

oj dl "https://${problemname:0:6}.contest.atcoder.jp/tasks/${problemname:0:8}"

if [ ! -d test ]; then
    num=`expr ${problemname:3:3} + 3`
    if [ $num -lt 100 ]; then
        num='0'$num
    fi
    proNum='arc'$num
    if [ ${problemname:7:1} = "c" ] ; then
        proNum=$proNum'_a'
    elif [ ${problemname:7:1} = "d" ] ; then
        proNum=$proNum'_b'
    fi
    oj dl "https://${problemname:0:6}.contest.atcoder.jp/tasks/$proNum"
fi

### original datas ###
# oj dl "https://beta.atcoder.jp/contest/${problemname:0:6}/tasks/${problemname:0:8}"
# g++ -Wall -std=c++14 ./$1.cpp
# oj test
# rm -f a.out
# rm -rf test