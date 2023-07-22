#!/usr/bin/env bash

tmux split-pane -h
tmux select-pane -t 0
tmux split-pane -h
tmux select-pane -t 2
tmux split-pane -h

tmux select-pane -t 0
tmux split-pane -v
tmux select-pane -t 2
tmux split-pane -v
tmux select-pane -t 4
tmux split-pane -v
tmux select-pane -t 6
tmux split-pane -v


tmux select-pane -t 0
tmux send "nload s1-eth1" ENTER
tmux select-pane -t 2
tmux send "nload s1-eth2" ENTER
tmux select-pane -t 4
tmux send "nload s1-eth3" ENTER
tmux select-pane -t 6
tmux send "nload s1-eth4" ENTER

tmux select-pane -t 1
tmux send "nload s1-eth5" ENTER
tmux select-pane -t 3
tmux send "nload s1-eth6" ENTER
tmux select-pane -t 5
tmux send "nload s1-eth7" ENTER
tmux select-pane -t 7
tmux send "nload s1-eth8" ENTER

