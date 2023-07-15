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
tmux send "nload s1-eth1" ENTER
tmux select-pane -t 1
tmux send "nload s1-eth2" ENTER
tmux select-pane -t 2
tmux send "nload s1-eth3" ENTER


tmux select-pane -t 3
tmux send "nload s2-eth1" ENTER
tmux select-pane -t 4
tmux send "nload s2-eth2" ENTER
tmux select-pane -t 5
tmux send "nload s2-eth3" ENTER

tmux select-pane -t 6
tmux send "nload s3-eth1" ENTER
tmux select-pane -t 7
tmux send "nload s3-eth2" ENTER
tmux select-pane -t 8
tmux send "nload s3-eth3" ENTER

