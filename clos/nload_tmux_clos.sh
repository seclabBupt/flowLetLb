tmux split-pane -h
tmux split-pane -h
tmux split-pane -h
tmux select-pane -t 0
tmux split-pane -h
tmux split-pane -h
tmux split-pane -v
tmux split-pane -v
tmux split-pane -v
tmux select-layout tile


tmux select-pane -t 0
tmux send "nload s6-eth1" ENTER
tmux select-pane -t 1
tmux send "nload s6-eth2" ENTER
tmux select-pane -t 2
tmux send "nload s6-eth3" ENTER


tmux select-pane -t 3
tmux send "nload s7-eth1" ENTER
tmux select-pane -t 4
tmux send "nload s7-eth2" ENTER
tmux select-pane -t 5
tmux send "nload s7-eth3" ENTER

tmux select-pane -t 6
tmux send "nload s8-eth1" ENTER
tmux select-pane -t 7
tmux send "nload s8-eth2" ENTER
tmux select-pane -t 8
tmux send "nload s8-eth3" ENTER

